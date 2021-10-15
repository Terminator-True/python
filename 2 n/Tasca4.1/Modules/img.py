"""
El m`odul cont ́e les operacions prim`aries pel treball amb imatges, ja siguin imatges RGB,
d’escala de grisos o de blanc i negre.
"""
from PIL import Image, ImageChops, ImageEnhance, ImageOps

def null():
    return ('NULL',None)

def is_null(i):
    return i==('NULL',None)

def white_rgb(w,h):
    return ("RGB",[[(255,255,255)]*w]*h)
def white_grey(w,h):
    return ("L",[[255]*w]*h)
def white_bw(w,h):
    return ("1",[[255]*w]*h)
def format(i):
    return i[0]
def matrix(i):
    return i[1]
def i(matrix,tipe=""):
    L=False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not type(matrix[i][j])=="tuple":
                if 0==matrix[i][j] or 255==matrix[i][j]:
                    bn=True
                else:
                    L=True
            else:
                return "RGB",matrix
            
    if L:
        return "L",matrix
    elif bn:
        return "1",matrix

def get_w(i):
    return len(i[1][0])
def get_h(i):
    return len(i[1])
def subimg(i,ow,oh,w,h):
    return [i[0],[i[1][j][k] for j in range(oh,h) for k in range(ow,w)]]
