from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["movies_artists"]
myColMovies = mydb["movies"]
myColArtists = mydb["artists"]

with open('json/movie_collection.json') as f:
    file_data_movie = json.load(f)

with open('json/artist_collection.json') as f:
    file_data_artist = json.load(f)

try:
    myColMovies.insert(file_data_movie)
    myColArtists.insert(file_data_artist)
except Exception as e:
    print("mongo: " + str(e))
    pass

try:
    mydoc = myColMovies.find()
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

try:
    mydoc = myColArtists.find()
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
