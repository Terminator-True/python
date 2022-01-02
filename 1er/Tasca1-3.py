"""
Fes un programa per endevinar un nombre entre l’1 i el 9 (ambdós inclosos) que es genera aleatòriament. L’usuari introduirà el nombre per teclat i el programa retornarà:

si l’ha encertat : ENHORABONA!! Ets un crack!
sinó. Si la diferència és només d’1:
quasi, pels pèls!
si la diferència  és més de 4: dedica’t al parxís
si no: la propera vegada ho faràs millor


"""

import random   
numU=0
numR=0

NumR=random.randint(0,9)

NumU=input("Posa un número de l'1 al 9: ")

if numU==NumR:
    print("ENHORABONA!! Ets un crack!")

elif numU==numR+1 or numU==numR-1:
    print("Quasi, pels pèls!")
elif numU>=numR+4 or numU<=NumR-4:
    print("dedica’t al parxís")
else:
    print("la propera vegada ho faràs millor")