"""
Fes un programa que llegeixi del fitxer "text.txt", afegeixi un punt a totes les línies del fitxer "text.txt" i
 les escrigui en un fitxer nou de nom "text4.txt". Mostra en el mateix programa el contingut del fitxer "text4.txt" 
 (l'hauràs de tornar a obrir ara en mode lectura).

"""
with open("text/text.txt","r") as f:
    with open("text/text4.txt","w+") as f2:
        for el in f.readlines():
            f2.write(el.replace(" \n",". \n"))
        f2.seek(0)
        print(f2.read())