"""
==========================
Joel Farell, Jordi Oliveda
==========================
una línia seria:
	"Pepet, Nosurt, 666777888, pepet@nosurt.com, @pepetnosurt"
1r feu el menú:
	per exemple implementat de manera senxilla
	i anar fent
alta:
	demana les dades amb inputs
	construeix la línia separada per comes (no oblideu el salt de línia)
	i l’afegeix a l’arxiu
	opcional: si el correu electrònic o l’usuari de telegram ja existeix, es demanarà a l’usuari si desitja sobreescriure el contacte

llistat:
	obrir l’arxiu en mode lectura
	imprimir cada línia
	(una idea seria posar un número davant de cada línia)

modifica:
	utilitzeu llistat per mostrar les dades
	i podeu demanar quina entrada es vol modificar (si heu afegit el número)
	deseu les dades de l’arxiu en una llista i treballeu amb la llista
	ara podeu demanar quin camp es vol modificar
	feu les modificacions i torneu a construir la línia (podeu fer servir els mètodes split que ens converteix un text en una llista indicant el separador
	donada una linia = "Pepet, Nosurt, 666777888, pepet@nosurt.com, @pepetnosurt"

	liniaLista = [“Pepet”, “Nosurt”, “666777888”, “pepet@nosurt.com”, “@pepetnosurt”]

	us pot anar bé per modificar el camp que vulgueu
	torneu a transformar la llista en una cadena (ajuntant cada camp separant per comes)
	substituïu a la llista principal amb totes les dades
	deseu la llista sencera a l’arxiu (obriu en modus w i utilitzeu el mètode writelines)

elimina:
	procediu com en modifica, però ara elimineu la línia corresponent de la llista

recuperar segons un camp:
	aquest apartat és per a qui vulgui nota!!!!!!
"""

llista_informacio=["Nom","Cognom","Numero Telefon","Correu","Usuari Telegram"]
def comprovaFitxer(llista):
	try:
		with open ("Agenda.txt","r+") as f:
			for linia in f:
				if llista[3] in linia and llista[3]!="":
					return "01"
				if llista[4] in linia and llista[4]!="":
					return "02"
	except FileExistsError:
		print("Agenda no existent")
	except FileNotFoundError:
		print("Agenda no trobada")
	except:
		print("Error desconegut")
def comprovaCorreu(correu):
	correuDividit=correu.split("@")
	return len(correuDividit)==2 and "." in correuDividit[1] 

def informacio():
	S_N=""
	Sobrescriure=""
	while S_N!="S":
		llista=[input(el+":") for el in llista_informacio]
		while comprovaFitxer(llista)=="01" and Sobrescriure!="S" or comprovaFitxer(llista)=="02" and Sobrescriure!="S":

			while comprovaCorreu(llista[3])==False and llista[3]!="" :
				print("Correu incorrecte")
				llista[3]=input("Correu: ")

			if comprovaFitxer(llista)=="01":
				print("Correu es igual a un altre de la agenda")
				Sobrescriure=input("Sobrescriure el registre?")
				if Sobrescriure=="N":
					llista[3]=input("Correu: ")
				else:
					elimina(Consulta(llista[3],For_User=False),For_user=False)

			while llista[4][0]!="@" and llista[4]!="" :
				print("Usuari de telegram incorrecte Falta: '@'")
				llista[4]=input("Usuari Telegram: ")

			if comprovaFitxer(llista)=="02":
				print("Usuari de telegram es igual a un altre de la agenda")
				Sobrescriure=input("Sobrescriure el registre?")
				if Sobrescriure=="N":
					llista[4]=input("Usuari Telegram: ")
				else:
					elimina(Consulta(llista[4],For_User=False),For_user=False)

		S_N=input(",".join(llista)+"\n"+"Informació correcte?")

	return llista

def Alta():
		with open ("Agenda.txt","a+") as f:
			f.writelines(",".join(informacio()))
			f.write(" \n")

def modifica():
		try:
			with open ("Agenda.txt","r") as f:
				lineas=f.readlines()
				for i in range (len(lineas)):
					print("\n",i," ",lineas[i])
			linea=int(input("Línea a modificar: "))
			modificacio=lineas[linea]
			liniallista=modificacio.split(",")
			print("|".join(liniallista),"|".join(llista_informacio))
			camp=input("Quins camp vols modificar?")
			for i in range(len(llista_informacio)):
				if camp==llista_informacio[i]:
					print("Camp a modificar: ",liniallista[i])
					liniallista[i]=input("Modificació:")
					lineas[linea]=",".join(liniallista)
					if camp==llista_informacio[len(llista_informacio)-1]:
						lineas[linea]+=(" \n")
					with open ("Agenda.txt","w") as fi:
						fi.writelines(lineas)
		except ValueError:
			print("Ha de ser un número")
		except IndexError:
			print("Error, linia no existent")
		except FileExistsError:
			print("Agenda no existent")
		except FileNotFoundError:
			print("Agenda no trobada")
		except:
			print("Error desconegut")
def elimina(linea=-1,For_user=True):
	try:
		with open ("Agenda.txt","r+") as f:
			lineas=f.readlines()
			if For_user==True:
				for i in range (len(lineas)):
					print("\n",i," ",lineas[i])
				linea=int(input("Línea a Esborrar: "))
		lineas.pop(linea)		
		with open ("Agenda.txt","w") as fi:
			fi.writelines(lineas)
	except ValueError:
		print("Ha de ser un número")
	except IndexError:
		print("Error, linia no existent")
	except FileExistsError:
		print("Agenda no existent")
	except FileNotFoundError:
		print("Agenda no trobada")
	except:
		print("Error desconegut")

def Consulta(camp,For_User=True):
	i=0
	try:
		with open ("Agenda.txt","r") as f:
			for el in f:
				i+=1
				if camp in el and For_User==True:
					return el
				elif camp in el and For_User==False:
					return i-1
	except FileExistsError:
		print("Agenda no existent")
	except FileNotFoundError:
		print("Agenda no trobada")
	except:
		print("Error desconegut")
	

def ProgramaPrincipal(User_input):
	if User_input==5:
		return True
	elif User_input==1:
		Alta()
	elif User_input==2:
		modifica()
	elif User_input==3:
		elimina()
	elif User_input==4:
		camp=input("Buscar: ")
		print(Consulta(camp))
	else:
		print("Opció no existent")
		return False
def printMenu():
	imprimir=""
	imprimir+="==================================================\n"+"\n░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░\n"+"██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗\n"+"██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║\n"+"██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║\n"+"╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝\n"+"==================================================\n"
	print(imprimir)
	print("1: Alta\n"+"2: Modifica\n"+"3: Elimina\n"+"4: Consulta\n"+"5: Sortir\n")
acabat=False
while acabat is not True:
	try:
		printMenu()
		User_input=int(input("Opció a elegir: "))
		acabat=ProgramaPrincipal(User_input)
	except ValueError:
		print("Ha de ser un número")
	except KeyboardInterrupt:
		print("Adeu!")
		acabat=True
	except:
		print("Error desconegut")
