practica_acabada=False
vocals="AEIOUaeiou"
user_input=0
while practica_acabada!=True:
    
    user_input=int(input("Quin exercici vols execurtar?(0 per sortir) "))
    
    if user_input== 0:
        practica_acabada=True
        
    elif user_input== 1:
        #Creeu una llista idèntica a llistaExemple mitjançant la comprensió de la llista.
        llista1=[i for i in range(1,11)]
        print(llista1)
        
    elif user_input== 2:
        #Creeu una llista a partir dels elements d'un interval de 1200 a 1980 ambdós inclosos,
        #amb passos de 130, mitjançant la comprensió de la llista.
        llista2=[i for i in range(1200,1980,130)]
        print(llista2)
        
    elif user_input== 3:
        #Utilitzeu la comprensió de la llista per construir una llista nova a partir de l’anterior, però sumeu 6 a cada element.
        llista3=[i+6 for i in range(1200,1980,130)]
        print(llista3)
        
    elif user_input== 4:
        #Mitjançant la comprensió de la llista, construïu una llista que sigui els quadrats de cada element de la llista.
        llista4=[i**2 for i in range(1,11)]
        print(llista4)
        
    elif user_input== 5:
        #Mitjançant la comprensió de la llista, construïu una llista a partir dels quadrats de cada element de la llista,
        #si el quadrat és superior a 50.

        llista5=[i**2 for i in range(1,11) if i**2>50]
        print(llista5)
        
    elif user_input== 6:
        #Fes una llista amb tots els números de l’1 al 1000 que són divisibles per 7.
        llista6=[i for i in range(1,1001) if i%7==0]
        print(llista6)
    elif user_input== 7:
        #Fes una llista amb tots els números de l’1 al 1000 que tinguin un 3.
        llista7=[i for i in range(1,1001) if "3" in str(i)]
        print(llista7)
        
    elif user_input== 8:
        #Fent servir list comprehensions compteu el nombre d'espais d'una cadena
        nString = input("Escriu una frase: ")
        llarg=len(nString)
        llista8=[i  for i in range (0,llarg) if nString[i]==" " ]
        print("Hi han",len(llista8)," espais")
        
    elif user_input== 9:
        #Traieu totes les vocals d'una cadena.
        nString = input("Escriu una frase: ")
        llarg=len(nString)
        llista9=[nString[i]  for i in range (0,llarg) if nString[i] not in vocals ]
        print(llista9)
        
    elif user_input== 10:
        #Cerqueu totes les paraules d’una cadena de menys de 4 lletres.
        #Aquest exercici no he sigut capaç de fer-lo funcionar
        nString = input("Escriu una frase: ")
        llarg=len(nString)
        llista10=[nString.split()[i] for i in range(llarg)]
        print(llista10)
        
    