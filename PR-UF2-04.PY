"""
Programa la funció absolut que faci el mateix que la funció incorporada de Python abs() passant-li un nombre (enter o un float).

Programa la funció elevar que faci el mateix que la funció incorporada de Python pow() passant-li 2 enters, 2 floats, 1 enter i 1 float o 1 float i 1 enter.

Programa la funció longitud que faci el mateix que la funció incorporada de Python len() passant-li una cadena, una llista o un iterable.

Programa la funció alreves que faci el mateix que la funció incorporada (mètode) de Python list.reverse() passant-li una llista.

Programa la funció elevar que faci el mateix que la funció incorporada de Python pow() passant-li 3 enters (el darrer enter serveix per calcular el mòdul).

Programa la funció maxim que faci el mateix que la funció incorporada de Python max() passant-li una llista d’enters o una llista de cadenes de caràcters.

Programa la funció suma que faci el mateix que la funció incorporada de Python sum() passant-li un iterable (pot ser una llista o una tupla que és com una llista i 
s’accedeix igual però va entre parèntesis) de nombres. Opcionalment es pot passar un valor a afegir a la suma.

Programa la funció ordenat que faci el mateix que la funció incorporada de Python sorted() passant-li una llista o una tupla. Dels paràmetres opcionals que té la 
funció incorporada, programa el reverse que indica si s’ordena ascent o descent.

Programa la funció rang que faci el mateix que la classe incorporada de Python range() passant-li 1 enter que indica el final del rang. La nostra funció retornarà 
una llista o una tupla amb els valors generats.

Programa la funció rang que faci el mateix que la classe incorporada de Python range() passant-li 2 o 3 enters que indiquen l’inici del rang,i el final del rang i 
el pas. La nostra funció retornarà una llista o una tupla amb els valors generats. Es pot fer modicant l’anterior (ha de continuar funcionant) o fer-ne una versió 
nova.

"""
acabat=False
llista=[1,2,3,4,5,6,7,8,9,0]
llistaD=[3,2,6,2,1,6,4,5,9,8,0]

def absolut(n):
    if n<0:
        n-=n*2
    return n
def elevar(x,y):
    return x**y
def longitud(ll):
    i=0
    for el in ll:
        i+=1
    return i
def alreves(ll):
    ll2=[ll[i] for i in range(longitud(ll)-1,-1,-1)]
    return ll2
def elevar2(x,y,z):
    return ((x**y)%z)

def maxim(ll):
    i=0
    for el in ll:
        if el>ll[i-1]:
            maximo=el
        i+=1
    return maximo
def suma(ll,n):
    sumat=0
    for el in ll:
        sumat+=el
    return sumat+n

def ordenat(ll):
    i=0
    imprimir=[]
    User_input=input("Vols que s'ordeni ascendent o descendent?(A/D)")
    if User_input=="A" or User_input=="D":
        while i < longitud(ll):
            if i == 0 or ll[i] >= ll[i-1]:
                i = i+1
            else:
                temp = ll[i-1]
                ll[i-1] = ll[i]
                ll[i] = temp
                i = i-1
        imprimir=ll.copy()
    if User_input=="D":
        ll2=[ll[i] for i in range((longitud(ll)-1),-1,-1)]
        imprimir=ll2.copy()

    return imprimir

def rang(n):
    ll=[i for i in range(n)]
    return ll

def rang2(x,y,z):
    ll=[i for i in range(x,y,z)]
    return ll
while not acabat:

    imprimir="    Exercicis       \n"+"==================\n"+"1. \n"+"2. \n"+"3. \n"+"4.\n"+"5. \n"+"6.\n"+"7. \n"+"8. \n"+"9. \n"+"10. \n"
    print(imprimir)
    User_input=int(input("Quin exercici vols? "))

    if User_input==1:
        num=int(input("Posa un número: "))
        print(absolut(num))
    if User_input==2:
        num1=int(input("Posa un número: "))
        num2=int(input("Posa un altre número: "))
        print(elevar(num1,num2))
    if User_input==3:
        print(llista)
        print(longitud(llista))
    if User_input==4:
        print(llista)
        print(alreves(llista))
    if User_input==5:
        num1=int(input("Posa un número: "))
        num2=int(input("Posa un altre número: "))
        num3=int(input("Posa un altre número: "))
        print(elevar2(num1,num2,num3))
    if User_input==6:
        print(llista)
        print(maxim(llista))
    if User_input==7:
        num=0
        print(llista)
        Resposta=input("Vols afegir algún valor? (S/N)")
        if Resposta=="S":
            num=int(input("Valor a afegir: "))        
        print(suma(llista,num))
    if User_input==8:
        print(llistaD)
        print(ordenat(llistaD))        
    if User_input==9:
        num=int(input("Posa un número: "))
        print(rang(num))
    if User_input==10:
        num1=int(input("Posa inici: "))
        num2=int(input("Posa final: "))
        num3=int(input("Posa pas: "))
        print(rang2(num1,num2,num3))