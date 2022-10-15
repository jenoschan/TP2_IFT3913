import sys
import pathlib as pl
import pandas as pd

class nvloc:

    path = sys.argv[1]

    def nvloc(self, path):
        #if path is not a file 
        if not pl.Path(path).is_file():
            print("Path given is not a file")
        #get file name from path 
        file_name = pl.Path(path).name
        #open file and read it
        source_file = open(path, "r", encoding='utf-8',errors='ignore')
        
        #count the amount of non-empty lines for all paths in tp_2.csv
        count = 0
        for line in source_file:
            if line.strip():
                count += 1
                
        count = int(count)
        print(count)

        #if create tp_2.csv if it doesnt exist
        if not pl.Path("tp_2.csv").exists():
            print("tp_2.csv does not exist, create it using jls.py")
        else:
            #if NVLOC column is not in the csv file, create it and add the count to corresponding class
            if "NVLOC" not in open("tp_2.csv").read():
                #make copy of csv file
                df = pd.read_csv("tp_2.csv")
                #add NVLOC column
                df["NVLOC"] = ""
                #add count to corresponding class
                for i in range(len(df)):
                    #get class name from path
                    if df["nom de la classe"][i] == file_name:
                        #df["NVLOC"][i] = count	
                        df.at[i, "NVLOC"] = count

            else:
                df = pd.read_csv("tp_2.csv")
                for i in range(len(df)):
                    if df["nom de la classe"][i] == file_name:
                        df.at[i, "NVLOC"] = count

            df.to_csv("tp_2.csv", index=False)
            
            
        #iterate through all paths in tp_2.csv
        for i in range(len(df)):
            count_others= 0
            #open path
            source_file = open(df["chemin du ficher"][i], "r", encoding='utf-8',errors='ignore')
            #count the amount of non-empty lines for all paths in tp_2.csv
            for line in source_file:
                if line.strip():
                    count_others += 1
                df.at[i, "NVLOC"] = int(count_others)
        
        df.to_csv("tp_2.csv", index=False)

if __name__ == "__main__":
    instance = nvloc()

    instance.nvloc(instance.path)