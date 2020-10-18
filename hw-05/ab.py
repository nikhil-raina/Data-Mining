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
            if book["hairLn"][count] <= 8:
                if book["tailLn"][count] <= 9:
                    if book["reach"][count] <= 170:
                        if book["bangLn"][count] <= 6:
                            if book["tailLn"][count] <= 6:
                                if book["earLobes"][count] <= 0:
                                    if book["ht"][count] <= 135:
                                        displayList.append(1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    displayList.append(1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["age"][count] <= 36.0:
                                        displayList.append(1)
                                    else:
                                        if book["hairLn"][count] <= 5:
                                            displayList.append(1)
                                        else:
                                            if book["ht"][count] <= 130:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["earLobes"][count] <= 0:
                                        displayList.append(-1)
                                    else:
                                        if book["bangLn"][count] <= 3:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                        else:
                            displayList.append(1)
                    else:
                        displayList.append(-1)
                else:
                    if book["ht"][count] <= 135:
                        if book["reach"][count] <= 130:
                            displayList.append(1)
                        else:
                            if book["reach"][count] <= 140:
                                if book["age"][count] <= 34.0:
                                    displayList.append(-1)
                                else:
                                    displayList.append(-1)
                            else:
                                displayList.append(1)
                    else:
                        if book["earLobes"][count] <= 0:
                            displayList.append(-1)
                        else:
                            if book["age"][count] <= 62.0:
                                displayList.append(1)
                            else:
                                displayList.append(-1)
            else:
                displayList.append(1)
        else:
            if book["hairLn"][count] <= 10:
                if book["bangLn"][count] <= 5:
                    if book["hairLn"][count] <= 8:
                        if book["bangLn"][count] <= 4:
                            displayList.append(-1)
                        else:
                            if book["age"][count] <= 54.0:
                                if book["earLobes"][count] <= 0:
                                    displayList.append(-1)
                                else:
                                    if book["tailLn"][count] <= 14:
                                        if book["ht"][count] <= 135:
                                            if book["age"][count] <= 30.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 150:
                                            displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 156:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                            else:
                                displayList.append(-1)
                    else:
                        if book["bangLn"][count] <= 4:
                            if book["age"][count] <= 24.0:
                                displayList.append(1)
                            else:
                                if book["reach"][count] <= 156:
                                    if book["ht"][count] <= 150:
                                        if book["age"][count] <= 50.0:
                                            if book["age"][count] <= 44.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    displayList.append(-1)
                        else:
                            if book["tailLn"][count] <= 19:
                                if book["ht"][count] <= 140:
                                    if book["reach"][count] <= 142:
                                        if book["ht"][count] <= 135:
                                            if book["age"][count] <= 36.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 159:
                                        if book["ht"][count] <= 150:
                                            if book["reach"][count] <= 146:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 155:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                            else:
                                displayList.append(-1)
                else:
                    if book["tailLn"][count] <= 16:
                        if book["hairLn"][count] <= 8:
                            if book["age"][count] <= 48.0:
                                if book["earLobes"][count] <= 0:
                                    if book["tailLn"][count] <= 15:
                                        if book["hairLn"][count] <= 7:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 40.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    if book["ht"][count] <= 135:
                                        displayList.append(-1)
                                    else:
                                        if book["tailLn"][count] <= 15:
                                            if book["bangLn"][count] <= 6:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                            else:
                                if book["tailLn"][count] <= 12:
                                    if book["reach"][count] <= 141:
                                        displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    if book["reach"][count] <= 142:
                                        displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["reach"][count] <= 160:
                                    if book["bangLn"][count] <= 6:
                                        if book["tailLn"][count] <= 14:
                                            if book["age"][count] <= 36.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["tailLn"][count] <= 15:
                                            if book["ht"][count] <= 135:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                else:
                                    displayList.append(-1)
                            else:
                                if book["ht"][count] <= 130:
                                    displayList.append(-1)
                                else:
                                    if book["tailLn"][count] <= 14:
                                        displayList.append(1)
                                    else:
                                        if book["reach"][count] <= 158:
                                            if book["age"][count] <= 34.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                    else:
                        if book["reach"][count] <= 139:
                            displayList.append(1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["tailLn"][count] <= 19:
                                    if book["ht"][count] <= 135:
                                        displayList.append(-1)
                                    else:
                                        if book["reach"][count] <= 149:
                                            displayList.append(1)
                                        else:
                                            if book["age"][count] <= 38.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["bangLn"][count] <= 7:
                                        if book["tailLn"][count] <= 21:
                                            if book["reach"][count] <= 142:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        displayList.append(1)
                            else:
                                displayList.append(-1)
            else:
                if book["bangLn"][count] <= 5:
                    if book["age"][count] <= 56.0:
                        if book["ht"][count] <= 135:
                            displayList.append(-1)
                        else:
                            if book["tailLn"][count] <= 20:
                                if book["reach"][count] <= 165:
                                    if book["reach"][count] <= 149:
                                        displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 145:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    displayList.append(-1)
                            else:
                                displayList.append(-1)
                    else:
                        if book["ht"][count] <= 160:
                            if book["tailLn"][count] <= 18:
                                displayList.append(-1)
                            else:
                                displayList.append(-1)
                        else:
                            displayList.append(1)
                else:
                    if book["tailLn"][count] <= 20:
                        if book["reach"][count] <= 165:
                            displayList.append(1)
                        else:
                            displayList.append(-1)
                    else:
                        displayList.append(-1)
    return displayList

