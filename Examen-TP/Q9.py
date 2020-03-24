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
    qry = {"$and" : [{"Ville":{"$in":["VILLETANEUSE", "SARCELLES"]}},{"Surface":{"$gte": 400}}]}
    proj = {"NomGymnase":1, "Ville":1, "Surface":1}
    mydoc = gym.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
