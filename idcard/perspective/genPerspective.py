import cv2 as cv
import numpy as np
from imutils import perspective
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]

dir = Path(ROOT/"input/autogen").glob('*.jpg')
output = Path(ROOT/"output/expanded")

output.mkdir(exist_ok=True)

BORDER = 100

title_window = "output"


def on_trackbar(val):
    cv.imshow(title_window, expanded)


if(__name__ == '__main__'):
    for file in dir:
        img = cv.imread(str(file))
        expanded = cv.copyMakeBorder(img, BORDER, BORDER, BORDER, BORDER, cv.BORDER_CONSTANT)
        cv.imwrite(str(output/file.name), expanded)