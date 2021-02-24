"""
Fes un programa nou de la manera següent: 
agafa un programa d’ordenació dels que has fet (1 a 3), 
ordena L1 i 
fes-lo servir com a entrada del programa de cerca binària.

"""
trobat=False
inf=0
L1 = [ 8, 6, 4, 2, 10, 1, 3, 5, 7, 9]
sup=len(L1)-1
i=0
e=int(input("Quin número vols buscar? "))


while i<len(L1):
    
    if i==0 or L1[i]>=L1[i-1]:
        i=i+1
        continue
    else:
        C=L1[i-1]
        L1[i-1]=L1[i]
        L1[i]=C
        i=i-1
        
while (inf <= sup) and (not trobat):
    mig = (sup-inf)//2 + inf
    
    if e == L1[mig]:
        trobat=True
    else:
        if e < L1[mig]:
            sup = mig-1
        else:
            inf=mig+1
    
        
if trobat == False:
    print('no trobat')
else:
    print('trobat a la posició', mig+1)
