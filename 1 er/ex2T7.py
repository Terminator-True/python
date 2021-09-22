"""
Fes un programa en Python anomenat ex2.py que accepta 2 arguments, 
el primer comprova que és un string que només conté lletres, el segon comprova 
que són dígits i el transforma a sencer, i si és així fa un print de l’string 
tantes vegades com indica el paràmetre. Indica amb un print quin error ha comès l’usuari en 
cas que els arguments siguin incorrectes.
"""
import sys
User_input=sys.argv
if User_input[1].isdigit():
    print("El primer argument ha de ser un string")
else:
    if User_input[2].isdigit():
        for i in range(int(User_input[2])):
            print(User_input[1])
    else:
        print("El segon argument ha de ser un número")
