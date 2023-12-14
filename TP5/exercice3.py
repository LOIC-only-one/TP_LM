chaine = str(input("Entrez un mot ou une phrase : "))
chaine_formattee = "".join(char.lower() for char in chaine if char.isalpha())

if chaine_formattee == chaine_formattee[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")