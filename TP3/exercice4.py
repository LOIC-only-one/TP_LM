valeur = int(input("Entrez une valeur de la factorielle à calculer :"))

fact = 1
for i in range(1, valeur + 1):
    fact = fact * i
    print(f'Étape {i}: {fact}')
