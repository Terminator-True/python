"""
Programa l’algorisme del xifratge del Cèsar. Fes dues versions en Python: amb llistes i amb cadenes.
Prova’l amb la frase “m’agraden els algorismes classics”.

"""

T=input("Text a xifrar: ")
X=""
A="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

N=int(input("Posa un decalatge: "))
C=0
for i in range (len(T)):#Recorrem el input
    ll=T[i]
    for j in range (len(A)):#Comparem el input amb l'abcedari
        if ll==A[j]:
            C=j+N#Apliquem el decalatge
    print(A[C], end="")
        