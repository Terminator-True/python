"""
T’encarreguen programar una bàscula d’una fruiteria. L’objectiu serà fer el tiquet de de cada venda.
Declara un diccionari.  El diccionari tindrà com a clau  el nom de les fruites, i com a valor el preu per kg
de la fruita indicada (fes un diccionari que tingui 5 tipus de fruites diferents). Un cop creat el diccionari
demana per cada fruita el pes, i acumula en una variable import. Has d’imprimir en un format net i polit un tiquet
similar a l’exemple
"""

Fruites_dict={"Pomes":1.0,"Taronges":2.0,"Maduixes":1.2,"Mànec":4.0,"Peres":1.95}


fruites=False
total=0
tiquet="\n Fruiteria\n ===================\n"
for fruita in Fruites_dict:
    
    pes=float(input("Introdueix el pes de la fruita en kg: "+ fruita+"\t"))
    preu=pes*Fruites_dict[fruita]
    tiquet+="\n"+fruita+":"+str(pes)+"Kg \t"+str(preu)+"€"
    total+=preu
    
print(tiquet,"\n ===================\n")

print("Import total ",total,"€")
