import numpy as np
import cv2


img = cv2.imread("test2.jpg")

def convert_hsl(image):
    """
    Convert RGB images to HSL.
        Parameters:
            image: An np.array compatible with plt.imshow.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2HLS)


def RGB_color_selection(image):
    """
    Apply color selection to RGB images to blackout everything except for white and yellow lane lines.
        Parameters:
            image: An np.array compatible with plt.imshow.
    """
    lower_threshold = np.uint8([0, 0, 0])
    upper_threshold = np.uint8([80, 80, 80])
    black_mask = cv2.inRange(image, lower_threshold, upper_threshold)
    
    masked_image = cv2.bitwise_and(image, image, mask = black_mask)
    
    return masked_image

def HSL_color_selection(image):
    """
    Apply color selection to the HSL images to blackout everything except for white and yellow lane lines.
        Parameters:
            image: An np.array compatible with plt.imshow.
    """
    #Convert the input image to HSL
    converted_image = convert_hsl(image)
    
    lower_threshold = np.uint8([0, 0, 0])
    upper_threshold = np.uint8([80, 80, 80])
    black_mask = cv2.inRange(image, lower_threshold, upper_threshold)
    
    masked_image = cv2.bitwise_and(image, image, mask = black_mask)
    
    return masked_image

def gray_scale(image):
    """
    Convert images to gray scale.
        Parameters:
            image: An np.array compatible with plt.imshow.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def gaussian_smoothing(image, kernel_size = 3):
    """
    Apply Gaussian filter to the input image.
        Parameters:
            image: An np.array compatible with plt.imshow.
            kernel_size (Default = 13): The size of the Gaussian kernel will affect the performance of the detector.
            It must be an odd number (3, 5, 7, ...).
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def canny_detector(image, low_threshold = 50, high_threshold = 150):
    """
    Apply Canny Edge Detection algorithm to the input image.
        Parameters:
            image: An np.array compatible with plt.imshow.
            low_threshold (Default = 50).
            high_threshold (Default = 150).
    """
    return cv2.Canny(image, low_threshold, high_threshold)

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

new_img = HSL_color_selection(img)
new_img = gray_scale(new_img)
new_img = gaussian_smoothing(new_img)
new_img = canny_detector(new_img)
new_img = region_of_interest(new_img)

lines = cv2.HoughLinesP(new_img, 1, np.pi / 180, 50, 
                        np.array([]), minLineLength = 5, 
                        maxLineGap = 40)
# new_img = convert_hsl(new_img)
cv2.imshow("image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()