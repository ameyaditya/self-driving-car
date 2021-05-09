import RPi.GPIO as GPIO
from car_rotation import RotateWheel

rw = RotateWheel()

servo_pin = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin,GPIO.OUT)

p=GPIO.PWM(servo_pin,50)

rw.initialiseAxle(p)
try:
    while True:
        choice = input()
        if choice == "1":
            rw.turn_full_left(p)
        elif choice == "2":
            rw.turn_half_left(p)
        elif choice == "3":
            rw.turn_center(p)
        elif choice == "4":
            rw.turn_half_right(p)
        elif choice == "5":
            rw.turn_full_right(p)
except Exception as e:
    print(f"ERROR {e}")
    GPIO.cleanup()