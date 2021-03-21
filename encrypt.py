"""
Encriptar cosa :3
"""
import random
abc="abcdefghijklmnñopqrstuvwxyz"
abc2="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШ"
imprimir=""
codify=False
while codify != True:
    User_input=int(input("Elegir(1-Encript 2-Desencript): "))
    if User_input==1:
        Nombre=input("Nombre: ")
        for i in range(len(Nombre)):
            if Nombre[i]==" ":
                imprimir+=" "
            else:    
                for j in range(len(abc)):
                    if Nombre[i]==abc[j]:
                        imprimir+=abc2[j]
        print(imprimir)

    if User_input==2:
        Nombre=input("Nombre: ")
        for i in range(len(Nombre)):
            if Nombre[i]==" ":
                imprimir+=" "
            else:    
                for j in range(len(abc2)):
                    if Nombre[i]==abc2[j]:
                        imprimir+=abc[j]
        print(imprimir)
    else:
        break