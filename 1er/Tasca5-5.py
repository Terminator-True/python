"""
Programa l’algorisme de cerca seqüencial amb llista ordenada.
"""

L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]


i=0
e=int(input("Quin número vols buscar? "))

while (e > L3[i]) and (i < len(L3)):
    i+=1
    
if (e != L3[i]) or (i == len(L3)):
    print("No s'ha trobat")
else:
    print("Trobat a la posició: ",i)