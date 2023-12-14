def calculer_salaire(heures_travaillees, salaire_horaire):
    if heures_travaillees <= 160:
        salaire = heures_travaillees * salaire_horaire
    elif 161 <= heures_travaillees <= 200:
        salaire = 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
    else:
        salaire = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.5
    return salaire

heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = calculer_salaire(heures_travaillees, salaire_horaire)
print(f"Le salaire total est de {salaire_total} euros.")
