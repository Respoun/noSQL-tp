from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["movies_artists"]
myColMovies = mydb["movies"]
myColArtists = mydb["artists"]

try:
    mydoc = myColMovies.find().skip(9).limit(13)
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
