from pymongo import MongoClient
from pprint import pprint
import json
import pymongo

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["movies_artists"]
myColMovies = mydb["movies"]
myColArtists = mydb["artists"]

try:
    qry={}
    proj={"title":1}
    mydoc = myColMovies.find(qry, proj).skip(9).limit(13).sort("title", pymongo.ASCENDING)
    for data in mydoc:
      pprint(data)
      print("\n")
except Exception as e:
    print("mongo: " + str(e))

try:
    mydoc = myColMovies.find().skip(9).limit(13).sort("title", pymongo.DESCENDING)
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
