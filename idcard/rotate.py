import cv2
import numpy as np
import math

def getRotateRectImg(points : cv2.typing.MatLike, src = cv2.typing.MatLike) :
    h, w = src.shape[:2]
    center, size, angle = cv2.minAreaRect(points) # rotated rect
    width, height = size
    if(width < height): 
        width, height = height, width
        angle = angle - 90
    radAngle = -angle*math.pi/180
    sinA = math.sin(radAngle)
    cosA = math.cos(radAngle)
    affineMatrix = np.array([[cosA, -sinA, width / 2 - cosA * center[0] + sinA * center[1]],
                             [sinA, cosA, height / 2 - cosA * center[1] - sinA * center[0]]])
    # affineMatrix = cv2.getRotationMatrix2D(center, angle, 1)
    result = cv2.warpAffine(src, affineMatrix, (round(width),round(height)))
    return result, angle
