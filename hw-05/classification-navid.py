import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

qntz_age_lst = []
qntz_ht_lst = []

def quantize_data(fileName):
    dataFrame = pd.read_csv(fileName)
    age_list = dataFrame["Age"].tolist()
    ht_list = dataFrame["Ht"].tolist()
    
    for idx in age_list:
        qntz_age = round(idx/2.0)*2.0           # round age to nearest 2 years
        qntz_age_lst.append(qntz_age)

    for idx in ht_list:
        qntz_ht = round(idx/5)*5
        qntz_ht_lst.append(qntz_ht)
    
    

def read_attr(fileName):
    dataFrame = pd.read_csv(fileName)
    class_lst = dataFrame["Class"].tolist()
    return class_lst


def roc_curve(fp_rate, tp_rate):
    plt.title ("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.plot(fp_rate, tp_rate)
    plt.show()

def algorithm(class_lst):
    curr_cost = 0
    best_cost_func = float("inf")
    best_age = 0
    fn = []
    fp = []

    np_array = np.array(class_lst)

    bhuttan_count = np.count_nonzero(np_array=="Bhuttan")
    assam_count = np.count_nonzero(np_array=="Assam")
    
    for idx in range(0, len(qntz_age_lst)):
        false_neg = 0        # thought there was no fire, but actually there is (MISS)
        false_pos = 0        #  I thougt this is assam, and it is Assam
        fp_rate = 0          # false pos rate
        fn_rate = 0          # false neg rate
        tp_rate = 0          # true pos rate

        for jdx in range(0 , len(class_lst)):
            if qntz_age_lst[jdx] < qntz_age_lst[idx] and class_lst[jdx] == "Bhuttan" :
                false_pos += 1
            elif qntz_age_lst[jdx] > qntz_age_lst[idx] and class_lst[jdx] == "Assam":
                false_neg += 1
        
        cost = false_pos + false_neg
        
        fp_rate = false_pos / (len(class_lst)-bhuttan_count)
        fn_rate = false_neg / bhuttan_count
        tp_rate = 1-fn_rate
        
        fn.append(fn_rate)
        fp.append(fp_rate)
        


        if cost < best_cost_func:
            best_cost_func = cost
            best_age = qntz_age_lst[idx]


    print("Best Age: ", best_age)
    print("Best Cost: ", best_cost_func)
    return (best_age, fn, fp)




def main():
    fileName = "Abominable_Data_FOR_CLASSIFICATION_HW_v2201_720.csv"
    fileName2 = "test.csv"
    quantize_data(fileName)

    target_attr = read_attr(fileName)
    best_threshold = algorithm(target_attr)
    roc_curve(best_threshold[2], best_threshold[1])
    

main()