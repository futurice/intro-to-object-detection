"""
Display image with opencv

OpenCV image display is more convenient than the one from dlib since it does not require x11 on OSX.
"""

import cv2

# To display an image file
img = cv2.imread('image file path')
cv2.imshow('frame title', img)
cv2.waitKey(0) # This line is needed for the image window to display. It also returns a value of pressed key.
