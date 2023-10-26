x = int(input('Entrez un nombre entier: '))

if x == 0:
    print('Le nombre est zéro (et il est pair)')
else:
    if x > 0:
        if x % 2 == 0:
            print('Le nombre est positif et pair')
        else:
            print('Le nombre est positif et impair')
    else:
        if x % 2 == 0:
            print('Le nombre est négatif et pair')
        else:
            print('Le nombre est negatif et impair')