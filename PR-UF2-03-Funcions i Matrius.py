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
while not acabat:

    imprimir="    Exercicis       \n"+"==================\n"+"1. \n"+"2. \n"+"3. \n"+"4.\n"+"5. \n"+"6.\n"+"7. \n"+"8. \n"+"9. \n"+"10. \n"
    print(imprimir)
    User_input=int(input("Quin exercici vols?"))

    if User_input==1:
        num1=int(input("Posa un número: "))
        num2=int(input("Posa un altre número"))

        print("===========================")
        for el in matriu2d(num1,num2):
            print(" ".join(str(el2) for el2 in el))