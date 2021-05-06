"""
Crea un fitxer de text saluda.txt, amb python amb el contingut: "Bon dia CLASSE!!".  i tanca'l. Obre el fitxer anterior, i 
afegeix-li les següents frases, cadascuna en una línia diferent: 

Bona nit a tot@s !!!
Buff no puc dormir, potser que compti xaiets
"""

with open('saluda.txt','w') as f:
    f.write("Bon dia CLASSE!!")
with open('saluda.txt','a') as f:
    f.write("\nBona nit a tot@s !!\nBuff no puc dormir, potser que compti xaiets")
