from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

def get_frame():
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()