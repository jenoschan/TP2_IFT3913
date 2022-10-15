from radon.visitors import ComplexityVisitor
import sys
import pathlib as pl
import pandas as pd

class CycloComp:

    path = sys.argv[1]
    
    def cyclocomp(self, path):
        #calculate cyclomatic complexity for all files in tp_2.csv
        #and add the column to the csv
        
        #if path is not a file
        if not pl.Path(path).is_file():
            print("Path given is not a file")
        else: 
            #read file 
            source_file = open(path, "r", encoding='utf-8',errors='ignore')
            for line in source_file:
                #get chemin du fichier from line
                chemin = line.split(",")[0]
                #get cyclomatic complexity for chemin
                cc_value = ComplexityVisitor.from_code(open(chemin, "r", encoding='utf-8',errors='ignore').read()).total_complexity
                #get class name from chemin
                file_name = pl.Path(chemin).name
                #if create tp_2.csv if it doesnt exist
                if not pl.Path("tp_2.csv").exists():
                    print("tp_2.csv does not exist, create it using jls.py")
                else:
                    #if CC column is not in the csv file, create it and add the count to corresponding class
                    if "CC" not in open("tp_2.csv").read():
                        #make copy of csv file
                        df = pd.read_csv("tp_2.csv")
                        #add CC column
                        df["CC"] = ""
                        #add count to corresponding class
                        for i in range(len(df)):
                            #get class name from path
                            if df["nom de la classe"][i] == file_name:
                                #df["CC"][i] = cc_value	
                                df.at[i, "CC"] = cc_value
                    else:
                        df = pd.read_csv("tp_2.csv")
                        for i in range(len(df)):
                            if df["nom de la classe"][i] == file_name:
                                df.at[i, "CC"] = cc_value
                                
                                