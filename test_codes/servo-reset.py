import RPi.GPIO as GPIO
import time

SERVO_PIN = 33
SERVO_FREQUENCY = 50
DUTY_CYCLE = 6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
CONTROL_PIN = GPIO.PWM(SERVO_PIN, SERVO_FREQUENCY)
CONTROL_PIN.start(DUTY_CYCLE)
time.sleep(3)

CONTROL_PIN.ChangeDutyCycle(7.4)
time.sleep(0.2)
print("INITIAL TEST DONE")


# GPIO.output(SERVO_PIN, False)
# for i in range(5):
#     GPIO.output(SERVO_PIN, True)
#     CONTROL_PIN = GPIO.PWM(SERVO_PIN, SERVO_FREQUENCY)
#     CONTROL_PIN.ChangeDutyCycle(DUTY_CYCLE + 1)
input()


