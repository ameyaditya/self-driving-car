import numpy as np
import cv2

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

img=cv2.imread('test3.jpg')

kernel1 = np.ones((1,3),np.uint8)
kernel2 = np.ones((3,3),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBW=cv2.threshold(imgGray, 50, 200, cv2.THRESH_BINARY_INV)[1]
img1=cv2.erode(imgBW, kernel1, iterations=1)
img2=cv2.dilate(img1, kernel2, iterations=3)
img3 = cv2.bitwise_and(imgBW,img2)
img3= cv2.bitwise_not(img3)
img4 = cv2.bitwise_and(imgBW,imgBW,mask=img3)
img_temp = region_of_interest(img4)
cv2.imshow("THRESH", img_temp)
cv2.waitKey(0)
imgLines= cv2.HoughLinesP(img_temp,15,np.pi/180,10, minLineLength = 5, maxLineGap = 5)
print(imgLines)
for i in range(len(imgLines)):
    for x1,y1,x2,y2 in imgLines[i]:
        cv2.line(img_temp,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('Final Image with dotted Lines detected', img_temp)
cv2.waitKey(0)