from assets import requadre,de_hores_a_segons
from llistes import *
w = []
#Exercici 1
requadre(4,5)
print("Hola")
requadre(5,4)

#Exercici 2
User_input=int(input("Hores: "))
print(de_hores_a_segons(User_input))

#Exercici 3 
n = int( input('Quants elements? ') )

v = demana_llista(n)
imprimeix_llista(v)
w=omple_llista(w,n,-10,10)
imprimeix_llista(w)
v = suma_llistes(v, w)
imprimeix_llista(v)

ordena_llista(v)
imprimeix_llista(v)
