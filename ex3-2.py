"""
Donada la primera estrofa de "The fly song": 

Una mosca volava per la llum
i la llum es va apagar
i la pobre mosca va quedar a les fosques
i la pobre mosca no va poder volar. 

Crea un programa que escriu el fitxer the_fly_song.txt:

Per crear la cançó cal escriure la primera estrofa.
La segona estrofa és igual a la primera estrofa, però canviant les vocals per a. 
La tercera estrofa és igual a la primera estrofa, però canviant les vocals per e, ...etc...
"""
lletra="Una mosca volava per la llum\ni la llum es va apagar\ni la pobre mosca va quedar a les fosques\ni la pobre mosca no va poder volar.\n \n"
vocals="aeiou"

def Creacançó(lletra,vocals):
    return [[vocals[i] if lletra[j] in vocals else lletra[j] for j in range(len(lletra))]for i in range(len(vocals))]

with open("the_fly_song.txt","w") as f:
    f.write(lletra)
    for el in Creacançó(lletra,vocals):
        f.writelines(el)