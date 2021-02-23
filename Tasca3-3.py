"""
Fes un programa que calculi les n primeres potències d’un nombre fent servir el bucle for.
Per exemple si li introduïm el 2 i 4, la consola mostrarà:
"""

num=int(input("Posa un número: "))

potencia=int(input("Quants cops es repetirá l'operació: "))

for i in range (1,potencia): 
    resultat=i**num
    print(num,"elevat a ",i,"=",resultat)