# import the necessary packages
import cv2
import numpy as np
import matplotlib
import imutils

image1 = cv2.imread("stop_light3.jpg")
image = imutils.resize(image1, width=480)
cv2.imshow("RGB Image",image)

#corner = image[305:450, 170:310]
#cv2.imshow("Corner", corner)
#cv2.waitKey(0)

b,g,r = image[370,250]
bgr = [b, g, r]
print(bgr)
thresh = 10
hsv23 = [79, 253, 159]

#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
hsv1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print("hsv", hsv1)

minHSV = np.array([hsv23[0] - thresh, hsv23[1] - thresh, hsv23[2] - thresh])
maxHSV = np.array([hsv23[0] + thresh, hsv23[1] + thresh, hsv23[2] + thresh])
print(minHSV)
print(maxHSV)

maskHSV = cv2.inRange(hsv1, minHSV, maxHSV)

#cv2.imshow("Result HSV",resultHSV)
cv2.imshow("Mask HSV",maskHSV)
cv2.waitKey(0)

print("The program- was succesfully executed!")