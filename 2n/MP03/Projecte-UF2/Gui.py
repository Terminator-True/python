#Imports necessaris
from doctest import master
from function import *
import tkinter as tk
from tkinter import LEFT, Button, Entry, Label, Toplevel, ttk
from tkinter import filedialog

#Classe que fa el popup per a demanar el album 
#on s'afegirá la cançó
class album_window(object):
    def __init__(self,master,albums):
        self.albums=albums
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Album on afegir la cançó")
        self.l.pack()
        self.combo=ttk.Combobox(top,state="readonly",values=self.albums)
        self.combo.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.combo.get()
        self.top.destroy()
#Classe que crea el popup per a la creació de llistes de reproducció
#Depenent del que passem per parámetre, obre un tipus de diálog o un altre
class list_window(object):
    def __init__(self,master,params):
        self.params=params
        top=self.top=Toplevel(master)
        self.l=Label(top,text=self.params[0])
        self.l.pack()
        print(params)
        if params[0]=="Anys" or params[0]=="Cops":
            self.entry1 = tk.Entry (top) 
            self.entry2 = tk.Entry (top) 
            self.entry1.pack()
            self.entry2.pack()
        else:
            self.combo=ttk.Combobox(top,state="readonly",values=list(set(self.params[1])))
            self.combo.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        try:
            self.value=(self.entry1.get(),self.entry2.get())
        except:
            self.value=self.combo.get()
        self.top.destroy()

#Classe principal del programa
class Reproductor(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        #Configuració de la finestra
        self.master = master     
        master.title("SoundGround")
        master.geometry('650x300')

        #Fem que la finestra no es pugi redimensionar
        master.resizable(width=0, height=0)

        #Listar llistes de reproducció
        self.treeview = ttk.Treeview(self,height = 10,selectmode=tk.BROWSE)
        self.treeview.grid(row=0,column=0,columnspan=2,padx=0,pady=0)
        self.llista_reproduccio=self.item_selected()
        #Tag para registrar el evento 
        self.treeview.tag_bind("Seleccionado", "<<TreeviewSelect>>",
                               self.item_selected)
        #Menu
        menubar = tk.Menu(master)

        filemenu = tk.Menu(menubar, tearoff=0)
        # add a submenu
        sub_menu = tk.Menu(filemenu, tearoff=0)
        sub_menu.add_command(label='Autor',command=lambda type="autor":self.do_list(type))
        sub_menu.add_command(label='Génere',command=lambda type="genere":self.do_list(type))
        sub_menu.add_command(label='Anys',command=lambda type="anys":self.do_list(type))
        sub_menu.add_command(label='Cops',command=lambda type="cops":self.do_list(type))
        sub_menu.add_command(label='Personalitzada',command=self.tree_songs)

        # add the File menu to the menubar
        filemenu.add_cascade(
            label="Crear llista de reproducció",
            menu=sub_menu
        )        
        filemenu.add_command(label="Eliminar cançó",command=self.eliminar)
        filemenu.add_command(label="Afegir cançó", command=self.open)

        menubar.add_cascade(label="Options", menu=filemenu)

        master.config(menu=menubar)
        #RadioButton per el crear llistes de reproducció
        self.tree_list()
        #albums
        self.albums=init()

        #buttons
        Button(master, text="◄◄",width=5,command=lambda: Anterior()).place(x=0,y=270)
        Button(master, text="Reproduir/pausar",width=15,command= lambda:Play_Pause()).place(x=65,y=270)
        Button(master, text="►►",width=5,command=lambda: Next()).place(x=200,y=270)
        Button(master, text="+",width=3,command=lambda: ValumeMas()).place(x=260,y=270)
        Button(master, text="-",width=3,command=lambda: ValumeMenos()).place(x=305,y=270)
        Button(master, text="Reset",width=10, command=lambda: self.reset()).place(x=550,y=270)
        Button(master, text="Carregar llista",width=10, command=lambda list=self.llista_reproduccio:carrega(list)).place(x=450,y=270)
        
    #Detecta on s'ha fet click de la treeView y ho retorna
    def item_selected(self, event):
        curItem = self.treeview.focus()
        return self.treeview.item(curItem)["text"]
    #Obre un dialog per reguntar archiu en questió, seguidament pregunta al album on es vol afegir y l'afegeix
    def open(self):
        path=filedialog.askopenfilename(initialdir = "/",title = "Afegir cançó",filetypes = (("Sound files","*.mp3"),("All files","*.*")))
        self.popup_afegir()
        album_path=self.entryValue()
        for el in self.albums:
            if album_path == el.split("/")[-1]:
                album_path=el
                break
        aggregate(path,album_path)
        self.tree_list()

    #Popup que demana el album per a la funció open
    def popup_afegir(self):
        albums=[el.split("/")[-1] for el in self.albums.keys()]
        self.album=album_window(self.master,albums)
        self.master.wait_window(self.album.top)
    #Retorna el valor de el popup anterior  
    def entryValue(self):
        return self.album.value

    #Funció principal on es fan les llistes de reproducció
    def do_list(self,type):
        list_param=self.popup_list(type)
        #print(list_param)
        crear_llistes((type,list_param))
        self.tree_list()

    #Popup que demana el album per a la funció do_list
    #Depenent de l'opció que escollim al menú, obre una finestra
    #amb unas característiques o unes altres
    def popup_list(self,type):
        if type=="autor":
            params=["Autor",[self.albums[key].mostra().split(",")[4] for key in albums]]
        elif type == "genere":
            params=["Génere",[self.albums[key].mostra().split(",")[2] for key in albums]]
        elif type == "anys":
            params=["Anys",[self.albums[key].mostra().split(",")[3] for key in albums]]
        elif type == "cops":
            params=["Cops"]
        self.list=list_window(self.master,params)
        self.master.wait_window(self.list.top)
        return self.list.value

    #S'obre un dialog al directori de música
    # i s'elimina la cançó escollida 
    def eliminar(self):
        path=filedialog.askopenfilename(initialdir = directori+"/music",title = "eliminar cançó",filetypes = (("Sound files","*.mp3"),("All files","*.*")))
        deleteSong(path)


    #----------------------------------#
    #Llista totes les cançóns dividides per albums
    def tree_songs(self):
        self.treeview.delete(*self.treeview.get_children())
        albums=self.albums
        for album in albums:
            print(album)
            itemtree = self.treeview.insert("", tk.END, text=album.split("/")[-1],tags=("Seleccionado",))
            songs=albums[album].cançons
            for song in songs:
                self.treeview.insert(itemtree, tk.END, text=song,tags=("Seleccionado",))
        self.treeview.pack()
        self.pack()
    #Llista totes les llistes de reproducció
    def tree_list(self):
        self.treeview.delete(*self.treeview.get_children())
        llistes=os.popen("ls "+directori+"/playlist").read()
        #aprint(llistes)
        for el in llistes.split("\n"):
            self.treeview.insert("", tk.END, text=el.split(".")[0],tags=("Seleccionado",))
        self.treeview.pack()
        self.pack()
    #Fa el reset de el mpc i de la llista de llistes
    #de reproducció
    def reset(self):
        reset()
        self.tree_list()