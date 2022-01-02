"""from tkinter import *
root = Tk()

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
"""
telegram="joel,farl,321312312,joel@pepe.coc,terminamelamamahuebo"
correuDividit=telegram.split(",")
print(correuDividit[4][0])
if correuDividit[4][0]=="@":
    print("Correcte")
else:
    print("No es")