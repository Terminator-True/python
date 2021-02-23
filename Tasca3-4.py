"""
Escriviu un programa que mostri per pantalla el resultat de sumar i el resultat de multiplicar tots els elements d'una llista.
Cal introduir la llista per teclat. Ajuda: feu servir un bucle per afegir elements a la llista.
"""
j=0
nums=[]
resultat=0
resultatM=1
condicio=False
while condicio!=True:
    
    num=int(input("Pos un número(Posa un número negatiu per parar el bucle): "))
    
    nums.append(num)
    
    if num<0:
        condicio=True
    
    
    
X=nums.pop()

for i in range (len(nums)):
    resultat=resultat+nums[i]
    resultatM=resultatM*nums[i]
print(resultat)

print(resultatM)