"""
Part 1

Implementeu les classes Cua() i Pila() derivant-les de la classe list nativa de Python. 
La classe list ja disposa de mètodes que poden equivaldre al de les estructures cua i pila,
però volem que tinguin els noms dels mètodes tal i com estan en el TAD.

Cua: mètodes encua(elem), desencua() i esbuida()
Pila: mètodes apila(elem), desapila(), mostraPrimerElement() i esbuida()
Proveu que l'implementació funciona correctament.

Part 2

Utilitzeu les classes Cua() i Pila() que heu implementat per resoldre un comprovador d'expressions matemàtiques.

Un exemple d'expressió algebraica correcta seria:

25+3*(1+2+(30*4))/2
Exemples erronis:

25+3*(1+2+(30*4))/(2
25+3*(1+2+(30*4))/)2(
25+3*(1+2)+(30*4))/2
Com que realitzar el càlcul d'una expressió algebraica és complicat, limitarem l'exercici a 
comprovar que els parèntesis siguin correctes.

L'algorisme ha de fer:

Extreure els parèntesis de l'expressió i ficar-los en la Cua. En l'exemple (bo) de més amunt 
ens quedarien els següents elements a la cua:
['(','(',')',')']
Extreure element per element de la Cua i avaluar-lo utilitzant la Pila:
Si és "(" el fiquem a la pila.
Si és ")" extraiem un element de la pila. Si és un "(" tot ok. Si hem esgotat la pila, és que hi ha un error.
Al final de l'algorisme la pila ha d'estar buida, altrament és que hi ha algun error.
"""

class Cua:
    def __init__(self,cua=[]):
        self.cua=cua
    def encuar(self,thing):
        self.cua.append(thing)
    def desencuar(self):
        return self.cua.pop(0)
    def esbuida(self):
        return False if self.cua else True

class Pila:
    def __init__(self,pila=[]):
        self.pila=pila
    def apila(self,elem):
        self.pila.insert(0,elem)
    def desapila(self):
        return self.pila.pop()
    def mostraPrimerElement(self):
        return self.pila[0]
    def esbuida(self):
        return False if self.pila else True
"""
cua = Cua(["a","b","c"])
cua.encuar("d")
print(cua.cua)
print(cua.desencuar())
print(cua.cua)
cua.encuar("d")
print(cua.cua)
"""
"""
pila = Pila(["a","b","c"])
pila.apila("d")
print(pila.pila)
print(pila.desapila())
print(pila.pila)
print(pila.mostraPrimerElement())
pila.desapila()
pila.desapila()
pila.desapila()
print(pila.pila)
print(pila.esbuida())
"""
cua = Cua([])
pila = Pila([])
operacio="25+3*(1+2)+(30*4))/2"
for el in operacio:
    if el =="(" or el == ")":
            cua.encuar(el)
while not cua.esbuida():
    parentesis=cua.desencuar()
    if parentesis=="(":
        pila.apila(parentesis)
        if pila.esbuida() or not pila.esbuida() and cua.esbuida():
            print("Es erroni")
            break
    else:
        if pila.esbuida():
            print("Es erroni")
            break
        else:
            pila.desapila()

