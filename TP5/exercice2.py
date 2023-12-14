somme_note = 0
somme_coeff = 0
for i in range(0,4):
    note = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant: "))

    noote_format = note.split(" ")
    s3 = float(noote_format[0])
    s4 = float(noote_format[1])

    somme_note =+ s3
    somme_coeff =+ s4

    moyenne = (s3 * s4) / somme_coeff

    if s3 < 8:
        print("Pas admis")
    else:
         if moyenne >= 10:
            print("Admins !")