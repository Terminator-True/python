practica_acabada=False
user_input=0
aux=()
i=0
list2=[]
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
TEXT1 = "Com les maduixes Menja maduixes l’àvia d’abans de Sant Joan; per més frescor, les vol collides d’un infant. Per això la néta més petita, que és Pandara, sabeu, la que s’encanta davant d’una claror i va creixent tranquil·la i en ‘admiració i a voltes, cluca d’ulls, aixeca al cel la cara, ella, que encar no diu paraules ben ardides i que en barreja en una música els sentits, cull ara les maduixes arrupides, tintat de rosa el capciró dels dits. Les prunes d’or Aglaia té una set que eixuga el seny, la parla… Superbament s’aixeca, damnant el seu descans, i enfonsa en la prunera les cobejoses mans i enlaira tot el rostre, com si volgués besar-la. I l’arbre, que amb un lleu serpejament de branques sembla oferir-nos l’or, la mel d’algun pecat, s’estremeix un moment de la ferocitat del gran perfum impúdic i de les dents tan blanques. XVI Els codonys tardorals Però ja saps com elles es tornen malgirbades  per fills i feines, o perquè no n’han tingut, i amb cara tediosa caminen desmarxades i són codonys, diries, el fruit més boterut—. I l’altre amic que deia: —Quan fina tot esclat, nosaltres rondinem, esgarriant les passes, i flagel·lem el dia amb folles amenaces, saturns a la memòria del goig mal escampat. Llavores, el codony, que es féu vell en la branca,  dins el calaix perfuma la nostra roba blanca, i si l’amorosim al caliu de la llar i l’acostem als llavis sorruts, és dolç, encar."
TEXT2 = "Ho havia planificat tot durant 20 anys. S’havia desfet de tot i de tothom. Estava segur que, en aquells moments, ja no el coneixia ningú. No quedava cap fotografia amb el seu veritable físic. I havia tingut tantes identitats diferents que ni ell es recordava de totes. Ara havia decidit començar una nova vida en un lloc on no el coneixia ningú. Era un poble qualsevol que un dia va veure mentre feia un viatge. Havia pensat que seria un bon lloc per començar de zero. El trajecte era la part més difícil. A l’estació va comprar un bitllet de tren nocturn amb destinació a Manchester. No volia que el busquessin enlloc. Baixaria al poble que havia triat abans d’arribar a la ciutat. També s’havia preocupat pel físic: ara duia bigoti i inflava les galtes d’una manera que li canviava la cara. Dret al passadís va esperar la sortida del tren. I va encendre l’última cigarreta, perquè a la nova vida pensava desfer-se d’aquest costum. El tabac li va semblar més bo que altres vegades i va fumar lentament, per fer durar el plaer." 
signes=";.,"
j=0
llista1=[]
llista_accents1=[]
llista_accents2=[]
llista_compartir1=[]
llista_compartir2=[]
while practica_acabada!=True:
    user_input=int(input("Quin exercici vols execurtar?(0 per sortir) "))
    
    if user_input== 0:
        practica_acabada=True
    elif user_input==1:
        #Afegiu una llista d'elements a un conjunt determinat
        sampleSet = {"Yellow", "Orange", "Black"}
        sampleList = ["Blue", "Green", "Red"]
        sampleSet.update(sampleList)
        print(sampleSet)
    elif user_input==2:
        #Retorna un conjunt d’elements repetits

        print(set1 & set2)
    elif user_input==3:
        #Retorna un conjunt nou amb tots els elements dels dos conjunts eliminant els duplicats.
        print(set1 | set2)
    elif user_input==4:
        #Tenint en compte dos conjunts de Python, actualitzeu el
        #primer conjunt amb elements que només existeixen al primer conjunt i no al segon conjunt.
        set3 = {10, 20, 30}
        set4 = {20, 40, 50}

        print(set3 - set4)
    elif user_input==5:
        #Traieu 10, 20, 30 element d'un conjunt següent alhora
        set6={10,20,30}
        print(set1-set6)

    elif user_input==6:
        #Cerqueu si una cadena introduïda per teclat té caràcters únics.
        entrada=input("Posa un string: ")
        
        text=set(entrada)
        
        if len(entrada)!=len(text):
            print(entrada, "te lletres repetides")
        else:
            print(entrada, "no te lletres repetides")
        
    elif user_input==7:
        #Donades les variables TEX1 i TEX2  que trobaràs a https://repl.it/join/ontzbvzb-pilarmote que contenen
        #textos de Josep Carner i Manuel de Pedrolo respectivament, utilitzeu de manera òptima e
        #ls coneixements apresos fins ara per respondre a les següents preguntes:

        #Elimina en ambdues variables els signes de puntuació (,.;) i transforma a minúscules (mètode lower).
        #Quantes paraules té TEXT1? I quantes TEXT2?
        #Pregunta1
        TEXT3=TEXT1.lower()
        TEXT4=TEXT2.lower()
        
        TEXT1=[paraula for paraula in TEXT3.split() if paraula not in signes]
        TEXT2=[paraula for paraula in TEXT4.split()if paraula not in signes]
        
        print(TEXT1)
        print(TEXT2)
        
        print("---------")
        #Pregunta2
        print("text1 conté",len(TEXT1)," paraules, i text2 conté ",len(TEXT2))
        #Intent de pregunta 3
        for el in TEXT1:
            if 'a' in el:
                i=0
                for i in range(len(el)):
                    if el[i]=="a":
                        i+=1
                    elif i==2:
                        if el in TEXT2:
                            llista1.append(el)
                            
        print(llista1)
        
        #pregunta4
        accents="áéíóúàèìòù"
        
        for el in TEXT1:
            for el2 in el:
                if el2 in accents:
                    llista_accents1.append(el)
                    break
        for el in TEXT2:
            for el2 in el:
                if el2 in accents:
                    llista_accents2.append(el)
                    break
        print("Les següents paraules están repetides a les dos llistes:",end=" ")
        for el in llista_accents1:
            if el in llista_accents2:
                print(el," ",end="")
        #pregunta5
        signes2="·’-"
        print()
        print("Les següents paraules tenen apostrof, guió o punt volat i no están a text2: ")
        for el in TEXT1:
            for el2 in el:
                if el2 in signes2:
                    if el not in TEXT2:
                        print(el," ",end="")
        #pregunta 6
                        
        vocals="aeiou"
        i=0
        for el in TEXT1:
            for el2 in el:
                if el2 in vocals:
                    i+=1
                if i==4:
                    llista_compartir1.append(el)
        i=0
        for el in TEXT2:
            i=0
            for el2 in el:
                if el2 in vocals:
                    i+=1
                if i==4:
                    llista_compartir2.append(el)
        
        print()
        print("Paraules que tenen 4 vocals i les llistes no comparteixen: ",set(llista_compartir1) ^ set(llista_compartir2))
        
        
        