from flask import Flask, render_template, Response, request
from flask_cors import CORS
import time
import threading
import os

from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

camera = PiCamera()
camera.resolution = (720, 480)
rawCapture = PiRGBArray(camera)
print("INITIALISED THE CAMERA")

def get_frame():
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()

# pi_camera = VideoCamera(flip=False)

app = Flask(__name__)
CORS(app)

def gen():
    while True:
        print("GETTING A FRAME")
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
