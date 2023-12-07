L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""

tab1 = [0] * (max(L1) + 1)

for element in L1:
    tab1[element] = tab1[element] + 1

print(f"Le nombre le plus frequent dans la liste est le : {tab1.index(max(tab1))} ({max(tab1)}x)")


tab1 = [0] * (max(L1) + 1)

for element in L1:
    tab1[element] = L1.count(element)

# Trouver l'élément le plus fréquent et sa fréquence
element_plus_frequent = tab1.index(max(tab1))
frequence_plus_frequente = max(tab1)

print(f"Le nombre le plus fréquent dans la liste est le : {element_plus_frequent} ({frequence_plus_frequente}x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
