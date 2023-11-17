import time
valeur = int(input("Entrez une valeur:"))

for i in range(valeur,0,-1):
    print(i)
    time.sleep(1)

compteur = valeur + 1
while compteur != 1:
    compteur = compteur - 1 
    print(compteur)
    time.sleep(1)

