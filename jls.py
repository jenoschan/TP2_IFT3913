import pathlib as pl
import os
import sys
import csv

class jls:

    path = sys.argv[1]

    def jls(self, path):
        
        root = path.split('\\')[-1]
        content = []
        for files in os.walk(path):
            if len(files[2]) > 0:
                for file in files[2]:
                    if file[-5:] == '.java':
                        content.append(files[0] + '\\' + file)

        result = "chemin du ficher,nom du paquet,nom de la classe\n"
        for item in content:
            toAdd = item + ','
            candidate = item.split('\\')
            while candidate[0] != root:
                candidate.pop(0)
            candidate.pop(0)
            while len(candidate) > 1:
                if len(candidate) > 2:
                    toAdd += candidate.pop(0) + '.'
                else: toAdd += candidate.pop(0)
            toAdd += ',' + candidate.pop(0)
            result += toAdd + '\n'

        with open("tp_2.csv", "w") as file:
            file.write(result)
            file.close()

        #if path doesnt exist
        if not pl.Path(path).exists():
            print("Path is in a valid format, but doesn't exist on this computer")
            return

        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            #print directories
            if level == 0:
                print(root)
            #TODO : fix formatting
            indent = ' ' * 4 * (level) + "|__"
            print('{}{}/'.format(indent, os.path.basename(root)))
            #print files
            subindent = ' ' * 4 * (level+1) + "|__"
            for f in files:
                print('{}{}'.format(subindent, f))

if __name__ == '__main__':
    Jls = jls()

    Jls.jls(Jls.path)