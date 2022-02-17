from tkinter import *

class Calculadora:
    def __init__(self, master):
        #Configuració de la finestra
        self.master = master     
        master.title("Calculadora")
        #Fem que la finestra no es pugi redimensionar
        master.resizable(width=0, height=0)
        #Creació de la variable calcul 
        self.calcul=StringVar()
        #Caixa de text
        self.entry=Entry(master, textvariable=self.calcul,state="disabled",width=40)
        #Ubicar l'entry a la finestra
        self.entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        #Creació de botons:
        #Crea una llista, de botons amb els carácters '123*456/789-.0+C=' y cada cop que es fa click crida a la funció
        #click que gestiona l'acció segons el tipus de text del botó
        self.buttons=[Button(master, text=char,width=9,height=1,command=lambda char=char:self.click(char)) for char in "123*456/789-.0+C="]
        self.posicionar()
        self.calcul=""

    #Posiciona els botons a la finestra
    def posicionar(self):
        i=0
        for fila in range(1,5):
            for columna in range(4):
                self.buttons[i].grid(row=fila,column=columna)
                i+=1
        #Ubicar el caracter '=' al final
        self.buttons[16].grid(row=5,column=0,columnspan=4)

    #Mostra al entry un carácter pasat per parámetre
    def mostra(self,char):
        self.entry.configure(state="normal")
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")
    #Neteja el que hi ha escrit a l'entry
    def neteja(self):
        self.entry.configure(state="normal")
        self.entry.delete(0,'end')
        self.entry.configure(state="disabled")
    #Gestiona l'acció que fa un botó al fer click segons el carácter passat per parámetre
    def click(self,char):
        try:
            if char not in "0123456789+-/*.":
                if char == "=" and self.calcul!="":
                    res = str(eval(self.calcul))
                    self.calcul=""
                    self.neteja()
                    self.mostra(res)
                elif char == "C":
                    self.calcul=""
                    self.neteja()
            else:
                self.calcul+=str(char)
                self.mostra(char)
        except SyntaxError:
            self.calcul=""
            self.neteja()
            self.mostra("Error")
        except ZeroDivisionError:
            self.calcul=""
            self.neteja()
            self.mostra("No es pot dividir per 0")


#Programa principal
if __name__=="__main__":
    root = Tk()   
    finestra = Calculadora(root)
    root.mainloop()