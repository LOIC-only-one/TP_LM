"""
1e --> 0 ou 7 / 17 ou 24
2e --> 7 ou 17 
 Velo.py demandera à l'utilisateur de quelle heure à
quelle heure se fait la location et calculera le prix de la location en conséquence.


"""


debut = int(input("Entrez l'heure de début de la location : "))
fin = int(input("Entrez l'heure de fin de la location : "))

if debut and fin > 24:
    print(f"Les heures doivent être comprises entre 0 et 24 !,\n heure de fin {fin}, heure de debut {debut}")

if debut == fin:
    print("Attention ! l'heure de fin est identique à l'heure de début.\n")

    if fin - debut < 0:
        print(f"Attention ! le début de la location est après la fin ... heure de fin {fin} et heure de debut {debut}")
else:
    if 0 <= debut < 7 or 17 <= fin < 24:
        nb_heure = fin - debut
        result = nb_heure * 1
        print(f"Vous devrez payer {result} euros !")

    elif 7 <= debut and fin <= 17:  # 2e
        nb_heure = fin - debut
        result = nb_heure * 2
        print(f"Vous devrez payer {result} euros !")