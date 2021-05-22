from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
import RPi.GPIO as GPIO

from raspberry_pi_controller import RaspberryPiController
from config import Config as c

GPIO.setmode(GPIO.BOARD)

rpc = RaspberryPiController()

app = Flask(__name__)

def generate_response(data, status):
    return jsonify({
        "status": status,
        "data": data
    })

@app.route("/")
@cross_origin()
def home_page():
    return render_template("index.html")

@app.route("/api/v1/initialise_car_movement")
@cross_origin()
def initialise_car_movement():
    try:
        res = rpc.initialise_car_movement(c.M1_F, c.M1_B, c.M2_F, c.M2_B)
        if res:
            return generate_response({"message": "CAR MOVEMENT INITIALISED"}, 200)
        raise Exception("RPI NOT INITIALISED")
    except Exception as e:
        return generate_response({"message": "ERROR OCCURED", "error": str(e)}, 500)

@app.route("/api/v1/move_forward")
@cross_origin()
def move_forward():
    try:
        res = rpc.move_forward()
        if res:
            return generate_response({"message": "CAR MOVING FORWARD"}, 200)
        raise Exception("RPI NOT INITIALISED")
    except Exception as e:
        return generate_response({"message": "ERROR OCCURED", "error": str(e)}, 500)

@app.route("/api/v1/move_backward")
@cross_origin()
def move_backward():
    try:
        res = rpc.move_backward()
        if res:
            return generate_response({"message": "CAR MOVING BACKWARD"}, 200)
        raise Exception("RPI NOT INITIALISED")
    except Exception as e:
        return generate_response({"message": "ERROR OCCURED", "error": str(e)}, 500)

@app.route("/api/v1/stop")
@cross_origin()
def stop():
    try:
        res = rpc.stop()
        if res:
            return generate_response({"message": "CAR STOPPED"}, 200)
        raise Exception("RPI NOT INITIALISED")
    except Exception as e:
        return generate_response({"message": "ERROR OCCURED", "error": str(e)}, 500)

@app.route("/api/v1/kill_switch")
@cross_origin()
def kill_switch():
    try:
        rpc.kill_switch()
        return generate_response({"message": "rASPBERRY PI KILLED"}, 200)
    except Exception as e:
        return generate_response({"message": "ERROR OCCURED", "error": str(e)}, 500)

if __name__ == "__main__":
    app.run(debug=True)