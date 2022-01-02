"""
Encriptar cosa :3
"""
import random
<<<<<<< HEAD

=======
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Tk

txt1=""
txt2=""
>>>>>>> 91483482e477062c43477ff050f30db99db606f9
abc="abcdefghijklmnñopqrstuvwxyz"
abc2="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШы"
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
<<<<<<< HEAD

=======
>>>>>>> 91483482e477062c43477ff050f30db99db606f9
while acabat is not True:

    User_input=int(input("Elegir(1-Encript 2-Desencript 3-Exit): "))

    if User_input==1:
        Nombre=input("Nombre: ")
        print(encriptar(Nombre))
    if User_input==2:
        Nombre=input("Nombre: ")
        print(desencriptar(Nombre))
    if User_input==3:
        acabat=True