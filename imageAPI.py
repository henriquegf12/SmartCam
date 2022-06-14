import cv2
import time


class camera:
    fps = 0

    def __init__(self,enderecoCamera,seachForFace,reconhecerFace) -> None:
        self.camera = cv2.VideoCapture(enderecoCamera)
        self.seachForFace = seachForFace
        self.reconhecerFace = reconhecerFace
        self.classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.largura, self.altura = 220, 220
        self.reconhecedor = cv2.face.EigenFaceRecognizer_create()
        self.reconhecedor.read('C:\\Users\\henri\\TCC_SmartHome\\SmartHome\\API\\raspberryCam\\classificadorEigen.yml')
        self.versaoOpencv =cv2.__version__

    def getFps(self):
        return self.fps

    def gen_frames(self):
        contadorFrame = 0
        start = time.time()
        
        while True:
            success, frame = self.camera.read()  # read the camera frame
            if not success:
                break
            else:
                if(self.seachForFace):
                    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faceDetectadas = self.classificador.detectMultiScale(imagemCinza, scaleFactor=3, minNeighbors =5)
                    for (x, y, l ,a) in faceDetectadas:
                        if(self.reconhecerFace):
                            imagemFace = cv2.resize(imagemCinza[y:y+a,x:x+1],(self.largura,self.altura))
                            id, confianca = self.reconhecedor.predict(imagemFace)
                            if(id == 1):

                                cv2.putText(frame,'henrique',(x,y+(a+30)),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
                            
                        cv2.rectangle(frame, (x,y),(x+l,y+a), (0,0,255),2)

                   
                
                contadorFrame = contadorFrame + 1
                if(time.time()- start) >1:
                    self.fps = contadorFrame
                    start = time.time()
                    contadorFrame = 0
                cv2.putText(frame,str(self.fps),(10,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result