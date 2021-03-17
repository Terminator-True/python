import random
def inicialitza (w,l,m,M):
     w=[random.randint(m,M) for i in range(l)]

def demana_llista(n):
    return [input("Afegeix algun carácter: ") for i in range(n)] 
    