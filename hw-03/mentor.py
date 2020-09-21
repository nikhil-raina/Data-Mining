import pandas as pd

def make_dataFrame(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame


def algorithm(targetAttr, dataFrame, test_attr):
    best_cost = float("-inf")
    test_attr = dataFrame[test_attr].tolist()
    bins = 6
    blackBin = []
    rightBin = []
    best_mark = float("inf")
    # fp = []
    # fn = []

    # [sum of #x, sum of RED] 
    dic = {
        0: [0, 0],
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0]
       }
    
    for idx in range(0, len(targetAttr)):
        if test_attr[idx] == 0:
            dic[0][0] += 1
            if targetAttr[idx] == "black":
                dic[0][1] += 1
        elif test_attr[idx] == 1:
            dic[1][0] += 1
            if targetAttr[idx] == "black":
                dic[1][1] += 1
        elif test_attr[idx] == 2:
            dic[2][0] += 1
            if targetAttr[idx] == "black":
                dic[2][1] += 1
        elif test_attr[idx] == 3:
            dic[3][0] += 1
            if targetAttr[idx] == "black":
                dic[3][1] += 1
        elif test_attr[idx] == 4:
            dic[4][0] += 1
            if targetAttr[idx] == "black":
                dic[4][1] += 1
        elif test_attr[idx] == 5:
            dic[5][0] += 1
            if targetAttr[idx] == "black":
                dic[5][1] += 1

    best_cost = float("inf")
    best_threshold = 0
    # TARGET =>>> RED
    for thresh in range (0,6): 
        false_neg = 0   # All the Red in Black Pool
        false_pos = 0   # All the Black in the Red Pool
        if thresh == 0:
            for jdx in range (0, 6):
                false_neg += dic[jdx][0] - dic[jdx][1]
        else:
            # Runs a loop from 0 to the threshold value and counts all the 
            # total blacks in the Red Pool
            for jdx in range(0, thresh):   
                false_pos += dic[jdx][1]   
            # Run the loop from the threshold to the end of the list, and 
            # counts all the Reds in the Black Pool
            for jdx in range (thresh, 6):
                false_neg += dic[jdx][0] - dic[jdx][1]            
        cost_func = false_pos + false_neg

        if cost_func < best_cost:
            best_cost = cost_func
            best_threshold = thresh
    
    return (best_cost, best_threshold)
            
  
        
    
    
    


def main():
    fileName = "HW03_Marked_Cards_TRAINING_v07.csv"
    dataFrame = make_dataFrame(fileName)
    class_data = dataFrame["ColorName"].tolist()
    a = algorithm(class_data, dataFrame, "Scratched")
    print(a)
main()
