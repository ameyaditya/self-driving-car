import RPi.GPIO as GPIO

class CarMovement:
    def __init__(self, m1_f, m1_b, m2_f, m2_b):
        self.m1_f = m1_f
        self.m1_b = m1_b
        self.m2_f = m2_f
        self.m2_b = m2_b
        self.CURRENT_MOVEMENT = "STOP"
    
    def initialise(self):
        GPIO.setup(self.m1_f, GPIO.OUT)
        GPIO.setup(self.m1_b, GPIO.OUT)
        GPIO.setup(self.m2_f, GPIO.OUT)
        GPIO.setup(self.m2_b, GPIO.OUT)
    
    def move_forward(self):
        if self.CURRENT_MOVEMENT == "FORWARD":
            return
        GPIO.output(self.m1_b, False)
        GPIO.output(self.m2_b, False)
        GPIO.output(self.m1_f, True)
        GPIO.output(self.m2_f, True)
        self.CURRENT_DIRECTION = "FORWARD"
    
    def move_backward(self):
        if self.CURRENT_DIRECTION == "BACKWARD":
            return
        GPIO.output(self.m1_f, False)
        GPIO.output(self.m2_f, False)
        GPIO.output(self.m1_b, True)
        GPIO.output(self.m2_b, True)
        self.CURRENT_DIRECTION = "BACKWARD"
    
    def stop(self):
        if self.CURRENT_DIRECTION == "STOP":
            return
        GPIO.output(self.m1_f, False)
        GPIO.output(self.m2_f, False)
        GPIO.output(self.m1_b, False)
        GPIO.output(self.m2_b, False)
        self.CURRENT_DIRECTION = "STOP"
    