"""
Fes un programa que llegeixi del fitxer "text2.txt" i escrigui en un fitxer nou de nom "text6.txt" només les línies parells.
 Després llegeixi del fitxer "text3.txt" i escrigui a continuació en el fitxer "text6.txt" només les línies senars. 
 Mostra en el mateix programa el contingut del fitxer "text6.txt" (l'hauràs de tornar a obrir ara en mode lectura).

"""
i=0
with open("text/text2.txt","r") as f:
    with open("text/text3.txt","r") as f2:
        with open("text/text6.txt","a+") as f3:
            for el in f.readlines():
                i+=1
                if i%2==0:
                    f3.writelines(el)
            f3.write("\n")
            i=0
            for el in f2.readlines():
                i+=1
                if i%2!=0:
                    f3.writelines(el)
            f3.seek(0)
            print(f3.read())