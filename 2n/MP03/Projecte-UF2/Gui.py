from function import *
import tkinter as tk
from tkinter import ttk
class Reproductor(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        #Configuració de la finestra
        self.master = master     
        master.title("SoundGround")
        master.geometry('700x700')
        #Listar música
        self.treeview = ttk.Treeview(self,height = 30)
        self.treeview.place(x=0,y=0 )
    def Crea_llista(self):
        albums=init()
        for album in albums:
            print(album)
            itemtree = self.treeview.insert("", tk.END, text=album.split("/")[-1])
            songs=albums[album].cançons
            for song in songs:
                self.treeview.insert(itemtree, tk.END, text=song)
        self.treeview.pack()
        self.pack()




        