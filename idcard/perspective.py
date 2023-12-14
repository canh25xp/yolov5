import imp
import cv2
from imutils import perspective
from matplotlib import contour

def perspectiveTranform(points : cv2.typing.MatLike, src = cv2.typing.MatLike) :
    h, w = src.shape[:2]    
    # cv2.drawContours(contour, points, 0, (255,0,0), 3)
    print ("Contour has",len(points),"points")
    
    # rect = cv2.minAreaRect(points)
    # box = cv2.boxPoints(rect)
    # box = np.intp(box)
    # minRect = src.copy()
    # cv2.drawContours(minRect, [box], 0, (255,0,0), 3)
    
    hull = cv2.convexHull(points)
    # convexHull = src.copy()
    # cv2.drawContours(convexHull, [hull], 0, (255,0,0), 3)
    print ("Convex hull has ",len(hull),"points")
    
    epsilon = 0.1*cv2.arcLength(points, True)
    approx = cv2.approxPolyDP(points, epsilon, True)
    print ("Simplified contour has ",len(approx),"points")

    corners = approx.squeeze()
    warped = perspective.four_point_transform(src, corners)
    return warped, corners
