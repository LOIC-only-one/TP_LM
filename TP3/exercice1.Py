
## Exercice 1
def exoA():
    n= input("Entrez une valeur: ")
    n = int(n)
    somme = 0
    for i in range(0,n+1):
        somme = somme + i
    return somme


## Exercice 2
def exoB():
    while True:
        valeur = int(input("Entrez une valeur :"))
        if valeur == 100:
            break



## Exercice 3
def exo3():
    somme_10 = 0
    somme_10_15 = 0
    somme_15 = 0

    for valeur in range(0, 10):
        tch = int(input("Entrez une valeur :"))

        if tch < 10:
            somme_10 = somme_10 + 1
        elif tch >= 10 and tch < 15:
            somme_10_15 = somme_10_15 + 1
        elif tch >= 15:
            somme_15 = somme_15 + 1

    print(f'Inferieur a 10 {somme_10}')
    print(f'Superieur a 10 et inferieur a 15 {somme_10_15}')
    print(f'Supérieur ou égale à 15: {somme_15}')

    return somme_10, somme_10_15, somme_15


# Exercice 4
def exoC():
    x = float(input("Entrez une valeur pour X (supérieure à 1) : "))
    N = 0
    somme = 0

    while somme <= x:
        N += 1
        somme = somme + N
    N -= 1  

    return f"Le plus grand nombre N tel que ∑𝑖 de 0 à N est inférieur ou égal à {x} est : {N}"

print(exoC())