import numpy as np
import cv2

from sklearn.cluster import KMeans

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

def get_average_slope_intercept(lines, cluster_size = 2):
    fits = [[i[1], i[2]] for i in lines]   
    
    kmeans = KMeans(n_clusters = cluster_size, random_state = 0, max_iter = 10).fit(np.array(fits))
    line_averages = kmeans.cluster_centers_
    return line_averages