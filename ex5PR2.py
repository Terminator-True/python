"""
Fes un programa que llegeixi del fitxer "text2.txt" i del fitxer "text3.txt" i escrigui en un fitxer nou de nom "text7.txt" 
alternadament línies d'un fitxer i de l'altre (compte: els 2 fitxers no tenen el matexi nombre de línies, un s'acabarà abans que l'altre). 
Mostra en el mateix programa el contingut del fitxer "text7.txt" (l'hauràs de tornar a obrir ara en mode lectura).
"""
i=0
with open("text/text2.txt","r") as f:
    with open("text/text3.txt","r") as f2:
        with open("text/text7.txt","a+") as f3:
            text3=f2.readlines()
            for el in f.readlines():
                if i%2==0:
                    f3.write(el)
                else:
                    if len(text3)>=i:
                        f3.write(text3[i])
                i+=1
            f3.seek(0)
            print(f3.read())

                    

