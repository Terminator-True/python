"""
La idea és implementar en Python una versió senzilla del joc de la guerra de vaixells. Jugarem contra l'ordinador en un sol tauler de 10 x 10.
 El programa col·locarà els vaixells aleatòriament i el jugador els haurà de trobar.

Per fer el programa haureu d’implementar tot un seguit de funcions. Us fem una proposta del que és necessari. Recordeu que cal comprovar que funcionen 
amb diferents valors i es comporten correctament. Finalment ho ajuntarem tot i farem el programa general.

En cada posició del tauler hi ha una llista de 2 elements. El primer element és un booleà que desa si la casella ha estat destapada o no, i en el segon 
pot haver els següents valors:

“~” que representa aigua, i és el valor per defecte de totes les posicions 
“@” que representa una casella ocupada per un vaixell
“X” que representa una casella d’un vaixell tocat
“#” que representa una casella d’un vaixell tocat i enfonsat


Funcions:
creaTauler()
imprimeixTauler(tauler,dev)
tradueixIndex(fila,columna)
aigual(tauler, fila, columna) 
comprovaAreaH(tauler,f,c,mida)
colocaVaixellHoritzontal(tauler,fila,columna,mida)
colocaVaixellVertical(tauler,fila,columna,mida)
colocaFlota(tauler, flota) 
tret(tauler,f,c)
troba1acasellaH(tauler,x,y) 
trobaVaixellH(tauler,x,y)
troba1acasellaV(tauler,x,y) i trobaVaixellV(tauler,x,y)
tocatIEnfonsat(tauler,f,c)
partidaAcabada(tauler)
"""
#Imports

import random
#Constants
x = 10
y = 10
lletres=["A","B","C","D","E","F","G","H","I","J"]
flota = [5,4,4,3,3,3,2,2]


def creaTauler():
    m=[]
    for i in range(x):
        fila=[]
        for j in range(y):
                fila.append([False,"~"])
        m.append(fila)
    return m

def imprimeixTauler(m,dev=True):
    s= " "
    print("  ",end="")  
    for i in range(len(m)):
        print(lletres[i],end=s)
    print()

    for j in range(len(m)):
        print(j,end=s)
        for k in range(len(m[0])):
            if m[j][k][0] == False and not dev:
                print("·",end=s)
            else:
                print(m[j][k][1],end=s)   
        print() 

def tradueixIndex(f,c):
    for i in range(len(lletres)):
        if lletres[i]==c:
            return int(f),int(i)

def aigua(m,f,c):
        return m[f][c][1]=="~"

def comprovaAreaH(m,f,c,mida):
    principi=c
    final=mida
    voltes=3
    if c+mida>10:
        return False
    if c+mida<=9:
        final=mida+1
    else:
        final=mida
    if f!=0:
        f-=1
    else:
        voltes=2
    if c!=0:
        principi=c-1
    for i in range(voltes):
        for j in range(principi,c+final):
            if m[f][j][1]!="~":
                return False
        f+=1
        if f>=10:
            return True
    return True

def colocaVaixellHoritzontal(tauler,f,c,mida):
    if comprovaAreaH(tauler,f,c,mida):
      for i in range(c,c+mida):
          tauler[f][i][1]="@"  
    else:
        return False
    return True

def comprovaAreaV(m,f,c,mida):
    if f+mida>9:
        return False
    if c!=0:
        voltesP=c-1
    else:
        voltesP=c
    if voltesP+2<=9:
        voltesF=c+2
    else:
        voltesF=c+1
    if f!=0:
        principi=f-1
    else:
        principi=f
    if f+mida<=9:
        final=f+mida+1
    else:
        final=f+mida
    for i in range(principi,final):
        for j in range(voltesP,voltesF):
            if m[i][j][1]!="~":
                return False
    return True

def colocaVaixellVertical(tauler,f,c,mida):
    if comprovaAreaV(tauler,f,c,mida):
      for i in range(f,f+mida):
          tauler[i][c][1]="@"  
    else:
        return False
    return True


def colocaFlota(m,flota):
    for el in flota:
        VvsH=random.randint(0,1)
        i=0
        if VvsH==1 :
            acabat=False
            while not acabat:
                i+=1
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                if aigua(m,f,c):
                    acabat=colocaVaixellHoritzontal(m,f,c,el)
        
        elif VvsH==0:
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                if aigua(m,f,c):
                    acabat=colocaVaixellVertical(m,f,c,el)

def tret(m,f,c):
    m[f][c][0]=True
    if aigua(m,f,c):
        imprimir=("~  "*6)+"\n"+"     AIGUA    "+"\n"+("~  "*6)    
    else:
        m[f][c][1]=="X"
        if tocatIEnfonsat(m,f,c):
            imprimir=("=  "*6)+"\n"+"     ENFONSAT    "+"\n"+("=  "*6)
        else:
            imprimir=("-  "*6)+"\n"+"     TOCAT   "+"\n"+("-  "*6)
    print(imprimir)


def troba1acasellaH(m,x,y):
    principi=y
    final=0
    for i in range(principi,final,-1):
        if m[x][i][1]=="~":
            return x,i+1
        elif i==0:
            return x,i

def trobaVaixellH(m,x,y):
    mida=0
    principi=y
    final=len(m[x])
    for i in range(principi,final):
        if m[x][i][1]=="@" or m[x][i][1]=="X" :
            mida+=1
    return (x,y),mida

def troba1acasellaV(m,x,y):
    principi=x
    final=0
    for i in range(principi,final,-1):
        if m[i][y][1]=="~":
            print(i+1,y)
            return i+1,y
        elif i==0:
            return i,y

def trobaVaixellV(m,x,y):
    mida=0
    principi=x
    final=len(m[x])
    for i in range(principi,final):
        if m[i][y][1]=="@" or m[i][y][1]=="X" :
            mida+=1
    return (x,y),mida

def orientacio(m,f,c):
    if c==0 and not aigua(m,f,c+1):
        return True
    elif c==9 and not aigua(m,f,c-1):
        return True
    elif (c!=0 and c!=9) and (not aigua(m,f,c-1) or not aigua(m,f,c+1)):
        return True
    return False
        
def tocatIEnfonsat(m,f,c):
    tocats=0
    if orientacio(m,f,c):
        T=troba1acasellaH(m,f,c)
        print(T)
        x=T[0]
        y=T[1]
        vaixell=trobaVaixellH(m,x,y)
        print(vaixell)
        for i in range (vaixell[0][1],vaixell[1]):
            if m[x][i][1]=="X":
                tocats+=1
        if tocats==vaixell[1]:
            return True
            for i in range (vaixell[0][1],vaixell[1]):
                m[x][i][1]=="#"
        else:
            return False
    else:
        T=troba1acasellaV(m,f,c)
        print(T)
        x=T[0]
        y=T[1]
        vaixell=trobaVaixellV(m,x,y)
        print(vaixell)
        for i in range (vaixell[0][1],vaixell[1]):
            if m[i][y][1]=="X":
                tocats+=1
        if tocats==vaixell[1]:
            return True
            for i in range (vaixell[1][1],vaixell[2]):
                m[i][y][1]=="#"
        else:
            return False

def partidaAcabada(m):
    for fila in m:
        for el in fila:
            if el[1]=="@":
                return False
            else:
                return True
m=creaTauler()
colocaFlota(m,flota)
acabat=False
while acabat is False:
    imprimeixTauler(m)
    print("Coordenades del tret")
    f=input("Fila: ")
    c=input("Columna: ")
    T=tradueixIndex(f,c)
    x,y=T
    tret(m,x,y)
    if partidaAcabada(m):
        acabat=True
