import cv2 as cv

im1 = cv.imread("cpp.png", cv.IMREAD_GRAYSCALE)
im2 = cv.imread("runs/idcard/exp/test_0_mask.png", cv.IMREAD_GRAYSCALE)

diff = im1 - im2

count = cv.countNonZero(diff)

print(count)
