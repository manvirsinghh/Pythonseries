# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r'c:\Users\Win\Documents\download (2).jfif'

# Reading an image in default mode
image = cv2.imread(path) #to show image as it is  we use this line of code
# for showing image in gray color we use 0  along with path  or to add cv.IMREAD_GRAYSCALE to get gray image 
# by default the way the image is read as cv.IMREAD_COLOR

# Window name in which image is displayed


# Using cv2.imshow() method
# Displaying the image
cv2.imshow("image", image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
