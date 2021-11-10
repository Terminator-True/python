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

class Vaixell():
    def __init__(self):
        self.vaixells={"portaavions":4,"cuirassats":3,"fragates":2,"patrulleres":1}
    def RetornaVaixell(self,vaixell):
        return self.vaixells[vaixell]
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
    
if __name__=="__main__":
    missatges = {
        "ca": {
            "benvinguts": "Benviguts a la Batalla Naval!",
            "introdueix fila": "Introdueix fila: ",
            "introdueix columna": "Introdueix columna: ",
            "tocat": "tocat! segueix així...",
        },
        "es": {
            "benvinguts": "Bienvenidos a la Batalla Naval!",
            "introdueix fila": "Introduce fila: ",
            "introdueix columna": "Introduce columna: ",
            "tocat": "Tocado! sigue así...",
        },
        "en": {
            "benvinguts": "Welcome to Naval Wars!",
            "introdueix fila": "Insert row: ",
            "introdueix columna": "Insert column: ",
            "tocat": "Boum! Well done, keep it up...",
        },
    }
    acabat=False
    while not acabat:
        pass