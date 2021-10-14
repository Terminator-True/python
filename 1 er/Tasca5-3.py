"""
Programa l’algorisme d’ordenació de la bombolla.

"""

L1 = [ 8, 6, 4, 2, 10, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]

ll=len(L1)
ll2=len(L2)

intercanvi= True

while intercanvi:
    intercanvi = False
    for i in range (1,ll):
        if L1[i-1] > L1[i]:
            C=L1[i-1]
            L1[i-1]=L1[i]
            L1[i]=C
            intercanvi = True
    ll=ll-1
print(L1)

i=0
intercanvi= True

while intercanvi:
    intercanvi = False
    for i in range (1,ll2):
        if L2[i-1] > L2[i]:
            C=L2[i-1]
            L2[i-1]=L2[i]
            L2[i]=C
            intercanvi = True
    ll=ll-1
print(L2)