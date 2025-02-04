# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

import os
os.chdir(os.path.dirname(__file__))
os.chdir("Ex3 Videos")
for fichier in os.listdir("C:\\Users\\6256003\OneDrive - Cégep Édouard-Montpetit\\Prog2\\R03 Exercices Depart\\Ex3 Videos"):
    nom, ext = os.path.splitext(fichier)
    titre, cours, numero = nom.split("_")
    nouveau_nom = f"{titre.strip()}-{cours.strip()}-{numero.strip().zfill(2)}{ext}"
    os.rename("C:\\Users\\6256003\OneDrive - Cégep Édouard-Montpetit\\Prog2\\R03 Exercices Depart\\Ex3 Videos", "Exercies3Videos")
    
   

