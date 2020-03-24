# coding: utf-8
from pymongo import MongoClient
from pprint import pprint
import json
import pymongo

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["gym"]
gym = mydb["Gymnases"]
sportifs = mydb["Sportifs"]
collection = mydb.collection_names()

#Afficher toutes les collections
for x in collection:
    pprint(x)

#Compter nombre de documents par collection
countGym = gym.count()
countSportifs = sportifs.count()

print("Gym: " + str(countGym))
print("Sportifs: " + str(countSportifs))

try:
    mydoc = gym.find()
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

try:
    mydoc = sportifs.find()
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
