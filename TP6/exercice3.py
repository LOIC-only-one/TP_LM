def mafct(a, b=5):
    """Fonction qui retourne la somme de deux nombres"""
    return a + b
x= 3
print(mafct(x))
print(mafct(x, 2))


def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

## Le resultat de print(ajouter_elt()) est [0, 1, 2, 3]
## Le resultat apres deux tours de print(ajouter_elt()) est [0, 1, 2, 3, 3]

def ajouter_carac(ch="abc",elt="d"):
    return ch + elt
## Le resultat de print(ajouter_carac()) est abcd
## Le resultat apres deux tours de print(ajouter_carac()) est abcd car les chaines de caracteres sont immutables

