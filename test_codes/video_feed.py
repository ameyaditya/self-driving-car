import cv2

vcap = cv2.VideoCapture('http://192.168.1.82:5000/video_feed')
try:
    while True:
        ret, frame = vcap.read()
        if frame is not None:
            cv2.imshow("stream", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

except:
    cv2.destroyAllWindows()
