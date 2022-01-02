import sys
acabat=False
imprimir=""
opcions=["-i","-p","-P","-w","-f","--help"]
def lineas(arxiu):
        with open(arxiu,"r") as f:
            return len(f.readlines())

def caracter(arxiu,lletra):
    files=0
    with open(arxiu,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            if lletra in Arxiu[i]:
                files+=1
    return files

def comienza_por(arxiu,lletra):
    files=0
    with open(arxiu,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            if lletra==Arxiu[i][0]:
                files+=1
    return files   

def acaba_por(arxiu,lletra):
    files=0
    with open(arxiu,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            for j in range(len(Arxiu[i])-1,0,-1):
                if Arxiu[i][j]=="\n" or Arxiu[i][j]==" ":
                    continue
                else:
                    if Arxiu[i][j]==lletra:
                        files+=1
                        break
                    else:
                        break
    return files    
def compta_paraules(arxiu,lletra=""):
    paraules=0
    with open(arxiu,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            paraula = Arxiu[i].split()
            for el in paraula:
                if lletra=="":
                    paraules+=1
                else:
                    if lletra in el:
                        paraules+=1
    return paraules
def Filtre_Errors(User_input):
    try:
        with open(User_input[0],"r") as f:
            comprobar=True    
    except FileNotFoundError:
        print("Arxiu no existent")
        comprobar=False
    except IndexError:
        print("Fa falta posar un arxiu")
        comprobar=False
    else:
        if len(User_input)>3:
            for i in range(2,len(User_input)-1):
                if User_input[i] not in opcions:
                    comprobar=False
                    print("Opció"+el+"incorrecte")
    return comprobar    


User_input=sys.argv
User_input.pop(0)
if Filtre_Errors(User_input):
    arxiu=User_input[0]
    if len(User_input)==1:
        imprimir+="Hi han "+str(lineas(arxiu))+" linies que compleixen amb el criteri de búsqueda \n"
    elif len(User_input)>=2:
        imprimir+="Hi han "+str(caracter(arxiu,User_input[1]))+" linies que compleixen amb el criteri de búsqueda \n"
        if len(User_input)>2:
            for i in range(2,len(User_input)):
                if User_input[i]=="-p":
                    if "-i" in User_input:
                        imprimir+="Hi han "+str((lineas(arxiu))-(comienza_por(arxiu,User_input[1])))+" linies que compleixen amb criteri de búsqueda \n"
                    else:
                        imprimir+="Hi han "+str(comienza_por(arxiu,User_input[1]))+" linies que compleixen amb criteri de búsqueda \n"
                elif User_input[i]=="-P":
                    if "-i" in User_input:
                        imprimir+="Hi han "+str((lineas(arxiu))-(acaba_por(arxiu,User_input[1])))+" linies que compleixen amb criteri de búsqueda \n"
                    else:
                        imprimir+="Hi han "+str(acaba_por(arxiu,User_input[1]))+" linies que compleixen amb criteri de búsqueda \n"
                elif User_input[i]=="-w":
                    if User_input[1].isalpha() is True:
                        if "-i" in User_input:
                            imprimir+="Hi han "+str(compta_paraules(arxiu)-compta_paraules(arxiu,User_input[1]))+" paraules que compleixen amb criteri de búsqueda \n"     
                        else:
                            imprimir+="Hi han "+str(compta_paraules(arxiu,User_input[1]))+" paraules que compleixen amb criteri de búsqueda \n"
        if "-f" in User_input:
            with open("sortida.txt","w") as f:   
                f.write(imprimir) 
        if "--help" in User_input:
            imprimir+="Sintaxi: $python3 ex4.py /path/file [c] [-i -w -f -p -P] [--help]\n"+"\nArguments:\n\n"+"file:nom d'arxiu\n"+"c: carácter\n"+"-i:invers\n"+"-p: principi línia/paraula\n"+"-P:final línia/paraula\n"+"-w: Paraules amb el [c] \n"+"-f: sotida a un fitxer anomenat sortida.txt \n"+"\n--help: Ajuda"+"\n\nExemple de Crida\n"+"python3 ex4.py a -w -p -i"
print(imprimir)     
