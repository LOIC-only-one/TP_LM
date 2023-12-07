nMax = 3
while True:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    if 1 <= n <= nMax:
        break
    else:
        print(f"La taille doit être entre 1 et {nMax}.")

v1 = [0] * n
v2 = [0] * n

print("Saisie du premier vecteur :")
for i in range(n):
    v1[i] = float(input(f"v1[{i}] = "))

print("Saisie du second vecteur :")
for i in range(n):
    v2[i] = float(input(f"v2[{i}] = "))

# Calculer le produit scalaire
produit_scalaire = 0
for i in range(n):
    produit_scalaire += v1[i] * v2[i]

print("Le produit scalaire de v1 par v2 vaut", produit_scalaire)
