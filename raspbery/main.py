from pymongo import MongoClient
from datetime import datetime
import cv2
import os
client = MongoClient("mongodb://henriquegf12:jgs3er4b@192.168.15.38:27017")


if __name__ == "__main__":
    db = client.SmartCam
    idConfig = 0

    systemON = db.config.find({"id": idConfig})[0]['sistemaLigado']
    pathClassificador = db.config.find({"id": idConfig})[0]['pathClassificador']
    pathHaarcascadeFrontalFace = db.config.find({"id": idConfig})[0]['pathHaarcascadeFrontalFace']
    enderecoCamera = db.config.find({"id": idConfig})[0]['enderecoCamera']

    if(systemON):
        arquivoClassificador = os.path.exists(pathClassificador)
        arquivoHaarcascadeFrontalFace = os.path.exists(pathHaarcascadeFrontalFace)

        if(arquivoClassificador and arquivoHaarcascadeFrontalFace):
            classificadorFaces = cv2.CascadeClassifier(pathHaarcascadeFrontalFace)
            identificadorFaces = cv2.face.EigenFaceRecognizer_create()
            identificadorFaces.read(pathClassificador)
        else:
            doc =  {"tipo": "ERRO",
                    "desc": "Arquivos de configuração não encontrados(Identificador Faces = " + str(arquivoHaarcascadeFrontalFace) + " Reconhecimento Faces = " + str(arquivoClassificador),
                    "date": datetime.now()
                    }
            log = db.log_app_rapsberry
            log.insert_one(doc)
            systemON = False
        
        camera = cv2.VideoCapture(enderecoCamera)
        success, frame = camera.read()

        if not success:
            doc =  {"tipo": "ERRO",
                    "desc": "Camera não Encontrada",
                    "date": datetime.now()
                    }
            log = db.log_app_rapsberry
            log.insert_one(doc)
            systemON = False


    while(systemON):
        print("eu ")