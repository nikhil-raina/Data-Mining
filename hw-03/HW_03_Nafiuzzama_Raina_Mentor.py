"""
Filename: HW03_Nafiuzzaman_Raina_Trained.py
Name: Navid Nafiuzzaman <mxn4459@cs.rit.edu>
      Nikhil Raina       <nxr5013@cs.rit.edu>
Description: This file builds a classifier by choosing the best attribute 
based on the cost.
"""
import pandas as pd
import textwrap

"""
Build a pandas dataframe for the input CSV file

Parameter: CSV input file     
Return: Pandas DataFrame
"""
def make_dataFrame(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame


"""
Classifier Builder basically goes through the training csv's dataframe,
by going through the specified attribute passed as a parameter and returns
the best threshold, the cost and the attribute name. 

Return: tuple(best cost, best threshold)
"""

def classifier_builder(targetAttr, dataFrame, test_attr):
    test_attr = dataFrame[test_attr].tolist()
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
    for thresh in range(0, 6): 
        false_neg = 0   # All the Red in Black Pool
        false_pos = 0   # All the Black in the Red Pool
  
        # Runs a loop from 0 to the threshold value and counts all the 
        # total blacks in the Red Pool
        for jdx in range(0, thresh):   
            false_pos += dic[jdx][1]   
        # Run the loop from the threshold to the end of the list, and 
        # counts all the Reds in the Black Pool
        for jdx in range(thresh, 6):
            false_neg += dic[jdx][0] - dic[jdx][1]            
        cost_func = false_pos + false_neg

        if cost_func < best_cost:
            best_cost = cost_func
            best_threshold = thresh
    # returs a tupe with best_cost and best threshold
    return (best_cost, best_threshold)
            

"""
Iterates through all the attributes of the and finds the best attribute
to make the cluster.

Input: Target Variable, DataFrame
Return: tuple(attribute found best, the best cost function val, and best threshold)   
"""
def check_attr(class_data, dataFrame):
    active_attributes = ["PencilMark", "DrinkStain", "CrimpedBent", "Scratched", "Chocolate"]
    best_cost = float("inf")
    best_threshold = 0
    best_attr = ""
    for idx in active_attributes:
        result = classifier_builder(class_data, dataFrame, idx)
        if result[0] < best_cost:
            best_cost = result[0]
            best_threshold = result[1]
            best_attr = idx
    return (best_attr, best_cost, best_threshold)


"""
Writes the program to the training file
"""
def program_writer(csvFile, attribute, threshold):
    f = open("HW_03_Nafiuzzaman_Raina_Trained.py", "w") 
    col_dic = {
                "PencilMark": 0,
                "DrinkStain": 1,
                "CrimpedBent": 2,
                "Scratched": 3,
                "Chocolate": 4
    }
    f.write(
        "import csv \n")
    f.write(textwrap.dedent('''\
    def csv_parser(attr_num, threshold):
        fileName = input('Please input the file name: ')
        fileReader = csv.reader(open(fileName))
        next(fileReader)
        for row in fileReader:
            value = row[attr_num]
            if (int(value) < threshold):
                print("+1")
            else:
                print("-1") 
            \n
        '''))
    inputBuilder = str(col_dic[attribute]) + "," + str(threshold)
    fileInputString = "csv_parser(" + inputBuilder + ")"
    f.write(fileInputString)
    f.close()
    

"""
Calculate the accuracy of the selected attribute's prediction
Input: DataFrame, Attribute that we want to test the accuracy on, the threshold value

"""

def calculate_accuracy(dataFrame, attribute_name, threshold):
    actual_res_lst = dataFrame["Class"].tolist()

    our_res = []
    # tryes to predict the training dataset based on the best threshold
    for idx, row in dataFrame.iterrows():
        if row[attribute_name] < threshold:
            our_res.append(1)
        else:
            our_res.append(-1)
    
    counter  = 0

    # compares the predicted result with the actual result. 
    for idx in range(0, len(our_res)):
        if our_res[idx] == actual_res_lst[idx]:
            counter += 1
    
    
    calc = (counter/len(actual_res_lst)) * 100
    print("The best attribute is:", attribute_name)
    print("Accuracy of our selected attribute is ", calc)

            
        
"""
The main function of the program, entry point

"""
def main():
    fileName = input("Please type in the Input CSV File (including .csv): ")     # the training file's name
    dataFrame = make_dataFrame(fileName)                        # dataFrame made from the training file
    class_data = dataFrame["ColorName"].tolist()                # target attribute in list 
    attr_res = check_attr(class_data, dataFrame)                # calls the function to check all the attributes 
    program_writer(fileName, attr_res[0], attr_res[2])          # write the training file with the best found attr and threshold
    calculate_accuracy(dataFrame, attr_res[0], attr_res[2])     # prints out the accuracy of the selected attrbutes


main()
