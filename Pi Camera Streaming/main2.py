from flask import Flask, render_template, Response
from flask_cors import CORS
import picamera
import cv2
import socket
import io

app = Flask(__name__)
CORS(app)

vc = cv2.VideoCapture(0)

def gen():
    while True:
        rval, frame = vc.read()
        if rval:
            success, frame = cv2.imencode('.jpg', frame)
            frame = frame.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' +
                frame
                + b'\r\n')


@app.route('/video_feed') 
def video_feed(): 
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_2') 
def video_feed_2(): 
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__': 
	app.run(host='0.0.0.0', port=5001, threaded=True) 