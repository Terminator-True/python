"""
Ets un professor que acabes d’aprendre python i decideixes utilitzar els teus coneixements.
El programa ha de tenir les següents funcionalitats: Afegir Alumne, Eliminar alumne, Afegir  notes a alumne
(mòdul, nota), llistat de tots els alumnes (la llista de tots els alumnes), butlletí  d’un alumne (el nom de l’alumne i totes les seves notes),
estadístiques (que responen a les qüestions més avall) i sortir.

Demana els noms dels alumnes per teclat, els noms dels alumnes  d'una classe i
les notes que han obtingut. Cada alumne pot tenir diferent quantitat de notes, que també
s’introduiran per teclat, valida que siguin notes entre 0 i 10. Guarda la informació en un diccionari
les claus seran els noms dels alumnes i els valors seran llistes de 

"""
moduls="1234"
clase={
    "Maria":[("1",4),("2",5),("3",2),("4",7)],
    "Joan":[("1",10),("2",7),("3",10),("4",5)],
    "Kevin":[("1",6),("2",6),("3",7),("4",9)],
    "Jordi":[("1",10),("2",6),("3",7),("4",9)],
    }

acabat=False
Terminat=False
i=0
suma=0
tot_aprobat=0
Tres_suspeses=0
Repetir=""
mitjana=[]
llistat=[]
Millor=""
while acabat!=True:
    Imprimir="Opcións:"+"\n"+"==============="+"\n"+"1:Afegir alumne"+"\n"+"2:Afegir notes a alumne"+"\n"+"3:Eliminar alumne"+"\n"+"4:llistat alumnes"+"\n"+"5:Bulletí d'un alumne"+"\n"+"6:Estadístiques generals"+"\n"+"0:sortir"
    print(Imprimir)
    User_input=int(input("Que vols Fer?(0-5)"))
    
    if User_input>6 or User_input<0:
        print("No hi ha opció per aquest número")
        
    else:
        if User_input==0:
            acabat=True
        elif User_input==1:
            print("Has sel·leccionat afegir un alumne")
            Nom=input("Nom: ")
            if Nom not in clase:
                clase={Nom:[]}
                llistat+=clase.keys()
            else:
                print("Aquest nom ja existeix")
        elif User_input==2:
            print("Has sel·leccionat afegir notes a  un alumne existent")
            print(sorted(clase))
            Nom=input("A quin alumne vols afegir notes?")
            while Terminat!=True:
                modul=input("A quin mòdul vols afegir nota?(0-4) ")
                if modul=="0":
                    Terminat=True
                else:
                    Nota=int(input("Nota de mòdul "+modul+" :"))
                    clase[Nom]+=[(modul,Nota)]
    
        elif User_input==3:
             print("Has sel·leccionat eliminar a  un alumne existent")
             Nom=input("Quin alumne vols eliminar?")
             clase.pop(Nom)
        elif User_input==4:
            print("Has sel·leccionat Llistar els alumnes")
            print(sorted(clase))
        elif User_input==5:
            print("Has sel·leccionat Llistar el bolletí d'algún alumne")
            Nom=input("De quin alumne vols el bolletí? ")
            Notes=clase.get(Nom)
            for el in Notes:
                print(f"Modul: {el[0]} Nota: {el[1]} ")
        elif User_input==6:
            for el in clase:
                suspeses=0
                aprobades=0
                Alumne=clase.get(el)
                i=0
                suma=0
                for el2 in Alumne:
                    i+=1
                    if el2[1]>4:
                        aprobades+=1
                            
                    if el2[1]<5:
                        suspeses+=1
                    suma+=el2[1]
                mitjana.append(str(suma/i))
                posicio=mitjana.index(max(mitjana))
                Millor=llistat[posicio]
                if aprobades==4:
                    tot_aprobat+=1
                elif suspeses>=3:
                    Tres_suspeses+=1
                elif suspeses==4:
                    Repetir=el[0]
            Imprimir="Alumnes amb tot aprobat: "+str(tot_aprobat)+"\n"+"Alumnes amb més de tres suspeses: "+str(Tres_suspeses)+"\n"+"Alumnes que repetiran tot: "+Repetir+"\n"+"Alumne amb millor mitjana: "+Millor
            print(Imprimir)
                    
