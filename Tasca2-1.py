"""
Fes un programa que vagi demanant números per teclat fins que
introduïm un número negatiu i mostri per pantalla, per cada número entrat,
si és parell o és senar.
"""
num_negatiu=False

while num_negatiu==False:
    num=int(input("Posa un número: "))
    
    if num<0:
        num_negatiu=True   

    if num%2==0:

        print("El número ",num,"Es parell")

    else:

        print("El número ",num,"Es senar")

   