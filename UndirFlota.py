"""
La idea és implementar en Python una versió senzilla del joc de la guerra de vaixells. Jugarem contra l'ordinador en un sol tauler de 10 x 10.
 El programa col·locarà els vaixells aleatòriament i el jugador els haurà de trobar.

Per fer el programa haureu d’implementar tot un seguit de funcions. Us fem una proposta del que és necessari. Recordeu que cal comprovar que funcionen 
amb diferents valors i es comporten correctament. Finalment ho ajuntarem tot i farem el programa general.

En cada posició del tauler hi ha una llista de 2 elements. El primer element és un booleà que desa si la casella ha estat destapada o no, i en el segon 
pot haver els següents valors:

“~” que representa aigua, i és el valor per defecte de totes les posicions 
“@” que representa una casella ocupada per un vaixell
“X” que representa una casella d’un vaixell tocat
“#” que representa una casella d’un vaixell tocat i enfonsat


Funcions:
creaTauler(c)
imprimeixTauler(tauler,dev)
tradueixIndex(fila,columna)
aigual(tauler, fila, columna) 
comprovaAreaH(tauler,f,c,mida)
colocaVaixellHoritzontal(tauler,fila,columna,mida)
colocaVaixellVertical(tauler,fila,columna,mida)
colocaFlota(tauler, flota) 
tret(tauler,f,c)
troba1acasellaH(tauler,x,y) 
trobaVaixellH(tauler,x,y)
troba1acasellaV(tauler,x,y) i trobaVaixellV(tauler,x,y)
tocatIEnfonsat(tauler,f,c)
partidaAcabada(tauler)
"""



dsds