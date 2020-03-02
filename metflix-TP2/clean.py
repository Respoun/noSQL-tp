from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mydb = client["Blog"]
client.drop_database(mydb)
