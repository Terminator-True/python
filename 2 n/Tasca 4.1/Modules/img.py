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
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (0,0,0)==matrix[i][j] or (255,255,255)==matrix[i][j]:
                blanc_negre=True
            elif matrix[i][j][0]==matrix[i][j][1]==matrix[i][j][2]:
                gris=True
            else:
                return "RGB",matrix
            
    if blanc_negre and gris:
        return "L",matrix
    elif blanc_negre:
        return "1",matrix

def get_w(img):
    return len(img[1][0])
def get_h(img):
    return len(img[1])

#def subimg(img,ow,oh,w,h):


matriu=[[(255,255,255),(255,255,255),(255,255,255),(255,255,255)],
        [(0,0,0),(255,255,255),(255,255,255),(255,255,255)]]

print(img(matriu))