"""
Escriviu un programa per eliminar duplicats d'una llista. Bucle i funció integrada de python.
Per exemple: llista = [1,2,3,1,3,1,4,2], sortida = [1,2,3,4]

"""

nums=[1,2,3,1,3,1,4,2]
numsU=[]

i=0
EL2=0
for el in nums:
    if el not in numsU:
        numsU.append(el)
        
#Versió métode
numsU.sort()
print(numsU)

