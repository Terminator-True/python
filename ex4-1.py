import sys

def lineas(file):
        with open(file,"r") as f:
            return len(f.readlines())

def caracter(file,lletra):
    files=0
    with open(file,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            if lletra in Arxiu[i]:
                files+=1
    return files
"""
def comanda_inversa(file,lletra):
    return lineas(file)-caracter(file,lletra)
"""
def comienza_por(file,lletra):
    files=0
    with open(file,"r") as f:
        Arxiu=f.readlines()
        for i in range(len(Arxiu)):
            if lletra==Arxiu[i][0]:
                files+=1
    return files   

def acaba_por(file,lletra):
    files=0
    with open(file,"r") as f:
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
def compta_paraules(file,lletra=""):
    paraules=0
    with open(file,"r") as f:
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

User_input=sys.argv
User_input.pop(0)
print(User_input)