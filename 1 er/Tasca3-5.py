"""
Escriviu un programa per obtenir el nombre més gran, més petit i la mitjana d'una llista de sencers.
Cal introduir la llista per teclat. Fer versió bucle i versió mètodes.

"""
nums=[]
condicio=False
total=0
resultat=0
while condicio!=True:
    
    num=int(input("Pos un número(Posa un número negatiu per parar el bucle): "))
    
    nums.append(num)
    
    if num<0:
        condicio=True
    
    
    
X=nums.pop()
#Versió mètodes
print("Número més petit: ",min(nums))
print("Número més gran: ",max(nums))


for i in range (len(nums)):
    total=total+nums[i]
    
resultat=total/len(nums)

print("La mitja:",resultat)
    
#Versió Bucle:

for j in range (len(nums)):
    if j==0:
        continue
    else:
        if nums[j]>nums[j-1]:
            NumG=nums[j]
        
        if nums[j]<nums[j-1]:
            NumP=nums[j]
            
print("Número més petit: ",NumP)
print("Número més gran: ",NumG)