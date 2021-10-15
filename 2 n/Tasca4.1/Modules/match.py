"""
Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta.
"""

from img import subimg
import os
from imgio import read_bn
def load_patterns(prefix):
    """Aquesta funci ́o rep com a par`ametre el prefix dels noms dels fitxers que contenen els patrons
    dels d ́ıgits i retorna la llista d’imatges corresponent als patrons dels d ́ıgits ordenats de 0 a 9.
    Per exemple, si l’argument  ́es patro voldr`a dir que els arxius dels patrons que s’hauran de
    llegir s’anomenaran: patro_0.jpeg, patro_1.jpeg, . . . , patro_9.jpeg."""   
    path="2 n/Tasca4.1/patrons"
    content = os.listdir(path)
    for i in range(len(content)):
        archiu=content[i].split("_")
        archiu[0]=prefix
        os.rename(path+"/"+content[i],path+"/"+"_".join(archiu))
    for i in range(len(content)-1):
        if content[i].split("_")[1]=="gruixut":
            try:
                if content[i].split("_")[2]>content[i+1].split("_")[2]:
                    content[i],content[i+1]=content[i+1],content[i]
            except:
                pass
    return content
def match(img,patlst):
    """Donada una llista de patrons patlst i una imatge img retorna un enter que correspon amb el
    dıgit mes semblant d’acord amb els conjunt de patrons usat. La imatge img ha de tenir la
    mateixa alçada que els patrons."""
    for el in patlst:
        comparation=read_bn(el)
        if len(comparation[0])>len(img[0]):
            for i in range(len(img)):
                for j in range(len(img[i])):
                    