import csv


def csv_parser(fileName, attr_num):
    threshold = 0
    fileReader = csv.reader(open(fileName))
    for row in fileReader:
        value = row[attr_num]
        if (value < threshold):
            print("The card is +1")
        else:
            print("The card is -1")
            
