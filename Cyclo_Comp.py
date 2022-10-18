import math
import pathlib as pl
import pandas as pd

class CycloComp:
    
    def cyclocomp(self):
        #calculate cyclomatic complexity for all files in tp_2.csv
        #and add the column to the csv
        
        #if tp_2.csv doesnt exist
        if not pl.Path("tp_2.csv").exists():
            print ("tp_2.csv does not exist, create it with jls.py first")
        else:
        #for line in csv file, get path 
            csv_file = pd.read_csv("tp_2.csv")
            #iterate through lines in csv file
            for i in range(len(csv_file)):
                #get chemin du fichier
                path = csv_file["chemin du ficher"][i]
                #read path
                source_file = open(path, "r", encoding='utf-8',errors='ignore')
                
                count = 0 
                #for every conditional contruct in the file
                for line in source_file:
                    if 'if' in line or 'for' in line or 'while' in line or 'case' in line:
                        count += 1
                    #if there are any additional boolean condition
                    if '&&' in line or '||' in line:
                        count += 1
                source_file.close()
                
                #in tp_2.csv, add the cyclomatic complexity to the corresponding class
                for i in range(len(csv_file)):
                    if csv_file["nom de la classe"][i] == pl.Path(path).name:
                        #if CC column doesnt exist, create it
                        if "CC" not in open("tp_2.csv").read():
                            csv_file["CC"] = ""
                            csv_file.at[i, "CC"] = count
                        else:
                            csv_file.at[i, "CC"] = count
                
                #acending order of CC
                csv_file = csv_file.sort_values(by=['CC'], ascending=True)
                
                csv_file.to_csv("tp_2.csv", index=False, encoding='utf-8')
            
            #count the amount of classes with CC < 10
            below10 = 0
            for i in range(len(csv_file)):
                if csv_file["CC"][i] < 10:
                    below10 += 1
                
            result = math.floor(below10/len(csv_file)*100)
            print("The percentage of classes with CC < 10 is: ", result, "%")
            

if __name__ == '__main__':
    CycloComp = CycloComp()

    CycloComp.cyclocomp()