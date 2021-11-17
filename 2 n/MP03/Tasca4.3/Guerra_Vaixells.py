"""
Fes un joc de batalla naval per jugar contra l'ordinador.

Especificacions:

Taulell de 10x10 posicions.
Hi col·locarem aleatòriament els següents vaixells ( no es poden tocar entre ells):
1 portaavions de 4 caselles.
2 cuirassats de 3 caselles.
3 fragates de 2 caselles.
4 patrulleres d'1 casella.
A cada pas es mostrarà la matriu indicant les cel·les ocultes, tocades i buides.
L'usuari introduirà fila i columna.
Quan s'enfonsin tots els vaixells la partida s'acaba i sortim del programa (amb un missatge de congratulations!).
Opció en català, anglès i alguna altra llengua.
Cal que puguis jugar diverses partides simultànies (diferents taulells). El jugador ha de poder anar canviant entre les diverses partides i reprendre on l'ha deixat.
Cal fer-ho amb OOP i, per tant, primer cal definir els objectes i les estructures de dades i decidir com utilitzar-les en el codi principal. 
Com a mínim, heu d'implementar les següents classes: class Tauler(), class Vaixell() i class Casella()."""
import random

#OBJECTES------------------------------------------------------
class Tauler:
    def __init__(self,x,y,m):
        self.x=x
        self.y=y
        self.m=m

    def GetTauler(self):
        return self.m
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def SetTauler(self,m):
        self.m=m

class Vaixell:
    def __init__(self,flota):
        self.flota=flota
    def GetFlota(self):
        return self.flota

class Casella:
    def __init__(self,lletres):
        self.lletres=lletres
    def GetCasellaBuida():
        return [False,"~"]
    def Getlletres(self):
        return self.lletres
#FUNCIONS-------------------------------------------------------
casella = Casella(["A","B","C","D","E","F","G","H","I","J"])
def creaTauler(x,y):
    return [[Casella.GetCasellaBuida() for j in range(y)] for i in range(x)]
def imprimeixTauler(lletres,m,dev=True):
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
def tradueixIndex(f,c,lletres):
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

def colocaFlota(m,flota,lletres):
    for el in flota:
        VvsH=random.randint(0,1)
        if VvsH==1 :
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                f,c=tradueixIndex(f,c,casella.Getlletres())
                if aigua(m,f,c):
                    acabat=colocaVaixellHoritzontal(m,f,c,el)
        
        elif VvsH==0:
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                f,c=tradueixIndex(f,c,casella.Getlletres())
                if aigua(m,f,c):
                    acabat=colocaVaixellVertical(m,f,c,el)
    return m

def tret(idioma,missatges,m,f,c):
        m[f][c][0]=True
        if aigua(m,f,c):
            imprimir=("~  "*6)+"\n"+"     "+missatges[idioma]["aigua"]+"    "+"\n"+("~  "*6)    
        else:
            if  m[f][c][1]=="X":
                imprimir=missatges[idioma]["posuse"]
            elif m[f][c][1]=="#":
                imprimir=missatges[idioma]["shipuse"]
            else:
                m[f][c][1]="X"
                if tocatIEnfonsat(m,f,c):
                    imprimir=("=  "*6)+"\n"+"     "+missatges[idioma]["enfonsat"]+"     "+"\n"+("=  "*6)
                else:
                    imprimir=("-  "*6)+"\n"+"     "+missatges[idioma]["tocat"]+"   "+"\n"+("-  "*6)
        print(imprimir) 

def troba1acasellaH(m,x,y):
    principi=y
    final=-1
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
        if m[x][i][1]=="@" or m[x][i][1]=="X":
            mida+=1
        elif m[x][i][1]=="~":
            return x,y,mida
        elif i==final:
            mida+=1
            return x,y,mida

def troba1acasellaV(m,x,y):
    principi=x
    final=-1
    for i in range(principi,final,-1):
        if m[i][y][1]=="~":
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
        elif m[i][y][1]=="~":
            return x,y,mida
        elif i==final:
            mida+=1
            return x,y,mida
#Funció que retorna true si el vaixell és horitzontal o False si es vertical. Va comparant l'alrededor de
#la posició f,c pero saber-ho
def orientacio(m,f,c):
    return c==0 and not aigua(m,f,c+1) or c==9 and not aigua(m,f,c-1) or (c!=0 and c!=9) and (not aigua(m,f,c-1) or not aigua(m,f,c+1))
        
