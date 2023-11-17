from random import randint

rand = randint(0,100)
print(rand)
compteur = 0

while True:
    user_answer = int(input('Entrez une valeur : '))
    compteur = compteur + 1

    if user_answer == rand:
        print("Vous avez trouvé !")
        break
    else:
        if user_answer < rand:
            print("Valeur trop petite !")
            print(compteur)
        else:
            print("Valeur trop grande !")
            print(compteur)