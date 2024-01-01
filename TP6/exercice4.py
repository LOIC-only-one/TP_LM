def generer(nbr,vmin, vmax):
    tab = []
    for i in range(nbr):
        tab.append(random.randint(vmin, vmax))
    return tab

def combienInferieur(table, vseuil):
    total = 0
    for element in table:
        if element < vseuil:
            total += 1
    return total

nb = int(input("Combien de nombres entiers voulez-vous générer ? "))
vmax = int(input("Quelle valeur maximale ? "))
vmin = int(input("Quelle valeur minimale ? "))

seuil_specifie = input("Voulez-vous préciser le seuil ? (O/N) ")
if seuil_specifie.lower() in ['oui', 'o']:
    seuil = int(input("Quel seuil ? "))
else:
    seuil = 30

print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")