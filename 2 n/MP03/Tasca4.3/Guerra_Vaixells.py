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
class Vaixell():
    def __init__(self):
        self.Flota=[5,4,4,3,3,3,2,2]
    def RetornaFlota(self):
        return self.Flota
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
    def colocaVaixellVertical(self,tauler,f,c,mida):
        if self.comprovaAreaV(tauler,f,c,mida):
            for i in range(f,f+mida):
                tauler[i][c][1]="@"  
        else:
            return False
        return True
    def colocaVaixellHoritzontal(self,tauler,f,c,mida):
        if self.comprovaAreaH(tauler,f,c,mida):
            for i in range(c,c+mida):
                tauler[f][i][1]="@"  
        else:
            return False
        return True

class Casella():
    def __init__(self):
        self.lletres=["A","B","C","D","E","F","G","H","I","J"]
    def RetornaCasellaBuida():
        return [False,"~"]
    def aigua(m,f,c):
        return m[f][c][1]=="~"  
    def tradueixIndex(self,f,c):
        for i in range(len(self.lletres)):
            if self.lletres[i]==c:
                return int(f),int(i)
class Tauler():
    def __init__(self):
        self.x,self.y,self.lletres,self.taulell = 10,10,["A","B","C","D","E","F","G","H","I","J"],[]
    def RetornaLletres(self):
        return self.lletres 
    def creaTauler(self):
        self.taulell=[[Casella.RetornaCasellaBuida() for j in range(self.x)] for i in range(self.y)]
    def imprimeixTauler(self,dev=False):
        s= " "
        print("  ",end="")  
        for i in range(len(self.taulell)):
            print(self.lletres[i],end=s)
        print()

        for j in range(len(self.taulell)):
            print(j,end=s)
            for k in range(len(self.taulell[0])):
                if self.taulell[j][k][0] == False and not dev:
                    print("·",end=s)
                else:
                    print(self.taulell[j][k][1],end=s)   
            print() 
    def colocaFlota(self,m,flota):
        for el in flota:
            VvsH=random.randint(0,1)
            if VvsH==1 :
                acabat=False
                while not acabat:
                    f=random.randint(0,9)
                    c=random.choice(self.RetornaLletres())
                    f,c=Casella.tradueixIndex(f,c)
                    if Casella.aigua(m,f,c):
                        acabat=Vaixell.colocaVaixellHoritzontal(m,f,c,el)
            
            elif VvsH==0:
                acabat=False
                while not acabat:
                    f=random.randint(0,9)
                    c=random.choice(self. RetornaLletres())
                    f,c=Casella.tradueixIndex(f,c)
                    if Casella.aigua(m,f,c):
                        acabat=Vaixell.colocaVaixellVertical(m,f,c,el)
class Partida():
    def tret(self,idioma,missatges,m,f,c):
        m[f][c][0]=True
        if Casella.aigua(m,f,c):
            imprimir=("~  "*6)+"\n"+"    "+missatges[idioma]["aigua"]+"    "+"\n"+("~  "*6)    
        else:
            if  m[f][c][1]=="X":
                imprimir="Aquesta posició ja ha estat elegida"
            elif m[f][c][1]=="#":
                imprimir="Aquest vaixell ja ha estat enfonsat"
            else:
                m[f][c][1]="X"
                if self.tocatIEnfonsat(m,f,c):
                    imprimir=("=  "*6)+"\n"+"     ENFONSAT    "+"\n"+("=  "*6)
                else:
                    imprimir=("-  "*6)+"\n"+"     "+missatges[idioma]["tocat"]+"   "+"\n"+("-  "*6)
        print(imprimir)
    def tocatIEnfonsat(self,m,f,c):
        tocats=0
        if self.orientacio(m,f,c):
            x,y=self.troba1acasellaH(m,f,c)
            vaixell=self.trobaVaixellH(m,x,y)
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
            x,y=self.troba1acasellaV(m,f,c)
            vaixell=self.trobaVaixellV(m,x,y)
            for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                if m[i][y][1]=="X":
                    tocats+=1
            if tocats==vaixell[2]:
                for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                    m[i][y][1]="#"
                return True
            else:
                return False
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
        return c==0 and not Casella.aigua(m,f,c+1) or c==9 and not Casella.aigua(m,f,c-1) or (c!=0 and c!=9) and (not Casella.aigua(m,f,c-1) or not Casella.aigua(m,f,c+1))
    
    def tocatIEnfonsat(self,m,f,c):
        tocats=0
        if self.orientacio(m,f,c):
            x,y=self.troba1acasellaH(m,f,c)
            vaixell=self.trobaVaixellH(m,x,y)
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
            x,y=self.troba1acasellaV(m,f,c)
            vaixell=self.trobaVaixellV(m,x,y)
            for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                if m[i][y][1]=="X":
                    tocats+=1
            if tocats==vaixell[2]:
                for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                    m[i][y][1]="#"
                return True
            else:
                return False

if __name__=="__main__":
    missatges = {
        "ca": {
            "benvinguts": "Benviguts a la Batalla Naval!",
            "introdueix fila": "Introdueix fila: ",
            "introdueix columna": "Introdueix columna: ",
            "tocat": "tocat! segueix així...",
            "aigua":"Aigua",
        },
        "es": {
            "benvinguts": "Bienvenidos a la Batalla Naval!",
            "introdueix fila": "Introduce fila: ",
            "introdueix columna": "Introduce columna: ",
            "tocat": "Tocado! sigue así...",
            "aigua":"Agua"
        },
        "en": {
            "benvinguts": "Welcome to Naval Wars!",
            "introdueix fila": "Insert row: ",
            "introdueix columna": "Insert column: ",
            "tocat": "Boum! Well done, keep it up...",
            "aigua":"Miss"
        },
    }
    acabat=False
    while not acabat:
        pass