l1 = list("kfzmorergjkljkzefveirozjgoirzejgwagonwagon")

def taille(l1):
    somme = 0
    for element in l1:
        somme += 1
    return somme

def pourcentage_voyelles(l1):
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    nb_voyelles = 0
    for element in l1:
        if element in voyelles:
            nb_voyelles += 1
    pourcentage = (nb_voyelles / taille(l1)) * 100

    return pourcentage

def check(l1):
    nb_occurence = 0
    for i in range(len(l1)):
        if l1[i] == "w":
            if l1[i+1] == "a":
                if l1[i+2] == "g":
                    if l1[i+3] == "o":
                        if l1[i+4] == "n":
                            nb_occurence += 1
    return nb_occurence

print(check(l1)) 
