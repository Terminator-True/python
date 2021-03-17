def esDigit(c):
    nums="1234567890"
    if c in nums:
        return True
    else:
        return False
def esEspai(c):
    if c == " ":
        return True

    else:   
        return False
def esSimbol(c):
    simbols="ºª|”@·#$%&/()=’¡?¿`^*+[]]<}{”’<>,;.:-_"
    if c in simbols:
        return True
    else:
        return False

def fesTrim(cadena):
    cadena=cadena.strip()
    for i in range (1,len(cadena)):
        if esEspai(cadena[i]) and esEspai(cadena[i-1]):
                cadena=cadena.replace(cadena[i],"")    
    return cadena

def netejaCadena(cadena):
    for el in cadena:
        if esDigit(el):
            cadena=cadena.replace(el,"")
        elif esSimbol(el):
            cadena=cadena.replace(el,"")
    neta=fesTrim(cadena)
    return neta


User_input=input("Posa una cadena de carácters: ")

print(netejaCadena(User_input))

