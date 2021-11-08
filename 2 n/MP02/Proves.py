from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
mydb = client.Tasca4_3
print (mydb.collection_names())
