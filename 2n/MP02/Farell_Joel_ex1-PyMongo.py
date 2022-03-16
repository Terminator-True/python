from pymongo import MongoClient
#Obrim conexió amb el mongo db
with MongoClient('localhost',27017,username='Joel_r',password='Admin@123') as client:

    #Llistat d'objectes de la práctica anterior
    objectes = [{"estudiant":"lluis","nota":5,"tipus":"examen"},
    {"estudiant":"Joan","nota":5,"tipus":"exercici"},
    {"estudiant":"Pep","nota":2,"tipus":"test"},
    {"estudiant":"Joaquim","nota":7,"tipus":"examen"},
    {"estudiant":"Alex","nota":9,"tipus":"treball"},
    {"estudiant":"María","nota":10,"tipus":"test"},
    {"estudiant":"Joan","nota":1,"tipus":"test"},{
    "estudiant":"Armand","nota":0,"tipus":"exercici"},
    {"estudiant":"Jordi","nota":6,"tipus":"treball"},
    {"estudiant":"Francesc","nota":10,"tipus":"test"}]
    #Creació de la base de dades, si ja existeix asigna aquesta a la variable mydb
    mydb = client.JoelFarell
    #Creació de la col·lecció, si ja existeix asigna aquesta a la variable mycol
    mycol = mydb.estudiants
    #Si la col·lecció está buida inserta el llistat d'objectes
    if mycol.find_one()== None:
        mycol.insert_many(objectes)

    for el in mycol.find():
        print(el)
    #Modifiquem tots els que tenen un 5 de nota a un 10
    mycol.update_many({"nota":10},{"$set": {"nota":5}})
    print("")
    for el in mycol.find({"nota":5}):
        print(el)

    mycol.delete_one({"estudiant":"Francesc"})

    client.close()
