"""
Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta.
"""

from img import subimg
import os

def load_patterns(prefix):
    """Aquesta funci ́o rep com a par`ametre el prefix dels noms dels fitxers que contenen els patrons
    dels d ́ıgits i retorna la llista d’imatges corresponent als patrons dels d ́ıgits ordenats de 0 a 9.
    Per exemple, si l’argument  ́es patro voldr`a dir que els arxius dels patrons que s’hauran de
    llegir s’anomenaran: patro_0.jpeg, patro_1.jpeg, . . . , patro_9.jpeg."""   
    path="2 n/Tasca4.1/patrons"
    content = os.listdir(path)
    i=0
    acabat=False
    for el in content:
        archiu=el.split("_")
        archiu[0]=prefix
        while not acabat:
            i+=1
            if archiu[2]

        os.rename(path+"/"+el,path+"/"+"_".join(archiu))

    content = os.listdir(path)

    print(content)
load_patterns(prefix="patron")