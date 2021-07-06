import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, trigger_pin, echo_pin):
        self.TRIGGER_PIN = trigger_pin
        self.ECHO_PIN = echo_pin

    def initialise(self):
        GPIO.setup(self.TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)
        GPIO.output(self.TRIGGER_PIN, False)
        time.sleep(2)
    
    def get_distance(self):
        GPIO.output(self.TRIGGER_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIGGER_PIN, False)

        while GPIO.input(self.ECHO_PIN)==0:
            pulse_start = time.time()
        
        while GPIO.input(self.ECHOs_PIN)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance+1.15, 2)
        return distance
