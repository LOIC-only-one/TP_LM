binome = ('BeardDeamon',1,'Link67',2)
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[2]}")

"""
2. Vous souhaitez changer à présent de binôme, proposez la saisie du nouveau login et
modifier le second élément du tuplet « binome » en conséquence. Que constatezvous ?

Ca ne fonctionnera pas car le tuple est un types non muable


"""
del(binome[1])
print(binome)