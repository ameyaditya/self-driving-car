class Config:
    #PINS

    #MOVEMENT PINS
    M1_F = 16
    M1_B = 18
    M2_F = 22
    M2_B = 15

    #ROTATION PINS
    SERVO_PIN = 13

    INITIAL_DUTY_CYCLE = 9.0
    MINIMUM_DUTY_CYCLE = 10.0
    MAXIMUM_DUTY_CYCLE = 8.0

    DUTY_CYCLE_CHANGE_INTERVAL = 0.1
    TURN_SPEED = 0.1
    SERVO_FREQUENCY = 50

    DIRECTION = {
    "FULL_LEFT": {"DUTY_CYCLE": 8.0},
    "HALF_LEFT": {"DUTY_CYCLE": 8.4},
    "CENTER": {"DUTY_CYCLE": 9.0},
    "HALF_RIGHT": {"DUTY_CYCLE": 9.6},
    "FULL_RIGHT": {"DUTY_CYCLE": 10.0}
    }
