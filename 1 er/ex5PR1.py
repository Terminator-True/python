"""
Fes un programa que llegeixi del fitxer "text.txt" i escrigui el contingut en un fitxer nou de nom "text2.txt". 
Mostra en el mateix programa el contingut del fitxer "text2.txt" (l'hauràs de tornar a obrir ara en mode lectura).

"""

try:
    with open("text/text.txt","r") as f:
            with open("text/text2.txt","w") as f2:
                linies=f.readlines()
                f2.writelines(linies)
finally:
    with open("text/text2.txt","r") as f:
        print(f.read())
