"""
Fes un altre programa en python amb un menú per fer la crida a les següents funcions:

Nom funció:  factorial. Funcionalitat: Calcula el factorial d'un número (un enter no negatiu). La funció accepta el nombre com a paràmetre i
retorna el factorial, o bé un error (-1), el missatge d’error s’imprimirà després de la crida.

Nom funció:  comptaMajusMinus. Funcionalitat: accepta una cadena com a paràmetre  i retorna el nombre de lletres majúscules i minúscules.
Cadena de mostra: ‘Una Cadena De Prova' Sortida esperada: (4,12). El missatge es mostra després de la crida.

Nom funció:  llistaUnitaria. Funcionalitat: Donada una  llista que li passem com paràmetre, retorna una nova llista amb elements únics de
la primera llista. Llista de mostres: [1,2,3,3,3,3,4,5] Llista unitària: [1, 2, 3, 4, 5]. No es pot utilitzar la comanda set.

Nom funció:  primer. Funcionalitat: Escriu una funció Python que pren un nombre com a paràmetre menor que 10000 i comproveu si el
número és primer o no, o bé error. (podeu utilitzar l’algoritme del sedàs d’Eratòstanes)

Nom funció parells: Funcionalitat: Retorna els números parells d'una llista determinada passada com paràmetre.
Llista de mostres: [1, 2, 3, 4, 5, 6, 7, 8, 9] Resultat esperat: [2, 4, 6, 8] 

Nom funció perfecte: Funcionalitat: Escriviu una funció Python per comprovar si un número és perfecte o no.
Segons Wikipedia: En la teoria de nombres, un nombre perfecte és un enter positiu que és igual a la suma dels seus divisors positius correctes, és a dir, la suma dels seus divisors positius excloent el nombre en si (també conegut com la seva suma alíquota). De forma equivalent, un nombre perfecte és un nombre que és la meitat de la suma de tots els seus divisors positius (incloent-hi). Exemple: el primer nombre perfecte és 6, perquè 1, 2 i 3 són els seus divisors positius correctes, i 1 + 2 + 3 = 6. Igualment, el número 6 és igual a la meitat de la suma de tots els seus divisors positius: (1 + 2 + 3 + 6) / 2 = 6. El següent número perfecte és 28 = 1 + 2 + 4 + 7 + 14. 

Nom funció palíndrom: Funcionalitat: verifica si una cadena passada com paràmetre és palíndrom o no.

"""
acabat=False
num=0
nums=[1,2,3,4,5,6,7,8,9]
pr=[2,3,5,7]

def factorial(num):
    f=1
    if num<0:
        print("Error: el número no pot ser inferior a 0")
    else:
        for i in range(1,num+1):

            f*=i
    return f
def ComptaMajusMinus(cadena):
    Majus=0
    Minus=0
    for el in cadena:
        if el == " ":
            continue
        elif el == el.upper():
            Majus+=1
        elif el == el.lower():
            Minus+=1
    return "Majúscules:",Majus,"Minúscules:",Minus
def llistaUnitaria(nums):
    nums2=[]
    for i in range (len(nums)):
        if nums[i]not in nums2:
            nums2.append(nums[i])
    return nums2
def primer(nums):
    llista_nums=[]
    for el in range(1,1001):
        llista_nums.append(el)
        
    i=0
    ll=len(llista_nums)
    esprimer=1
    
    while(i<=ll):
        aux=2
        esprimer=1
        while(aux<=i/2 and esprimer!=0):
            esprimer=i%aux
            if esprimer==0:
                llista_nums.remove(i)
            aux+=1
        i+=1
    if num in llista_nums:
        return True
    else:
        return False
def parells(nums):
    
    for el in nums:
        if el%2==0:
            continue
        else:
            nums.remove(el)
    return nums
def perfecte(num):
    sumat=0
    for i in range(1,num):
        if (num%i==0):
            sumat+=i
    if num==sumat:
        return True
    else:
        return False
def palindrom(cadena):
    reves=''.join(reversed(cadena))
    if reves==cadena:
        return True
    else:
        return False
    
while not acabat:
        
    imprimir="    Funcións      \n"+"==================\n"+"1. Factorial \n"+"2. ComptaMajusMinus \n"+"3. LlistaUnitaria \n"+"4. Primer \n"+"5. Parells \n"+"6. Perfecte \n"+"7. Palindrom \n"+"8. sortir \n"
    print(imprimir)
    User_input=int(input("Opció: "))
    if User_input==1:
        num=int(input("Posa un número: "))
        print("El factorial de: ",num," és ",factorial(num))
    elif User_input==2:
        cadena=input("Posa una cadena: ")
        print("La cadena'",cadena,"'conté les següents majúscules i minúscules respectivament: ",ComptaMajusMinus(cadena))
    elif User_input==3:
        print(llistaUnitaria(nums))
    elif User_input==4:
        num=int(input("Posa un número: "))
        print(primer(num))
    elif User_input==5:
        print(parells(nums))
    elif User_input==6:
        num=int(input("Posa un número: "))
        print(perfecte(num))
        if perfecte(num):
            print("Si es perfecte")
        else:
            print("No es perfecte")
            
    elif User_input==7:
        cadena=input("Posa una cadena: ")
        if palindrom(cadena):
            print(palindrom(cadena)," Si es un palindrom")
        else:
            print("No es palindrom")
    elif User_input==8:
        acabat=True