"""
Programa l’algorisme d’ordenació del nan. Prova’l amb L1 i L2.

"""

L1 = [ 8, 6, 4, 2, 10, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
C=0
i=0
while i<len(L1):
    
    if i==0 or L1[i]>=L1[i-1]:
        i=i+1
        continue
    else:
        C=L1[i-1]
        L1[i-1]=L1[i]
        L1[i]=C
        i=i-1
while i<len(L2):
    
    if i==0 or L2[i]>=L2[i-1]:
        i=i+1
        continue
    else:
        C=L2[i-1]
        L2[i-1]=L2[i]
        L2[i]=C
        i=i-1
            
print(L1)