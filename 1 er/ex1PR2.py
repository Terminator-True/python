"""
Fes un programa que llegeixi del fitxer "text.txt" i escrigui les línies parells en un fitxer nou de nom "text3.txt". 
Mostra en el mateix programa el contingut del fitxer "text3.txt" (l'hauràs de tornar a obrir ara en mode lectura).

"""
i=0
with open("text/text.txt","r") as f:
    with open("text/text3.txt","w+") as f2:
        for el in f.readlines():
            i+=1
            if i%2==0:
                f2.writelines(el)
        f2.seek(0)
        print(f2.read())