import cv2 as cv
import numpy as np
import utils

#Read picture
src = cv.imread('test2.jpg')
height, width = src.shape[:2]
#Gauss noise reduction
src1 = cv.GaussianBlur(src,(5,5),0,0)
# cv.imshow('gaosi',src1)
#Grayscale processing
src2 = cv.cvtColor(src1,cv.COLOR_BGR2GRAY)
# cv.imshow('huidu',src2)
#Edge detection
lthrehlod = 50
hthrehlod =150
src3 = cv.Canny(src2,lthrehlod,hthrehlod)
# cv.imshow('bianyuan',src3)
#ROI delimit the interval and turn the non-this interval into black
# regin = np.array([[(0,660),(690,440),
# (1200,700),(src.shape[1],660)]]) #Why do you need two square brackets?
regin = np.array([[(0, 0), (src.shape[1], 0), (src.shape[1], src.shape[0] // 3), (0, src.shape[0] // 3)]])
regin = np.array([[
        [0, height // 3], [width, height // 3],[width, height], [0, height]
        ]])
mask = np.zeros_like(src3)
mask_color = 255   #src3The number of channels of the image is 1, and it is a grayscale image, so the color value is 0-255
cv.fillPoly(mask,regin,mask_color)
src4 = cv.bitwise_and(src3,mask)
# cv.imshow('bianyuan2',src4)
# cv.waitKey(0)

#Using the principle of Hough transformation to find the straight line composed of pixels in the above picture, and then draw it
rho = 1
theta = np.pi/180
threhold =50
minlength = 5
maxlengthgap = 40
lines = cv.HoughLinesP(src4,rho,theta,threhold,np.array([]),minlength,maxlengthgap)
#Drawing Line
linecolor =[0,255,255]
linewidth = 4
src5 = cv.cvtColor(src4,cv.COLOR_GRAY2BGR) #Converted to three-channel image




# Optimization
def choose_lines(lines, threhold):  # Filter points with large differences in slope
    slope = [(y2 - y1) / (x2 - x1) for line in lines for x1, x2, y1, y2 in line]
    while len(lines) > 0:
        mean = np.mean(slope)  # Average slope
        diff = [abs(s - mean) for s in slope]
        idx = np.argmax(diff)
        if diff[idx] > threhold:
            slope.pop(idx)
            lines.pop(idx)
        else:
            break
    return lines


lefts =[]
rights =[]
leftlength=[]
rightlength=[]
for line  in lines:
    for x1,y1,x2,y2 in line:
        #cv.line(src5,(x1,y1),(x2,y2),linecolor,linewidth)
        # Left and right lanes
        k = (y2-y1)/(x2-x1)
        length= ((y2-y1)**2+(x2-x1)**2)**0.5#Calculate the length of the line segment
        if k<0:
                lefts.append(line)
                leftlength.append(length)
        else:
                rights.append(line)
                rightlength.append(length)

# print(max(leftlength))
# print(max(rightlength))

if max(leftlength)>max(rightlength):
    text="The left-hand side is the solid line"
else:
    text="The right-hand side is the solid line"



def clac_edgepoints(points, ymin, ymax):  # Can be understood as finding the end of a line
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    k = np.polyfit(y, x, 1)
    func = np.poly1d(k)  # The equation is a function of y with respect to x, because the input ymin ymax. Xmin, xmax required

    xmin = int(func(ymin))
    xmax = int(func(ymax))

    return [(xmin, ymin), (xmax, ymax)]


good_leftlines = choose_lines(lefts, 0.1)  # Processed point
good_rightlines = choose_lines(rights, 0.1)

leftpoints = [(x1, y1) for left in good_leftlines for x1, y1, x2, y2 in left]
leftpoints = leftpoints + [(x2, y2) for left in good_leftlines for x1, y1, x2, y2 in left]
rightpoints = [(x1, y1) for right in good_rightlines for x1, y1, x2, y2 in right]
rightpoints = rightpoints + [(x2, y2) for right in good_rightlines for x1, y1, x2, y2 in right]

lefttop = clac_edgepoints(leftpoints, 500, src.shape[0])  # To draw the end points of the left and right lane lines
righttop = clac_edgepoints(rightpoints, 500, src.shape[0])

src6 = np.zeros_like(src5)

cv.line(src6, lefttop[0], lefttop[1], linecolor, linewidth)
cv.line(src6, righttop[0], righttop[1], linecolor, linewidth)

# cv.imshow('onlylane',src6)

#Image overlay
src7 = cv.addWeighted(src1,0.8,src6,1,0)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(src7,text,(100,100), font, 1,(255,255,255),2)
cv.imshow('Finally Image',src7)

cv.waitKey(0)
cv.destroyAllWindows()