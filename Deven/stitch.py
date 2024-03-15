from panorama import Stitcher
import argparse
import cv2
import imutils

# Read images
imageA = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\IMG_2355.jpg')
imageB = cv2.imread(r'C:\Users\Deven Mills\Documents\OU Spring 2024\ECE-5973-Computer_Vision\Project\Code\computer_vision_project\Deven\IMG_2356.jpg')

# Resize images
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# Stitch the images together to create a panorama
stitcher = Stitcher()
result = stitcher.stitch([imageA, imageB], showMatches=True)

# Check if stitching was successful
if result is not None:
    (result, vis) = result

    # Show the images
    cv2.imshow("Image A", imageA)
    cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    cv2.imshow("Result", result)
    cv2.waitKey(0)
else:
    print("Stitching failed. Unable to create panorama.")
