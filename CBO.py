from tkinter import W
import sys
import pathlib as pl
import os
import csv
import pandas as pd

class CBO:

    path = sys.argv[1]
    csv_path = sys.argv[2]
    

    def cbo(self, path, csv_path):
        #Create the cbo program that takes as input the path of a folder and the path for tp1_1.csv

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
        visits = []
        for i in range(len(files)):
            visited = []
            count = 0
            f = open(files[i][0], 'r', encoding = 'utf-8', errors='ignore')
            txt = f.read()
            f.close()
            for j in range(len(files)):
                if j != i:
                    if files[j][1] in txt:
                        count += 1
                        visited.append(files[j][1])
            visits.append(visited)

            # get the number of times the class is mentioned in other classes

            for j in range(len(files)):
                if j != i:
                    f = open(files[j][0], 'r', encoding = 'utf-8', errors='ignore')
                    txt = f.read()
                    f.close()
                    if files[i][1] in txt and files[j][1] not in visits[i]:
                        count += 1
                        if i == 4:
                            print(files[j][0])
            counts.append(count)
        
        # adding the column to the csv

        data = pd.read_csv(csv_path)

        if 'CBO' in data.columns:
            data.drop('CBO', axis = 1)
        data['CBO'] = counts

        data.to_csv('tp_2.csv', index=False)
        
        #NOTE: if CBO is high, class is not modular and reutilizable...
        #TODO: reorganize CSV in asceding order of CBO
        
        #in tp_2.csv, reorganize in ascending order of CBO
        data = pd.read_csv('tp_2.csv')
        
        data = data.sort_values(by=['CBO'], ascending=False)
        
        data.to_csv('tp_2.csv', index=False)
        

if __name__ == "__main__":
    CBO = CBO()

    CBO.cbo(CBO.path, CBO.csv_path)
