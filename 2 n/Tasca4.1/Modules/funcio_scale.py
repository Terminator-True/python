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

    return img.img(dst, '1')
