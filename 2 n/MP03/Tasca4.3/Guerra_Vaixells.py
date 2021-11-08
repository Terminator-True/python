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
Cal que puguis jugar diverses partides simultànies (diferents taulells). 
El jugador ha de poder anar canviant entre les diverses partides i reprendre on l'ha deixat.
Cal fer-ho amb OOP i, per tant, primer cal definir els objectes i les estructures de dades i decidir com utilitzar-les en el codi principal. 
Com a mínim, heu d'implementar les següents classes: class Tauler(), class Vaixell() i class Casella()."""

class Casella():
    def __init__(self):
        pass
class Tauler():
    def __init__(self):
        self.x,self.y,self.lletres,self.taulell = 10,10["A","B","C","D","E","F","G","H","I","J"],[] 
    def creaTauler(self):
        self.taulell=[[[False,"~"] for j in range(self.x)] for i in range(self.y)]
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
    
