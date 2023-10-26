Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nom="Maurer"
>>> prenom="Loïc"
>>> math=12.4
>>> anglais=12.1
>>> info=17.2
>>> promotion=1
>>> type(nom)
<class 'str'>
>>> type(prenom)
<class 'str'>
>>> type(math)
<class 'float'>
>>> type(anglais)
<class 'float'>
>>> type(info)
<class 'float'>
>>> type(promotion)
<class 'int'>
>>> moy = (math+anglais+info)/3
>>> print(f"Létudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {mo}
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"Létudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {mo}")
...       
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(f"Létudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {mo}")
NameError: name 'mo' is not defined. Did you mean: 'moy'?
>>> print(f"Létudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {moy}")
...       
Létudiant Loïc Maurer de la promotion 1 a une moyenne de 13.9
