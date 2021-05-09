import time

INITIAL_DUTY_CYCLE = 7.4
DUTY_CYCLE_CHANGE_INTERVAL = 0.2
TURN_SPEED = 0.5 # increase this value to make it turn slower

DIRECTION = {
    "CENTER": {"DUTY_CYCLE": 7.4},
    "HALF_RIGHT": { "DUTY_CYCLE": 8.0},
    "FULL_RIGHT": {"DUTY_CYCLE": 8.4},
    "HALF_LEFT": {"DUTY_CYCLE": 6.8},
    "FULL_LEFT": {"DUTY_CYCLE": 6.4}
}


class RotateWheel:

    def __init__(self):
        self.DUTY_CYCLE = INITIAL_DUTY_CYCLE
        self.CURRENT_DIRECTION = None

    def initialiseAxle(self, control_pin):
        control_pin.start(self.DUTY_CYCLE)
        self.CURRENT_DIRECTION = "CENTER"
        print("SERVO INITIALISED, INSERT THE AXLE")

    def turn(self, direction, control_pin):
        if direction == self.CURRENT_DIRECTION:
            return
        
        updater = 0
        if self.DUTY_CYCLE < DIRECTION[direction]["DUTY_CYCLE"]:
            updater = 1
        else:
            updater = -1
        
        while self.DUTY_CYCLE != DIRECTION[direction]["DUTY_CYCLE"]:
            print(self.DUTY_CYCLE)
            self.DUTY_CYCLE = round(self.DUTY_CYCLE + (DUTY_CYCLE_CHANGE_INTERVAL * updater), 1)
            control_pin.ChangeDutyCycle(self.DUTY_CYCLE)
            time.sleep(TURN_SPEED)
        self.CURRENT_DIRECTION = direction
        print("TURN COMPLETE")
    
    def turn_full_right(self, control_pin):
        self.turn("FULL_RIGHT", control_pin)
    
    def turn_half_right(self, control_pin):
        self.turn("HALF_RIGHT", control_pin)
    
    def turn_center(self, control_pin):
        self.turn("CENTER", control_pin)

    def turn_half_left(self, control_pin):
        self.turn("HALF_LEFT", control_pin)
    
    def turn_full_left(self, control_pin):
        self.turn("FULL_LEFT", control_pin)
