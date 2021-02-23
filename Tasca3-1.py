"""
Fes un programa que suma un valor introduït per teclat a tots els elements de la llista
[1,2,3,4,5,6,7,8,9,10] utilitzant un bucle for, cal modificar la llista original.

"""

nums=[1,2,3,4,5,6,7,8,9,10]

num=input("Posa un número: ")

j=0
for i in nums: 
    nums[j]=int(i)+int(num)
    
    j=j+1
print(nums)