from panorama import Stitcher
import argparse
import cv2
import imutils

# Read images
#imageA = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\one.jpg')
#imageB = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\two.jpg')

cap1 = cv2.VideoCapture(1) # use 0 if you only have front facing camera
ret, imageA = cap1.read() #read one frame


cap2 = cv2.VideoCapture(2) # use 0 if you only have front facing camera
ret, imageB = cap2.read() #read one frame

imageA = cv2.flip(imageA, 1)
imageB = cv2.flip(imageB, 1)

# Resize images
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# Stitch the images together to create a panorama
stitcher = Stitcher()
result = stitcher.stitch([imageA, imageB])

# Check if stitching was successful

   

    
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)   
cv2.imshow("Result", result)
cv2.waitKey(0)

