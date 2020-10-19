import csv 
import pandas as pd 
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
    fileName = "tmp.csv"
    dataFrame = pd.read_csv(fileName)
    book = create_dictionary(dataFrame)
    displayList = list()
    for count in range(len(book["age"])):
        if book["tailLn"][count] <= 10:
            if book["tailLn"][count] <= 8:
                if book["bangLn"][count] <= 4:
                    displayList.append(1)
                else:
                    displayList.append(1)
            else:
                if book["hairLn"][count] <= 9:
                    displayList.append(1)
                else:
                    displayList.append(1)
        else:
            if book["hairLn"][count] <= 10:
                if book["bangLn"][count] <= 5:
                    displayList.append(-1)
                else:
                    displayList.append(-1)
            else:
