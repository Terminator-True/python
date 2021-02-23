"""
Escriviu un programa que elimina l’element n-èssim d’una llista introduïda per teclat.

"""

Mostres=['Vermell', 'Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']
print(Mostres)

Res=int(input("Quin color no vols?(0-6) "))


for j in Mostres:
    if Mostres[Res]==j:
        Mostres.remove(j)
            
print(Mostres)