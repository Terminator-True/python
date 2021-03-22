from tkinter import *
root = Tk()

def Take_input(): 
    INPUT = inputtxt.get("1.0", "end-1c") 
    print(INPUT) 
    if(INPUT == "120"): 
        Output.insert(END, 'Correct') 
    else: 
        Output.insert(END, "Wrong answer") 

l = Label(text = "What is 24 * 5 ? ") 
inputtxt = Text(root, height = 10, 
                width = 25, 
                bg = "light yellow") 

Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan") 

Display = Button(root, height = 2, 
                 width = 20,
                 text ="Show", 
                 command = lambda:Take_input())
"""

while acabat is not True:

    User_input=int(input("Elegir(1-Encript 2-Desencript 3-Exit): "))

    if User_input==1:
        Nombre=input("Nombre: ")
        print(encriptar(Nombre))
    if User_input==2:
        Nombre=input("Nombre: ")
        print(desencriptar(Nombre))
    if User_input==3:
        acabat=True
"""