acabat=False

while acabat is not True:
    try:
        User_input=int(input("Exercici a executar: "))
    except ValueError:
        print("Ha de ser un número")
    else:
        if  User_input==0:
            acabat=True
        elif User_input==1:
                pass