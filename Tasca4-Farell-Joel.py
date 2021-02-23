"""
El programa generarà una seqüència aleatòria de mida 4 que serà una combinació de les següents possibles lletres “ABCDE”,
pot haver-hi lletres repetides, per exemple AABB, ACBD, ADAB, BBDC, etc.
L'usuari té 5 vides, és a dir 5 possibilitats per intentar encertar la combinació.
Mentre no hagi encertat la combinació, i encara tingui vides fer:
Resta una vida. Mostra les vides restants..
Mostra els intents que ha fet fins el moment. (fer al final)
Demana una combinació de lletres per teclat i no avança fins que no sigui una combinació possible
(mida 4 i formada per les lletres possibles)
Compta quantes lletres encertades estan en la posició correcta.
Marca aquestes posicions per evitar comptar-les dues vegades.
Compta quantes lletres encertades en posició incorrecta hi ha.
Marca aquestes posicions per evitar comptar-les dues vegades.
Si la combinació és guanyadora,
Mostra missatge d’enhorabona i finalitza el programa.
En altre cas:
Mostra quines lletres en posició correcta hi ha amb el símbol ‘#’.
Mostra quines lletres encertades hi ha en posició incorrecta amb el símbol ‘*’.
Mostra les lletres no existents a la combinació amb el símbol ‘-’.
Per exemple si la combinació guanyadora és AACB i l’usuari entra ACDE ha de mostrar # * - -.
La A és correcta i està en la posició correcta #, la C és correcta en posició incorrecta * i la resta D E no encertades, per tant - -.

"""

import random
Score=""
board=[]
lletres=["A","B","C","D","E"]
fin=False
contador=1
string=[]
vides=5
UserInput=[]
mida=4
#Creem un string de cuatre lletres random
for i in range (mida):
    num=random.randint(0,4)
    string.append(lletres[num])
#Comença el joc
while fin!=True:
    Final=""
    print("Vides restants: ",vides)
    Resp=input("Introdueix una combinació de 4 lletres formades per ABCDE: ")
    
    #Afegim la resposta del usuari a una llista 
    for el in Resp:
        UserInput.append(el)
    el=""
    
    print(Resp,"=>",end=" ")
    #Comparem el string fet anteriorment amb el Input del usuari, afegint # si la lletra es al lloc correcte,
    #* si la lletra es correcte pero al lloc incorrecte i - si la lletra es incorrecte
    for i in range (mida):
        if UserInput[i]==string[i]:
            Final=Final+"#"
        else:
            if UserInput[i] in string:
                Final=Final+"*"
            elif UserInput[i] not in string:
                Final=Final+"-"
    
    print(Final)
    
    #Afegim l'Score a una llista
    Score=Resp+" => "+Final
    board.append(Score)
    
    #Fem print de tot l'score aconseguit:
    for j in range (len(board)):
        if j==0:
            continue
        else:
            print(board[j])
    #Comprobem si es correcte, sino resta una vida i si el contador de vides es queda a 0, es termina el Joc
    if Final=="####":
        fin=True
        print("Has encertat!!")
    else:
        vides=vides-1
        if vides == 0:
            fin=True
            print("-----GAME OVER-----")
                
    UserInput.clear()
    