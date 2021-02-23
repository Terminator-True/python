"""
Escriu un programa que donat un string que cal introduir per teclat, comprovi si:
    
És de mida superior a 10 caràcters
És de mida inferior a 10 caràcters i conté algun dels següents caràcters: * + / -
És de mida 10 caràcters i comença per -
És de mida 10 caràcters i acaba per .

"""

cosa=input("Escriu alguna cosa: ")
caracters="*+/-"
l=len(cosa)
x=j=0

if l>10:
    print("Té més de 10 caràcters")
    
elif l<10:#Si el string te menys de 10 caracters, recorre lletra a lletra mirant si te els caracters esmentats anteriorment
    for i in cosa:
        for j in caracters:
            if i==j:
                x=1
    
    if x==1:
        print("Conté algún els següents carácters",caracters)

else: 
    if cosa[0]=="-":
        print("Comença per -  i es de mida 10")
    elif cosa[l-1]==".":
        print("Acaba en . i es de mida 10")
      
