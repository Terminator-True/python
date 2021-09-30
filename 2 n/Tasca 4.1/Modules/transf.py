"""
Es el m`odul que concentra les eines per transformar imatges. En particular per escalar,  ́
 ́es a dir per a obtenir imatges de resolucions diferents a partir d’una resoluci ́o donada i per
retallar,  ́es a dir per reduir una imatge fins que nom ́es cont ́e els d ́ıgits que la formen.
"""

from PIL import Image

from img import subimg

def vtrim(img):
    for i in range(len(img)): 
        for j in range(len(img[j])):
            if img[i][j]==(0,0,0):
                

