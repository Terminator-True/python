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
        
class Reproductor(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        #Configuració de la finestra
        self.master = master     
        master.title("SoundGround")
        master.geometry('700x700')
        #Listar música
        self.treeview = ttk.Treeview(self,height = 10,selectmode=tk.BROWSE)
        self.treeview.grid(row=0,column=0,columnspan=2,padx=0,pady=0)
        #Tag para registrar el evento 
        self.treeview.tag_bind("Seleccionado", "<<TreeviewSelect>>",
                               self.item_selected)
        #Menu
        menubar = tk.Menu(master)

        filemenu = tk.Menu(menubar, tearoff=0)
        # add a submenu
        sub_menu = tk.Menu(filemenu, tearoff=0)
        sub_menu.add_command(label='Autor')
        sub_menu.add_command(label='Génere')
        sub_menu.add_command(label='Anys')
        sub_menu.add_command(label='Cops')
        sub_menu.add_command(label='Personalitzada',command=self.tree_songs)

        # add the File menu to the menubar
        filemenu.add_cascade(
            label="Crear llista de reproducció",
            menu=sub_menu
        )        
        filemenu.add_command(label="Eliminar cançó")
        filemenu.add_command(label="Afegir cançó", command=self.open)

        menubar.add_cascade(label="Options", menu=filemenu)

        master.config(menu=menubar)
        #RadioButton per el crear llistes de reproducció
        self.tree_list()
        #albums
        self.albums=init()
    def item_selected(self, event):
        curItem = self.treeview.focus()
        print(self.treeview.item(curItem)["text"])
    #Obre un dialog per reguntar archiu en questió, seguidament pregunta al album on es vol afegir y l'afegeix
    def open(self):
        path=filedialog.askopenfilename(initialdir = "/",title = "Afegir cançó",filetypes = (("Sound files","*.mp3"),("All files","*.*")))
        self.popup()
        album_path=self.entryValue()
        for el in self.albums:
            if album_path == el.split("/")[-1]:
                album_path=el
                break
        aggregate(path,album_path)

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

    def tree_list(self):
        self.treeview.delete(*self.treeview.get_children())
        llistes=os.popen("ls "+directori+"/playlist").read()
        for el in llistes.split("\n"):
            self.treeview.insert("", tk.END, text=el.split(".")[0],tags=("Seleccionado",))
        self.treeview.pack()
        self.pack()
    #Popup que demana el album per a la funció open
    def popup(self):
        albums=[el.split("/")[-1] for el in self.albums.keys()]
        self.album=album_window(self.master,albums)
        self.master.wait_window(self.album.top)
    #retorna el valor de el popup anterior  
    def entryValue(self):
        return self.album.value