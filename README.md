# TP2_IFT3913

Jenny Diep (20036864)
Charbel Machaalani (20204556)


Rapport: 
https://docs.google.com/document/d/14R9WeQpYGdCj4hUKa0z97eTgLdVUpKZfozytkgDXoVU/edit?usp=sharing 

Repo: 
https://github.com/jenoschan/TP2_IFT3913 

Pour utiliser CLOC_Ratio.py:

1) commencez par run jls.py avec le dossier source comme argument, cela va generer un fichier tp_2.csv

2) executer CLOC_Ratio avec le path de n'importe quel fichier java dans le dossier que vous analysez comme argument. Le script va print le nombre de classes avec une densitée de commentaire plus petite que 10% et va mettre le ratio de ligne de commentaire sur ligne de code en tout dans une autre colonne dans tp_2.csv pour chaque classe.

Pour utiliser CBO.py:

1) commencez par run jls.py avec le dossier source comme argument, cela va generer un fichier tp_2.csv

2) executer CBO.py avec le chemin du dossier à analyzer et le chemin vers le fichier csv, le script va comparer le contenu avec tp_2.csv est déterminer le couplage de chaque classe avec tous les autres classes. La classe avec le plus haut CBO est imprimé dans le terminal. Le reste des résultats est dans le fichier csv. S'il y a un grand nombre de classe avec un grand nombre de CBO, le code n'est pas modulaire.

Pour utiliser NOC.py

1) commencez par run jls.py avec le dossier source comme argument, cela va generer un fichier tp_2.csv

2) executer NOC.py avec le path du dossier que vous voulez analyser comme premier argument et le fichier tp_2.csv comme deuxieme arguement que jls aurait produit. Le script va ajouter le nombre d'enfants de chaque classe dans le dossier dans la colonne NOC dans tp_2.csv


Pour utiliser WMC.py

1) commencez par run jls.py avec le dossier source comme argument, cela va generer un fichier tp_2.csv

2) executer WMC.py avec le path du dossier que vous voulez analyser comme premier argument et le fichier tp_2.csv comme deuxieme arguement que jls aurait produit. Le script va ajouter le nombre de methodes de chaque classe dans le dossier dans la colonne WMC dans tp_2.csv



