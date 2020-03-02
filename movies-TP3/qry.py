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

#Afficher les infos du film dont l'id est 2 ? Se limiter aux infos relatives au titre, au genre et au summary ?
try:
    qry={"_id": "movie:2"}
    proj={"title":1, "summary":1, "genre":1}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))


# Combien de films ont été produit en en 1979 et les afficher en se limitant aux infos relatives au titre, à l'année
#et à la liste des acteurs suivant un ordre alphabétique décroissant sur le titre.
try:
    qry={"year": 1979}
    proj={"title":1, "year":1, "actors":1}
    mydoc = myColMovies.find(qry, proj).sort("title", pymongo.ASCENDING)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

#Q : Afficher les infos sur le film dont le genre est "Science-fiction" et produit en 1979 sans préciser l'_id et le summary ?
try:
    qry={"genre": "Science-fiction", "year": 1979}
    proj={"_id":0, "summary":0}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))


#Q : Combien de films produits par le director dont l'id est 4 et les afficher de plus récent au moins récent (sans le résumé ni le country ni le genre) ?
try:
    qry={"director": {"_id": "artist:4"}}
    proj={"country":0, "summary":0, "genre":0}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))

#Q : Combien de films produits par le director qui porte l'id 4 et dont l'un des acteurs a joué le rôle de Maximus et les afficher sans le résumé ni le country ni le genre ?
try:
    qry={"director": {"_id": "artist:4"}, "actors.role": "Maximus"}
    proj={"country":0, "summary":0, "genre":0}
    mydoc = myColMovies.find(qry, proj)
    for data in mydoc:
      print("\nResultat:\n")
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
