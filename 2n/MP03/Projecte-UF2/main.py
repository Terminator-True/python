from Gui import *
#Programa principal
if __name__=="__main__":
    root = tk.Tk()   
    finestra = Reproductor(root)
    finestra.Crea_llista()
    root.mainloop()