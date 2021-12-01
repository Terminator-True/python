"""
Fes un programa en python que imprimeix les taules de multiplicar de l’1 a 10 amb un for niuat.
"""
fila=[1,2,3,4,5,6,7,8,9,10]
columna=[1,2,3,4,5,6,7,8,9,10]
for i in fila:
    for j in columna:
        Mult=i*j
        print(i,"x",j,"=",Mult)