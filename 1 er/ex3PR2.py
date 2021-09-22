"""
Fes un programa que llegeixi del fitxer "text2.txt" i l'escrigui en un fitxer nou de nom "text5.txt".
 Després llegeixi del fitxer "text3.txt" i l'escrigui a continuació en el fitxer "text5.txt" 
 (hi haurà tot el contingut del fitxer "text2.txt" i després tot el contingut del fitxer "text3.txt") . 
 Mostra en el mateix programa el contingut del fitxer "text5.txt" (l'hauràs de tornar a obrir ara en mode lectura).

"""
with open("text/text2.txt","r") as f:
    with open("text/text3.txt","r") as f2:
        with open("text/text5.txt","a+") as f3:
            f3.writelines(f.readlines())
            f3.write("\n")
            f3.writelines(f2.readlines())
            f3.seek(0)
            print(f3.read())