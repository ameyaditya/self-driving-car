class Config:
    #PINS

    #MOVEMENT PINS
    M1_F = 16
    M1_B = 18
    M2_F = 22
    M2_B = 15

    CAR_MOVEMENT_FREQUENCY = 100
    DEFAULT_FORWARD_SPEED = 40
    DEFAULT_BACKWARD_SPEED = 50

    #ROTATION PINS
    SERVO_PIN = 13

    INITIAL_PULSE_WIDTH = 1400
    MINIMUM_PULSE_WIDTH = 1175
    MAXIMUM_PULSE_WIDTH = 1625

    PULSE_WIDTH_CHANGE_INTERVAL = 25
    TURN_SPEED = 0.1
    SERVO_FREQUENCY = 50

   # ULTRASONIC CONFIG
    TRIGGER_PIN = 29
    ECHO_PIN = 31

    DIRECTION = {
    "FULL_LEFT": {"DUTY_CYCLE": 8.0},
    "HALF_LEFT": {"DUTY_CYCLE": 8.4},
    "CENTER": {"DUTY_CYCLE": 9.0},
    "HALF_RIGHT": {"DUTY_CYCLE": 9.6},
    "FULL_RIGHT": {"DUTY_CYCLE": 10.0}
    }
