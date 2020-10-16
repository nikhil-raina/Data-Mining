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
    fileName = input('Please input the file name: ')
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
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        if book["ht"][count] <= 135:
                                            displayList.append(1)
                                        else:
                                            displayList.append(1)
                            else:
                                displayList.append(-1)
                        else:
                            if book["age"][count] <= 54.0:
                                if book["age"][count] <= 52.0:
                                    if book["reach"][count] <= 164:
                                        if book["ht"][count] <= 145:
                                            if book["reach"][count] <= 145:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["earLobes"][count] <= 0:
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
                                    if book["age"][count] <= 62.0:
                                        displayList.append(-1)
                                    else:
                                        displayList.append(1)
                    else:
                        if book["reach"][count] <= 164:
                            displayList.append(1)
                        else:
                            displayList.append(-1)
                else:
                    displayList.append(1)
            else:
                if book["hairLn"][count] <= 9:
                    if book["bangLn"][count] <= 5:
                        if book["ht"][count] <= 135:
                            if book["earLobes"][count] <= 0:
                                if book["ht"][count] <= 130:
                                    if book["reach"][count] <= 122:
                                        displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 125:
                                            displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 133:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 138:
                                        if book["age"][count] <= 46.0:
                                            displayList.append(1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["hairLn"][count] <= 6:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 24.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                            else:
                                if book["bangLn"][count] <= 4:
                                    displayList.append(-1)
                                else:
                                    if book["age"][count] <= 46.0:
                                        if book["hairLn"][count] <= 6:
                                            displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 138:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        if book["hairLn"][count] <= 5:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["reach"][count] <= 140:
                                    displayList.append(1)
                                else:
                                    displayList.append(-1)
                            else:
                                if book["bangLn"][count] <= 3:
                                    if book["hairLn"][count] <= 8:
                                        displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    if book["age"][count] <= 62.0:
                                        if book["bangLn"][count] <= 4:
                                            if book["reach"][count] <= 144:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                    else:
                        if book["ht"][count] <= 130:
                            if book["earLobes"][count] <= 0:
                                if book["age"][count] <= 48.0:
                                    if book["reach"][count] <= 135:
                                        if book["ht"][count] <= 125:
                                            if book["reach"][count] <= 130:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["hairLn"][count] <= 7:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                    else:
                                        if book["reach"][count] <= 138:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    displayList.append(-1)
                            else:
                                if book["reach"][count] <= 133:
                                    if book["ht"][count] <= 125:
                                        if book["hairLn"][count] <= 8:
                                            if book["reach"][count] <= 127:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["hairLn"][count] <= 7:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    if book["tailLn"][count] <= 9:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 46.0:
                                            if book["age"][count] <= 38.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["bangLn"][count] <= 6:
                                    if book["ht"][count] <= 135:
                                        if book["reach"][count] <= 138:
                                            if book["age"][count] <= 36.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["age"][count] <= 34.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 164:
                                        if book["reach"][count] <= 148:
                                            if book["reach"][count] <= 147:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["reach"][count] <= 139:
                                        if book["hairLn"][count] <= 7:
                                            displayList.append(1)
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
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                            else:
                                if book["bangLn"][count] <= 5:
                                    displayList.append(-1)
                                else:
                                    if book["age"][count] <= 30.0:
                                        displayList.append(1)
                                    else:
                                        displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["bangLn"][count] <= 6:
                                    if book["reach"][count] <= 142:
                                        if book["age"][count] <= 50.0:
                                            if book["bangLn"][count] <= 4:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["age"][count] <= 54.0:
                                        displayList.append(1)
                                    else:
                                        displayList.append(1)
                            else:
                                if book["ht"][count] <= 135:
                                    if book["reach"][count] <= 139:
                                        if book["bangLn"][count] <= 5:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    displayList.append(1)
                    else:
                        displayList.append(1)
        else:
            if book["hairLn"][count] <= 10:
                if book["bangLn"][count] <= 5:
                    if book["tailLn"][count] <= 15:
                        if book["earLobes"][count] <= 0:
                            if book["reach"][count] <= 143:
                                if book["ht"][count] <= 130:
                                    displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 138:
                                        if book["tailLn"][count] <= 11:
                                            displayList.append(1)
                                        else:
                                            if book["hairLn"][count] <= 8:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 140:
                                            if book["reach"][count] <= 141:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                            else:
                                displayList.append(-1)
                        else:
                            if book["ht"][count] <= 135:
                                displayList.append(-1)
                            else:
                                if book["bangLn"][count] <= 4:
                                    if book["bangLn"][count] <= 3:
                                        displayList.append(-1)
                                    else:
                                        if book["tailLn"][count] <= 13:
                                            if book["age"][count] <= 58.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 34.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["tailLn"][count] <= 14:
                                        displayList.append(1)
                                    else:
                                        if book["reach"][count] <= 145:
                                            displayList.append(1)
                                        else:
                                            if book["age"][count] <= 38.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                    else:
                        if book["tailLn"][count] <= 18:
                            if book["reach"][count] <= 153:
                                if book["ht"][count] <= 145:
                                    if book["bangLn"][count] <= 4:
                                        displayList.append(-1)
                                    else:
                                        if book["reach"][count] <= 144:
                                            if book["hairLn"][count] <= 9:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["age"][count] <= 54.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["earLobes"][count] <= 0:
                                        if book["hairLn"][count] <= 8:
                                            if book["age"][count] <= 48.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["reach"][count] <= 150:
                                            displayList.append(1)
                                        else:
                                            if book["ht"][count] <= 150:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                            else:
                                displayList.append(-1)
                        else:
                            displayList.append(-1)
                else:
                    if book["tailLn"][count] <= 17:
                        if book["hairLn"][count] <= 8:
                            if book["ht"][count] <= 130:
                                displayList.append(-1)
                            else:
                                if book["tailLn"][count] <= 13:
                                    if book["earLobes"][count] <= 0:
                                        if book["bangLn"][count] <= 6:
                                            if book["reach"][count] <= 140:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["hairLn"][count] <= 5:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 135:
                                            if book["reach"][count] <= 137:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["bangLn"][count] <= 6:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                else:
                                    if book["bangLn"][count] <= 6:
                                        if book["reach"][count] <= 146:
                                            if book["ht"][count] <= 140:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["earLobes"][count] <= 0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 42.0:
                                            if book["ht"][count] <= 135:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["bangLn"][count] <= 7:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                        else:
                            if book["ht"][count] <= 130:
                                if book["bangLn"][count] <= 7:
                                    if book["age"][count] <= 16.0:
                                        displayList.append(1)
                                    else:
                                        if book["earLobes"][count] <= 0:
                                            if book["reach"][count] <= 120:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 133:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    displayList.append(1)
                            else:
                                if book["reach"][count] <= 160:
                                    if book["earLobes"][count] <= 0:
                                        if book["bangLn"][count] <= 6:
                                            if book["reach"][count] <= 142:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 68.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        if book["tailLn"][count] <= 14:
                                            if book["ht"][count] <= 135:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["bangLn"][count] <= 6:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                else:
                                    if book["bangLn"][count] <= 6:
                                        if book["earLobes"][count] <= 0:
                                            displayList.append(-1)
                                        else:
                                            if book["tailLn"][count] <= 14:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        if book["earLobes"][count] <= 0:
                                            if book["ht"][count] <= 155:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["tailLn"][count] <= 15:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                    else:
                        if book["earLobes"][count] <= 0:
                            if book["tailLn"][count] <= 20:
                                if book["hairLn"][count] <= 8:
                                    if book["reach"][count] <= 139:
                                        displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 6:
                                            if book["reach"][count] <= 159:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 46.0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    if book["reach"][count] <= 147:
                                        if book["age"][count] <= 54.0:
                                            if book["reach"][count] <= 144:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        if book["reach"][count] <= 163:
                                            if book["ht"][count] <= 150:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["bangLn"][count] <= 6:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                            else:
                                if book["reach"][count] <= 139:
                                    displayList.append(1)
                                else:
                                    if book["tailLn"][count] <= 22:
                                        if book["age"][count] <= 28.0:
                                            displayList.append(1)
                                        else:
                                            if book["bangLn"][count] <= 7:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                    else:
                                        displayList.append(-1)
                        else:
                            if book["reach"][count] <= 145:
                                if book["ht"][count] <= 140:
                                    if book["reach"][count] <= 140:
                                        if book["tailLn"][count] <= 22:
                                            if book["age"][count] <= 32.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(-1)
                                    else:
                                        if book["ht"][count] <= 135:
                                            displayList.append(-1)
                                        else:
                                            if book["reach"][count] <= 143:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                                else:
                                    displayList.append(1)
                            else:
                                displayList.append(-1)
            else:
                if book["bangLn"][count] <= 5:
                    if book["tailLn"][count] <= 16:
                        if book["ht"][count] <= 130:
                            if book["reach"][count] <= 131:
                                displayList.append(-1)
                            else:
                                if book["age"][count] <= 36.0:
                                    displayList.append(-1)
                                else:
                                    displayList.append(-1)
                        else:
                            if book["earLobes"][count] <= 0:
                                if book["age"][count] <= 48.0:
                                    if book["reach"][count] <= 143:
                                        displayList.append(1)
                                    else:
                                        if book["tailLn"][count] <= 14:
                                            if book["hairLn"][count] <= 11:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            if book["tailLn"][count] <= 15:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                else:
                                    if book["reach"][count] <= 141:
                                        displayList.append(1)
                                    else:
                                        if book["tailLn"][count] <= 15:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                            else:
                                if book["tailLn"][count] <= 15:
                                    if book["ht"][count] <= 135:
                                        if book["reach"][count] <= 137:
                                            displayList.append(1)
                                        else:
                                            if book["reach"][count] <= 140:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                    else:
                                        displayList.append(1)
                                else:
                                    if book["reach"][count] <= 156:
                                        if book["ht"][count] <= 145:
                                            if book["bangLn"][count] <= 4:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 4:
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                    else:
                        if book["hairLn"][count] <= 11:
                            if book["age"][count] <= 28.0:
                                displayList.append(1)
                            else:
                                if book["reach"][count] <= 138:
                                    displayList.append(1)
                                else:
                                    if book["ht"][count] <= 140:
                                        displayList.append(-1)
                                    else:
                                        if book["reach"][count] <= 147:
                                            displayList.append(1)
                                        else:
                                            if book["tailLn"][count] <= 17:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                        else:
                            if book["age"][count] <= 56.0:
                                if book["earLobes"][count] <= 0:
                                    if book["tailLn"][count] <= 23:
                                        if book["ht"][count] <= 145:
                                            if book["reach"][count] <= 140:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["age"][count] <= 40.0:
                                        displayList.append(1)
                                    else:
                                        if book["age"][count] <= 44.0:
                                            displayList.append(-1)
                                        else:
                                            if book["age"][count] <= 52.0:
                                                displayList.append(-1)
                                            else:
                                                displayList.append(-1)
                            else:
                                displayList.append(-1)
                else:
                    if book["tailLn"][count] <= 23:
                        if book["tailLn"][count] <= 18:
                            if book["ht"][count] <= 130:
                                if book["reach"][count] <= 135:
                                    if book["age"][count] <= 54.0:
                                        if book["ht"][count] <= 115:
                                            displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                    else:
                                        displayList.append(-1)
                                else:
                                    if book["bangLn"][count] <= 7:
                                        displayList.append(-1)
                                    else:
                                        displayList.append(1)
                            else:
                                if book["reach"][count] <= 168:
                                    if book["age"][count] <= 64.0:
                                        displayList.append(1)
                                    else:
                                        if book["age"][count] <= 66.0:
                                            displayList.append(-1)
                                        else:
                                            if book["tailLn"][count] <= 14:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                else:
                                    if book["ht"][count] <= 165:
                                        displayList.append(-1)
                                    else:
                                        if book["age"][count] <= 62.0:
                                            displayList.append(1)
                                        else:
                                            displayList.append(-1)
                        else:
                            if book["age"][count] <= 50.0:
                                if book["hairLn"][count] <= 11:
                                    if book["reach"][count] <= 146:
                                        displayList.append(1)
                                    else:
                                        if book["bangLn"][count] <= 6:
                                            if book["ht"][count] <= 150:
                                                displayList.append(1)
                                            else:
                                                displayList.append(-1)
                                        else:
                                            displayList.append(1)
                                else:
                                    if book["age"][count] <= 48.0:
                                        displayList.append(1)
                                    else:
                                        displayList.append(1)
                            else:
                                if book["reach"][count] <= 157:
                                    if book["reach"][count] <= 142:
                                        displayList.append(1)
                                    else:
                                        if book["ht"][count] <= 140:
                                            displayList.append(-1)
                                        else:
                                            if book["earLobes"][count] <= 0:
                                                displayList.append(1)
                                            else:
                                                displayList.append(1)
                                else:
                                    displayList.append(-1)
                    else:
                        if book["hairLn"][count] <= 11:
                            displayList.append(-1)
                        else:
                            displayList.append(1)
    return displayList

def main():
    lst = csv_parser()
    for result in lst:
        print(result)
main()
