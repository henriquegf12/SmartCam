from pymongo import MongoClient
from datetime import datetime
class BancoDados:

    def __init__(self,usuario,senha,ip,porta):
        ConectionString = "mongodb://" + usuario + ":" + senha + "@" + ip + ":" + porta
        self.client = MongoClient(ConectionString)
        self.db = self.client.SmartCam

    #Funções de Escrita 
    def escreveLogDB(self,tipo,desc):
        doc =  {"tipo": tipo,
                "desc": desc,
                "date": datetime.now()
                }
        log = self.db.log_app_raspberry
        log.insert_one(doc)

    #Funções de Consulta
    def buscaConfigbyId(self, idConfig):
        config = self.db.config.find({"id": idConfig})[0]
        return config