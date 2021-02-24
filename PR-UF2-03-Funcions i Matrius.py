"""
Programa la funció matriu2d, que li passes 2 nombres enters n1, n2 i retorna una matriu m de 2 dimensions n1 x n2 plena de nombres aleatoris entre l’1 i el 100.

Programa la funció printMatriu, que imprimeix la matriu que li passes com a paràmetre de manera similar a l’exemple:

Programa la funció llistaMultiples que li passes la matriu m de 2 dimensions com a argument, i un enter e entre l’1 i el 10 i retorna una llista ll d’1 
dimensió formada pels múltiples d’e existents a la matriu.

Programa la funció llistaUnica que li passes la matriu m i retorna una llista única (sense elements repetits) d’1 dimensió.

Programa la funció minMax que retorna el mínim i el màxim de la matriu m que li passes com a paràmetre.

Programa la funció acabaEn que li passes la matriu m com a argument, i un enter e entre l’0 i el 9 i retorna una llista d’1 dimensió formada pels nombres que 
la seva última xifra és e.

Programa la funció quadrat que donat un sencer s entre 10 i 20 retorna una matriu quadrada de 2 dimensions de mida s x s inicialitzada al caràcter que li passes 
com a segon paràmetre.

Programa la funció inicialitza que inicialitza tots els elements de la matriu al caràcter que li passes per argument. (arguments, la matriu q i el caràcter c).

Programa la funció diagonal que posa en les diagonals de la matriu quadrada q, el caràcter c. Es passen com a paràmetres de la funció q i c.


"""
import random
acabat=False

def matriu2d(n1,n2):
    if n1>0 and n2>0:
        m=[]
        for i in range(n1):
            fila=[]
            for j in range(n2):
                fila.append(random.randint(1,100))
            m.append(fila)
    else:
        m=-1
    return m    
def printMatriu():
    for el in matriu2d(num1,num2):
        print( " ".join(str(el2) for el2 in el))

def llistaMultiples(e,m):
    Multiples=[]
    for el in m:
        Multiples+=[el2 for el2 in el if el2%e==0]
    return Multiples

def llistaUnitaria(m):
    ll=[el2 for el in m for el2 in el]
    set(ll)
    return list(ll)
        
def minMax(m):
    ll=[int(el2) for el in m for el2 in el]
    return min(ll),max(ll)
def acabaEn(e,m):
    ll=[el2 for el in m for el2 in el if el2-e==0 or (el2-e)%10==0] #Comproba si a el2 li restem e i dona 0 o es múltiple de 10, significa que el numero 
    return ll                                                       #enmagatzemat en el2 acaba amb el numero enmagatzemat a e
def quadrat(s,c):
    m=[]
    for i in range (s):
        print(s*c)


                                                                    
while not acabat:

    imprimir="    Exercicis       \n"+"==================\n"+"1. \n"+"2. \n"+"3. \n"+"4.\n"+"5. \n"+"6.\n"+"7. \n"+"8. \n"+"9. \n"+"10. \n"
    print(imprimir)
    User_input=int(input("Quin exercici vols? "))

    if User_input==1:
        num1=int(input("Posa un número: "))
        num2=int(input("Posa un altre número: "))
        print(matriu2d(num1,num2))
        m=matriu2d(num1,num2)
    if User_input==2:
        print("===========================")
        printMatriu()
    if User_input==3:
        e=1
        while e<10 and e>0:
            e=input("Posa un número entre 1-10: ")
        
        print(llistaMultiples(e,m))
    if User_input==4:
        print(llistaUnitaria(m))
    if User_input==5:
        print(minMax(m))
    if User_input==6:
        num=int(input("Posa un número entre l'1 i el 9: "))
        print(acabaEn(num,m))
    if User_input==7:
        sencer=int(input("Posa un número entre el 10 i el 20: "))
        caracter=input("Posa un caracter: ")
        quadrat(sencer,caracter)
