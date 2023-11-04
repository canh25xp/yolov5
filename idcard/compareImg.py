import cv2 as cv

cpp = cv.imread("cpp.png", cv.IMREAD_GRAYSCALE)
py = cv.imread("py.png", cv.IMREAD_GRAYSCALE)

diff = cpp - py

count = cv.countNonZero(diff)

print(count)
