"""
Filename: HW05_Nafiuzzaman_Raina_Mentor.py
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
Return the total number of values that are less than or equal to the current
threshold in the current feature data being passed in

feature_data: feature data being passed in
current_threshold: the current threshold with regards to the feature data
target: [Assam or Bhuttan]
target_attr_category_data: The list of the Class column
"""
def less_than_sum_categories(feature_data, current_threshold, target, target_attr_category_data):
    total = 0
    for index in range(len(feature_data)):
        if feature_data[index] <= current_threshold:
            if target_attr_category_data[index] == target:
                total += 1
    return total


"""
Return the total number of values that are greater than the current threshold in the
current feature data being passed in

feature_data: feature data being passed in
current_threshold: the current threshold with regards to the feature data
target: [Assam or Bhuttan]
target_attr_category_data: The list of the Class column
"""
def greater_than_sum_categories(feature_data, current_threshold, target, target_attr_category_data):
    total = 0
    for index in range(len(feature_data)):
        if feature_data[index] > current_threshold:
            if target_attr_category_data[index] == target:
                total += 1
    return total


"""
Finds the best gini index and the threshold of the current data entered.

target_attr_category_data: The current node or the dataset of the Class column
feature_data: current feature data
target_attr_categories: [Assam, Bhuttan]
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

        curr_gini_index_1 = 1 - ((c10/(c10+c11))**2) - ((c11/(c10+c11))**2)
        curr_gini_index_2 = 1 - ((c20/(c20+c21))**2) - ((c21/(c20+c21))**2)
        curr_gini_index = (((c10+c11)/(c10+c11+c20+c21)) * curr_gini_index_1) + (((c20+c21)/(c10+c11+c20+c21)) * curr_gini_index_2)

        if curr_gini_index < gini_index:
            gini_index = curr_gini_index
            best_threshold = curr_threshold

    return (gini_index, best_threshold)


"""
finds the sum of the target_attr [Assam or Bhuttan] from the data entered

data: The current node or the dataset of the Class column
target_attr: [Assam or Bhuttan]
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

data: The current node or the dataset
curr_best_feature: the current best feature from the current dataset
threshold: the threshold
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

data: The current node or the dataset
curr_best_feature: the current best feature from the current dataset
threshold: the threshold
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
Decision tree algorithm for classification

data: The current node or the dataset
tab_sequence: Number of tabs to be added to the file when writing the trainer
target_attr_categories: [Assam, Bhuttan]
file_obj: file obj where the data will be written to
depth: recursive depth
"""
def decision_tree_recursive(data, tab_sequence, target_attr_categories, file_obj, depth, purity, depth_level, data_records):
    attr_1 = attr_sum(data["class"], target_attr_categories[0])     # total number of values matching attr 1 in the dataset
    attr_2 = len(data["class"]) - attr_1                            # total number of values matching attr 2 in the dataset

    # stopping condition
    # -> size of the node [current dataset] < 10
    # -> node [current dataset] > 95% of a specific class
    # -> tree depth of 10
    if len(data["class"]) < data_records or (attr_1/len(data["class"]) > purity or attr_2/len(data["class"])) > purity or depth == depth_level:    # depth var , #0.95 == purity, # data-record (b)
        for tab_count in range(tab_sequence):
            file_obj.write('    ')
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

        # ignores this class to avoid perfect classification error
        if key_feature == 'class':
            continue
        (gini_index, threshold) = best_threshold_gini_index(data['class'], data[key_feature], target_attr_categories)

        # updates the best attributes after implementing the gini index, if needed.
        if gini_index < best_attr[2]:
            best_attr = [key_feature, threshold, gini_index]

    for tab_count in range(tab_sequence):
        file_obj.write('    ')

    # displays the header of the csv file
    file_obj.write('if book["' + best_attr[0] + '"][count] <= ' + str(best_attr[1]) + ':\n')

    # splits the left data from the current data to act as a node
    left_data = data_parser_left(data, best_attr[0], best_attr[1])

    # recursive call
    decision_tree_recursive(left_data, tab_sequence + 1, target_attr_categories, file_obj, depth + 1 if depth_level > -1 else 0, purity, depth_level, data_records)

    for tab_count in range(tab_sequence):
        file_obj.write('    ')

    file_obj.write('else:\n')

    # splits the right data from the current data to act as a node
    right_data = data_parser_right(data, best_attr[0], best_attr[1])

    # recursive call
    decision_tree_recursive(right_data, tab_sequence + 1, target_attr_categories, file_obj, depth + 1 if depth_level > -1 else 0, purity, depth_level, data_records)


"""
Initial function call to allow the writing of the return of the
displayList on to the current file_obj and closes the file. 
"""
def decision_tree_start(data, tab_sequence, target_attr_categories, file_obj, depth, purity, depth_level, data_records):
    decision_tree_recursive(data, tab_sequence, target_attr_categories, file_obj, depth, purity, depth_level, data_records)      # generate the tree
    file_obj.write("    return displayList\n")
    file_obj.close()


"""
Writes the initial lines of code to the training file
"""
def program_writer():
    f = open("hw-05/trained_file.py", "wt")
    f.write("import csv \n")
    f.write("import pandas as pd \n")
    f.write(textwrap.dedent('''\
    def create_dictionary(dataFrame):
        book = {
            "age"       :  dataFrame["Age"].tolist(),
            "ht"        :  dataFrame["Ht"].tolist(),
            "tailLn"    :  dataFrame["TailLn"].tolist(),
            "hairLn"    :  dataFrame["HairLn"].tolist(),
            "bangLn"    :  dataFrame["BangLn"].tolist(),
            "reach"     :  dataFrame["Reach"].tolist(),
            "earLobes"  :  dataFrame["EarLobes"].tolist()
        }

        return book

    def csv_parser():
        fileName = "hw-05/testing_file.csv"
        dataFrame = pd.read_csv(fileName)
        book = create_dictionary(dataFrame)
        displayList = list()
        for count in range(len(book["age"])):
        '''))
    return f


"""
Rounds the data in the data frame and stores it in a dictionary. This makes finding the thresholds
for each feature easier and reduces possible float errors.

