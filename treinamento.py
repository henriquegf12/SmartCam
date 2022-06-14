import cv2
import os
import cv2
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50,threshold=10000)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImagemComID():
    caminhos = [os.path.join("C:\\Users\\henri\\TCC_SmartHome\\SmartHome\\API\\raspberryCam\\imagensTreinamento",f) for f in os.listdir("C:\\Users\\henri\\TCC_SmartHome\\SmartHome\\API\\raspberryCam\\imagensTreinamento")]
    print(caminhos)
    faces = []
    ids = []

    for  caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem),cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('_')[1])
        ids.append(id)
        faces.append(imagemFace)

    return np.array(ids), faces
 
ids, faces = getImagemComID()

print("Treinando ...")

eigenface.train(faces,ids)
eigenface.write('C:\\Users\\henri\\TCC_SmartHome\\SmartHome\\API\\raspberryCam\\classificadorEigen.yml')

print("Treinamento finalizado ...")