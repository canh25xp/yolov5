import cv2
import numpy as np
import math
import imutils


src = cv2.imread("data/images/autogen/cccdc_front_2.jpg")
bg = np.zeros((720,1280,3), dtype="uint8")
rotated = imutils.rotate_bound(src, 30)
h,w,c = rotated.shape
dst_w = 1280
dst_h = 960
w_off = dst_w - w
h_off = dst_h - h
dst = cv2.copyMakeBorder(rotated, 0, h_off, w_off, 0, cv2.BORDER_CONSTANT)
# cv2.imshow("rotated", rotated)
# cv2.imshow("bg",bg)
# cv2.imshow("dst", dst)
cv2.imwrite("test_960.jpg", dst)
cv2.waitKey(0)
