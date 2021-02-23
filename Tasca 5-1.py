"""
Programa l’algorisme d’ordenació per inserció. Prova’l amb L1 i L2.
"""
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]

for i in range (len(L1)):
    X=L1[i]
    j=i-1
    while j>=0 and L1[j]>X:
        L1[j+1]=L1[j]
        j=j-1
    
    L1[j+1]=X
    
print(L1)

for i in range (len(L2)):
    X=L2[i]
    j=i-1
    while j>=0 and L2[j]>X:
        L2[j+1]=L2[j]
        j=j-1
    
    L2[j+1]=X
    
print(L2)