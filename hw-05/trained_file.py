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
    fileName = "hw-05/testing_file.csv"
    dataFrame = pd.read_csv(fileName)
    book = create_dictionary(dataFrame)
    displayList = list()
    for count in range(len(book["age"])):
        if book["tailLn"][count] <= 10:
            if book["tailLn"][count] <= 8:
                if book["bangLn"][count] <= 4:
                    if book["hairLn"][count] <= 9:
                        if book["tailLn"][count] <= 6:
                            if book["reach"][count] <= 162:
                                if book["age"][count] <= 48.0:
                                    displayList.append(1)
                                else:
                                    if book["earLobes"][count] <= 0:
                                        if book["reach"][count] <= 150:
                                            if book["tailLn"][count] <= 5:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        if book["ht"][count] <= 135:
                                            if book["reach"][count] <= 138:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                            else:
                                displayList.append(-1)
                        else:
                            if book["tailLn"][count] <= 7:
                                if book["bangLn"][count] <= 3:
                                    displayList.append(-1)
                                else:
                                    if book["hairLn"][count] <= 8:
                                        if book["age"][count] <= 46.0:
                                            if book["ht"][count] <= 135:
                                                if book["earLobes"][count] <= 0:
                                                    displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                            else:
                                                if book["ht"][count] <= 155:
                                                    displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        if book["ht"][count] <= 110:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 40.0:
                                                displayList.append(1)
                                            else:
                                                if book["age"][count] <= 42.0:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                            else:
                                if book["reach"][count] <= 153:
                                    if book["ht"][count] <= 145:
                                        if book["hairLn"][count] <= 6:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 24.0:
                                                displayList.append(1)
                                            else:
                                                if book["ht"][count] <= 130:
                                                    if book["earLobes"][count] <= 0:
                                                        displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                                else:
                                                    if book["reach"][count] <= 138:
                                                        displayList.append(1)
                                                    else:
                                                        if book["reach"][count] <= 147:
                                                            if book["age"][count] <= 38.0:
                                                                displayList.append(1)
                                                            else:
                                                                if book["reach"][count] <= 144:
                                                                    displayList.append(-1)
                                                                else:
                                                                    displayList.append(1)
                                                        else:
                                                            displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    if book["earLobes"][count] <= 0:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 36.0:
                                            displayList.append(1)
                                        else:
                                            if book["age"][count] <= 62.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                    else:
                        if book["reach"][count] <= 164:
                            displayList.append(1)
                        else:
                            if book["tailLn"][count] <= 2:
                                displayList.append(1)
                            else:
                                displayList.append(-1)
                else:
                    displayList.append(1)
            else:
                if book["hairLn"][count] <= 9:
                    if book["bangLn"][count] <= 5:
                        if book["ht"][count] <= 130:
                            if book["hairLn"][count] <= 8:
                                if book["reach"][count] <= 118:
                                    displayList.append(1)
                                else:
                                    if book["bangLn"][count] <= 4:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 46.0:
                                            if book["reach"][count] <= 133:
                                                if book["ht"][count] <= 125:
                                                    if book["age"][count] <= 42.0:
                                                        displayList.append(-1)
                                                    else:
                                                        if book["age"][count] <= 44.0:
                                                            displayList.append(1)
                                                        else:
                                                            displayList.append(-1)
                                                else:
                                                    if book["earLobes"][count] <= 0:
                                                        displayList.append(1)
                                                    else:
                                                        if book["age"][count] <= 36.0:
                                                            displayList.append(-1)
                                                        else:
                                                            if book["reach"][count] <= 132:
                                                                displayList.append(-1)
                                                            else:
                                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                            else:
                                if book["age"][count] <= 50.0:
                                    if book["reach"][count] <= 133:
                                        if book["ht"][count] <= 125:
                                            if book["reach"][count] <= 126:
                                                if book["bangLn"][count] <= 4:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 36.0:
                                                if book["age"][count] <= 34.0:
                                                    displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 4:
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                else:
                                    displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["reach"][count] <= 139:
                                    if book["age"][count] <= 24.0:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 46.0:
                                            displayList.append(1)
                                        else:
                                            if book["age"][count] <= 48.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                else:
                                    if book["reach"][count] <= 142:
                                        if book["ht"][count] <= 135:
                                            if book["age"][count] <= 24.0:
                                                if book["hairLn"][count] <= 5:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["reach"][count] <= 137:
                                        if book["age"][count] <= 40.0:
                                            displayList.append(1)
                                        else:
                                            if book["hairLn"][count] <= 7:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        if book["reach"][count] <= 138:
                                            if book["hairLn"][count] <= 5:
                                                displayList.append(1)
                                            else:
                                                if book["age"][count] <= 42.0:
                                                    if book["hairLn"][count] <= 8:
                                                        displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                                else:
                                                    displayList.append(-1)
                                        else:
                                            if book["hairLn"][count] <= 7:
                                                displayList.append(-1)
                                            else:
                                                if book["age"][count] <= 46.0:
                                                    if book["age"][count] <= 44.0:
                                                        if book["tailLn"][count] <= 9:
                                                            if book["age"][count] <= 30.0:
                                                                displayList.append(-1)
                                                            else:
                                                                if book["age"][count] <= 34.0:
                                                                    displayList.append(1)
                                                                else:
                                                                    displayList.append(-1)
                                                        else:
                                                            displayList.append(-1)
                                                    else:
                                                        if book["reach"][count] <= 140:
                                                            displayList.append(-1)
                                                        else:
                                                            displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                else:
                                    if book["bangLn"][count] <= 3:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 62.0:
                                            if book["bangLn"][count] <= 4:
                                                if book["reach"][count] <= 144:
                                                    displayList.append(1)
                                                else:
                                                    if book["ht"][count] <= 145:
                                                        displayList.append(-1)
                                                    else:
                                                        if book["reach"][count] <= 160:
                                                            if book["hairLn"][count] <= 5:
                                                                if book["age"][count] <= 44.0:
                                                                    displayList.append(1)
                                                                else:
                                                                    displayList.append(-1)
                                                            else:
                                                                displayList.append(1)
                                                        else:
                                                            if book["hairLn"][count] <= 5:
                                                                displayList.append(1)
                                                            else:
                                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                    else:
                        if book["ht"][count] <= 130:
                            if book["reach"][count] <= 133:
                                if book["ht"][count] <= 125:
                                    if book["hairLn"][count] <= 8:
                                        if book["reach"][count] <= 121:
                                            displayList.append(1)
                                        else:
                                            if book["hairLn"][count] <= 6:
                                                if book["age"][count] <= 44.0:
                                                    if book["age"][count] <= 28.0:
                                                        displayList.append(-1)
                                                    else:
                                                        displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                            else:
                                                if book["reach"][count] <= 127:
                                                    if book["ht"][count] <= 120:
                                                        displayList.append(-1)
                                                    else:
                                                        displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                                    else:
                                        if book["ht"][count] <= 110:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 44.0:
                                                displayList.append(1)
                                            else:
                                                if book["age"][count] <= 48.0:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                else:
                                    if book["hairLn"][count] <= 7:
                                        if book["age"][count] <= 38.0:
                                            displayList.append(1)
                                        else:
                                            if book["reach"][count] <= 128:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        displayList.append(1)
                            else:
                                if book["earLobes"][count] <= 0:
                                    if book["age"][count] <= 48.0:
                                        if book["tailLn"][count] <= 9:
                                            if book["age"][count] <= 38.0:
                                                displayList.append(1)
                                            else:
                                                if book["age"][count] <= 40.0:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                        else:
                                            if book["reach"][count] <= 136:
                                                if book["age"][count] <= 38.0:
                                                    if book["hairLn"][count] <= 5:
                                                        displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                                else:
                                                    if book["hairLn"][count] <= 7:
                                                        if book["age"][count] <= 42.0:
                                                            displayList.append(1)
                                                        else:
                                                            displayList.append(-1)
                                                    else:
                                                        displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["tailLn"][count] <= 9:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 38.0:
                                            displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 135:
                                                displayList.append(-1)
                                            else:
                                                if book["hairLn"][count] <= 8:
                                                    displayList.append(1)
                                                else:
                                                    displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["bangLn"][count] <= 6:
                                    if book["ht"][count] <= 135:
                                        if book["reach"][count] <= 138:
                                            if book["age"][count] <= 36.0:
                                                if book["age"][count] <= 32.0:
                                                    displayList.append(1)
                                                else:
                                                    if book["tailLn"][count] <= 9:
                                                        displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["age"][count] <= 34.0:
                                                if book["age"][count] <= 24.0:
                                                    if book["tailLn"][count] <= 9:
                                                        displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                            else:
                                                if book["reach"][count] <= 139:
                                                    if book["age"][count] <= 40.0:
                                                        displayList.append(-1)
                                                    else:
                                                        displayList.append(1)
                                                else:
                                                    if book["age"][count] <= 40.0:
                                                        if book["age"][count] <= 36.0:
                                                            displayList.append(-1)
                                                        else:
                                                            displayList.append(1)
                                                    else:
                                                        displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 164:
                                        if book["reach"][count] <= 148:
                                            if book["reach"][count] <= 147:
                                                if book["age"][count] <= 48.0:
                                                    if book["ht"][count] <= 135:
                                                        if book["reach"][count] <= 137:
                                                            displayList.append(1)
                                                        else:
                                                            if book["age"][count] <= 36.0:
                                                                if book["age"][count] <= 32.0:
                                                                    displayList.append(1)
                                                                else:
                                                                    displayList.append(-1)
                                                            else:
                                                                displayList.append(1)
                                                    else:
                                                        displayList.append(1)
                                                else:
                                                    if book["age"][count] <= 50.0:
                                                        displayList.append(-1)
                                                    else:
                                                        displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 160:
                                            if book["age"][count] <= 58.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["reach"][count] <= 139:
                                        if book["hairLn"][count] <= 7:
                                            if book["age"][count] <= 36.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 6:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    if book["reach"][count] <= 170:
                                        displayList.append(1)
                                    else:
                                        if book["age"][count] <= 62.0:
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                else:
                    if book["hairLn"][count] <= 10:
                        if book["ht"][count] <= 130:
                            if book["reach"][count] <= 132:
                                if book["ht"][count] <= 115:
                                    displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 127:
                                        displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 125:
                                            if book["reach"][count] <= 131:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(1)
                            else:
                                if book["bangLn"][count] <= 5:
                                    displayList.append(-1)
                                else:
                                    if book["age"][count] <= 30.0:
                                        displayList.append(1)
                                    else:
                                        if book["age"][count] <= 54.0:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["bangLn"][count] <= 6:
                                    if book["reach"][count] <= 140:
                                        if book["age"][count] <= 50.0:
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    displayList.append(1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["reach"][count] <= 139:
                                        if book["bangLn"][count] <= 5:
                                            if book["tailLn"][count] <= 9:
                                                if book["bangLn"][count] <= 4:
                                                    displayList.append(-1)
                                                else:
                                                    displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 7:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    displayList.append(1)
                    else:
                        displayList.append(1)
        else:
            if book["hairLn"][count] <= 10:
                if book["bangLn"][count] <= 5:
                    if book["tailLn"][count] <= 16:
                        if book["earLobes"][count] <= 0:
                            if book["reach"][count] <= 143:
                                if book["ht"][count] <= 130:
                                    displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 138:
                                        if book["reach"][count] <= 136:
                                            displayList.append(1)
                                        else:
                                            if book["bangLn"][count] <= 4:
                                                if book["age"][count] <= 42.0:
                                                    if book[""][count] <= 0:
