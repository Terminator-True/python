"""
Programa l’algorisme dEuclides (les dues versions). Prova’l amb 1071 i 462

"""

#Versió residu
a=int(input("Escriu el divident: "))
b=int(input("Escriu el divisor: "))
a1=a
b1=b

while b !=0:
    t=b
    b=a%b
    a=t
    
print("El mcd de ",a1,"i",b1,"és",a)


#Versió resta
a=int(input("Escriu el divident: "))
b=int(input("Escriu el divisor: "))
a1=a
b1=b
while b !=0:
    if a > b:
        a=a-b
    else:
        b=b-a
print("El mcd de ",a1,"i",b1,"és",a)


