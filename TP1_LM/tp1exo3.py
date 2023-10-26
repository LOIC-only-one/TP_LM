"""
Exercice 3 :
Reprenez l’exercice 2 pour le transformer en script que vous nommerez «tp1exo3.py ».
Prévoir une saisie interactive en affichant un message d’invite personnalisé pour chaque
variable « jour », « heure » et « minute ». Le script doit calculer le nombre de minutes
écoulées depuis le début du mois, puis il affiche le résultat à l’écran
"""

jour = input("Entrez quel jour nous somme: ")
heure = input("Quelle heure sommes nous: ")
minute = input("Combien de minute ce sont écoulé: ")

jour = int(jour)
heure = int(heure)
minute = int(minute)

resultat = (jour*24*60+heure*60+minute)
print(resultat)