def tocatIEnfonsat(m,f,c):
    tocats=0
    if orientacio(m,f,c):
        x,y=troba1acasellaH(m,f,c)
        vaixell=trobaVaixellH(m,x,y)
        for i in range (vaixell[1],(vaixell[1]+vaixell[2])):
            if m[x][i][1]=="X":
                tocats+=1
        if tocats==vaixell[2]:
            for i in range (vaixell[1],(vaixell[1]+vaixell[2])):
                m[x][i][1]="#"
            return True
        else:
            return False
    else:
        x,y=troba1acasellaV(m,f,c)
        vaixell=trobaVaixellV(m,x,y)
        for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
            if m[i][y][1]=="X":
                tocats+=1
        if tocats==vaixell[2]:
            for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                m[i][y][1]="#"
            return True
        else:
            return False
#Va sumant els # dels vaixells enfonsats i quan la suma d'aquests és igual
#a la suma de totes les mides de la flota sencera, retorna True
def partidaAcabada(flota,m):
    Quantitat=0
    for fila in m:
        for el in fila:
            if el[1]=="#":
                Quantitat+=1
    return Quantitat==sum(flota)

def partida(missatges,idioma,flota,m):
    acabat=False
    while partidaAcabada(flota,m) is not True or acabat is not True:
        imprimeixTauler(casella.Getlletres(),m)
        print("Coordenades del tret")
        f=input("Fila: ")
        c=input("Columna: ")
        if f == "quit" or c == "quit":
            break
        f,c=tradueixIndex(f,c,casella.Getlletres())
        tret(idioma,missatges,m,f,c)
    imprimeixTauler(casella.Getlletres(),m)
    imprimir=("$  "*6)+"\n"+"\tGOOD ENDING \n YOU WON    "+"\n"+("$  "*6)    
    print(imprimir)
if __name__=="__main__":
    #try:
        missatges = {
            "ca": {
                "benvinguts": "Benviguts a la Batalla Naval!",
                "introdueix fila": "Introdueix fila: ",
                "introdueix columna": "Introdueix columna: ",
                "tocat": "tocat! segueix així...",
                "aigua": "aigua",
                "enfonsat": "enfonsat",
                "posuse": "Aquesta posició ja ha estat elegida",
                "shipuse": "Aquest vaixell ja ha estat enfonsat",
                "menu":" 0: Crear nou tauler \n 1: Carregar tauler \n 2: Sortir \n",
                "avis" : "Per sortir, escriure quit",
                "escull" : "Escull tauler"
            },
            "es": {
                "benvinguts": "Bienvenidos a la Batalla Naval!",
                "introdueix fila": "Introduce fila: ",
                "introdueix columna": "Introduce columna: ",
                "tocat": "Tocado! sigue así...",
                "aigua": "agua",
                "enfonsat": "hundido",
                "posuse": "Esta posición ya ha sido elegida",
                "shipuse": "Este barco ya ha sido hundido",
                "menu":" 0: Crear nuevo tablero \n 1: Cargar tablero \n 2: Salida \n",
                "avis" : "Para salir, escribir quit",
                "escull" : "elige tablero"
            },
            "en": {
                "benvinguts": "Welcome to Naval Wars!",
                "introdueix fila": "Insert row: ",
                "introdueix columna": "Insert column: ",
                "tocat": "Boum! Well done, keep it up...",
                "aigua": "miss",
                "enfonsat": "sunk",
                "posuse": "This position has already been chosen",
                "shipuse": "This ship has already been sunk",
                "menu":" 0: Create new board \n 1: Upload board \n 2: Exit \n",
                "avis" : "To go out, write quit",
                "escull" : "Choose board"
            },
        }
        partides = []
        acabat = False
        vaixell = Vaixell([5,4,4,3,3,3,2,2])
        idioma=input("Language: (ca,es,en): ")
        print(missatges[idioma]["benvinguts"])
        while acabat is not True:
            opcio = int(input(missatges[idioma]["menu"]))
            if opcio == 0:
                partides.append(Tauler(10,10,[]))
                tauler=partides[len(partides)-1]
                tauler.SetTauler(creaTauler(tauler.GetX(),tauler.GetY()))
                tauler.SetTauler(colocaFlota(tauler.GetTauler(),vaixell.GetFlota(),casella.Getlletres()))
                partida(missatges,idioma,vaixell.flota,tauler.GetTauler())
            elif opcio == 1:
                if partides:
                    for el in partides:
                        imprimeixTauler(casella.Getlletres(),el.GetTauler(),dev=False)
                    tauler = partides[int(input(missatges[idioma]["escull"]+": "))]
                    partida(vaixell.flota,tauler.GetTauler())

                else:
                    print("No hi ha taulers creats")
            elif opcio == 2:
                acabat=True
    #except:
        #print("Error")