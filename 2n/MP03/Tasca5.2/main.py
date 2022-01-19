"""
Tokenitzador

Abans que res caldrà tokenitzar el codi que ens ve en un string. Un "token" és un element significatiu per l'aplicació, com per exemple: 
un tag, un símbol ">" o les cometes.

Cal fer una funció tokenitza(s) que ens transformarà el codi en elements clau: un string són caràcters sense significat; en canvi, després de 
"tokenitzar" tindrem elements significatius per comprovar:

Exemple: abans de tokenitzar:

<html><head><title>Exemple</title></head><body><h1>Hola món</h1></body></html>
Després de tokenitzar, tindrem els següents elements (en una llista).

<,html,>,<,head,>,<,title,>,<,/,title,>,<,/,head,>,<,body,>,<,h1,>,<,/,h1,>,<,/,body,>,<,/,html,>


Un cop tinguem aquesta llista d'elements clau, amb una cua i una pila hem de comprovar que s'obren i es tanquen tots els tags correctament. 
En cas contrari, mostrar un error.
"""
import re
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
        
def token_html(string):
    final=[]
    paraula=""
    for char in string:
        if char == "<" or char==">" or char == "/":
            if paraula:
                final.append(paraula)
            final.append(char)
            paraula=""
        else:
            paraula+=char
    return final
if __name__=="__main__":
    html="<html><head><title>Exemple</title></head><body><h1>Hola món</h1></body></html>"
    processed_html=token_html(html)
    print(processed_html)
