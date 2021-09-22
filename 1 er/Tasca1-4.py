"""
Fes un programa en Python que comprovi que s’ha introduït una lletra per teclat (no més d’una)
i després que comprovi si la lletra introduïda és una vocal o bé una consonant.
"""
i=0
int(i)
Vocals="aeiouAEIOU"

lletra=input("Posa una lletra: ")



while i<4:
    i=i+1
    v=Vocals[i]

    if v==lletra:
        print("Es una vocal")
        