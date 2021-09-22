"""
Modifica l’algorisme d’endevinar un nombre. El programa demanarà nombres fins que l’encertis.

Fes un algorisme per endevinar un nombre entre l’1 i el 9 (ambdós inclosos) que es genera aleatòriament.
L’usuari introduirà el nombre per teclat i el programa retornarà:
si l’ha encertat : ENHORABONA!! Ets un crack!
sinó. Si la diferència és només d’1:
quasi, pels pèls!
si la diferència  és més  4: dedica’t al parxís
si no: la propera vegada ho faràs millor

"""

import random   
numU=0
numR=0
Correcte=False

NumR=random.randint(0,9)
print(NumR)
while Correcte == False:
    

    NumU=int(input("Posa un número de l'1 al 9: "))

    if NumR==NumU:
        print("ENHORABONA!! Ets un crack!")
        Correcte=True
        
    elif numU==NumR+1 or numU==NumR-1:
          print("Quasi, pels pèls!")
    elif NumU>=NumR+4 or NumU<=NumR-4:
        print("dedica’t al parxís")
    else:
        print("la propera vegada ho faràs millor")
