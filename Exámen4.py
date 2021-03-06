"""
Encara hi ha places lliures per treballar al creuer i decideixen obrir inscripcions, t'encarreguen fer el formulari d'inscripció: 

Demana per teclat el nom, i no permet avançar fins que el nom no sigui correcte (permet qualsevol string sempre que no hi hagi números i
la primera lletra sigui en majúscules)
Demana per teclat el gènere, i no permet avançar fins que és M (masculí), F (femení) o I (indefinit)
Demana per teclat el grup_sanguini, i no permet avançar fins que el grup sanguini sigui un dels correctes (O+,O-,A+,A-,B+,B-,AB+,AB-)
Demana per teclat l'any de naixement i no deixa avançar fins el tripulant és major d'edat i menor de 65
Demana per teclat el sou i no deixa avançar fins que sigui un nombre positiu
Finalment afegeix el tripulant a la llista de tripulants, comprova-ho amb un print del darrer element de la llista tripulants


"""
tripulants = [{'nom': 'Laura Eaton', 'grup_sanguini': 'AB-', 'genere': 'F', 'any_naix': 1990, 'sou': 2230}, {'nom': 'Kimberly Gonzalez', 'grup_sanguini': 'A+', 'genere': 'F', 'any_naix': 1964, 'sou': 2400}, {'nom': 'Aaron Palmer', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1979, 'sou': 1600}, {'nom': 'Christopher Robles', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1960, 'sou': 1700}, {'nom': 'Christopher Nguyen', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1959, 'sou': 2070}, {'nom': 'Karina Nelson', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1963, 'sou': 1990}, {'nom': 'Kelsey Moreno', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1969, 'sou': 1620}, {'nom': 'Dawn Peterson', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1966, 'sou': 990}, {'nom': 'Arthur Daniel', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1980, 'sou': 2300}, {'nom': 'Jeffrey Garcia', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1959, 'sou': 1340}, {'nom': 'John Young', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1977, 'sou': 940}, {'nom': 'Peter Peck', 'grup_sanguini': 'O+', 'genere': 'M', 'any_naix': 1953, 'sou': 1750}, {'nom': 'Amanda Ramirez', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1980, 'sou': 1510}, {'nom': 'Richard Lester', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1985, 'sou': 1340}, {'nom': 'Charles Dillon', 'grup_sanguini': 'O+', 'genere': 'M', 'any_naix': 1999, 'sou': 2130}, {'nom': 'Brandon Shaffer', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1976, 'sou': 2500}, {'nom': 'Sheila Zimmerman', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1972, 'sou': 1850}, {'nom': 'Amanda Ochoa', 'grup_sanguini': 'AB-', 'genere': 'F', 'any_naix': 1982, 'sou': 1810}, {'nom': 'Melanie Lambert', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1980, 'sou': 1110}, {'nom': 'Brent Bauer', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1967, 'sou': 1800}, {'nom': 'Michael Santos', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1958, 'sou': 1710}, {'nom': 'William Lopez', 'grup_sanguini': 'AB-', 'genere': 'M', 'any_naix': 1997, 'sou': 2270}, {'nom': 'Megan Graham', 'grup_sanguini': 'O+', 'genere': 'F', 'any_naix': 1954, 'sou': 2420}, {'nom': 'Rhonda Riley', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1984, 'sou': 1900}, {'nom': 'Kelly Vargas', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1970, 'sou': 2490}, {'nom': 'Susan Gutierrez MD', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1957, 'sou': 830}, {'nom': 'Manuel Ramsey', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1981, 'sou': 2380}, {'nom': 'John Vega', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1981, 'sou': 1870}, {'nom': 'Christopher Williamson', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1987, 'sou': 2200}, {'nom': 'Christopher Foster', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1972, 'sou': 2090}, {'nom': 'Jose Wilson', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1975, 'sou': 1630}, {'nom': 'Christopher Camacho', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1991, 'sou': 1060}, {'nom': 'Carol Newton', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1960, 'sou': 1540}, {'nom': 'Shaun Mcguire', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1959, 'sou': 1690}, {'nom': 'Gabrielle Mccoy', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1973, 'sou': 2380}, {'nom': 'Kyle Hebert', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1971, 'sou': 1440}, {'nom': 'Stephanie Padilla', 'grup_sanguini': 'AB-', 'genere': 'F', 'any_naix': 1952, 'sou': 1330}, {'nom': 'David George', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1966, 'sou': 2090}, {'nom': 'John Mack', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1981, 'sou': 2240}, {'nom': 'Lori Wilson', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1985, 'sou': 2440}, {'nom': 'Sergio Williams', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1968, 'sou': 1110}, {'nom': 'Donald Murphy', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1963, 'sou': 1550}, {'nom': 'Timothy Ramirez', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1995, 'sou': 2390}, {'nom': 'Christina Roach', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1978, 'sou': 2030}, {'nom': 'Brandon Gilmore', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1981, 'sou': 1280}, {'nom': 'William Cobb', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 2001, 'sou': 1540}, {'nom': 'Regina Young', 'grup_sanguini': 'O+', 'genere': 'F', 'any_naix': 1974, 'sou': 1010}, {'nom': 'Raven Hanna', 'grup_sanguini': 'O+', 'genere': 'F', 'any_naix': 1979, 'sou': 1790}, {'nom': 'Alice Bonilla', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 2001, 'sou': 1390}, {'nom': 'Jennifer Sanchez', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1993, 'sou': 1860}, {'nom': 'Samantha Rogers', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1968, 'sou': 1150}, {'nom': 'Adrienne Cook', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1997, 'sou': 2230}, {'nom': 'Brittany Matthews', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1977, 'sou': 1480}, {'nom': 'John Mcgee', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1983, 'sou': 1710}, {'nom': 'Tabitha Davis MD', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1999, 'sou': 1780}, {'nom': 'Brad Combs', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1981, 'sou': 2120}, {'nom': 'Destiny Deleon', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1993, 'sou': 1000}, {'nom': 'Cindy Barrett', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1973, 'sou': 990}, {'nom': 'Theodore Johnson', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1962, 'sou': 1450}, {'nom': 'Anne Cox', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1962, 'sou': 1260}, {'nom': 'James Johnson', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1971, 'sou': 1260}, {'nom': 'John Valencia', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1980, 'sou': 2380}, {'nom': 'Jeffrey Strong', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1976, 'sou': 1590}, {'nom': 'Kathryn Mack', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1985, 'sou': 2420}, {'nom': 'Karen Hayes', 'grup_sanguini': 'AB-', 'genere': 'F', 'any_naix': 1982, 'sou': 2190}, {'nom': 'Joseph Walsh', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1970, 'sou': 1070}, {'nom': 'Wendy Pugh', 'grup_sanguini': 'AB-', 'genere': 'F', 'any_naix': 1996, 'sou': 1660}, {'nom': 'Jenny Ramirez', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1955, 'sou': 1000}, {'nom': 'Melissa Cervantes', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1953, 'sou': 840}, {'nom': 'James Dickson', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1981, 'sou': 1830}, {'nom': 'Kimberly Reeves', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1956, 'sou': 1710}, {'nom': 'Kendra Martin', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1973, 'sou': 1960}, {'nom': 'Kimberly Shields', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1958, 'sou': 1370}, {'nom': 'John Berry', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1973, 'sou': 1240}, {'nom': 'Zachary Fisher', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1961, 'sou': 1270}, {'nom': 'Mitchell Wood', 'grup_sanguini': 'AB-', 'genere': 'M', 'any_naix': 1970, 'sou': 1580}, {'nom': 'Hannah Villa', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1979, 'sou': 2250}, {'nom': 'Roberta Edwards', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 2001, 'sou': 2230}, {'nom': 'Nicole Williams', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1967, 'sou': 2170}, {'nom': 'Derrick Smith', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1987, 'sou': 1640}, {'nom': 'Ronald Brown', 'grup_sanguini': 'A-', 'genere': 'M', 'any_naix': 1998, 'sou': 1660}, {'nom': 'Stephanie Smith', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1992, 'sou': 1320}, {'nom': 'Jennifer White', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1954, 'sou': 1480}, {'nom': 'Paul Smith', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1997, 'sou': 2410}, {'nom': 'Kevin Coffey', 'grup_sanguini': 'O-', 'genere': 'M', 'any_naix': 1965, 'sou': 1990}, {'nom': 'Lacey Butler', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1984, 'sou': 1370}, {'nom': 'Margaret Cook', 'grup_sanguini': 'B+', 'genere': 'F', 'any_naix': 1981, 'sou': 1150}, {'nom': 'Shawna Martin', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1988, 'sou': 920}, {'nom': 'Bradley Massey', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1981, 'sou': 1470}, {'nom': 'Jeremy Diaz', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1991, 'sou': 1850}, {'nom': 'Zachary Cunningham DDS', 'grup_sanguini': 'B+', 'genere': 'M', 'any_naix': 1994, 'sou': 1280}, {'nom': 'Julie Lewis', 'grup_sanguini': 'O-', 'genere': 'F', 'any_naix': 1967, 'sou': 1690}, {'nom': 'Brian Lewis', 'grup_sanguini': 'A+', 'genere': 'M', 'any_naix': 1969, 'sou': 1740}, {'nom': 'Teresa Hancock', 'grup_sanguini': 'A+', 'genere': 'F', 'any_naix': 1999, 'sou': 800}, {'nom': 'Carmen Mccoy', 'grup_sanguini': 'B-', 'genere': 'F', 'any_naix': 1991, 'sou': 2430}, {'nom': 'Gerald Jackson', 'grup_sanguini': 'B-', 'genere': 'M', 'any_naix': 1986, 'sou': 1540}, {'nom': 'Michael Barnett', 'grup_sanguini': 'AB+', 'genere': 'M', 'any_naix': 1957, 'sou': 800}, {'nom': 'Robert Walters', 'grup_sanguini': 'O+', 'genere': 'M', 'any_naix': 1975, 'sou': 2400}, {'nom': 'Kaitlin Keller', 'grup_sanguini': 'AB+', 'genere': 'F', 'any_naix': 1953, 'sou': 1890}, {'nom': 'Amber Coleman', 'grup_sanguini': 'A-', 'genere': 'F', 'any_naix': 1966, 'sou': 1640}]

