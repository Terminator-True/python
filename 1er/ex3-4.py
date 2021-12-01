"""
Crea un fitxer de text abece.txt, en python amb el contingut: 
a
bb
ccc
dddd
...
zzzzzzzzz...zz

utilitzarem una trampeta
lletra="a"
lletraSeguent=chr(ord(lletra)+1)
"""
abecedari="abcdefghijklmnñopqrstuvwxyz"
i=0
with open("text/abece.txt","w") as f:
    for el in abecedari:
        i+=1
        f.write(el*i+"\n")
