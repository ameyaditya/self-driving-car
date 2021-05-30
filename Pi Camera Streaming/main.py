from flask import Flask, render_template, Response, request
from flask_cors import CORS
import time
import threading
import os
import io
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

camera = PiCamera()
camera.resolution = (736, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(736,480))
camera.capture(rawCapture, format="bgr")
print("INITIALISED THE CAMERA")
my_stream = io.BytesIO()


# def get_frame():
#     image = camera.capture(format="jpeg", use_video_port=True)
    
#     return jpeg.tobytes()

# pi_camera = VideoCamera(flip=False)
# with PiCamera() as camera:
#     camera.start_preview()
#     time.sleep(2)
#     with PiRGBArray(camera) as stream:
#         camera.capture(stream, format='bgr')
#         # At this point the image is available as stream.array
#         image = stream.array
    
app = Flask(__name__)
CORS(app)

# def gen():
#     while True:
#         frame = get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
