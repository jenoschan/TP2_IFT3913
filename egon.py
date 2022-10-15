from math import ceil
import os
import sys
import csv
import pandas as pd #pip install pandas

import pathlib as pl

class egon:
    def egon(self):
        #given a folder with java files with a threshold, print the number of classes that have a coupling higher than the threshold
        #get path of folder and threshold
        path = sys.argv[1]
        threshold = sys.argv[2]

        #if tp1_1.csv doesnt exist
        if not pl.Path("tp_2.csv").exists():
            print("tp_2.csv does not exist, create it using jls.py")

        #if path doesnt exist
        elif not pl.Path(path).exists():
            print("Path given does not exist")

        df = pd.read_csv('tp_2.csv')

        #new data fram with sorted values of NVLOC column in descending order
        df = df.sort_values(by=['NVLOC'], ascending=False)
        #new dataframe with sorted values of CSEC column in descending order
        df2 = df.sort_values(by=['CSEC'], ascending=False)

        #threashold number from len(df)
        threshold = ceil(int(threshold)/100 * len(df))

        #get the threshold value from beggining of df and df2
        threshold_value = df.head(threshold)
        threshold_value2 = df2.head(threshold)
        
        #join the two dataframes
        df3 = pd.concat([threshold_value, threshold_value2])
        duplicatedRows = df3[df3.duplicated()]
        
        #if tp_1B.csv doesnt exist
        desired_path = ".\TP1_IFT3913\PARTIE4"
        if not pl.Path("tp_1B.csv").exists():
            with open('tp_1B.csv', 'a') as f:
                f.write("chemin du ficher,nom du paquet,nom de la classe, NVLOC, CSEC\n")
                df3.to_csv(f, header=False, index=False)
        else:
            os.remove("tp_1B.csv")
            with open('tp_1B.csv', 'a') as f:
                f.write("chemin du ficher,nom du paquet,nom de la classe, NVLOC, CSEC\n")
                df3.to_csv(f, header=False, index=False)
            

if __name__ == "__main__":
    instance = egon()
    instance.egon()

