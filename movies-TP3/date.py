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
start = 2000
end = 2005

# Q : Ts les films produits après 2000 et avant 2005 ?

try:
    qry={'year': {'$lt': end, '$gte': start}}
    proj={"title":1, "year":1}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))


#Q : Lister les films parus en 1997 ou avec l'acteur id = 147 ?
try:
    qry={'$or' : [{"year": 1997}, {"actors._id": "artist:147"}]}
    proj={"title":1}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
