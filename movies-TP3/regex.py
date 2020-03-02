# coding: utf-8
from pymongo import MongoClient
from pprint import pprint
import json
import pymongo
import re

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["movies_artists"]
myColMovies = mydb["movies"]
myColArtists = mydb["artists"]
regex = re.compile("^Re", re.IGNORECASE)
regex2 = re.compile("la$", re.IGNORECASE)
regex3 = re.compile("147$", re.IGNORECASE)

try:
    qry={"title": regex}
    proj={"title":1, "summary":1, "year":1}
    mydoc = myColMovies.find(qry,proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

try:
    qry={"title": regex2}
    proj={"title":1, "summary":1, "year":1}
    mydoc = myColMovies.find(qry,proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))


try:
    qry={"actors._id": regex3}
    proj={"title":1, "actors":1}
    mydoc = myColMovies.find(qry,proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
