# -*- encoding: utf-8 -*-
import img

def rgb_to_lum(pixel):
    """
    Returns the luminance level off a RGB pixel
    """
    return int(1/3.0 * sum(pixel))

def luminance_img(i):
    """
    Transforms a RGB image to a L image using luminance
    """
    mat = img.matrix(i)
    matlum = [[rgb_to_lum(p) for p in F] for F in mat]
    return img.img(matlum, 'L')

def histogram(i):
    """
    Histogram of grey values of `i`
    """
    h = [0] * 256
    for f in img.matrix(i):
        for greyval in f:
            h[greyval] += 1
    return h

def get_threshold(h):
    """
    Get the (index of) two max elements of the histogram
    Usem Otsu thresholding algorithm.
    http://www.labbookpages.co.uk/software/imgProc/otsuThreshold.html
    """
    # Pes del background vs foreground Wb + Wf = 1
    Wb = Wf = 0.0
    # pes total (num pixels)
    total = float(sum(h))
    #
    sumB = 0.0
    # suma ponderada de totes observacions
    sump = sum(float(i)*h for i,h in enumerate(h))

    # maxims temptatius
    threshold = 0
    varMax    = 0.0

    # recorre els possibles discriminants buscant el de variància
    # màxima
    for t, ht in enumerate(h):
        Wb += ht
        if Wb == 0: continue

        Wf = total - Wb
        if Wf == 0: break

        sumB += t * ht
        mB = sumB / Wb
        mF = (sump - sumB) / Wf

        # variancia entre classes
        varE = Wb * Wf * (mB - mF) * (mB - mF)
        
        # determina si es màxim
        if varE > varMax:
            varMax = varE
            threshold = t

    return threshold




def rgb_to_bn(i):
    L = luminance_img(i)
    H = histogram(L)
    discr = get_threshold(H)
    matl = img.matrix(L)
    matbw = [[(0 if greyval < discr else 255) for greyval in f] for f in matl]
#    bw_mean(BW)
    return img.img(matbw, '1')
