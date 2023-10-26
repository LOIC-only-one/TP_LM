BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input('Combien de convive : '))

t_fromage = fromage * nbConvives / BASE
t_eau = eau*nbConvives / BASE
t_ail = ail * nbConvives / BASE
t_pain = pain * nbConvives / BASE


print(f'''Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :
- {t_fromage} gr de fromage
- {t_eau} dl d'eau
- {t_ail} gousse(s) d'ail
- {t_pain} gr de pain''')