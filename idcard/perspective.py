import cv2
from imutils import perspective

def perspectiveTranform(points : cv2.typing.MatLike, src = cv2.typing.MatLike) :
    h, w = src.shape[:2]
    epsilon = 0.1*cv2.arcLength(points, True)
    approx = cv2.approxPolyDP(points, epsilon, True)
    # print ("Simplified contour has ",len(approx),"points")

    corners = approx.squeeze()
    warped = perspective.four_point_transform(src, corners)
    return warped, corners
