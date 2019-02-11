import cv2
import numpy as np
import colormath
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from functools import lru_cache

import time

import c16

cs_rgb = [
    [49, 40, 41],
    [255, 255, 255],
    [255, 211, 115],
    [115, 255, 173],
    [115, 130, 255],
    [247, 105, 90],
    [255, 215, 198],
    [181, 174, 165]
]


def color_diff(x, y):
    color1_rgb = sRGBColor(x[2], x[1], x[0], is_upscaled=True)
    color2_rgb = sRGBColor(y[0], y[1], y[2], is_upscaled=True)

    color1_lab = convert_color(color1_rgb, LabColor)
    color2_lab = convert_color(color2_rgb, LabColor)
    return delta_e_cie2000(color1_lab, color2_lab)


@lru_cache(65535)
def to8color(x, y, z):
    # print(x,y,z)
    ret = [0, 0, 0]
    min_d = 1145141919810
    miniI = 0
    for i,c in enumerate(cs_rgb):
        t = color_diff([x, y, z], c)
        if t < min_d:
            min_d = t
            ret = c
            miniI = i
    return np.array(ret[::-1], dtype='uint8'),miniI


def make(img):
    if isinstance(img, str):
        img = cv2.imread(img, -1)
    if (img.shape[2]) == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img = c16.make(img, 16)
    # cv2.imshow("img16",img)
    # print(img.shape)
    img *= 255
    imgLen = img.shape[0] * img.shape[1]
    # print(img.shape[0] * img.shape[1])
    img2Arr = []
    img2ArrFollow = []
    for x in img.reshape(imgLen, 3):
        color,i = to8color(x[0], x[1], x[2])
        img2Arr.append(color)
        img2ArrFollow.append(i)
    img2ArrFollow = np.array(img2ArrFollow).reshape(img.shape[:2])
    img2 = np.array(img2Arr, dtype='uint8').reshape(img.shape)
    # img2 = np.array([to8color(x[0],x[1],x[2]) for x in img.reshape(imgLen, 3)], dtype='uint8').reshape(img.shape)
    # cv2.imwrite('sysfout12.png', img2)
    return img2,img2ArrFollow


if __name__ == '__main__':
    t0 = time.perf_counter()
    # img = cv2.imread("output12.bmp", -1)
    # if (img.shape[2]) == 4:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    # print(img.shape)
    # print(img.shape[0] * img.shape[1])
    # img2 = np.array([to8color(x[0], x[1], x[2]) for x in img.reshape(-1, 3)]).reshape(img.shape)
    # cv2.imwrite('sysfout12.png', img2)
    img8 = make("test.png")
    cv2.imshow("img8", img8)
    print(time.perf_counter() - t0)
    cv2.waitKey(0)