dataFrame: csv file in the dataFrame format
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
    decision_tree_start(book, tab_sequence, target_attr_categories, file_obj, 0)


"""
Calculate the accuracy of the selected attribute's prediction
Input: DataFrame, Attribute that we want to test the accuracy on, the threshold value
"""
def calculate_accuracy(dataFile, resultFile):
    dataFrame = pd.read_csv(dataFile)
    actual_res_lst = dataFrame["Class"].tolist()

    assam_counter = 0                   # total assam
    bhuttan_counter = 0                 # total bhuttan in dataset
    
    right_assam_hit = 0                 # confusion matrix 
    right_bhutan_hit = 0
    false_assam = 0
    false_bhutan = 0

    lines = resultFile                          # updated form HW05, its just comparing a list now
    for i in range(0, len(actual_res_lst)):     # compare with our result file
        city = actual_res_lst[i]
        predicted_city = lines[i]
        if city == "Bhuttan":
            bhuttan_counter +=1
        if city == "Assam":
            assam_counter += 1
        if predicted_city == 1 and city == "Assam":
            right_assam_hit +=1
        elif predicted_city == -1 and city == "Bhuttan":
            right_bhutan_hit +=1
        elif predicted_city == 1 and city == "Bhuttan":
            false_assam +=1
        elif predicted_city == -1 and city == "Assam":
            false_bhutan +=1

    all_hits = right_assam_hit + right_bhutan_hit
    all_misses = false_assam + false_bhutan
    all_records = assam_counter + bhuttan_counter
    calc = all_hits / all_records                   # calculates the accuracy of our decision tree
    accuracy_rate = calc * 100              

    return (accuracy_rate, all_hits, all_misses, all_records)

def makee_split_df(lst):
    headerCol = ["Age","Ht","TailLn","HairLn","BangLn","Reach","EarLobes","Class"]
    dataFrame_lst = []
    for i in range(0, len(lst)):
        df =  pd.DataFrame(data= lst[i], columns=headerCol)
        dataFrame_lst.append(df)
    return dataFrame_lst

"""
Outputs a TMP CSV file consisting of 9 dataframes    
"""
def make_csv(df_lst):
    df_lst.to_csv("hw-05/testing_file.csv", index=False)         # dump rest of the dataframe to tst.csv
    return 1
    # for i in range(0, len(df_lst)):
    #     selected_df = df_lst[i]
    #     selected_df.to_csv("out.csv", index=False)
    #     break


"""
Function stores the results of the current N Fold Cross Validation sequence
"""
def csvWriter(st):
    file = open("hw-05/output_results_file.csv", "a")
    file.write(st)
    file.close()


