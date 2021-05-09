import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
servo = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)

p=GPIO.PWM(servo,50)

p.start(2.5)
try:
    while True:
        print("FORWARD")
        for i in control:
            p.ChangeDutyCycle(i)
            time.sleep(1)
            print(i)
        
        print("REVERSE")
        for i in control[::-1][2:]:
            p.ChangeDutyCycle(i)
            time.sleep(1)
            print(i)
except KeyboardInterrupt:
    GPIO.cleanup()