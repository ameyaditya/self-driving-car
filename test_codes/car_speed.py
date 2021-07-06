import RPi.GPIO as GPIO
import time

M1_F = 16
GPIO.setmode(GPIO.BOARD)

GPIO.setup(M1_F, GPIO.OUT)

M1_CONTROLLER = GPIO.PWM(M1_F, 100)

M1_CONTROLLER.start(0)
time.sleep(1)

M1_CONTROLLER.ChangeDutyCycle(10)
time.sleep(5)

M1_CONTROLLER.ChangeDutyCycle(0)
time.sleep(5)

M1_CONTROLLER.ChangeDutyCycle(100)
time.sleep(5)

GPIO.cleanup()