"""
Implements the N Fold Cross Validation algorithm for the dataset its been given
"""
def n_fold_algorithm(df_lst):
    purity_lst = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.98]
    data_record_lst = [30, 25, 20, 15, 10, 8, 6, 5, 4, 3, 2]
    depth_level_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    constant_data_records = 10      # constant data record number as mentioned in the document
    constant_purity = 0.95          # constant purity number as mentioned in the document
    constant_depth = -1             # -1 indicates that the value shouldn't be used while for the algorithm

    for idx in range(0, len(df_lst)):
        test_dataframe = df_lst[idx]                             # dataFrame for testing            (1)  
        train_dataFrame_lst = df_lst[:idx] + df_lst[idx+1 : ]       # training data frames lst 
        train_dataFrame = pd.concat(train_dataFrame_lst)            # make it into a big train dataset (9)

        ######################################################################################
        ## THIS FOLLOWING BLOCK OF CODE IS FOR MAKE DECISION TREE WITH OUR SELECTED DATAFRAME
        book = round_data(train_dataFrame)
        
        print('Test block: ',idx,' for depth')
        for depth in depth_level_lst:
            print('depth at:', depth)
            book["class"] = train_dataFrame["Class"].tolist()
            target_attr_categories = train_dataFrame["Class"].unique().tolist()
            file_obj = program_writer()
            tab_sequence = 2

            decision_tree_start(book, tab_sequence, target_attr_categories, file_obj, 0, constant_purity, depth, constant_data_records)      # generate the tree
            ####################################################################################

            make_csv(test_dataframe)
            trained_file = __import__("trained_file")
            resultLst = trained_file.csv_parser()
            statis = calculate_accuracy("hw-05/testing_file.csv", resultLst)
            csvStr = str(constant_purity)+ "," + str(constant_data_records) + "," + str(depth) + "," + str(statis[0])  + "," + str(statis[1]) + "," + str(statis[2]) + "," + str(statis[3]) +"\n"
            csvWriter(csvStr)
        
        print('Test block: ',idx,' for data record')
        for dataRec in data_record_lst:
            print('data record at:', dataRec)
            book["class"] = train_dataFrame["Class"].tolist()
            target_attr_categories = train_dataFrame["Class"].unique().tolist()
            file_obj = program_writer()
            tab_sequence = 2

            decision_tree_start(book, tab_sequence, target_attr_categories, file_obj, 0, constant_purity, constant_depth, dataRec)      # generate the tree
            ####################################################################################

            make_csv(test_dataframe)
            trained_file = __import__("trained_file")
            resultLst = trained_file.csv_parser()
            statis = calculate_accuracy("hw-05/testing_file.csv", resultLst)
            csvStr = str(constant_purity)+ "," + str(dataRec) + "," + str(constant_depth) + "," + str(statis[0])  + "," + str(statis[1]) + "," + str(statis[2]) + "," + str(statis[3]) +"\n"
            csvWriter(csvStr)
        
        print('Test block: ',idx,' for purity')
        for prt in purity_lst:
            print('purity at:', prt)
            book["class"] = train_dataFrame["Class"].tolist()
            target_attr_categories = train_dataFrame["Class"].unique().tolist()
            file_obj = program_writer()
            tab_sequence = 2

            decision_tree_start(book, tab_sequence, target_attr_categories, file_obj, 0, prt, constant_depth, constant_data_records)      # generate the tree
            ####################################################################################

            make_csv(test_dataframe)
            trained_file = __import__("trained_file")
            resultLst = trained_file.csv_parser()
            statis = calculate_accuracy("hw-05/testing_file.csv", resultLst)
            csvStr = str(prt) + "," + str(constant_data_records) + "," + str(constant_depth) + "," + str(statis[0])  + "," + str(statis[1]) + "," + str(statis[2]) + "," + str(statis[3]) + "\n"
            csvWriter(csvStr)

     
"""
Function call for implementing the N Cross Validation concept on the data
"""
def n_fold_cross_validation(fileName, cluster_divisions):
    large_dataFrame = make_dataFrame(fileName)    
    large_array = large_dataFrame.to_numpy()
    splitted = np.split(large_array, cluster_divisions)

    dataFrameLst = makee_split_df(splitted)         # contains the number of dataframes as per cluster_division
    n_fold_algorithm(dataFrameLst)


if __name__ == "__main__":
    fileName = "hw-05/Abominable_Data_HW05_v725.csv"
    # fileName = "Abominable_Data_HW05_v725.csv"
    n_fold_cross_validation(fileName, 10)
    # main()
