import cv2 as cv
import numpy as np
from imutils import perspective
from pathlib import Path
import os
import argparse

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]

def main(args):
    inputPath = Path(args.source)
    outputPath = Path("output/"+inputPath.stem)

    maskPath = "warp_perspective/mask/"+ inputPath.name
    
    outputPath.mkdir(exist_ok=True)
        
    img = cv.imread(str(inputPath))
    mask = cv.imread(maskPath, cv.COLOR_BGR2GRAY)
    out = img.copy()
    
    ret, mask = cv.threshold(mask, 127, 255, cv.THRESH_BINARY)
    
    pixels = cv.countNonZero(mask)
    
    print(pixels)
    
    height, width, channel = img.shape
    
    print(img.shape)
    
    print(height * width)

    # # dilate threshold image
    # kernel = np.ones((3,3), np.uint8)
    # dilated = cv.dilate(mask, kernel, iterations=3)
    # cv.imwrite(outputPath+"/dilated.jpg",dilated)

    # # find contours
    # contours, hierarchy = cv.findContours(dilated,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # contour = img.copy()
    # cv.drawContours(contour, contours, 0, (255,0,0), 3)
    # print ("Contours:",len(contours))
    # print ("Largest contour has ",len(contours[0]),"points")
    # cv.imwrite(outputPath+"/contour.jpg",contour)

    # # # minAreaRect
    # # rect = cv.minAreaRect(contours[0])
    # # box = cv.boxPoints(rect)
    # # box = np.intp(box)
    # # rect = img.copy()
    # # cv.drawContours(rect, [box], 0, (255,0,0), 3)
    # # cv.imwrite(outputPath+"/minRect.jpg",rect)

    # # # convex hull (the smallest convex polygon containing all the given points)
    # # hull = cv.convexHull(contours[0])
    # # # cv.drawContours(img, [hull], 0, (255,0,0), 3)
    # # print ("Convex hull has ",len(hull),"points")

    # # simplify contour
    # epsilon = 0.1*cv.arcLength(contours[0], True)
    # approx = cv.approxPolyDP(contours[0], epsilon, True)
    # quadrilateral = img.copy()
    # cv.drawContours(quadrilateral, [approx], 0, (255,0,0), 3)
    # print ("Simplified contour has ",len(approx),"points")
    # cv.imwrite(outputPath+"/quadrilateral.jpg",quadrilateral)

    # points = approx.squeeze()
    # print (points)
    # warped = perspective.four_point_transform(out, points)
    # cv.imwrite(outputPath+"/warped.jpg",warped)

    # cv.imshow("input", img)
    # cv.imshow("mask", mask)
    # # cv.imshow("warped", warped)
    # # cv.imshow("dilated", dilated)

    # cv.waitKey()
    # cv.destroyAllWindows()

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default= ROOT/'input/warp_perspective/cccd_back_1.jpg', help='input path')
    parser.add_argument('--save', action='store_true', help='save images')
    args = parser.parse_args()
    main(args)