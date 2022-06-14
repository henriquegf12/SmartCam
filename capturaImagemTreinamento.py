import cv2



if __name__ == "__main__":
    id = input("Digite o ID da pessoa: ")
    qtdFotos = input("Digite a quantidade de fotos: ")
    largura, altura = 220,220
    cap = cv2.VideoCapture(0)
    terminou = True
    classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    adressFile = "C:\\Users\\henri\\TCC_SmartHome\\SmartHome\\API\\raspberryCam\\imagensTreinamento\\"
    fileName = "face_"
    numeroDaFoto = 0
    for i in range(int(qtdFotos)):
        while terminou:
            ret,frame = cap.read()
            imagemCinza= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faceDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=3, minNeighbors =5)
            for (x, y, l ,a) in faceDetectadas:
                cv2.rectangle(frame, (x,y),(x+l,y+a), (0,0,255),2)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    imagemFaceCinza= cv2.resize(imagemCinza[y:y+a,x:x+l],(largura,altura))
                    cv2.imwrite(adressFile + fileName + str(id) + "_" + str(numeroDaFoto) + ".png",imagemFaceCinza)
                    print("Foto " + str(numeroDaFoto) + " tirada com sucesso")
                    numeroDaFoto = numeroDaFoto + 1
            cv2.imshow("Frame",frame)
            if numeroDaFoto > int(qtdFotos):
                terminou = False

            


