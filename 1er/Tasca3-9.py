"""
Escriviu un programa per imprimir els números d'una llista especificada per teclat i després d'eliminar-ne els números parells. 

"""

nums=[]
condicio=False

while condicio!=True:
    
    num=int(input("Pos un número(Posa un número negatiu per parar el bucle): "))
    
    nums.append(num)
    
    if num<0:
        condicio=True
    
    
    
X=nums.pop()

print(nums)

for el in nums:
    if el%2==0:
        nums.remove(el)
        
print(nums)