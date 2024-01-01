li = [0]*3
print("Liste : ", li)
print("Type : ", type(li))
print("id : ", id(li))

for element in li:
    print(f"Element {element}: valeur={element}, type={type(element)}, id={id(element)}")

li[1] += 1
print("Liste après modification:", li)
print("Type de la liste après modification:", type(li))
print("ID de la liste après modification:", id(li))

## L'id a changer car on a modifier la liste

for element in li:
    print(f"Element {element}: valeur={element}, type={type(element)}, id={id(element)}")

## L'id du deuxieme element a changer car on a modifier la liste

machaine = "Bonjour"
for char in machaine:
    print(f"Char {char}: valeur={char}, type={type(char)}, id={id(char)}")
    
    ## On voit que chaque lettre a un id different
