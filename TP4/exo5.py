def annee_bi(ch: str) -> str:
    # Vérifier la longueur de la chaîne
    if len(ch) != 8:
        return "Format incorrect : Veuillez entrer une date sous la forme jjmmaaaa."

    # Extraire l'année
    annee = int(ch[-4:])

    # Vérifier si l'année est bissextile
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        mois = int(ch[2:4])
        jour = int(ch[:2])

        # Vérifier la validité du jour en fonction du mois
        if mois == 2 and (jour > 29):
            return "incorrecte"
        elif (mois in [4, 6, 9, 11]) and (jour > 30):
            return "incorrecte"
        elif jour > 31:
            return "incorrecte"

        return "Date correcte."


    # Si l'année n'est pas bissextile, vérifier la validité du jour et du mois
    mois = int(ch[2:4])
    jour = int(ch[:2])

    if mois == 2 and (jour > 28):
        return "incorrecte"
    elif (mois in [4, 6, 9, 11]) and (jour > 30):
        return "incorrecte"
    elif jour > 31:
        return "incorrecte"

    return "Date correcte."






# Tester avec les dates
test = ["31021999", "31042000", "32052020", "30032021", "29022022"]
for element in test:
    print(f"{element}: {annee_bi(element)}")
