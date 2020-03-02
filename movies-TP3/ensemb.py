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

# combien de films dans lesquels ont joué au moins un des artistes suivants : 34, 98 et 1 et
# afficher leur titre et la liste des actors ; sens du tri : chronologique et alphabétique croissant ?

try:
    qry={ "$or": [{"actors._id": "artist:34"}, {"actors._id": "artist:98"}, {"actors._id": "artist:1"}]}
    proj={"title":1, "actors":1, "year":1}
    mydoc = myColMovies.find(qry, proj).sort("title",pymongo.ASCENDING).sort("year", pymongo.ASCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))


# Q : Chercher les films dans lesquels ont joué ensemble les actors 23 et 147 ?
try:
    qry={ "$and": [{"actors._id": "artist:23"}, {"actors._id": "artist:147"}]}
    proj={"title":1, "actors":1, "year":1}
    mydoc = myColMovies.find(qry, proj).sort("title",pymongo.ASCENDING).sort("year", pymongo.ASCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

#Q : Combien de films dans lesquels n'ont joué ni l'acteur 34, ni 98, ni 1 et afficher leur titre et la liste des actors ; sens du tri : chronologique décroissant et alphabétique croissant ?

try:
    qry={ "$nor": [{"actors._id": "artist:34"}, {"actors._id": "artist:98"}, {"actors._id": "artist:1"}]}
    proj={"title":1, "actors":1, "year":1}
    mydoc = myColMovies.find(qry, proj).sort("title",pymongo.DESCENDING).sort("year", pymongo.DESCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
