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
        print(type(frame))
        success, encoded_image = cv2.imencode('.jpg', image)
        bytes_image = encoded_image.tobytes()
        cv2.imwrite('pic.jpg', frame)
        image = open('pic.jpg', 'rb').read()
        print(type(image))
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               bytes_image
               + b'\r\n')


@app.route('/video_feed') 
def video_feed(): 
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__': 
	app.run(host='0.0.0.0', port=5001, threaded=True) 