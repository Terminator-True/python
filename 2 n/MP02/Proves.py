from pymongo import MongoClient
with MongoClient('localhost', 27017) as client:
    mydb = client.Tasca4_3
    col = mydb.cataleg
    for el in col.find():
        print(el)
