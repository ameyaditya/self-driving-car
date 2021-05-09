import RPi.GPIO as GPIO
import time

servo_pin = 16
initial_duty_cycle = 7.5
angle = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin,GPIO.OUT)

p=GPIO.PWM(servo_pin,50)

p.start(initial_duty_cycle) # start with a duty cycle of 7.5, center position
input() # wait for axle to be setup

try:
    while True:
        calculated_duty_cycle = initial_duty_cycle
        print("ROTATING TO RIGHT")
        for i in range(11):
            calculated_duty_cycle += 0.1
            angle += 3.6
            p.ChangeDutyCycle(calculated_duty_cycle)
            time.sleep(1)
            print(f"ROTATED TO {angle} DEGREES")
        
        for i in range(22):
            calculated_duty_cycle -= 0.1
            angle -= 3.6
            p.ChangeDutyCycle(calculated_duty_cycle)
            time.sleep(1)
            print(f"ROTATED TO {angle} DEGREES")
        
        for i in range(11):
            calculated_duty_cycle += 0.1
            angle += 3.6
            p.ChangeDutyCycle(calculated_duty_cycle)
            time.sleep(1)
            print(f"ROTATED TO {angle} DEGREES")
        print("FINISHED ONE COMPLETE CYCLE")
except Exception:
    GPIO.cleanup()
        