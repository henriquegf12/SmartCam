from BancoDados import BancoDados
import sys
from pymongo import MongoClient
from datetime import datetime
import cv2
import os


#Funções para verificação e inicialização do sistema
#Inicialização do Banco de Dados
def conexaoBancoDados():
    try:
        DBconection = BancoDados("henriquegf12","jgs3er4b","192.168.15.10","27017")
        DBconection.escreveLogDB("INI","Inicialização do Sistema [0//6]")
        DBconection.escreveLogDB("INI","Conexão BD OK [1//6]")
        return True, DBconection
    except:
        return False, ""

#Buscando as configurações do sistema no Banco de Dados
def buscaConfigs(DBconection,idConfig):
    try:
        config = DBconection.buscaConfigbyId(idConfig)
        if( config['sistemaLigado'] != '' 
        and config['pathClassificador']!= '' 
        and config['pathHaarcascadeFrontalFace']!= '' 
        and config['enderecoCamera']!= ''
        and config['pathArquivosFotos'] != '' ):
            DBconection.escreveLogDB("INI","Documento Config OK [2//6]")
            return True, config
        else:
            DBconection.escreveLogDB("ERROR","Documento Config com erro")
            return False, config
    except:
        DBconection.escreveLogDB("ERROR","Documento Config não encontrado")
        return False, config

#Verifica a existencias dos arquivos da biblioteca OpenCV
def verificaArquivosOPENCV(DBconection,pathClassificador,pathHaarcascadeFrontalFace):
    if(os.path.exists(pathClassificador) and os.path.exists(pathHaarcascadeFrontalFace)):
        DBconection.escreveLogDB("INI","Arquivos OpenCV OK [3//6]")
        return True
    else:
        DBconection.escreveLogDB("ERROR","Não encontrado arquivos OpenCV")
        return False

#Verifica se o caminho para salvar imagens existe
def verificaPastaArquivosFotos(DBconection,pathArquivosFotos):
    if(os.path.exists(pathArquivosFotos)):
        DBconection.escreveLogDB("INI","Pasta Arquivos Fotos OK [4//6]")
        return True
    else:
        DBconection.escreveLogDB("ERROR","Não encontrado pasta arquivos Fotos")
        return False

#Cria os calssificadores de Face e do Reconhecimento Facial
def criaClassificadoresOpenCV(DBconection,pathHaarcascadeFrontalFace,pathClassificador):
    try:
        classificadorFaces = cv2.CascadeClassifier(pathHaarcascadeFrontalFace)
        identificadorFaces = cv2.face.EigenFaceRecognizer_create()
        identificadorFaces.read(pathClassificador)
        DBconection.escreveLogDB("INI","Classificadores do OpenCV setados OK [5//6]")
        return True, classificadorFaces,identificadorFaces
    except:
        DBconection.escreveLogDB("ERROR","Erro na criação dos classificadores OpenCV")
        return False, "", ""

#Instancia a camera para captura de imagens
def instanciaCamera(DBconection,endereCamera):
    try:
        camera = cv2.VideoCapture(endereCamera)
        success, frame = camera.read()
        if(success):
            DBconection.escreveLogDB("INI","Camera Funcionando [6//6]")
            return True, camera
        else:
            DBconection.escreveLogDB("ERROR","Camera não Funcionando")
            return False, ""
    except:
        DBconection.escreveLogDB("ERROR","Camera não instanciada")
        return False, ""

#funções para serem implementadas
def encerraSistema():
    sys.exit()

def instanciaIO():
    
    return True,True,True
#MAIN
if __name__ == "__main__":
    print("Iniciando o Sistema")
    print("Conectando com o Banco da Dados")
    statusConexaoBD, db = conexaoBancoDados()
    print("Conexão com o Banco de dados: " + str(statusConexaoBD))
    if(statusConexaoBD):
        statusConfig, config = buscaConfigs(db,0)
        print("Importação das Configurações: " + str(statusConfig))
    else:
        encerraSistema()

    if(statusConfig):
        systemON = config['sistemaLigado'] 
        pathClassificador = config['pathClassificador']
        pathHaarcascadeFrontalFace = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        enderecoCamera = config['enderecoCamera']
        pathArquivosFotos = config['pathArquivosFotos']
        print("Configurações Setadas")
    else:
        encerraSistema()

    statusArquivosOPENCV = verificaArquivosOPENCV(db,pathClassificador,pathHaarcascadeFrontalFace)
    statusPastaImagens = verificaPastaArquivosFotos(db,pathArquivosFotos)
    if(statusArquivosOPENCV and statusPastaImagens):
        print("Arquivose Pastas Encontrados")
        statusClassificadores,classificadorFaces,identificadorFaces = criaClassificadoresOpenCV(pathClassificador,pathHaarcascadeFrontalFace)
    else:
        encerraSistema()
    
    if(statusClassificadores):
        print("Classificadores Setados")
        statusCamera, camera= instanciaCamera(enderecoCamera)
    else:
        encerraSistema()
    
    if(statusCamera):
        print("Camera Conectada")
        statusIO, led, releFechadura = instanciaIO()
    else:
        encerraSistema()
    
    if(statusConexaoBD and statusConfig and statusArquivosOPENCV and statusPastaImagens and statusClassificadores and statusCamera and statusIO):
        while(1):
            henrique = "LINDO"
            if henrique == "LINDO":
                a=0
            else:
                a=10
    else:
        encerraSistema()

    
        
