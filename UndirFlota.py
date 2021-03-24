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
#Constants
x = 10
y = 10
lletres=" ABCDEFGHIJ"


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
            return (f,i-1)

def aigua(m,fc):
    if m[f][c][1]=="~":
        return True

def comprovaAreaH(m,f,c,mida):
    comprovacio=False
    i=-1
    while comprovacio not True:
        if c==0:     
            continue
        else:
            c-=1
        if f==0:
            continue
        else:
            f-=1
            for i in range(m[f+i][c],m[f+i][c+(mida+1)]):
                if m[f][i][0]=="@":
                    return False
        i+=1
        if i==2:
            comprovacio==True

                