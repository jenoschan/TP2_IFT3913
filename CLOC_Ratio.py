import sys
import pathlib as pl
import pandas as pd

class CLOC_Ratio:

    path = sys.argv[1]

    def CLOC_Ratio(self, path):
        #if path is not a file 
        if not pl.Path(path).is_file():
            print("Path given is not a file")
        #get file name from path 
        file_name = pl.Path(path).name
        #open file and read it
        source_file = open(path, "r", encoding='utf-8',errors='ignore')
        
        #count the amount of non-empty lines for all paths in tp_1.csv
        count = 0
        for line in source_file:
            if line.strip():
                count += 1
                
        count = int(count)

        #if create tp_1.csv if it doesnt exist
        if not pl.Path("tp_1.csv").exists():
            print("tp_1.csv does not exist, create it using jls.py")
        else:
            #if CLOC_Ratio column is not in the csv file, create it and add the count to corresponding class
            if "CLOC_Ratio" not in open("tp_1.csv").read():
                #make copy of csv file
                df = pd.read_csv("tp_1.csv")
                #add CLOC_Ratio column
                df["CLOC_Ratio"] = ""
                #add count to corresponding class
                for i in range(len(df)):
                    #get class name from path
                    if df["nom de la classe"][i] == file_name:
                        df.at[i, "CLOC_Ratio"] = count

            else:
                df = pd.read_csv("tp_1.csv")
                for i in range(len(df)):
                    if df["nom de la classe"][i] == file_name:
                        df.at[i, "CLOC_Ratio"] = count

            df.to_csv("tp_1.csv", index=False)
            
            
        #iterate through all paths in tp_1.csv
        below10 = 0
        for i in range(len(df)):
            count_others= 0
            commentLines = -35 # on enleve toutes les lignes du copyright claim
            #open path
            source_file = open(df["chemin du ficher"][i], "r", encoding='utf-8',errors='ignore')
            #count the amount of non-empty lines for all paths in tp_1.csv
            for line in source_file:
                if line.strip():
                    count_others += 1
                if "*" in line or "/" in line:
                    commentLines += 1
                df.at[i, "CLOC_Ratio"] = int(commentLines*100/count_others)
            if commentLines*100/count_others < 10:
                below10 += 1


        print('number of classes: ' + str(len(df)))
        print('number of classes with CLOC_Ratio bellow 10: ' + str(below10))
        print('percent ratio of classes with CLOC_Ratio bellow 10: ' + str(below10*100/len(df)))

        
        df.to_csv("tp_1.csv", index=False)

if __name__ == "__main__":
    instance = CLOC_Ratio()

    instance.CLOC_Ratio(instance.path)