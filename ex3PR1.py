"""
Fes un programa que afegeixi una línia més al fitxer de text "text.txt" i el mostri per pantalla. Fes-lo usant les comandes open i close.
 Per poder afegir al fitxer cal obrir-lo en mode append i després per mostrar-lo cal tornar-lo a obrir en mode read.

"""
try:
    f=open("text/text.txt","a+t")
    f.write("Quarta línea \n")
    f.seek(0)
    print(f.read())
finally:
    f.close()
    print("Fet correctament")