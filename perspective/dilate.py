import cv2 as cv
import numpy as np
from imutils import perspective

img = cv.imread("input/test2.png")
out = img.copy()

# threshold image
ret, thresh = cv.threshold(img, 127, 255, 0)

# dilate threshold image
kernel = np.ones((3,3), np.uint8)
dilated = cv.dilate(thresh, kernel, iterations=3)

# convert from BGR to grayscale (8UC1) format before finding contours. FindContours function only supports a grayscale image format.
dilated = cv.cvtColor(dilated, cv.COLOR_BGR2GRAY)

# find contours
contours, hierarchy = cv.findContours(dilated,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img, contours, 0, (0,0,255), 1)
print ("Contours:",len(contours))
print ("Largest contour has ",len(contours[0]),"points")

# minAreaRect
rect = cv.minAreaRect(contours[0])
box = cv.boxPoints(rect)
box = np.intp(box)
# cv.drawContours(img, [box], 0, (255,0,0), 1)

# convex hull (the smallest convex polygon containing all the given points)
hull = cv.convexHull(contours[0])
# cv.drawContours(img, [hull], 0, (255,0,0), 3)
print ("Convex hull has ",len(hull),"points")

# simplify contour
epsilon = 0.1*cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
# cv.drawContours(out, [approx], 0, (255,0,0), 3)
print ("Simplified contour has ",len(approx),"points")

points = approx.squeeze()
print (points)
warped = perspective.four_point_transform(out, points)

cv.imshow("input", img)
# cv.imshow("threshold", thresh)
# cv.imshow("dilated", dilated)
cv.imshow("output", warped)

cv.waitKey()
cv.destroyAllWindows()

