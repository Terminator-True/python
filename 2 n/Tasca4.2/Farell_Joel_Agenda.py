"""
Dissenyeu una aplicació anomenada cognom_nom_agenda.py que permeti entrar dades de clients en una agenda, mostrar-les i enregistrar-les en un arxiu (amb el format que vulgueu). Cal verificar que totes les dades entrades tinguin el format i la longitud correctes.



Crea una classe Client que contingui:

 - les dades per un sol client: nom,cognoms,data_naixement,telefon

 - els mètodes d'entrada: un per a cada atribut

 - els mètodes d'impressió de dades: un per a cada atribut



L'aplicació principal ha de mostrar el següent menú:

1: Introdueix dades a l'agenda.
2: Importa agenda de l'arxiu desitjat.
3: Mostra dades de l'agenda actual.
4: Exporta l'agenda actual a l'arxiu desitjat.
5: Sortir

"""

class client(object):
    def __init__(self):
        self.nom,self.cognoms,self.data_naixement,self.telefon = "","","","",""
        self.dades={}
    def definir_nom(self,nom):  
        self.nom=nom
    def definir_cognoms(self,cognoms):
        self.cognoms=cognoms
    def definir_data_naixement(self,data_naixement):
        self.data_naixement=data_naixement
    def definir_telefon(self,telefon):
        self.telefon=telefon
    def mostra_nom(self):  
        return self.nom
    def mostra_cognoms(self):  
        return self.cognoms
    def mostra_data_naixement(self):  
        return self.data_naixement
    def mostra_telefon(self):  
        return self.telefon
    def afegeix_dades(self):
        self.dades=dict(zip(["nom","cognoms","data_naixement","telefon"],[client.definir_nom(),client.definir_cognoms(),client.definir_data_naixement(),client.definir_telefon()]))
    def __str__(self) -> str:
        return " ,".join(['{0} : {1}'.format(key,self.dades[key]) for key in self.dades])

def inputValors():
    n = input("Nom:")
    c = input("Cognoms:")
    d = input("data_naixement:")
    t = input("teléfon:")
    return n,c,d,t

def ComprovaPrincipi():
	try:
		with open ("Agenda.txt","r") as f:
			pass
	except FileNotFoundError:
		with open ("Agenda.txt","w") as f:
			pass

def ProgramaPrincipal(User_input):
	if User_input==5:
		return True
	elif User_input==1:
		valors=inputValors()
	elif User_input==2:
		pass
	elif User_input==3:
		pass
	elif User_input==4:
		pass
	else:
		print("Opció no existent")
		return False
if __name__=="__main__":

    acabat=False
    while acabat is not True:
        try:
            ComprovaPrincipi()
            print("==================================================\n"+"\n░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░\n"+"██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗\n"+"██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║\n"+"██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║\n"+"╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝\n"+"==================================================\n",
                "1: Introdueix dades a l'agenda.\n",
                "2: Importa agenda de l'arxiu desitjat.\n",
                "3: Mostra dades de l'agenda actual.\n",
                "4: Exporta l'agenda actual a l'arxiu desitjat.\n",
                "5: Sortir\n")
            User_input=int(input("Opció a elegir: "))
            acabat=ProgramaPrincipal(User_input)
        except ValueError:
            print("Ha de ser un número")

        except KeyboardInterrupt:
            print("Adeu!")
            acabat=True
        except:
            print("Error desconegut")