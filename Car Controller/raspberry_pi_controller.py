import RPi.GPIO as GPIO
import time

from car_movement import CarMovement
from car_rotation import CarRotation

class RaspberryPiController:
    def __init__(self):
        self.RPI_INITIALISED = True
        print("INITIALISING RASPBERRY PI")
    
    def initialise_car_movement(self, m1_f, m1_b, m2_f, m2_b, servo_pin):
        if not self.RPI_INITIALISED:
            return False
        
        self.car_movement = CarMovement(m1_f, m1_b, m2_f, m2_b)
        self.car_movement.initialise()
        print("CAR MOVEMENT INITIALISED")

        self.car_rotation = CarRotation(servo_pin)
        self.car_rotation.initialise()
        print("CAR ROTATION INITIALISED")
        print("MOUNT AXLE")
        return True
    
    def move_forward(self):
        if not self.RPI_INITIALISED:
            return False
        self.car_movement.move_forward()
        return True
    
    def move_backward(self):
        if not self.RPI_INITIALISED:
            return False
        self.car_movement.move_backward()
        return True
    
    def turn_right(self):
        if not self.RPI_INITIALISED:
            return False
        self.car_rotation.turn_right()
        return True
    
    def turn_left(self):
        if not self.RPI_INITIALISED:
            return False
        self.car_rotation.turn_left()
        return True
        
    def stop(self):
        if not self.RPI_INITIALISED:
            return False
        self.car_movement.stop()
        return True
    
    def kill_switch(self):
        self.RPI_INITIALISED = False
        GPIO.cleanup()


