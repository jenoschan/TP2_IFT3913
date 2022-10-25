import sys
import pathlib as pl
import pandas as pd


class RFC:

    def RFC(self):
        #if create tp_2.csv if it doesnt exist
        if not pl.Path("tp_2.csv").exists():
            print("tp_2.csv does not exist, create it using jls.py")
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
                #count all function calls
                for line in source_file:
                    if "();" in line:
                        count += 1
                    if "(" && ");" in line:
                        count += 1
                        
                if csv_file["nom de la classe"][i] == pl.Path(path).name:
                    #if CC column doesnt exist, create it
                    if "CC" not in open("tp_2.csv").read():
                        csv_file["CC"] = ""
                        csv_file.at[i, "RFC"] = count
                    else:
                        csv_file.at[i, "RFC"] = count
                        
                #acending order of CC
            csv_file = csv_file.sort_values(by=['RFC'], ascending=False)
                
            csv_file.to_csv("tp_2.csv", index=False, encoding='utf-8')
            
if __name__ == "__main__":
    RFC = RFC()
    RFC.RFC()