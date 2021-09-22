#Jordi Oliveda
import sys
acabat=False
vocals="aeiouAEIOUáàéèíìóòúÁÀÉÈÍÌÓÒÚ"

def llegirN(arxiu,n,top=True):
    c=0
    with open(arxiu,'r') as f:
        if top is True:
            for linia in f:
                if n > c:
                    print(linia)
                c+=1
        elif top is False:
            for linia in f:
                if n > c:
                    print(linia)
                c+=1

def copiaNumerada(arxiu):
    if "." in arxiu:
        carxiu=arxiu+"-numerat.txt"
    else:
        carxiu=arxiu+"-numerat"
    c=0
    with open(arxiu,'r') as f1:
        f1.read()
    with open(carxiu,'a') as f2:
        for linia in f1:
            c+=1
            f2.write(c+". "+linia)
            if linia!=" ":
                f2.write(c+". "+linia)
            else:
                f2.write(linia)

def informe(arxiu):
    linies=0
    paraules=0
    caracters=0
    pvocals=0
    Plong=0
    spai=0
    spaiLlong=0
    PspaiLlong=""
    spaicurt=9
    pspaicurt=""
    with open(arxiu,'r') as f:
        for linia in f:
            linies+=1
            for caracter in linia:
                caracters+=1
                spai+=1
                PspaiLlong+=caracter
                pspaicurt+=caracter
                if caracter==" ":
                    paraules-=1
                    if spai > spaiLlong:
                        spaiLlong=spai
                    if spai < spaicurt:
                        spaicurt=spai
                        pspaicurt=" "
                    PspaiLlong=""
                    spai=0
                if caracter in vocals:
                    pvocals+=1
    final="El nombre de línes és:"+str(linies)+"\nEl nombre de paraules és: "+str(paraules)+"\nEl nombre de caràcters és:"+str(caracters)+"\nEl nombre de vocals és: "+str(pvocals)+"\nLa paraula més llarga és: "+str(PspaiLlong)+"\nLa paraula més curta és: "+str(pspaicurt)
    print(final)
    with open("informa.txt",'a') as f:
        f.write(final)

def afegir(arxiu):
    try:
        with open("informa.txt",'r') as f:
            arxiu=f.read()
        with open("informa.txt",'a') as f1:
            f1.write(arxiu)
    except FileNotFoundError:
        print("Encara no has generat l'informe")

try:
    with open(sys.argv[1],'r') as f:
        print("Existix el axriu")
        while acabat is not True:
            try:
                print("\n1.Mostra les n primerres lines d'un arxiu\n2.Mostra les n darreres línes de l'arxiu\n3.Fes còpia numerada\n4.Genera informe\n5.Afegeix a l'informe\n6.sortir")
                User_input=int(input("Opció a elegir: "))
                arxiu=sys.argv[1]
                if User_input==1:
                    n=int(input("quantes lineas? "))
                    llegirN(sys.argv[1],n)
                elif User_input==2:
                    n=int(input("quantes lineas? "))
                    llegirN(sys.argv[1],n,top=False)
                elif User_input==3:
                    copiaNumerada(arxiu)
                elif User_input==4:
                    informe(arxiu)
                elif User_input==5:
                    afegir(arxiu)
                elif User_input==6:
                    acabat=True
            except ValueError:
                print("Ha de ser un número") 
except FileNotFoundError:
    print("l'arxiu no existeix")
except IndexError:
    print("No s'ha especificat cap arxiu")
