"""
El m`odul cont ́e les operacions prim`aries pel treball amb imatges, ja siguin imatges RGB,
d’escala de grisos o de blanc i negre.
"""
from PIL import Image, ImageChops, ImageEnhance, ImageOps
import funcio_scale

def null():
    return ('NULL',None)

def is_null(i):
    return i==('NULL',None)

def white_rgb(w,h):
    return ("RGB",[[(255,255,255)]*w]*h)
def white_grey(w,h):
    return ("L",[[(255,255,255)]*w]*h)
def white_bw(w,h):
    return ("1",[[(255,255,255)]*w]*h)


print(white_rgb(10,10))
#def subimg(img,ow,oh,w,h):
    
