import numpy as np
import cv2 as cv
import math

# read input
img = cv.imread("input/test.png")
hh, ww = img.shape[:2]

# specify input coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
input = np.float32([[136,113], [206,130], [173,207], [132,196]])

# get top and left dimensions and set to output dimensions of red rectangle
width = round(math.hypot(input[0,0]-input[1,0], input[0,1]-input[1,1]))
height = round(math.hypot(input[0,0]-input[3,0], input[0,1]-input[3,1]))
print("width:",width, "height:",height)

# set upper left coordinates for output rectangle
x = input[0,0]
y = input[0,1]

# specify output coordinates for corners of red quadrilateral in order TL, TR, BR, BL as x,
output = np.float32([[x,y], [x+width-1,y], [x+width-1,y+height-1], [x,y+height-1]])

# compute perspective matrix
matrix = cv.getPerspectiveTransform(input,output)
print(matrix)

# do perspective transformation setting area outside input to black
# Note that output size is the same as the input image size
imgOutput = cv.warpPerspective(img, matrix, (ww,hh), cv.INTER_LINEAR, borderMode=cv.BORDER_CONSTANT, borderValue=(0,0,0))

# save the warped output
cv.imwrite("output/output.jpg", imgOutput)

# show the result
cv.imshow("output", imgOutput)
cv.imshow("input", img)
cv.waitKey(0)
cv.destroyAllWindows() 