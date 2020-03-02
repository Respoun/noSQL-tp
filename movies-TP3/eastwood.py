# coding: utf-8
from pymongo import MongoClient
from pprint import pprint
import json
import pymongo

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["movies_artists"]
myColMovies = mydb["movies"]
myColArtists = mydb["artists"]
eastwood = myColArtists.find_one({"first_name": "Clint", "last_name": "Eastwood"})

try:
    qry={"director._id": eastwood['_id']}
    proj={"title":1, "summary":1, "year":1}
    mydoc = myColMovies.find(qry,proj).sort("title",pymongo.ASCENDING).sort("year", pymongo.ASCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
