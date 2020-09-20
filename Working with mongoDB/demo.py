from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.examples
print (db.arachnid.find_one())