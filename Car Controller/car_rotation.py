import RPi.GPIO as GPIO
import time

from config import Config as c


class CarRotation:
    def __init__(self, servo_pin):
        self.DUTY_CYCLE = c.INITIAL_DUTY_CYCLE
        self.MINIMUM_DUTY_CYCLE = c.MINIMUM_DUTY_CYCLE
        self.MAXIMUM_DUTY_CYCLE = c.MAXIMUM_DUTY_CYCLE
        self.SERVO_FREQUENCY = c.SERVO_FREQUENCY
        self.SERVO_PIN = servo_pin
        self.CURRENT_DIRECTION = None
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        self.CONTROL_PIN = GPIO.PWM(self.SERVO_PIN, self.SERVO_FREQUENCY)

    def initialise(self):
        # self.CONTROL_PIN.start(self.DUTY_CYCLE)
        self.CONTROL_PIN.start(0)
        time.sleep(0.2)
        self.CONTROL_PIN.ChangeDutyCycle(self.DUTY_CYCLE)
        time.sleep(0.2)
        self.CONTROL_PIN.stop()
        self.CURRENT_DIRECTION = "CENTER"

    def turn(self, direction):
        if direction == self.CURRENT_DIRECTION:
            return

        updater = 0
        if self.DUTY_CYCLE < c.DIRECTION[direction]["DUTY_CYCLE"]:
            updater = 1
        else:
            updater = -1

        while self.DUTY_CYCLE != c.DIRECTION[direction]["DUTY_CYCLE"]:
            self.DUTY_CYCLE = round(
                self.DUTY_CYCLE + (c.DUTY_CYCLE_CHANGE_INTERVAL * updater), 2)
            self.CONTROL_PIN.ChangeDutyCycle(self.DUTY_CYCLE)
            time.sleep(c.TURN_SPEED)
        self.CURRENT_DIRECTION = direction

    def turn_full_right(self):
        self.turn("FULL_RIGHT")

    def turn_half_right(self):
        self.turn("HALF_RIGHT")

    def turn_center(self):
        self.turn("CENTER")

    def turn_half_left(self):
        self.turn("HALF_LEFT")

    def turn_full_left(self):
        self.turn("FULL_LEFT")

    def turn_right(self):
        if self.DUTY_CYCLE == self.MAXIMUM_DUTY_CYCLE:
            return

        self.DUTY_CYCLE = round(
            self.DUTY_CYCLE + (c.DUTY_CYCLE_CHANGE_INTERVAL), 2)
        self.CONTROL_PIN.ChangeDutyCycle(self.DUTY_CYCLE)

    def turn_left(self):
        if self.DUTY_CYCLE == self.MINIMUM_DUTY_CYCLE:
            return

        self.DUTY_CYCLE = round(
            self.DUTY_CYCLE - (c.DUTY_CYCLE_CHANGE_INTERVAL), 2)
        self.CONTROL_PIN.ChangeDutyCycle(self.DUTY_CYCLE)
