import time
import requests

class CarController:
    def __init__(self, base_url):
        self.BASE_URL = base_url
    
    def move_forward(self, speed = 40, for = 2):
        requests.get(f"{self.BASE_URL}/api/v1/move_forward")
        time.sleep(for)
        requests.get(f"{self.BASE_URL}/api/v1/stop")
    
    def move_backward(self, speed = 50, for = 2):
        requests.get(f"{self.BASE_URL}/api/v1/move_backward")
        time.sleep(2)
        requests.get(f"{self.BASE_URL}/api/v1/stop")
    
