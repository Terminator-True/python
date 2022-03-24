from doctest import master
from function import *
import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import filedialog

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
        #Listar toda la música en una treeview
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
        filemenu.add_command(label="Modificar album")
        filemenu.add_command(label="Afegir cançó", command=self.open)

        menubar.add_cascade(label="Options", menu=filemenu)

        master.config(menu=menubar)
        #RadioButton per el crear llistes de reproducció
        self.radioValue = tk.IntVar() 
        self.tree_list()
    def item_selected(self, event):
        curItem = self.treeview.focus()
        print(self.treeview.item(curItem)["text"])

    def open(self):
        print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Sound files","*.mp3"),("All files","*.*"))))
    def tree_songs(self):
        self.treeview.delete(*self.treeview.get_children())
        albums=init()
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