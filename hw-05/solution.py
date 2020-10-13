# hw-05 solution

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

def main():
    fileName = "Abominable_Data_FOR_CLASSIFICATION_HW_v2201_720.csv"
    quantize_data(fileName)

    target_attr = read_attr(fileName)
    best_threshold = algorithm(target_attr)
    roc_curve(best_threshold[2], best_threshold[1])