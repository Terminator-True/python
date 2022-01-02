

tasca=False
while tasca!=True:
    
    user_input=int(input("Quin exercici vols? (0 per sortir) "))
    
    if user_input== 0:
        tasca=True
    
    if user_input==1:
        """
        Demana un nombre per teclat, comprova que sigui més gran que 1000, i no avancis fins que així sigui i després
        crea un diccionari on  les claus siguin des del número 1 fins al número indicat, i que sigui múltiple de 10 , i
        els valors siguin la meitat de les claus. Fes dues versions, amb bucle for i amb dictionary comprehension 

        """
        num=0
        while num<=1000:
            num=int(input("Posa un número mes gran de 1000: "))
            dict_ex1={i:i/2 for i in range(1,int(num),1) if i%10==0}
            dict_ex1_for={}
            
            for i in range (1,num):
                if i%10==0:
                    dict_ex1_for[i]=i/2
                    
        print(dict_ex1,"\n",dict_ex1_for)
    if user_input==2:
        """
        Demana una cadena per teclat  i genera  un diccionari amb la quantitat aparicions de cada caràcter en la cadena.
        """
        cadena=input("Introdueix una cadena: ")
        claus=set(cadena)
        num=0
        dict_ex2={el:num for el in cadena if el in claus }
                            