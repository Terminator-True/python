"""
Per tal de fer els números de telèfons més fàcils de memoritzar, als proveidors de servei telefònic els agrada trobar paraules (mnemònics) 
que facin que el número sigui fàcil de recordar. Per exemple, el número 6378687 pot ser recordat fàcilment per un dels seus mnemònics, NERVOUS.

Suposeu que heu estat llogats per una companyia telefònica local amb l’objectiu de dissenyar i implementar òptimament la funció recursiva llistarMnemonics, 
que generarà totes les possibles combinacions de lletres corresponents a un número donat, representat com a un string de dígits. Per exemple, la crida a llistarMnemonics("", 2, “723”, diccionari_teclat) ha de generar les següents 27 combinacions possibles de lletres corresponents al prefix 723.
PAD PBD PCD RAD RBD RCD SAD SBD SCD
PAE PBE PCE RAE RBE RCE SAE SBE SCE
PAF PBF PCF RAF RBF RCF SAF SBF SCF

NOTA: La resolució del problema mitjançant una funció no recursiva tindrà una puntuació nul·la.

"""
import random


def crea_diccionari(nums=[2,3,4,5,6,7,8,9],lletres="ABCDEFGHIJKLMNOPRSTUVWXY"):
    dic= {}
    i=0
    for num in nums:
        dic[num]=[lletra for lletra in lletres[i:i+3]]
        i+=3
    return dic

def llistar_mnemonics(res,len,nums,dic=crea_diccionari()):
    if len == -1:
        return res+" "
    else:
        cadena = ""
        for x in dic[int(nums[len])]:
            cadena+=llistar_mnemonics(res+x,len-1,nums,dic)
        return cadena


if __name__=="__main__":
    val = input("Valor: ")
    len = len(val)-1
    print(llistar_mnemonics("",len,val))
