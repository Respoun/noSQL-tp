from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient('localhost', 27017)

#Set db/collections
mydb = client["Blog"]
myColUsers = mydb["Users"]
myColArticle = mydb["Article"]

date = datetime.now()

#json data
myDictUsers = [{
		"username": "Jose",
		"password": "toto",
		"author": 1
	},
	{
		"username": "Jean-marc",
		"password": "toto",
		"author": 1
	},
	{
		"username": "Josianne",
		"password": "toto",
		"author": 0
	}
]



myDictData = [{
	"title": "post1",
	"author": "Jean-marc",
	"date": date,
	"tags": ["chats", "chien"],
	"post": "ceci est un exemple de post",
	"commentaires": [{"user": "Josianne",
                     "commentaire": "ceci est un commentaire"
    }]
}, {
	"title": "post2",
	"author": "Jean-marc",
	"date": date,
	"tags": ["voiture", "moto"],
	"post": "ceci est un exemple de post",
	"commentaires": [{"user": "Josianne",
                     "commentaire": "ceci est un commentaire"
    }]
}, {
	"title": "post3",
	"author": "Jose",
	"date": date,
	"tags": ["voiture", "chien"],
	"post": "ceci est un exemple de post",
	"commentaires": [{"user": "Josianne",
                     "commentaire": "ceci est un commentaire",
    }]
}, {
	"title": "post4",
	"author": "Jose",
	"date": date,
	"tags": ["chats", "moto"],
	"post": "ceci est un exemple de post",
	"commentaires": [{"user": "Josianne",
                     "commentaire": "ceci est un commentaire"
    },{
                     "user": "jose",
                     "commentaire": "ceci est un deuxieme commentaire"

    }]
}]

#Insert data
try:
    a = myColUsers.insert_many(myDictUsers)
    c = myColArticle.insert_many(myDictData)
except Exception as e:
    print("mongo: " + str(e))
    pass

#Get data
try:
    mydoc = myColArticle.find({"author": "Jose"})
    for data in mydoc:
      pprint(data)
except Exception as e:
    print("mongo: " + str(e))
