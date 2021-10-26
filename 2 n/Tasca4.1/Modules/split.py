"""
El m`odul t ́e com a responsabilitat trencar una imatge blanc i negre en un conjunt d’imatges
m ́es petites cadascuna de les quals cont ́e  ́unicament un element (una xifra).
"""

from img import null, subimg
from transf import vtrim,htrim

def split_digit(img):
    detectat=False
    for i in range(len(img[1])): 
        wp = 0
    for j in range(len(img[1][i])):
        if img[1][j][i]==(0,0,0):
            oh = 0
            ow = j-1
            #Una vegada que es detecta un píxel negre, fa que la vegada que es detecti una línea completament blanca
            #Es retalli el caracter
            detectat = True
        elif img[1][j][i]==(255,255,255):
            #White pixel o wp, compta els píxels blancs en una línea
            wp += 1
            #Si tota la línea es de píxels blancs, vol dir que el caracter ja ha terminat, així que ho retallem
            if wp == len(img[1][j]) and detectat:
                w=j
                h=len(img[1])
                return subimg(img,ow,oh,w,h),subimg(img,ow=w,oh=h,w=len(img[1][0]),h=len(img[1]))

    if not detectat:
        return None   