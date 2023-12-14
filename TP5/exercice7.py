import os
from datetime import datetime

def obtenir_derniere_modification(path):
    timestamp = os.path.getmtime(path)
    date_modification = datetime.fromtimestamp(timestamp)
    return date_modification

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    derniere_modification_fichier1 = obtenir_derniere_modification(fichier1)
    derniere_modification_fichier2 = obtenir_derniere_modification(fichier2)
    print(f"Dernière modification de {fichier1}: {derniere_modification_fichier1}")
    print(f"Dernière modification de {fichier2}: {derniere_modification_fichier2}")

    if derniere_modification_fichier1 > derniere_modification_fichier2:
        print(f"{fichier1} est plus récent.")
    elif derniere_modification_fichier1 < derniere_modification_fichier2:
        print(f"{fichier2} est plus récent.")
    else:
        print("Les deux fichiers ont été modifiés à la même date.")
else:
    print("Au moins l'un des fichiers n'existe pas.")
