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
    qry ={"$and":[
            {"Age": {"$in": [20,30]}},
            {"Sexe": "M"}
        ]}
    proj = {"Nom":1, "Prenom":1, "_id":0}
    mydoc = sportifs.find(qry, proj).sort("Nom", pymongo.ASCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
