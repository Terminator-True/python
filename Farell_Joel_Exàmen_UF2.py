
import sys

O="D"
def creaMatriu(x,y):
    m=[]
    for i in range (x):
        fila=[]
        for j in range (y):
            fila.append(i*j)
        m.append(fila)
    return m 

def printMatriu(m):
    for fila in m:
        for el in fila:
            print(el,end=" ")
        print()

def generaNombre(ll):
    nombre=""
    for el in ll:
        nombre+=str(el)
    return int(nombre)

def generaLlistaN(m):
    return [generaNombre(fila) for fila in m]

def shift(ll,O="D"):
    if O=="E":
        ll.append(ll[0])        
        ll.remove(ll[0])
    else:
        ll.insert(0,ll[len(ll)-1])
        ll.pop(len(ll)-1)
        
def nShift(ll,n,O="D"):
    i=0
    while i<n:
        shift(ll,O)
        i+=1

def shiftMatriu(m,n,O="D"):
    for fila in m:
        i=0
        while i<n:
            nShift(fila,n,O)
            i+=1

def comprova(Parametres):
    Parametres.pop(0)
    f,c,n=Parametres[0],Parametres[1],Parametres[2]
    existeix=False
    correctes=0

    if "E" in Parametres or "D" in Parametres:
        O=Parametres[3]
        existeix=True
    else:
        O="D"

    if f.isdigit():
        correctes+=1
        f=int(f)
    else:
        print("Les files han de ser un número")
        return False
    if c.isdigit():
        correctes+=1
        c=int(c)
    else:
        print("Les columnes han de ser un número")
        return False
        
    if f>10 and f<3:
        print("Número de files incorrcte")
        return False
    else:
        correctes+=1
    if c>10 and c<3:
        print("Número de columnes incorrcte")
        return False
    else:
        correctes+=1
    if n.isdigit():
        correctes+=1
        n=int(n)
    else:
        print("Variable N(Número de shifts) incorrecte")
        return False
    if existeix is True and O=="E" or O=="D":
        correctes+=1
    else:
        print("La variable opcional O, es incorrecte")
        return False

    if correctes==6:
        return True

Parametres=sys.argv
if comprova(Parametres):
    f,c,n=Parametres[0],Parametres[1],Parametres[2]
    f=int(f)
    c=int(c)
    n=int(n)
    if "E" in Parametres or "D" in Parametres:
        O=Parametres[3]
    m=creaMatriu(f,c)
    printMatriu(m)
    print("")
    shiftMatriu(m,n,O)
    printMatriu(m)
    print(generaNombre(generaLlistaN(m)))