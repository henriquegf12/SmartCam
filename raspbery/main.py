#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
from time import time
from pymongo import MongoClient
from datetime import datetime
import cv2
import os
import time
id= 1
client = MongoClient("mongodb://henriquegf12:jgs3er4b@192.168.15.10:27017")


def escreveLogDB(tipo,desc,db):
    doc =  {"tipo": tipo,
            "desc": desc,
            "date": datetime.now()
            }
    log = db.log_app_raspberry
    log.insert_one(doc)
def criaClassificadoresOpenCV(pathHaarcascadeFrontalFace,pathClassificador):
    try:
        classificadorFaces = cv2.CascadeClassifier(pathHaarcascadeFrontalFace)
        identificadorFaces = cv2.face.EigenFaceRecognizer_create()
        identificadorFaces.read(pathClassificador)
        escreveLogDB("INI","Classificadores do OpenCV setados OK [5//6]",db)
        return True, classificadorFaces,identificadorFaces
    except:
        escreveLogDB("ERROR","Erro na criação dos classificadores OpenCV",db)
        return False, "", ""


def verificaArquivosOPENCV(pathClassificador,pathHaarcascadeFrontalFace):
    if(os.path.exists(pathClassificador) and os.path.exists(pathHaarcascadeFrontalFace)):
        escreveLogDB("INI","Arquivos OpenCV OK [3//6]",db)
        return True
    else:
        escreveLogDB("ERROR","Não encontrado arquivos OpenCV",db)
        return False
def verificaPastaArquivosFotos(pathArquivosFotos):
    if(os.path.exists(pathArquivosFotos)):
        escreveLogDB("INI","Pasta Arquivos Fotos OK [4//6]",db)
        return True
    else:
        escreveLogDB("ERROR","Não encontrado pasta arquivos Fotos",db)
        return False

def verificaConexaoBD():
    try:
        db = client.SmartCam
        escreveLogDB("INI","Inicialização do Sistema [0//6]",db)
        escreveLogDB("INI","Conexão BD OK [1//6]",db)
        return True, db
    except:
        print("An exception occurred") 
        return False, ""

def instanciaCamera(endereCamera):
    try:
        camera = cv2.VideoCapture(endereCamera)
        success, frame = camera.read()
        if(success):
            escreveLogDB("INI","Camera Funcionando [6//6]",db)
            return True, camera
        else:
            escreveLogDB("ERROR","Camera não Funcionando",db)
            escreveLogDB("ERROR","Camera não Funcionando -endereco = "+endereCamera+ " sucess = "+ str(success)+" frame = "+str(frame),db)
            return False, ""
    except:
        escreveLogDB("ERROR","Camera não instanciada",db)
        return False, ""
    


def buscaConfigs(idConfig):
    try:
        config = db.config.find({"id": idConfig})[0]
        if( config['sistemaLigado'] != '' 
        and config['pathClassificador']!= '' 
        and config['pathHaarcascadeFrontalFace']!= '' 
        and config['enderecoCamera']!= ''
        and config['pathArquivosFotos'] != '' ):
            escreveLogDB("INI","Documento Config OK [2//6]",db)
            return True, config
        else:
            escreveLogDB("ERROR","Documento Config com erro",db)
            return False, config
    except:
        escreveLogDB("ERROR","Documento Config não encontrado ",db)
        return False, config

         
if __name__ == "__main__":
    print("Comecou")
    statusConexaoBD, db = verificaConexaoBD()
    print(statusConexaoBD)
    if(statusConexaoBD):
        statusConfig, config = buscaConfigs(id)
        print(statusConfig)
        if(statusConfig):
            systemON = config['sistemaLigado'] 
            pathClassificador = config['pathClassificador']
            pathHaarcascadeFrontalFace = config['pathHaarcascadeFrontalFace']
            enderecoCamera = config['enderecoCamera']
            pathArquivosFotos = config['pathArquivosFotos']
            
            if(verificaArquivosOPENCV(pathClassificador,cv2.data.haarcascades + "haarcascade_frontalface_default.xml") and verificaPastaArquivosFotos(pathArquivosFotos)):
                print("arquivos verificados")
                statusClassificadores,classificadorFaces,identificadorFaces = criaClassificadoresOpenCV(pathClassificador,pathHaarcascadeFrontalFace)
                if(statusClassificadores):
                    statusCamera, camera= instanciaCamera(enderecoCamera)
    while(1):
        henrique = "LINDO"
        if henrique == "LINDO":
            a=0
        else:
            a=10
        
