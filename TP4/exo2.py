nombreEtudiant = int(input("Donnez le nombre d'étudiants: "))
moyenne = 0.0
notes = []
somme = 0

for i in range(0,nombreEtudiant):
    x = int(input(f"Entrez votre note etudiant {i}: "))
    notes.append(x)

for element in notes:
    somme = somme + element
    moyenne = somme / len(notes)

print(f"La moyenne est de : {moyenne}")
for note in notes:
    print(f"L'étudiant {notes.index(note)} a une note de {note} et une différence de {note-moyenne}")
