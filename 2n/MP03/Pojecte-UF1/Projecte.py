import os 
directori = "/home/joel/Escritorio/python/2n/MP03/Pojecte-UF1"
albums={}
class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops

    def mostra(self):
        return ",".join([self.ruta,"|".join(self.cançons),self.genere,self.any,self.autor,str(self.numero_cops)])

    def get_cançons(self):
        return self.cançons

    def set_cançons(self,new_cançons):
        self.cançons=new_cançons

def ComprovaArchiu(Arxiu):
    try:
        with open (Arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False

def init_dir():
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
    if ComprovaArchiu(directori+"/backups.txt"):
        with open (directori+"/backups.txt","r") as f:
            text=f.read()
            list=text.split(":")
            for i in range(len(list)):
                if i%2!=0:
                    info=list[i].split(",")
                    albums[list[i-1]]=album(info[0],info[1].split("|"),info[2],info[3],info[4],info[5])
    
    if ComprovaArchiu(directori+"/estat_reproductor.txt"):
        with open (directori+"/estat_reproductor.txt","r") as f:
            info=f.readlines()
            os.system("mpc add directori"+'/'+info[0])
            os.system('mpc seek'+info[1].split("(")[1].replace(")",""))
            os.system("mpc volume 30")

def Editar_albums():
    print("|".join([el.split("/")[-1] for el in albums.keys()]))
    albu=input("Quin album vols editar? ")
    for key in albums:
        if key.split("/")[-1].lower()==albu.lower():
            opcio=input("1. Afegir cançons\n2. Eliminar cançons\n")
            if opcio==1:
                path=input("Direcció de cançó a afegir: ")
                os.system("mv"+path+" "+directori+"/music/album2/album6")
            elif opcio==2:
                print("\n".join(albums[key].get_cançons()))
                cancion=input("Cançó a eliminar: ")
                llistaSongs=albums[key].get_cançons()
                if cancion in llistaSongs:
                    llistaSongs.remove(cancion)
                    albums[key].set_cançons(llistaSongs)
                else:
                    print("Cançó no existent")
                
def crear_llistes(param):
    if param==1:
        genero=input("Genere: ")
        for key in albums:
            if albums[key].genere.lower() == genero.lower():
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+genero)
            
    elif param==2:
        autor=input("Autor: ")
        for key in albums:
            if albums[key].autor.lower() == autor.lower():
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+autor)
            
    elif param==3:
        anys=input("Anys: ")
        for key in albums:
            if int(albums[key].any) >= int(anys.split(" ")[0]) and int(albums[key].any) <= int(anys.split(" ")[1]):
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(anys.split(" ")))
    
    elif param==3:
        anys=input("Anys: ")
        for key in albums:
            if int(albums[key].any) >= int(anys.split(" ")[0]) and int(albums[key].any) <= int(anys.split(" ")[1]):
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(anys.split(" ")))

def Reproduir():
    os.system("mpc ls "+directori+"/playlist")
    num=int(input("Cual quieres reproduir?(numero) "))
    os.system("mcp play "+num-1)

def Play_Pause():
    os.system("mpc toggle")

def Next():
    os.system("mpc next")

def Anterior():
    os.system("mpc prev")

def ValumeMas():
    os.system("mpc volume + 5")

def ValumeMenos():
    os.system("mpc volume - 5")

def programa_principal(menu):
    if menu == 1:
        Play_Pause()
    elif menu ==2:
        Next()
    elif menu==3:
        Anterior()
    elif menu==4:
        ValumeMas()
    elif menu==5:
        ValumeMenos()
    elif menu==6:
        Editar_albums()
    elif menu==7:
        Reproduir()
    elif menu==8:
        menu8=int(input("Crear llistes de reproducció segons :\n1. Génere.\n2. Autor.\n3. Interval anys.\n4. Cops que s'ha reproduït l'album\n"))
        crear_llistes(menu8)
    elif menu==9:
        sortir()
    elif menu==10:
        reset()

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
            print(albums)
            menu=int(input("1. Reproduir/pausar.\n2. Cançó següent.\n3. Cançó anterior.\n4. Augmentar volum.\n5. Disminuir volum.\n6. Editar àlbums. Afegir o eliminar cançons\n7. Reproduir una llista de reproducció.\n8. Crear llistes de reproducció\n9. Sortir.\n10.Reset.\n"))
            programa_principal(menu)
        except ValueError:
            print("Entrada no valida")
        except:
            print("Error desconegut")
    sortir()