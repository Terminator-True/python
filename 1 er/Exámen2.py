"""
Donada una llista d’N enters que representen les diferents cotes d’una muntanya,
definim els cims d’aquesta muntanya com aquells punts on la cota puja i després baixa
(no necessàriament a continuació).

No es considera un cim el cas en què la cota puja però no baixa
(per exemple [1,3,3,3,3], quan la cota baixa però no puja (per exemple [3,1,1,1,1]),
o quan ni puja ni baixa (per exemple [1,1,1,1,1]).

Es demana crear un programa en Python que generi una llista de 10 enters aleatoris entre 0 i 20,
que representen les cotes d’una muntanya, i a continuació determini quants cims té aquesta muntanya.
La sortida del programa ha de ser la mateixa que es mostra en els exemples.

"""
import random
N=10
Nums=[]
cims=0
i=0
while i!=N:
    i+=1
    Nums.append(random.randint(0,20))
    
    
for i in range(1,N):
    if Nums[i] > Nums[i-1]:
        continue
    if Nums[i] < Nums[i-1]:
        if Nums[i-1]==Nums[0]:
            continue
        else:
            print("El valor: ",Nums[i-1]," es un cim")
            cims+=1
print("Total de Cims:\n",cims)
        
        
    