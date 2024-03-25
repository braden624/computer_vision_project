from panorama import Stitcher
import argparse
import cv2
import imutils

# Read images
imageA = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\one.jpg')
imageB = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\two.jpg')

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

