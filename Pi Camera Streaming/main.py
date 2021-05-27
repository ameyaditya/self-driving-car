from flask import Flask, render_template, Response, request
from flask_cors import CORS
import time
import threading
import os

from camera_frames import get_frame

# pi_camera = VideoCamera(flip=False)

app = Flask(__name__)
CORS(app)

def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
