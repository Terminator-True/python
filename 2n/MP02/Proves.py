from pymongo import MongoClient
with MongoClient('localhost',27017,username='Joel_r',password='Admin@123') as client:
    mydb = client.admin
    print(mydb)


