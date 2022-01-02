import random

def creaMatriu(n1,n2):
    if n1>0 and n2>0:
        m=[]
        for i in range(n1):
            fila=[]
            for j in range(n2):
                fila.append(random.randint(1,100))
            m.append(fila)
    else:
        m=-1
    return m  

def printMatriu(m):
    imprimir=""
    for el in m:
        imprimir+=" ".join(str(el2) for el2 in el)+"\n"
    print("* "*(len(el)*2),"\n",imprimir)
def mides(m):
    files=0
    columnes=0
    for el in m:
        for el2 in el:
            if columnes==0:
                files+=1
        columnes+=1
    return (columnes,files)
def dimensionsiguals(m1,m2):
    if mides(m1)==mides(m2):
        return True
    else:
        return False
def sumaMatrius(m1,m2):
    matriuN=[]
    i=0
    if dimensionsiguals(m1,m2)==True:
        for el in m1:
            fila=[]
            for el2 in m2:
                fila.append(el[i]+ el2[i])
                i+=1
            i=0
            matriuN.append(fila)
        return(matriuN)
    else:   
        return "Error, han de ser dos matrius iguals"

def producteEscalar(m,n):
    i=0
    matriuN=[]
    for el in m:
            fila=[]
            for el2 in el:
                fila.append(el2*n)
                i+=1
            i=0
            matriuN.append(fila)
    return matriuN
def transposar(m):
    i=0
    matriuN=[]
    for i in range(len(m)+1):
        fila=[]
        for el in m:
            fila.append(el[i])
        matriuN.append(fila)
    return matriuN



matriu=creaMatriu(5,15)
matriu1=creaMatriu(3,4)
matriu2=creaMatriu(3,4)
printMatriu(matriu)
printMatriu(matriu1)
printMatriu(matriu2)

print("Les mides de la matriu:",mides(matriu))
print("Les mides de la matriu1:",mides(matriu1))
print("Les mides de la matriu2:",mides(matriu2))

print(dimensionsiguals(matriu1,matriu2))
print("Suma matriu1 i matriu2")
printMatriu(sumaMatrius(matriu1,matriu2))
print("Producte escalar:")
printMatriu(matriu1)
printMatriu(producteEscalar(matriu1,10))
printMatriu(matriu2)
printMatriu(transposar(matriu2))