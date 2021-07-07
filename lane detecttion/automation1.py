import time
import numpy as np
import cv2

from automation_utils import canny_edge_detector, region_of_interest, get_average_slope_intercept
from control_car import CarController
import config as c

cc = CarController(c.BASE_URL)
def check_right_lane():
    pass

def get_hog_lines(image):
    frame = image.copy()
    canny_image = canny_edge_detector(frame)
    cropped_image = region_of_interest(canny_image)

    lines = cv2.HoughLinesP(cropped_image, 1, np.pi / 180, 50, 
                        np.array([]), minLineLength = 5, 
                        maxLineGap = 40)
    new_lines = []
    for k in range(len(lines)):
        a,b,c,d = lines[k][0]
        slope = (d-b) / (c-a)
        intercept = b - (slope * a)
        theta = np.arctan(slope)
        degrees = np.rad2deg(abs(theta))
        if (degrees >= 80 and degrees <= 100) or (degrees >= 0 and degrees <= 10):
            continue
        else:
            new_lines.append((lines[k], slope, intercept))

        print(a,b,c,d)
        print("SLOPE: ", slope)
        print("THETA: ", theta)
    return new_lines

def check_if_two_lanes(lines):
    averaged_lines = get_average_slope_intercept(lines, 2)
    slope1 = averaged_lines[0][0]
    slope2 = averaged_lines[1][0]

    if (slope1 < 0 and slope2 > 0) or (slope2 < 0 and slope1 > 0):
        return True
    return False

def check_average_slope(width_lower_limit, width_upper_limit, lines):
    slopes = []
    intercepts = []
    for line in lines:
        a,b,c,d = line[0][0]
        if a >= width_lower_limit and a <= width_upper_limit and c >= width_lower_limit and c <= width_upper_limit:
            slopes.append(line[1])
            intercepts.append(line[2])
    return (np.average(slopes), np.average(intercepts))

def run(image):
    height, width = image.shape[:2]
    lines = get_hog_lines(image)
    while True:
        if check_if_two_lanes(lines):
            cc.move_forward(for = 1)
        else:
            left_slopes = check_average_slope(0, width // 2, lines)
            right_slopes = check_average_slope(width // 2, width, lines)
            if left_slopes[0] != np.nan and left_slopes[0] > 0:
                cc.move_forward(for = 1)
            elif right_slopes[0] != np.nan and right_slopes[0] < 0:
                cc.move_forward(for = 1)
            else:
                print("CANNOT FIND LANES... EXITING")



img = cv2.imread("test1.jpg")
get_hog_lines(img)
