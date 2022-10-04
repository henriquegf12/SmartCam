from pymongo import MongoClient
from datetime import datetime
class BancoDados:

    def __init__(self,usuario,senha,ip,porta):
        ConectionString = "mongodb://" + usuario + ":" + senha + "@" + ip + ":" + porta
        self.client = MongoClient(ConectionString)

    def escreveLogDB(tipo,desc,db):
        doc =  {"tipo": tipo,
                "desc": desc,
                "date": datetime.now()
                }
        log = db.log_app_raspberry
        log.insert_one(doc)

