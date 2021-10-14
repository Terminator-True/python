import sys
parametre=sys.argv
parametre.pop(0)
imprimir=""
def Filtre_Errors(parametre):
    try:
        with open(parametre[0],"r") as f:
            comprobar=True    
    except FileNotFoundError:
        print("Arxiu no existent")
        comprobar=False
    except IndexError:
        print("Fa falta posar un arxiu")
        comprobar=False
    return comprobar   

def mostra_linies(parametre,top=False):
    User_input=int(input("Cuantes línies vols imprimir?"))
    with open(parametre[0],"r") as f:
        llinies=f.readlines()
        if top:
            if User_input>len(llinies)-1:
                print("".join(llinies))
            else:
                print("".join(llinies[User_input:]))

        else:    
            if User_input>len(llinies)-1:
                print("".join(llinies))
            else:
                print("".join(llinies[:User_input]))

def copiaNumerada(parametre):
    i=0
    ArxiuNou=[]
    with open(parametre[0],"r") as f:
        linies=f.readlines()
        for el in linies:
            i+=1
            if el != "\n":
                ArxiuNou.append(str(i)+". "+el)   
            else:
                ArxiuNou.append(el)   
                i-=1     

    with open("Archiu_ex_enumerat.txt","w") as fN:
        fN.writelines(ArxiuNou)

def genera_informe(parametre):
    with open(parametre[0],"r") as f:
        vocals="aeiouàèéíòóú"
        Nvocals=0
        linies=f.readlines()
        imprimir=""
        numero_paraules=0
        numero_caracters=0
        paraula_llarga=0
        paraula_curta=100
        espais=0
        imprimir+="Nombre de línies: "+str(len(linies))+"\n"
        paraules=[el.split() for el in linies]
        for el in linies:
            for el2 in el:
                if el2==" ":
                    espais+=1
                if el2 in vocals:
                    Nvocals+=1

        for el in paraules:
            numero_paraules+=len(el)
            for el2 in el:
                numero_caracters+=len(el2)
                if len(el2)>len(str(paraula_llarga)):
                    paraula_llarga=str(el2)
                elif len(el2)<len(str(paraula_curta)):
                    paraula_curta=str(el2)
                

        
        imprimir+="Nombre de paraules: "+str(numero_paraules)+"\n"
        imprimir+="Nombre de carácters: "+str(numero_caracters+espais)+"\n"
        imprimir+="Número de vocals: "+str(Nvocals)+"\n"
        imprimir+="Paraula mes llarga: "+str(paraula_llarga)+"\n"
        imprimir+="Paraula mes curta: "+str(paraula_curta)+"\n"
        print(imprimir)
        with open("informe.txt","w") as fN:
            fN.write(imprimir)

def afegeix(parametre):
    try:
        with open("informe.txt","r") as f:
            pass
    except FileNotFoundError:
        print("Arxiu informe.txt no existent, general primer utilitzant la opció 4 del menú")
    else:
        with open("informe.txt","a") as f:
            with open(parametre[0],"r") as fN:
                f.writelines(fN.readlines())

acabat=False
imprimir+="0.Sortir\n"+"1. Mostra les N primeres línies d'un archiu\n"+"2. Mostra les N darreres línies d'un archiu\n"+"3. Fes una còpia numerada \n"+"4. Genera informe \n"+"5.Afegeix l'arxiu al informe"

if Filtre_Errors(parametre):
    while acabat is not True:
        print(imprimir)
        try:
            User_input=int(input("Exercici a executar: "))
        except ValueError:
            print("Ha de ser un número")
        else:
            if  User_input==0:
                acabat=True
            elif User_input==1:
                mostra_linies(parametre)
            elif User_input==2:
                mostra_linies(parametre,top=True)
            elif User_input==3:
                copiaNumerada(parametre)
            elif User_input==4:
                genera_informe(parametre)
            elif User_input==5:
                afegeix(parametre)
else:
    print("Començem malament")