import cv2
import numpy as np
import argparse

def main(args):
    print(args.source)
    input = cv2.imread(args.source)
    
    ret, thresh = cv2.threshold(input, 127, 255, 0)
    cv2.imshow("input", input)
    cv2.imshow("thresh", thresh)
    cv2.waitKey()
    cv2.destroyAllWindows()
    

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default= 'input/warp_perspective/cccd_back_1.jpg', help='input images')
    args = parser.parse_args()
    main(args)