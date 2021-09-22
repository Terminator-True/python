"""
Programa l’algorisme del sedàs d’Eratòstanes. Busca els nombres primers del 2 al 120.
Busca els 50 primers nombres primers..

"""

inf=2
sup = 121
P=[]
el=0
Terminat=False
coincidencia=0
num=[2,3,5,7]
borrar=[]
for i in range(2,sup):
    P.append(i)
print(P)

i=0
while Terminat!=True:#Seguidament calculem els múltiples de 2,3,5,7:
    for el in P:
        coincidencia=num[i]*el
        for el2 in P:
            if coincidencia==el2:
               borrar.append(coincidencia)
    for el3 in P:
        if el3 in borrar:
            P.remove(el3)
    i+=1   
    if i==4:
        Terminat=True
print(P)