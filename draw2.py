import c8
import minifyImg
import cv2
import numpy as np
import os
import c16

CWD = os.path.dirname(os.path.abspath(__file__))

pixlels = [cv2.imread(os.path.realpath(os.path.join(CWD,f"./pixels/{x}.jpg"))) for x in range(8)]

def make(imgPath,w=37,h=22,blur=3):
    # print(f"img,imgFollow = minifyImg.make({imgPath},w,h,blur)")
    imgMini = minifyImg.make(imgPath,w,h,blur)
    # img8c,img8cFollow = c8.make(imgMini)
    img8cFollow = c16.make(imgMini)
    return img8cFollow

def draw(imgPath,w=37,h=22,blur=3):
    blank = np.zeros((h*20,w*20,3), dtype='uint8')
    blank.fill(255)

    imgFollow = make(imgPath,w,h,blur)
    startY = round((h - imgFollow.shape[0])/2)
    startX = round((w - imgFollow.shape[1])/2)
    for y in range(startY):
        for x in range(w):
            blank[y * 20:y * 20 + 20,x*20:x*20+20, :] = pixlels[0]
    for x in range(startX):
        for y in range(h):
            blank[y * 20:y * 20 + 20,x*20:x*20+20, :] = pixlels[0]
    for y in range(imgFollow.shape[0]):
        for x in range(imgFollow.shape[1]):
            X = x + startX
            Y = y + startY
            p = imgFollow[y,x]
            # print("p",p)
            # print(pixlels[p])
            # print(blank[y:y+20,x:x+20,:])
            blank[Y*20:Y*20+20,X*20:X*20+20,:] = pixlels[p]
    for y in range(startY + imgFollow.shape[0],h):
        for x in range(w):
            blank[y * 20:y * 20 + 20,x*20:x*20+20, :] = pixlels[0]
    for x in range(startX + imgFollow.shape[1],w):
        for y in range(h):
            blank[y * 20:y * 20 + 20,x*20:x*20+20, :] = pixlels[0]
    return blank

if __name__ == '__main__':
    # img,imgF = make("test4.png")
    # cv2.imshow("img",img)
    # print(imgF)
    # import time
    # t0 = time.perf_counter()
    img = draw("testimg/1.jpg",37*4,22 * 4,blur=0)
    cv2.imshow("img",img)
    cv2.imwrite("ooo.png",img)
    # t1 = time.perf_counter()
    # print(t1 - t0)
    cv2.waitKey(0)


