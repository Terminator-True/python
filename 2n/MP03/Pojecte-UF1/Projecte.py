import os 

class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops
    def mostra(self):
        return self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops

def ComprovaArchiu(Arxiu):
    try:
        with open (Arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False

def init_dir():
    albums={}
    for base, dirs, files in os.walk('/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1/music'):
        if files:
            song=[file for file in files if file.split(".")[1]=="mp3"]
            if ComprovaArchiu(base+"/info.txt"):
                with open (base+"/info.txt","r") as f:
                    info=f.read()
                    albums[base]=album(base,song,info.split(":")[0],info.split(":")[2],info.split(":")[1],0)
    with open ("/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1/backups.txt","w") as f:
        f.writelines(" : ".join(['{0} : {1}'.format(key,albums[key].mostra()) for key in albums]))
    return albums

def init():
    pass
def reset():
    directori="/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1/music/"
    os.system("rm -r "+directori)
    init_dir()
    os.system("/etc/init.d/mpd restart")
    os.system("mpc update")
    init()

def sortir():
    directori="/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1/"
    stat=os.system("mpc status")
    text=stat+' > '+directori+"estat_reproductor.txt"
    os.system(text)

if __name__=="main":
    init()
    menu=0
    while menu != 9:
        try:
            menu=int(input("1. Reproduir/pausar.\n2. Cançó següent.\n3. Cançó anterior.\n4. Augmentar volum.\n5. Disminuir volum.\n6. Editar àlbums. Afegir o eliminar cançons\n7. Reproduir una llista de reproducció.\n8. Crear llistes de reproducció\n9. Sortir.\n10.Reset.\n"))
        except ValueError:
            print("Entrada no valida")
        except:
            print("Error desconegut")
    sortir()