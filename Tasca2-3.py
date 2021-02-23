"""
Fes un algorisme que comprovi la validesa d’un password. Demanarem el password per teclat i hem de comprovar que:

Comenci per la lletra ‘A’
Almenys tingui una xifra (del 0 al 9)
Tingui una llargada mínima de 6 caràcters
Tingui una llarga màxima de 16 caràcters
Contingui 1 dels següents caràcters especials ( ) / ! $ % & 

L’usuari haurà de continuar introduint strings fins que n’introdueixi un de vàlid.

"""

nums="0123456789"
caracters="()/!$%&"
Correctesa=False
correcte=0
x=0


while Correctesa==False:
    
    password=input("Posa el teu password: ")
    
    if password[0]=='A' or password[0]=='a':
        correcte=correcte+1
    else:
        print("Falta la lletra A al principi")
        
    for i in password:
        
        for j in nums:
            
            if i==j:
                correcte=correcte+1
                x=x+1
        for k in caracters:
            
            if i==k:
                correcte=correcte+1
                x=x+1
                
                
    correcte=correcte-(x-2)
    
    
   
    lon=len(password)
            
    if lon>=6:
        correcte=correcte+1
    else:
        print("El teu password es molt curt")
        
    if lon<=16:
        correcte=correcte+1
    else:
        print("El teu password es molt llarg")
        
    if correcte==5:
        Correctesa=True
        print("El teu password es correcte!!")
        
            