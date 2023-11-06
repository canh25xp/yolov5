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


if __name__ == '__main__':
    img_path = 'data/images/idcard.jpg'
    txt_path = 'runs/idcard/exp/labels/idcard.txt'
    
    img = cv2.imread(img_path)
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        labels =  line.split()
    
    class_index = labels[0]
    conf = labels[1]
    x,y,w,h = labels[2:6]
    segment = labels[6:]
    
    count = len(segment)
    
    pairs = []
    for i in range((int)(count/2)):
        pairs.append([(int)(segment[2*i]), (int)(segment[2*i+1])])
        
    segment = np.array(pairs, np.int32)
    
    result, angle = getRotateRectImg(pairs, img)
    
    print(angle)
   
    