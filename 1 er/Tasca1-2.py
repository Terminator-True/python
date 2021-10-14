"""
Escriviu un programa Python per comprovar que un nombre que introduïm per teclat és múltiple de 7 i múltiple de 5.

"""

num=int(input("Posa un número: "))

if num%5==0:
    print(num," es múltiple de 5")
else:
    print(num," no es múltiple de 5")

if num%7==0:
    print(num,"es múltiple de 7")
else:
    print(num," no es múltiple de 7")