from function import *
import tkinter as tk
from tkinter import ttk
class Reproductor(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        #Configuració de la finestra
        self.master = master     
        master.title("SoundGround")
        #Listar música
        self.treeview = ttk.Treeview(self)
        item = self.treeview.insert("", tk.END, text="Elemento 1")
        subitem = self.treeview.insert(item,tk.END, text="Subelemento 1")
        self.treeview.insert(subitem, tk.END, text="Otro elemento")
        self.treeview.pack()
        self.pack()

    


        