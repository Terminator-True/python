"""
Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta.
"""

from img import subimg
import os
from imgio import read_bn
def load_patterns(prefix="patro"):
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
                if content[i].split("_")[2][0]>content[i+1].split("_")[2][0]:
                    content[i],content[i+1]=content[i+1],content[i]
            except:
                pass
    return content
def match(img,patlst):
    def ordena(elem):
        return elem[1]
    """Donada una llista de patrons patlst i una imatge img retorna un enter que correspon amb el
    dıgit mes semblant d’acord amb els conjunt de patrons usat. La imatge img ha de tenir la
    mateixa alçada que els patrons."""
    similituds=[]
    pi=0
    for z in range(len(patlst)):
        ColIguals=0
        comparation=read_bn("2 n/Tasca4.1/patrons/"+patlst[z])
        if len(comparation[1][0])>len(img[1][0]):
            files=len(comparation[1])
            rows=len(comparation[1][0])
            arow=len(img[1][0])
            longer=comparation[1]
            shorter=img[1]
        else:
            files=len(img[1])
            rows=len(img[1][0])
            arow=len(comparation[1][0])
            longer=img[1]
            shorter=comparation[1]
        for i in range(files):
            pi=0
            for k in range(arow-rows+1):
                m=i
                for j in range(rows):
                    if longer[j][i]==shorter[j][m]:
                        pi=pi+1
                m+1
            #print("Pixels identics:",pi)
            #print(len(img[1]))
            if pi<len(img[1]):
                ColIguals+=1
        similituds.append((patlst[z].split("_")[len(patlst[z].split("_"))-1][0],ColIguals))

    similituds.sort(key=ordena,reverse=True)
    print(similituds)
    return similituds[0][0]

print(match(read_bn("/home/joel/Escritorio/python/2 n/Tasca4.1/sortida/digit_1.jpeg"),load_patterns()))
