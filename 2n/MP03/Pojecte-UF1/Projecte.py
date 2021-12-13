import os 

class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops
        



def init_dir():
    for base, dirs, files in os.walk('music'):
        print(files)
init_dir()