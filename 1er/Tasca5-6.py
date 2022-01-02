"""
Programa l’algorisme de cerca binària. Prova’l amb L3 i un valor entrat per teclat.

"""

L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

trobat=False
inf=0
sup=len(L3)-1
e=int(input("Quin número vols buscar? "))

while (inf <= sup) and (not trobat):
    mig = (sup-inf)//2 + inf
    
    if e == L3[mig]:
        trobat=True
    else:
        if e < L3[mig]:
            sup = mig-1
        else:
            inf=mig+1
    
        
if trobat == False:
    print('no trobat')
else:
    print('trobat a la posició', mig+1)
