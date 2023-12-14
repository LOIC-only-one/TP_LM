# Fonction pour décomposer la somme en billets et pièces
def decomposer_monnaie(somme):
    billet100 = somme // 100
    reste = somme % 100
    billet50 = reste // 50
    reste %= 50
    billet10 = reste // 10
    reste %= 10
    piece2 = reste // 2
    piece1 = reste % 2

    return billet100, billet50, billet10, piece2, piece1

# Lecture de la somme depuis l'utilisateur
somme = int(input("Entrez une somme d'argent en euros : "))

# Appel de la fonction de décomposition
billet100, billet50, billet10, piece2, piece1 = decomposer_monnaie(somme)

# Affichage des résultats
message = f"{somme} euros, c'est donc {billet100} billets de 100, {billet50} de 50, {billet10} de 10, {piece2} pièces de 2 et {piece1} pièce de 1."
print(message)
    