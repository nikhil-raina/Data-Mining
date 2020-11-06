import pathlib
import pandas as pd
import numpy as np
from numpy import linalg as LA      # for eighen stuffs
import matplotlib.pyplot as plt


def make_dataFrame(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame



def main():
    fileName = "Abominable_Data_HW05_v4201.csv"
    dataFrame = make_dataFrame(fileName)
    labels_drop = ["EarLobes", "Age"]
    dataFrame = dataFrame.drop(labels=labels_drop, axis=1)         # earlob and age dropped
    np_array = dataFrame.to_numpy()
    # find the eighen vector
    # find the eigenvalues 
    # QUESTION: What to do with Hair, Talk , BanG
    #
    



main()