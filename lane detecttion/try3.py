import cv2
import numpy as np

from sklearn.cluster import KMeans

img = cv2.imread("test2.jpg")
img_shape = img.shape
colors = [(255,0, 0), (0, 255, 0), (0,0,255)]

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

def create_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (2 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    fits = [[i[1], i[2]] for i in lines]   
    
    kmeans = KMeans(n_clusters = 3, random_state = 0, max_iter = 10).fit(np.array(fits))
    line_averages = kmeans.cluster_centers_
    print(line_averages)
    line1 = create_coordinates(image, line_averages[0])
    line2 = create_coordinates(image, line_averages[1])
    line3 = create_coordinates(image, line_averages[2])
    return np.array([line1, line2, line3])

def get_average_slope_intercept(lines):
    fits = [[i[1], i[2]] for i in lines]   
    
    kmeans = KMeans(n_clusters = 3, random_state = 0, max_iter = 10).fit(np.array(fits))
    line_averages = kmeans.cluster_centers_
    return line_averages


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    counter = 0
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), colors[counter], 10)
            counter += 1
    return line_image

frame = img.copy()
canny_image = canny_edge_detector(frame)
cropped_image = region_of_interest(canny_image)

temp_img = img.copy()

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

    cv2.line(temp_img, (a,b), (c,d), (255, 0, 0), 3, cv2.LINE_AA)

    print(a,b,c,d)
    print("SLOPE: ", slope)
    print("THETA: ", theta)

averaged_lines = average_slope_intercept(frame, new_lines)
line_image = display_lines(frame, averaged_lines)
combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)


cv2.imshow("results", combo_image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
