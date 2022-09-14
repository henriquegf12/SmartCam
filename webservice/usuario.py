from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)


class Usuario():      
    def getAllUser():
        db = client.SmartCam
        users = db.User
        usuarios = users.find()
        list_cur = list(usuarios)
        json_data = json.dumps(list_cur)
        return json_data

    def getUserbyID(id):
        db = client.SmartCam
        users = db.User
        usuario = users.find({"id": id})
        return usuario

    def createUser(nome,dataNascimento):
        db = client.SmartCam
        users = db.User

        id = 0
        if users.count_documents == 0 :
            id = 0
        else:
            id = users.find().sort("id",-1)[0]['id'] + 1

        doc =  {"id": id,
                "name": nome,
                "dataNascimento": dataNascimento}

        users.insert_one(doc)
        return True