def ajouter_elt(lst,elt):
    lst.append(elt)
    return lst
lst1 = [0,1,2]
lst2 = ajouter_elt(lst1,len(lst1))

print(f'Type de lst1 : {type(lst1)}, id de lst1 : {id(lst1)}')
print(f'Type de lst2 : {type(lst2)}, id de lst2 : {id(lst2)}')

print(lst1)
print(lst2)

## On voit que les deux listes ont le meme id
## On voit que les deux listes ont le meme type
