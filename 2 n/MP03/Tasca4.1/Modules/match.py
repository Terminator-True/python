"""
Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta.
"""

from img import subimg
import os
from imgio import read_bn,show,read_rgb
from transf import scale,vtrim
from discret import rgb_to_bn
def load_patterns(prefix="patro"):
    def ordena(elem):
        return elem.split("_")[2][0]
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
    content.sort(key=ordena)
    return content

def match(img,patlst):
    def ordena(elem):
        return elem[1]
    """Donada una llista de patrons patlst i una imatge img retorna un enter que correspon amb el
    dıgit mes semblant d’acord amb els conjunt de patrons usat. La imatge img ha de tenir la
    mateixa alçada que els patrons."""
    similituds=[]
    k=0
    for z in range(len(patlst)):
        pi=0
        comparation=read_bn("2 n/Tasca4.1/patrons/"+patlst[z])
        img=vtrim(img)
        if len(comparation[1])<len(img[1]):
            img=scale(img,len(comparation[1]))
        else:
            comparation=scale(comparation,len(img[1]))
        if len(comparation[1][0])>len(img[1][0]):
            columnes=len(comparation[1])
            files=len(comparation[1][0])
            alterFiles=len(img[1][0])
            longer=comparation[1]
            shorter=img[1]
        else:
            columnes=len(img[1])
            files=len(img[1][0])
            alterFiles=len(comparation[1][0])
            longer=img[1]
            shorter=comparation[1]
        for i in range(files):
            for k in range(i,i+files-alterFiles+1):
                for j in range(columnes):
                    try:
                        if longer[j][k]==shorter[j][k]:
                            pi+=1
                    except:
                        pass
        similituds.append((patlst[z].split("_")[len(patlst[z].split("_"))-1][0],pi))
    similituds.sort(key=ordena,reverse=True)
    print(similituds)
    return similituds[0][0]

print(match(read_bn("2 n\Tasca4.1\sortida\digit_2.jpeg"),load_patterns()))
