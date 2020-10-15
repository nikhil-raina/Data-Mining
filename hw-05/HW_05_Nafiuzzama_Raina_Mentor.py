"""
Filename: HW05_Nafiuzzaman_Raina_Trained.py
Name: Navid Nafiuzzaman <mxn4459@cs.rit.edu>
      Nikhil Raina       <nxr5013@cs.rit.edu>
Description: This file builds a classifier by choosing the best attribute 
based on the cost.
"""
import pandas as pd
import numpy as np
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

"""
def less_than_sum_categories(feature_data, current_threshold, target, target_attr_category_data):
    total = 0
    for index in range(len(feature_data)):
        if feature_data[index] <= current_threshold:
            if target_attr_category_data[index] == target:
                total += 1
    return total

"""

"""
def greater_than_sum_categories(feature_data, current_threshold, target, target_attr_category_data):
    total = 0
    for index in range(len(feature_data)):
        if feature_data[index] > current_threshold:
            if target_attr_category_data[index] == target:
                total += 1
    return total
    

"""

"""
def best_threshold_gini_index(target_attr_category_data, feature_data, target_attr_categories):
    min_value = min(feature_data)
    max_value = max(feature_data)

    best_threshold = float("inf")
    
    # This is the worst value for the Gini index
    gini_index = 0.5

    for curr_threshold in np.arange(min_value, max_value):
        c10 = less_than_sum_categories(feature_data, curr_threshold, target_attr_categories[0], target_attr_category_data)
        c11 = less_than_sum_categories(feature_data, curr_threshold, target_attr_categories[1], target_attr_category_data)
        c20 = greater_than_sum_categories(feature_data, curr_threshold, target_attr_categories[0], target_attr_category_data)
        c21 = greater_than_sum_categories(feature_data, curr_threshold, target_attr_categories[1], target_attr_category_data)

        curr_gini_index_1 = 1 - (c10/(c10+c11))**2 - (c11/(c10+c11))**2
        curr_gini_index_2 = 1 - (c20/(c20+c21))**2 - (c21/(c20+c21))**2
        curr_gini_index = ((c10+c11)/(c10+c11+c20+c21)) * curr_gini_index_1 + ((c20+c21)/(c10+c11+c20+c21)) * curr_gini_index_2

        if curr_gini_index < gini_index:
            gini_index = curr_gini_index
            best_threshold = curr_threshold

    return (gini_index, best_threshold)

"""

"""
def attr_sum(data, target_attr):
    total = 0
    for attr in data:
        if target_attr == attr:
            total += 1
    return total

"""
Splits the current dataset, from the left, with respect to the current best 
feature till the threshold and returns the dataset
"""
def data_parser_left(data, curr_best_feature, threshold):
    target_data = data[curr_best_feature]
    features = data.keys()
    book = {key: [] for key in features}
    for count in range(len(data["class"])):
        if target_data[count] <= threshold:
            for feature in features:
                book[feature].append(data[feature][count])
    return book


"""
Splits the current dataset, from the left, with respect to the current best 
feature till the threshold and returns the dataset
"""
def data_parser_right(data, curr_best_feature, threshold):
    target_data = data[curr_best_feature]
    features = data.keys()
    book = {key: [] for key in features}
    for count in range(len(data["class"])):
        if target_data[count] > threshold:
            for feature in features:
                book[feature].append(data[feature][count])
    return book

"""

