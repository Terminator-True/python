"""
Donat un nombre natural k, es defineix la seqüència de Collatz com una successió de nombres que comença per k,
i a cada pas aplica la següent lògica:

si el nombre és parell es divideix entre dos,
si el nombre és senar es multiplica per 3 i se li suma 1.

La successió acaba quan arriba al número 1.

Es demana crear un programa en Python que donat un nombre natural major que 1 calculi la seva seqüència de Collatz.
Nota: el programa no avançarà fins que les dades introduïdes siguin correctes.

"""

num=0

while num<1:
    num=int(input("Posa un número major que 1: "))

print("La seqüència de Collatz de ",num,"és: ",end="")

while num!=1:
    if num%2==0:
        num=num//2
        print(num," ",end="")
    else:
        num=(num*3)+1
        print(num," ",end="")