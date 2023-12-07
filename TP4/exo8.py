dico = {"firstname": "loic", "name": "maurer", "promo": "2023", "group": "121"}
binome = {"login1": {"firstname": "loic", "name": "maurer", "promo": "2023", "group": "121"}, "login2": {"firstname": "David", "name": "Pujadace", "promo": "1200", "group": "670"}}

print("votre nom est", dico["name"], ", prénom est", dico["firstname"], ", vous faites partie de la promo", dico["promo"], "et votre groupe est", dico["group"])

print("Les clés du dictionnaire sont :")
for i in dico.keys():
    print("-", i)

print("Les valeurs du dictionnaire sont :")
for i in dico.values():
    print("-", i)
print("Les tuplet du dictionnaire sont :")
for i in dico.items():
    print("-", i)

print("Les étudiants formants le binôme sont :")
for i in binome.values():
    print("- L'étudiant", i["firstname"], i["name"], "du groupe", i["group"])