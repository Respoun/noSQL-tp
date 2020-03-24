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
    qry = {"Sexe":"F"}
    proj = {"Nom":1, "Prenom":1, "Age":1}
    mydoc = sportifs.find(qry, proj)
    pprint(mydoc.count())
except Exception as e:
    print("mongo: " + str(e))
