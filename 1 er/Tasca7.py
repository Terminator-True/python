practica_acabada=False
user_input=0
aux=()
i=0
list2=[]
while practica_acabada!=True:
    i=0
    
    user_input=int(input("Quin exercici vols execurtar?(0 per sortir) "))
    if user_input== 0:
        practica_acabada=True
    elif user_input== 1:
        #Crea una tupla nova que sigui la tupla girada (al revés)
        aTuple = (10, 20, 30, 40, 50)
        bTuple = tuple([aTuple[i] for i in range(4,-1,-1)])
        print(bTuple)
    elif user_input== 2:
        #Fes una tupla d’un sol element anomenada unSol i amb contingut 50
        unSol=(50)
        
    elif user_input== 3:
        #Fes un swap de les següents tuples 2 versions, amb variable auxiliar i directament
        tuple1 = (99, 88)
        tuple2 = (11, 22)
        
        print(tuple1,tuple2)
        
        aux = tuple1
        tuple1 = tuple2
        tuple2 = aux
        
        print(tuple1,tuple2)
        
    elif user_input==4:
        tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
        llista=[]
        resultat=[]
        
        for i in range(len(tuple1)):
            valor=tuple1[i][1]
            llista.append(valor)

        A=llista
        i=1
        while i < len(A):
            x=A[i] 
            j=i-1
            while j >= 0 and A[j] > x: 
                A[j+1]=A[j]
                j=j-1
            A[j+1]=x 
            i+=1
        j=0
        for i in range(len(A)):
            for j in range(len(tuple1)):
                
                valor1=A[i]
                if valor1 in tuple1[j]:
                    resultat.append(tuple1[j])
        print(resultat)

        
    elif user_input==5:
        #Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?
        tuple1 = (50, 10, 60, 70, 50)
        num=tuple1.count(50)
        percent=2*100/5
        print("Hi han",num,"50s",", ocupen un ",percent,"%","del total")
    elif user_input==6:
        #Comprova si tots els ítems de la tupla tenen el mateix valor
        tuple1 = (45, 45, 45, 45)
        for el in tuple1:
            if max(tuple1)==el:
                print("El número,",el,"es igual al máxim")
                i=i+1
                if i==3:
                    print("Tots els numeros tenen el mateix valor")
    elif user_input==7:
        #Com es crea una tupla buida? Com es converteix una tupla en una llista?

        tuplaBuida=()
        list(tuplaBuida)
    elif user_input==8:
        #Tenint una llista de números, escriviu un codi Python per crear una llista de tuples que tinguin el primer element
        #com a número i el segon element com a cub del número.
        list1 = [1, 2, 3, 4, 5]
        for el in list1:
            afegit=el,el**3
            list2.append(tuple(afegit))
        print(list2)

    elif user_input==9:
        #Fes una llista de tuples de totes les combinacions  possibles de 2 tuples d'arguments.
        t1 = (7, 2)
        t2 = (7, 8)
        llista=[]
    
        for i in range(len(t1)):
            for j in range(len(t2)):
                r=t1[j],t2[i]
                r1=t2[i],t1[j]
                llista.append(r)
                llista.append(r1)
        print(llista)

    elif user_input==10:
        #Escriviu un codi en Python per trobar els elements repetits d’una llista i construeix una
        #llista de tuples on surti en primer terme l’element i en segon terme quantes vegades apareix.
        llista = [1,2,3,1,2,1,1]
        
        for i in range (len(llista)):
            cops=0
            for el in llista:
                if llista[i]==el:
                    cops+=1
            afegit=llista[i],cops
            if afegit not in list2:
                list2.append(tuple(afegit))
        
        print(list2)
    elif user_input==11:
        #Troba en quina posició es troba l’element 20:
        aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
        
        for el in aTuple:
            i+=1
            if "20" in str(el):
                print("El número 20 está a la posició",i,"de la tupla")
                for j in range(len(el)):
                    if el[j]==20:
                        print("Y a la posició ",j,"dins de un/a", type(el))


        
            