"""
def decision_tree(data, tab_sequence, target_attr_categories, file_obj, depth): # 3rd parameter should be the file writer object
    attr_1 = attr_sum(data["class"], target_attr_categories[0])     # total number of values matching attr 1 in the dataset
    attr_2 = len(data["class"]) - attr_1                            # total number of values matching attr 2 in the dataset

    # stopping condition
    # -> size of the node [current dataset] < 10
    # -> node [current dataset] > 95% of a specific class
    # -> tree depth of 10
    if len(data["class"]) < 10 or (attr_1/len(data["class"]) > 0.95 or attr_2/len(data["class"])) > 0.95 or depth == 3:
        for tab_count in range(tab_sequence):
            file_obj.write('\t')
        out = 1
        if attr_1 < attr_2:
            out = -1
        file_obj.write('displayList.append(' + str(out) + ')\n')
        return
    
    # default values set for the best attributes for the following:
    # -> feature index
    # -> threshold
    # -> gini index
    best_attr = ["", 0, 0.5]

    for key_feature in data:
        if key_feature == 'class':
            continue
        (gini_index, threshold) = best_threshold_gini_index(data['class'], data[key_feature], target_attr_categories)

        if gini_index < best_attr[2]:
            best_attr = [key_feature, threshold, gini_index]
    
    for tab_count in range(tab_sequence):
        file_obj.write('\t')

    file_obj.write('if feature_rows["' + best_attr[0] + '"] <= ' + str(gini_index) + ':\n')

    # splits the left data from the current data to act as a node 
    left_data = data_parser_left(data, best_attr[0], best_attr[1])

    # recursive call
    decision_tree(left_data, tab_sequence + 1, target_attr_categories, file_obj, depth + 1)


    for tab_count in range(tab_sequence):
        file_obj.write('\t')

    file_obj.write('else:\n')

    # splits the right data from the current data to act as a node 
    right_data = data_parser_right(data, best_attr[0], best_attr[1])

    # recursive call
    decision_tree(right_data, tab_sequence + 1, target_attr_categories, file_obj, depth + 1)

    # for tab_count in range(tab_sequence):
    #     file_obj.write('\t')
    


        
"""
Writes the program to the training file
"""
def program_writer():
    f = open("HW_05_Nafiuzzaman_Raina_Trained.py", "w") 
    f.write("import csv \n")
    book = {
        "age"       :  0,
        "ht"        :  1,
        "tailLn"    :  2,
        "hairLn"    :  3,
        "bangLn"    :  4,
        "reach"     :  5,
        "earLobes"  :  6
    }
    f.write(textwrap.dedent('''\
    def csv_parser():
        book = {
        "age"       :  0,
        "ht"        :  1,
        "tailLn"    :  2,
        "hairLn"    :  3,
        "bangLn"    :  4,
        "reach"     :  5,
        "earLobes"  :  6
        }
        fileName = input('Please input the file name: ')
        fileReader = csv.reader(open(fileName))
        displayList = list()
        for feature_rows in fileReader:
        \t'''))
    return f
    

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
Rounds the data in the data frame and stores it in a dictionary. This makes finding the thresholds
for each feature easier and reduces possible float errors.
"""
def round_data(dataFrame):
    age_list = dataFrame["Age"].tolist()
    ht_list = dataFrame["Ht"].tolist()
    tailln_list = dataFrame["TailLn"].tolist()
    hairln_list = dataFrame["HairLn"].tolist()
    bangln_list = dataFrame["BangLn"].tolist()
    reach_list = dataFrame["Reach"].tolist()
    earlobes_list = dataFrame["EarLobes"].tolist()
    book = {
        "age"       :  [],
        "ht"        :  [],
        "tailLn"    :  [],
        "hairLn"    :  [],
        "bangLn"    :  [],
        "reach"     :  [],
        "earLobes"  :  []
    }
        
    for index in range(0, len(age_list)):
        book["age"].append(round(age_list[index]/2.0)*2.0)          # round age to nearest 2 years
        book["ht"].append(round(ht_list[index]/5)*5)                # round the height to nearest 5 cm
        book["tailLn"].append(round(tailln_list[index]))            # round the TailLn
        book["hairLn"].append(round(hairln_list[index]))            # round the HairLn
        book["bangLn"].append(round(bangln_list[index]))            # round the BangLn 
        book["reach"].append(round(reach_list[index]))              # round the Reach
        book["earLobes"].append(round(earlobes_list[index]))        # round the EarLobes
    
    return book


def main_writer(f):
    f.write("    return displayList")
    f.write("\n")
    
    f.write(textwrap.dedent('''\
    def main():
        lst = csv_parser()
        for i in lst:
            print(i)
    main()
    \t'''))
    
        
"""
The main function of the program, entry point
"""
def main():
    # fileName = input("Please type in the Input CSV File (including .csv): ")     # the training file's name
    fileName = "Abominable_Data_HW05_v725.csv"
    dataFrame_data = make_dataFrame(fileName)                           # dataFrame made from the training file
    tab_sequence = 2
    book = round_data(dataFrame_data)
    book["class"] = dataFrame_data["Class"].tolist()                       # target attribute list 
    target_attr_categories = dataFrame_data["Class"].unique().tolist()         # target categories
    file_obj = program_writer()
    decision_tree(book, tab_sequence, target_attr_categories, file_obj, 0)
    main_writer(file_obj)


main()
