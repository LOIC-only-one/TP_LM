def accents(texte):
    texte = texte.replace('à', 'a')
    texte = texte.replace('â', 'a')
    texte = texte.replace('é', 'e')
    texte = texte.replace('è', 'e')
    texte = texte.replace('ê', 'e')
    texte = texte.replace('ë', 'e')
    texte = texte.replace('î', 'i')
    texte = texte.replace('ï', 'i')
    texte = texte.replace('ô', 'o')
    texte = texte.replace('ö', 'o')
    texte = texte.replace('ù', 'u')
    texte = texte.replace('û', 'u')
    texte = texte.replace('ü', 'u')
    texte = texte.replace('ç', 'c')
    return texte

def est_palindrome(texte):
    texte = texte.lower()
    return texte == texte[::-1]

texte = input("Entrez un texte : ")
texte = accents(texte)
if est_palindrome(texte):
    print("Le texte est un palindrome.")
else:
    print("Le texte n'est pas un palindrome.")