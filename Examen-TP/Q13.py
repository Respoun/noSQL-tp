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

try:
    qry = {"$and": [
    {"Seances": {"$elemMatch": {"Libelle": {"$eq" :"Volley ball"}}}},
    {"Seances": {"$elemMatch": {"Libelle": {"$eq" :"Basket ball"}}}}
    ]}
    proj = {"NomGymnase":1, "Ville":1}
    mydoc = gym.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
