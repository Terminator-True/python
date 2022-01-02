"""
Modifica l’exercici anterior substituint els prints per returns:

Nom funció: Multiplica. Funcionalitat: calcula i retorna el resultat de multiplicar dos números introduïts per teclat.

Nom funció: anys2000. Funcionalitat: Demana a l’usuari l’any actual i retorna: “Des del 2000 han passat x anys”, substituint la x pel
nombre d’anys que han passat
    
Nom funció:  notaUF. Funcionalitat: Demana la nota de l’examen i la nota de pràctiques. Fa el càlcul següent: 
Només fa mitja si les dues notes són més grans o iguals que 4
Nota Mòdul = 70% * NotaEx +30% * NotaPr
Si la nota és més gran o igual que 5 arrodoneix i retorna el literal corresponent ( 5 Aprovat, 6 Bé, 7 8 Notable, 9 10 Execel·lent)
Si està suspès demana si ha comprat un pernil al professor. Si és que si retorna  “aprovat perniler”, sinó “Ens veiem al juny”


"""

acabat=False

def Multiplica(x,y):
    return x*y
def anys2000():
    year=0
    while year<2000:    
        year=int(input("Posa un any: "))
    return year-2000
            
            
    input("\nPulsa return per continuar")
def tiquetFruita():
    
    Fruites_dict={"Pomes":1.0,"Taronges":2.0,"Maduixes":1.2,"Mànecs":4.0,"Peres":1.95}


    fruites=False
    total=0
    tiquet="\n Fruiteria\n ===================\n"
    for fruita in Fruites_dict:
        
        pes=float(input("Introdueix el pes de la fruita en kg: "+ fruita+"\t"))
        preu=pes*Fruites_dict[fruita]
        tiquet+="\n"+fruita+":"+str(pes)+"Kg \t"+str(preu)+"€"
        total+=preu
        
    tiquet=tiquet+"\n ===================\n"+"Import total "+str(round(total))+"€"
    
    return tiquet

def notaUF():
    
    practiques=int(input("Nota de práctiques: "))
    examen=int(input("Nota de exàmen: "))
    
    NotaFinal=int(((70*examen)/100)+((30*practiques)/100))
    if NotaFinal<=4:
        Perniler=input("La teva nota es inferior a 5... Has comprat el pernil?(S/N)")
        if Perniler=="S" or Perniler=="s":
            imprimir="Aprovat perniler "+"( ❛ ͜ʖ ❛ )"
        else:
            imprimir=":( Ens veiem al juny"

    elif NotaFinal>=5:
        if NotaFinal==5:
            imprimir="Nota mitja: "+str(NotaFinal)+" Suficient"
        elif NotaFinal==6:
             imprimir="Nota mitja: "+str(NotaFinal)+" Bé"
        elif NotaFinal==7 or NotaFinal==8:
             imprimir="Nota mitja: "+str(NotaFinal)+" Notable"
        elif NotaFinal==9 or NotaFinal==10:
             imprimir="Nota mitja: "+str(NotaFinal)+" Excelent"
    return imprimir
while acabat!=True:
        
    imprimir="    Funcións  1    \n"+"==================\n"+"1. Multiplica \n"+"2. anys2000 \n"+"3. tiquetFruita \n"+"4. notaUF \n"+"5. Sortir \n"
    print(imprimir)
    User_input=int(input("Opció: "))
    if User_input==1:
        x=int(input("Posa un número: "))
        y=int(input("Posa un  altre número: "))
        print(x,"x",y,"=",Multiplica(x,y))
    elif User_input==2:
        print("Desde l'any 2000 han passat: ",anys2000()," anys")
    elif User_input==3:
        print(tiquetFruita())
    elif User_input==4:
        print(notaUF())
    elif User_input==5:
        acabat=True

