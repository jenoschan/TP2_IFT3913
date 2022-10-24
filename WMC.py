from tkinter import W
import sys
import pathlib as pl
import os
import csv
import pandas as pd

class lWMC:

    path = sys.argv[1]
    csv_path = sys.argv[2]
    

    def lWMC(self, path, csv_path):
        #Create the WMC program that takes as input the path of a folder and the path for tp1_1.csv

        #if path doesnt exist
        if not pl.Path(path).exists():
            print("Path given does not exist")
        #if csv file doesnt exist
        elif not pl.Path(csv_path).exists():
            print("CSV file given does not exist")
        else: 
            print("File has been updated with results")

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
            f = open(files[i][0], 'r', encoding = 'utf-8', errors='ignore')
            txt = f.read()
            f.close()
            count += txt.count('public void')

            counts.append(count)
        
        # adding the column to the csv
        data = pd.read_csv(csv_path)

        if 'WMC' in data.columns:
            data.drop('WMC', axis = 1)
        data['WMC'] = counts

        #sort by WMC
        data = data.sort_values(by=['WMC'], ascending=False)
    
        data.to_csv('tp_2.csv', index=False)
        
        #median of WMC
        median = data['WMC'].median()
        print("Median of WMC is: " + str(median))

if __name__ == "__main__":
    Lls = lWMC()
    Lls.lWMC(Lls.path, Lls.csv_path)
