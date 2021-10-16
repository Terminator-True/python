"""
Es el m`odul que concentra les eines per transformar imatges. En particular per escalar,  ́
 ́es a dir per a obtenir imatges de resolucions diferents a partir d’una resoluci ́o donada i per
retallar,  ́es a dir per reduir una imatge fins que nom ́es cont ́e els d ́ıgits que la formen.
"""

from PIL import Image as img
import img 
from img import subimg
from imgio import read_bn,show

def vtrim(img):
    detectat=False
    for i in range(len(img[1])): 
        wp = 0
        for j in range(len(img[1][i])):
            if img[1][i][j]==0 and not detectat:
                detectat = True
                ow = 0
                oh = i
                #Una vegada que es detecta un píxel negre, fa que la vegada que es detecti una línea completament blanca
                #Es retalli el caracter
            elif img[1][i][j]==255:
                #White pixel o wp, compta els píxels blancs en una línea
                wp += 1
                #Si tota la línea es de píxels blancs, vol dir que el caracter ja ha terminat, així que ho retallem
            if wp == len(img[1][j]) and detectat or i==len(img[1])-1 and detectat:
                w=len(img[1][j])
                h=i
                return subimg(img,ow,oh,w,h)
          
       # if not detectat:
        #   return None
def htrim(img):
    """Fa una feina similar a la funci ́o vtrim() per`o en la direcci ́o horitzontal."""
    i=0
    j=0
    fi=len(img[1][0])-1
    fj=len(img[1])-1
    VI=False
    VF=False
    while not VI and not VF:
        if img[1][j][i] == 0:
            print("hola")
            oh=0
            ow=i-1
            VI=True
        
        if  img[1][fj][fi] == 0:
            h=len(img[1])
            w=i-1
            VF=True

        j+=1
        i+=1
        fi-=1
        fj-=1
    return subimg(img,ow,oh,w,h)
            
def scale(src, h):
    """
    Escala la imatge a l'alçada `h` conservant l'aspect ratio
    """
    # Compute src and dst sizes
    src_h = img.get_h(src)
    src_w = img.get_w(src)

    # Scaling factor
    fh = float(src_h) / h

    # dst dimension
    dst_h = h
    dst_w = int(round(src_w / fh))

    # Mostrejem matriu original
    sm = img.matrix(src)
    dst = [ [sm[int(round(fh*h))][int(round(fh*w))] for w in range(dst_w)] 
            for h in range(dst_h)]             

    return img.i(dst, '1')

#show(vtrim(read_bn("2 n\Tasca4.1\sortida\digit_3.jpeg")))