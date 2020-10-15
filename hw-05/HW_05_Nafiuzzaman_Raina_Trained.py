import csv 
def csv_parser():
	book = {
        "age"       :  [],
        "ht"        :  [],
        "tailLn"    :  [],
        "hairLn"    :  [],
        "bangLn"    :  [],
        "reach"     :  [],
        "earLobes"  :  []
    }
    fileName = input('Please input the file name: ')
    fileReader = csv.reader(open(fileName))
    displayList = list()
    for feature_rows in fileReader:
		if feature_rows["tailLn"] <= 0.4949133483734521:
			if feature_rows["tailLn"] <= 0.22522310255616929:
				if feature_rows["bangLn"] <= 0.10930860115904467:
					displayList.append(1)
				else:
					displayList.append(1)
			else:
				if feature_rows["hairLn"] <= 0.4009403975364361:
					displayList.append(1)
				else:
					displayList.append(1)
		else:
			if feature_rows["hairLn"] <= 0.4129189771150357:
				if feature_rows["bangLn"] <= 0.332517754168703:
					displayList.append(-1)
				else:
					displayList.append(-1)
			else:
				if feature_rows["bangLn"] <= 0.33711792919067174:
					displayList.append(1)
				else:
					displayList.append(1)
	return 0


def main():
    lst = csv_parser()
    for i in lst:
        print(i)
main()
