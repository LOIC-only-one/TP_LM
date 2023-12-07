def multiplication(n):
    tab = []

    for i in range(0,9):
        tab.append(round(n*i,2))
    
    return tab

print(multiplication(1.2))