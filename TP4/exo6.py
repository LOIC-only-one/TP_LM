l1= [5, 2, 4, 8, 1, 3]

def tri_de_liste(liste: list) -> list:
    for i in range(len(liste)):
        print(liste)
        min_index = i

        for j in range(i + 1, len(liste)):
            if liste[min_index] > liste[j]:
                min_index = j

        # Échange des éléments une fois le minimum trouvé
        tmp = liste[i]
        liste[i] = liste[min_index]
        liste[min_index] = tmp

    return liste

print(tri_de_liste(l1))

print("Affichage avec sorted")
print(sorted(l1))

print("Affichage avec methode sort")
l1.sort()
print(l1)