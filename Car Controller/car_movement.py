import RPi.GPIO as GPIO

from config import Config as c

class CarMovement:
    def __init__(self, m1_f, m1_b, m2_f, m2_b):
        self.m1_f = m1_f
        self.m1_b = m1_b
        self.m2_f = m2_f
        self.m2_b = m2_b

        self.m1_f_controller = None
        self.m1_b_controller = None
        self.m2_f_controller = None
        self.m2_b_controller = None
        
        self.CURRENT_MOVEMENT = "STOP"
    
    def initialise(self):
        GPIO.setup(self.m1_f, GPIO.OUT)
        GPIO.setup(self.m1_b, GPIO.OUT)
        GPIO.setup(self.m2_f, GPIO.OUT)
        GPIO.setup(self.m2_b, GPIO.OUT)

        self.m1_f_controller = GPIO.PWM(self.m1_f, c.CAR_MOVEMENT_FREQUENCY)
        self.m1_b_controller = GPIO.PWM(self.m1_b, c.CAR_MOVEMENT_FREQUENCY)
        self.m2_f_controller = GPIO.PWM(self.m2_f, c.CAR_MOVEMENT_FREQUENCY)
        self.m2_b_controller = GPIO.PWM(self.m2_b, c.CAR_MOVEMENT_FREQUENCY)

        self.m1_f_controller.start(0)
        self.m1_b_controller.start(0)
        self.m2_f_controller.start(0)
        self.m2_b_controller.start(0)
    
    def move_forward(self, speed = c.DEFAULT_FORWARD_SPEED):
        if self.CURRENT_MOVEMENT == "FORWARD":
            return

        self.m1_b_controller.ChangeDutyCycle(0)
        self.m2_b_controller.ChangeDutyCycle(0)
        self.m1_f_controller.ChangeDutyCycle(speed)
        self.m2_f_controller.ChangeDutyCycle(speed)
        self.CURRENT_DIRECTION = "FORWARD"
    
    def move_backward(self, speed = c.DEFAULT_BACKWARD_SPEED):
        if self.CURRENT_DIRECTION == "BACKWARD":
            return

        self.m1_f_controller.ChangeDutyCycle(0)
        self.m2_f_controller.ChangeDutyCycle(0)
        self.m1_b_controller.ChangeDutyCycle(speed)
        self.m2_b_controller.ChangeDutyCycle(speed)
        self.CURRENT_DIRECTION = "BACKWARD"
    
    def stop(self):
        if self.CURRENT_DIRECTION == "STOP":
            return

        self.m1_f_controller.ChangeDutyCycle(0)
        self.m2_f_controller.ChangeDutyCycle(0)
        self.m1_b_controller.ChangeDutyCycle(0)
        self.m2_b_controller.ChangeDutyCycle(0)
        self.CURRENT_DIRECTION = "STOP"
    