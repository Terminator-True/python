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
def format(img):
    return img[0]
def matrix(img):
    return img[1]
def img(matrix):
    L=False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (0,0,0)==matrix[i][j] or (255,255,255)==matrix[i][j]:
                bn=True
            elif matrix[i][j][0]==matrix[i][j][1]==matrix[i][j][2]:
                L=True
            else:
                return "RGB",matrix
            
    if bn and L:
        return "L",matrix
    elif bn:
        return "1",matrix

def get_w(img):
    return len(img[1][0])
def get_h(img):
    return len(img[1])

#def subimg(img,ow,oh,w,h):


matriu=[[(255,255,255),(255,255,255),(255,255,255),(255,255,255)],
        [(140,140,140),(255,255,255),(255,255,255),(255,255,255)]]

print(img(matriu))