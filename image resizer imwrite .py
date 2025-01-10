import cv2
import os

# Load the image 
image = cv2.imread(r"c:\Users\Win\Documents\download (3).jfif") 

# Check if the image was loaded successfully
    # Display the image
cv2.imshow("Image", image)

    # Wait for a key press
cv2.waitKey(0)
cv2.imwrite("savedImage.jfif",image)
print(f"image saved to {"savedImage.jfif"}")
#to check the image has saved successfully we have to use this module 
if os.path.exists("savedImage"):
    print("image saved successfully")
else:
    print("image is not saved at specified location successfully")

    # Close all windows
cv2.destroyAllWindows()