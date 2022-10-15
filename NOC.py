from tkinter import W
import sys
import pathlib as pl
import os
import csv
import pandas as pd

class NOC:

    path = sys.argv[1]
    csv_path = sys.argv[2]
    

    def NOC(self, path, csv_path):
        #Create the NOC program that takes as input the path of a folder and the path for tp1_1.csv

        #get path of folder and csv file
        path = sys.argv[1]
        csv_path = sys.argv[2]

        #if path doesnt exist
        if not pl.Path(path).exists():
            print("Path given does not exist")
        #if csv file doesnt exist
        elif not pl.Path(csv_path).exists():
            print("CSV file given does not exist")
        else: 
            print("Path and CSV file given exist")

        #get paths and class names of files in csv
        files = []
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                files.append((row[0], row[2][:-5]))
            csv_file.close()
        files.pop(0)
        
        counts = []
        # get the number of other class mentions inside current class
        for i in range(len(files)):

            count = 0
            # get the number of times the class is mentioned in other classes

            for j in range(len(files)):
                if j != i:
                    f = open(files[j][0], 'r', encoding = 'utf-8', errors='ignore')
                    txt = f.read()
                    f.close()
                    if 'implements ' + str(files[i][1]) in txt or 'extends ' + str(files[i][1]) in txt:
                        count += 1
            counts.append(count)
        
        # adding the column to the csv

        data = pd.read_csv(csv_path)

        if 'NOC' in data.columns:
            data.drop('NOC', axis = 1)
        data['NOC'] = counts

        data.to_csv('tp_2.csv', index=False)


if __name__ == "__main__":
    Lls = NOC()

    Lls.NOC(Lls.path, Lls.csv_path)
