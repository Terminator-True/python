"""
Encriptar cosa :3
"""
import random
from tkinter import *
from tkinter import ttk


abc="abcdefghijklmnñopqrstuvwxyz"
abc2="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШ"
acabat=False

def encriptar(Nombre):
    imprimir=""
    for i in range(len(Nombre)):
        if Nombre[i]==" ":
            imprimir+=" "
        else:    
            for j in range(len(abc)):
                if Nombre[i]==abc[j]:
                    imprimir+=abc2[j]
    return imprimir


def desencriptar(Nombre):
    imprimir=""
    for i in range(len(Nombre)):
        if Nombre[i]==" ":
            imprimir+=" "
        else:    
            for j in range(len(abc2)):
                if Nombre[i]==abc2[j]:
                    imprimir+=abc[j]
    return imprimir

def clicked_encrypt():
    cripto=encriptar(txt1.get())
    lbl1.configure(text = cripto)

window = Tk()

window.title("Whatsapp Encriptado :3")

window.geometry('300x300')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='encrypt')

tab_control.add(tab2, text='Desencrypt')

lbl1 = Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

txt1 = Entry(window,width=20)

btn1 = Button(window ,text="➤" ,command=clicked_encrypt) 

window.mainloop()