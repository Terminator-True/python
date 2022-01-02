"""
Demana una cadena per teclat  i genera  un diccionari amb la quantitat aparicions de cada caràcter en la cadena.
"""
cadena=input("Introdueix una cadena: ")
num=0
dict_ex2={el:cadena.count(el) for el in set(cadena) }
print(dict_ex2)