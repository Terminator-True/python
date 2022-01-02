"""
Fes un programa en Python anomenat ex1.py que accepta 1 argument per la línia de comandes i si està format per 
lletres mostra per pantalla quantes vocals té.
"""
import sys
i=0
vocals="A","E","I","O","U","a","e","i","o","u"
User_input=sys.argv
if User_input[1].isdigit is not True:
    for el in User_input[1]:
        if el in vocals:
            i+=1
    print("Té",i,"Vocals")