sang=["O+","O-","A+","A-","B+","B-","AB+","AB-"]
majuscules="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
gens="MFI"
nums="1234567890"
inscrit=False
nom_correcte=False
gen_correcte=False
grup_correcte=False
any_correcte=False
sou_correcte=False
any_actual=2021
while nom_correcte!=True:
    nom=input("Posa el teu nom: ")
    if nom in nums:
        print("No pot tenir números")
    else:
        if nom[0] not in majuscules:
            print("La primera lletra ha d'estar en majúscules")

        else:
            nom_correcte=True
while gen_correcte!=True:
    gen=input("Posa el teu gènere(M (masculí), F (femení) o I (indefinit)): ")
    if gen not in gens:
        print("Ha de ser M (masculí), F (femení) o I (indefinit)")
    else:
        gen_correcte=True
while grup_correcte!=True:       
    grup_sanguini=input("Posa el teu grup sanguini(O+,O-,A+,A-,B+,B-,AB+,AB-): ")
    if grup_sanguini not in sang:
        print("EL grup sanguini ha de ser O+,O-,A+,A-,B+,B-,AB+,AB-")
    else:
        grup_correcte=True
        
while any_correcte!=True:
    any_neixement=int(input("Posa el teu any de neixment: "))
    if any_actual-any_neixement<18 or any_actual-any_neixement>65:
        print("Ha de ser major d'edat i menor de 65 anys")
    else:
        any_correcte=True
while sou_correcte!=True:
    sou=int(input("Posa el sou: "))
    if sou<0:
        print("El sou ha de ser positiu")
    else:
        sou_correcte=True
tripulants.append({'nom':nom,'grup_sanguini':grup_sanguini,'any_naix':any_neixement,'sou':sou})
print(tripulants[(len(tripulants))-1])