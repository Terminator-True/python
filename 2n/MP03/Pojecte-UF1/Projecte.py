import os 
directori = "/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1"
class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops
    def mostra(self):
        return ",".join([self.ruta,"|".join(self.cançons),self.genere,self.any,self.autor,str(self.numero_cops)])

def ComprovaArchiu(Arxiu):
    try:
        with open (Arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False

def init_dir():
    albums={}
    for base, dirs, files in os.walk(directori+"/music"):
        if files:
            song=[file for file in files if file.split(".")[1]=="mp3"]
            if ComprovaArchiu(base+"/info.txt"):
                with open (base+"/info.txt","r") as f:
                    info=f.read()
                    albums[base]=album(base,song,info.split(":")[0],info.split(":")[2],info.split(":")[1],0)
    with open (directori+"/backups.txt","w") as f:
        f.writelines(" : ".join(['{0} : {1}'.format(key,albums[key].mostra()) for key in albums]))
        
def init():
    albums={}
    if ComprovaArchiu(directori+"/backups.txt"):
        with open (directori+"/backups.txt","r") as f:
            text=f.read()
            list=text.split(":")
            for i in range(len(list)):
                if i%2!=0:
                    info=list[i].split(",")
                    albums[list[i-1]]=album(info[0],info[1].split("|"),info[2],info[3],info[4],info[5])
    else:
        albums={}
    
    if ComprovaArchiu(directori+"/estat_reproductor.txt"):
        with open (directori+"/estat_reproductor.txt","r") as f:
            info=f.readlines()
            os.system("mpc add directori"+'/'+info[0])
            os.system('mpc seek'+info[1].split("(")[1].replace(")",""))
            os.system("mpc volume 30")

    return albums

def Play_Pause():
    os.system("mpc toggle")

def Next():
    os.system("mpc next")

def Anterior():
    os.system("mpc prev")

def ValumeMas(num):
    os.system("mpc volume + "+num)

def ValumeMenos(num):
    os.system("mpc volume - "+num)

def reset():
    os.system("rm -r "+directori+"/playlist/")
    init_dir()
    os.system("/etc/init.d/mpd restart")
    os.system("mpc update")
    init()

def sortir():
    text="mpc status"+" > "+directori+"estat_reproductor.txt"
    os.system(text)

if __name__=="__main__":
    init_dir()
    menu=0
    while menu != 9:
        try:
            menu=int(input("1. Reproduir/pausar.\n2. Cançó següent.\n3. Cançó anterior.\n4. Augmentar volum.\n5. Disminuir volum.\n6. Editar àlbums. Afegir o eliminar cançons\n7. Reproduir una llista de reproducció.\n8. Crear llistes de reproducció\n9. Sortir.\n10.Reset.\n"))
        except ValueError:
            print("Entrada no valida")
        except:
            print("Error desconegut")
    sortir()