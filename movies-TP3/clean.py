from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mydb = client["movies_artists"]
client.drop_database(mydb)
