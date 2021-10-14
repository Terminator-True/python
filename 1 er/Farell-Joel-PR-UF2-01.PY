"""
Nom funció: Multiplica. Funcionalitat: calcula i imprimeix el resultat de multiplicar dos números introduïts per teclat, els inputs es fan a
fora de la funció.

Nom funció: anys2000. Funcionalitat: Input a dins de la funció. Demana a l’usuari l’any actual i escriu: “Des del 2000 han passat x anys”,
substituint la x pel nombre d’anys que han introduït.

Nom funció tiquetFruita. Funcionalitat: tiquet fruita fet a la tasca de dicionaris 9.

Nom funció:  notaUF. Funcionalitat: Demana la nota de l’examen i la nota de pràctiques. Fa el càlcul següent: 
Només fa mitja si les dues notes són més grans o iguals que 4
Nota Mòdul = 70% * NotaEx +30% * NotaPr
Si la nota és més gran o igual que 5 arrodoneix i imprimeix el literal corresponent ( 5 Aprovat, 6 Bé, 7 8 Notable, 9 10 Excel·lent)
Si està suspès demana si ha comprat un pernil al professor/a. Si és que sí imprimeix “aprovat perniler”.

"""

acabat=False

def Multiplica(x,y):
    return x*y
    input("\nPulsa return per continuar")
def anys2000():
    year=0
    while year<2000:    
        year=int(input("Posa un any: "))
        if year<2000:
            continue
        else:
            print("Desde l'any 2000 fins al ",year," han passat: ",year-2000," anys")
            
            
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
        
    print(tiquet,"\n ===================\n")

    print("Import total ",total,"€")
    input("\nPulsa return per continuar")

def notaUF():
    
    practiques=int(input("Nota de práctiques: "))
    examen=int(input("Nota de exàmen: "))
    
    NotaFinal=int(((70*examen)/100)+((30*practiques)/100))
    if NotaFinal<=4:
        Perniler=input("La teva nota es inferior a 5... Has comprat el pernil?(S/N)")
        if Perniler=="S" or Perniler=="s":
            print("Aprovat perniler","( ❛ ͜ʖ ❛ )")
        else:
            print(":(")

    elif NotaFinal>=5:
        if NotaFinal==5:
            print("Nota mitja: ",NotaFinal," Suficient")
        elif NotaFinal==6:
            print("Nota mitja: ",NotaFinal," Bé")
        elif NotaFinal==7 or NotaFinal==8:
            print("Nota mitja: ",NotaFinal," Notable")
        elif NotaFinal==9 or NotaFinal==10:
            print("Nota mitja: ",NotaFinal," Excelent")
    input("\nPulsa return per continuar")
while acabat!=True:
        
    imprimir="    Funcións  1    \n"+"==================\n"+"1. Multiplica \n"+"2. anys2000 \n"+"3. tiquetFruita \n"+"4. notaUF \n"+"5. Sortir \n"
    print(imprimir)
    User_input=int(input("Opció: "))
    if User_input==1:
        x=int(input("Posa un número: "))
        y=int(input("Posa un  altre número: "))
        print(x,"x",y,"=",Multiplica(x,y))
    elif User_input==2:
        anys2000()
    elif User_input==3:
        tiquetFruita()
    elif User_input==4:
        notaUF()
    elif User_input==5:
        acabat=True