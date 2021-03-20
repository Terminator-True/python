import random
def omple_llista (w,l,m,M):
     return [random.randint(m,M) for i in range(l)]
      
def demana_llista(n):
    return [int(input("Afegeix algun carácter: ")) for i in range(n) ] 
def imprimeix_llista(ll):
     print(ll)
def ordena_llista(ll):
     return ll.sort()
def suma_llistes(ll1,ll2):
     return [ll1[i]+ll2[i] for i in range(len(ll1))]
