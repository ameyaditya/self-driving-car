import cv2
import numpy as np

from sklearn.cluster import KMeans


img = cv2.imread("test1.jpg")
colors = [(0,0,255), (255,0,0), (0,255,0), (0,255,255), (255,0,255), (255,255,0), (0,0,0)]
counter = 0
def canny_edge_detector(image):
      
    # Convert the image color to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 
      
    # Reduce noise from the image
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0) 
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygons = np.array([
        [0, height // 3], [width, height // 3],[width, height], [0, height]
        ])
    mask = np.zeros_like(image)
      
    # Fill poly-function deals with multiple polygon
    cv2.fillPoly(mask, [polygons], 255) 
      
    # Bitwise operation between canny image and mask image
    masked_image = cv2.bitwise_and(image, mask) 
    return masked_image

def create_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines, lines_2):
    left_fit = []
    right_fit = []
    fits = []
    for i in range(len(lines)):
        if lines_2[i][0][1] < 0.5:
            continue

        x1, y1, x2, y2 = lines[i].reshape(4)
          
        # It will fit the polynomial and the intercept and slope
        parameters = np.polyfit((x1, x2), (y1, y2), 1) 
        slope = parameters[0]
        intercept = parameters[1]
        print(" SLOPE: ", slope, (x1, y1, x2, y2))
        fits.append([slope, intercept])
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    
    kmeans = KMeans(n_clusters = 3, random_state = 0, max_iter = 10).fit(np.array(fits))
    line_averages = kmeans.cluster_centers_
    print(line_averages)
    # left_fit_average = np.average(left_fit, axis = 0)
    # right_fit_average = np.average(right_fit, axis = 0)
    # left_line = create_coordinates(image, left_fit_average)
    # right_line = create_coordinates(image, right_fit_average)
    line1 = create_coordinates(image, line_averages[0])
    line2 = create_coordinates(image, line_averages[1])
    line3 = create_coordinates(image, line_averages[2])
    # return np.array([left_line, right_line])
    return np.array([line1, line2, line3])


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image

frame = img.copy()
canny_image = canny_edge_detector(frame)
cropped_image = region_of_interest(canny_image)
# cv2.imshow("cropped image", cropped_image)
lines = cv2.HoughLinesP(cropped_image, 1, np.pi / 180, 50, 
                        np.array([]), minLineLength = 5, 
                        maxLineGap = 40) 
lines_2 = cv2.HoughLines(cropped_image, 1, np.pi / 180, 50, 
                        np.array([]))
print("lines", lines)
print("lines_2", lines_2)
print("SIZES", len(lines), len(lines_2))
temp_img = img.copy()
for k in range(len(lines)):
    # if lines_2[k][0][1] > 1.39 and lines_2[k][0][1] < 1.74:
    #     continue
    a,b,c,d = lines[k][0]
    a = lines
    print(lines[k][0], colors[counter])
    cv2.line(temp_img, (a,b), (c,d), colors[counter], 3, cv2.LINE_AA)
    cv2.imshow("TEMP IMAGE", temp_img)
    cv2.waitKey(0) 
    counter = (counter + 1) % len(colors)

cv2.imshow("TEMP IMAGE", temp_img)
averaged_lines = average_slope_intercept(frame, lines, lines_2) 
line_image = display_lines(frame, averaged_lines)
combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

cv2.imshow("results", combo_image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 