"""
Programa l’algorisme de cerca seqüencial.
"""

L1 = [ 8, 6, 4, 2, 10, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]

i=0
e=int(input("Quin número vols buscar? "))

while (i<len(L1)) and (e != L1[i]):
    i+=1
    
if i==len(L1):
    print("No s'ha trobat")
else:
    print("Trobat a la posició: ",i)