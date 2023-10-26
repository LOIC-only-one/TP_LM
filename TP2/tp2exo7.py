from random import randint

x = randint(0,100) ## Génere un nombre aléatoire entre 0 et 100
if x < 2/3:
    print('Pile !')
else:
    print('Face !')