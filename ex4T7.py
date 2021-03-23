"""
Fes un programa en Python anomenat ex4.py que comprovi que el nombre d’arguments és superior a 1,
 que són alfabètics i en aquest cas que els ordeni alfabèticament. Sinó que mostri quin error hi ha.

"""
import sys
ll=sys.argv
ll.pop(0)
if len(sys.argv)>2:
    for el in ll:
        if el.isdigit is True:
            ll.remove(el)            
    ll.sort()
    print(ll)
            
else:
    print("Error, la llista ha de ser major a 1")