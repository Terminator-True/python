"""
Escriviu un programa que donada una llista de strings, no cal que sigui introduïda per teclat,
ens digui quants elements hi ha a la llista de longitud més gran o igual que 2, i comencen per ‘a’.
Mostrar per pantalla el resultat.

"""

ll=["Hola","que","tal","Arnau","?"]

for i in ll:
    if len(i)>=2:
        print("Aquest string conté més de 2 carácters:",i)
    if "A"==i[0] or "a"==i[0]:
        print("Aquest string comença per A: ",i)