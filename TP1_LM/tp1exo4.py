"""
Exercice 4 :
Ecrire un deuxième script nommé « tp1exo4.py » qui permet à l’utilisateur de saisir un
nombre représentant les minutes écoulées depuis le début du mois ( le mois en cours par
exemple) et affiche la date associée (le jour du mois).
"""

minute_total = input("Entrez le nombre de minute: ")
minute_total = int(minute_total)


heure = minute_total // 60
jour = heure // 24
print(jour)
