import RPi.GPIO as GPIO
import pigpio
import time

from config import Config as c


class CarRotation:
    def __init__(self, servo_pin):
        self.PULSE_WIDTH = c.INITIAL_PULSE_WIDTH
        self.MINIMUM_PULSE_WIDTH = c.MINIMUM_PULSE_WIDTH
        self.MAXIMUM_PULSE_WIDTH = c.MAXIMUM_PULSE_WIDTH
        self.SERVO_FREQUENCY = c.SERVO_FREQUENCY
        self.SERVO_PIN = servo_pin
        self.CURRENT_DIRECTION = None
        self.PWM = pigpio.pi()
        self.PWM.set_mode(self.SERVO_PIN, pigpio.OUTPUT)
        self.PWM.set_PWM_frequency(self.SERVO_PIN, self.SERVO_FREQUENCY)
        time.sleep(3)

    def initialise(self):
        self.PWM.set_servo_pulsewidth(self.SERVO_PIN, c.INITIAL_PULSE_WIDTH)
        time.sleep(0.2)
        self.CURRENT_DIRECTION = "CENTER"

    def turn(self, direction):
        if direction == self.CURRENT_DIRECTION:
            return
        self.CONTROL_PIN.start(0)
        updater = 0
        if self.PULSE_WIDTH < c.DIRECTION[direction]["PULSE_WIDTH"]:
            updater = 1
        else:
            updater = -1

        while self.PULSE_WIDTH != c.DIRECTION[direction]["PULSE_WIDTH"]:
            self.PULSE_WIDTH = self.PULSE_WIDTH + \
                (c.PULSE_WIDTH_CHANGE_INTERVAL * updater)
            self.PWM.set_servo_pulsewidth(self.SERVO_PIN, self.PULSE_WIDTH)
            time.sleep(c.TURN_SPEED)
        self.CURRENT_DIRECTION = direction
        self.CONTROL_PIN.stop()

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
        if self.PULSE_WIDTH == self.MAXIMUM_PULSE_WIDTH:
            return
        self.PULSE_WIDTH = self.PULSE_WIDTH + c.PULSE_WIDTH_CHANGE_INTERVAL
        self.PWM.set_servo_pulsewidth(
            self.SERVO_PIN, self.PULSE_WIDTH)
        time.sleep(c.TURN_SPEED)

    def turn_left(self):
        if self.PULSE_WIDTH == self.MINIMUM_PULSE_WIDTH:
            return
        self.PULSE_WIDTH = self.PULSE_WIDTH - c.PULSE_WIDTH_CHANGE_INTERVAL
        self.PWM.set_servo_pulsewidth(
            self.SERVO_PIN, self.PULSE_WIDTH)
        time.sleep(c.TURN_SPEED)