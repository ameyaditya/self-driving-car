import cv2
import numpy as np

from sklearn.cluster import KMeans
from utils import hough_lines_end_points

img = cv2.imread("test1.jpg")
img_shape = img.shape

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygons = np.array([
        [0, height // 3], [width, height // 3],[width, height], [0, height]
        ])
    mask = np.zeros_like(image)      
    cv2.fillPoly(mask, [polygons], 255) 
    masked_image = cv2.bitwise_and(image, mask) 
    return masked_image

def canny_edge_detector(image):      
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0) 
    canny = cv2.Canny(blur, 50, 150)
    return canny

frame = img.copy()
canny_image = canny_edge_detector(frame)
cropped_image = region_of_interest(canny_image)

temp_img = img.copy()
lines_r_theta = cv2.HoughLines(cropped_image, 1, np.pi / 180, 50, 
                        np.array([]))

lines_end_points = hough_lines_end_points(lines_r_theta, img_shape)
print("LINES", lines_end_points)
for k in range(len(lines_end_points)):
    if(len(lines_end_points[k]) < 2):
        continue
    # (a,b),(c,d) = lines_end_points[k][0]
    a,b = lines_end_points[k][0]
    c,d = lines_end_points[k][1]
    cv2.line(temp_img, (a,b), (c,d), (255, 0, 0), 3, cv2.LINE_AA)
    cv2.imshow("TEMP IMAGE", temp_img)
    cv2.waitKey(0) 

