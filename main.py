from flask import Flask, render_template, Response
from imageAPI import camera

app = Flask(__name__)

camera1 = camera(0,True,True)


@app.route('/cameraStatus')
def cameraStatus():
    return camera1.isOpened()

@app.route('/versaoOpencv')
def versaoOpencv():
    return camera1.versaoOpencv

@app.route('/video_feed')
def video_feed():
    return Response(camera1.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html',fps=camera1.fps)


if __name__ == '__main__':
    app.run(host='0.0.0.0')