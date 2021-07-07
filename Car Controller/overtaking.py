from car_rotation import CarRotation as cr
import requests
threshold = 30
turn_time = 1
overtake_time=5
while True:
    distance = requests.get("/api/v1/distance")

    if distance <=30:
        cr.turn_full_right()
        time.sleep(turn_time)
        cr.turn_center()
        time.sleep(overtake_time)
        cr.turn_full_left()
        time.sleep(turn_time)
        cr.turn_center()
    


