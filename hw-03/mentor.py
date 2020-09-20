import pandas as pd

def make_dataFrame(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame




def main():
    fileName = "HW03_Marked_Cards_TRAINING_v07.csv"
    dataFrame = make_dataFrame(fileName)
    targetAttr = dataFrame    

main()
