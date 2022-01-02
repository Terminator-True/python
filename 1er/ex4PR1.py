"""
Modifica els 3 programes anterior usant la comanda with i no fent servir la comanda close. Posa tot el codi en un sol programa.

"""

try:
    with open("text/text.txt","w") as f:
        lineas=["Primera línea \n","Segona línea \n","Tercera línea \n"] 
        f.writelines(lineas)

    with open("text/text.txt") as f:
        print(f.read())

    with open("text/text.txt","a+") as f:
        f.write("Quarta línea")
        f.seek(0)
        print(f.read())
finally:
    print("Tot correcte")