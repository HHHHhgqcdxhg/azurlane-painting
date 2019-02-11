import cv2
import numpy as np
cv = cv2

def edgeBlack(img,blur=3):
    blurred = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    if blur:
        blurred = cv.GaussianBlur(edge_output, (blur, blur), 0)
    else:
        blurred = edge_output
    ret, mask = cv2.threshold(blurred, 5, 255, cv2.THRESH_BINARY)
    black = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    blackCanny = cv2.bitwise_not(mask)
    blackCannyRGB = cv2.cvtColor(blackCanny, cv2.COLOR_GRAY2BGR)
    # cv.imshow("blackCannyRGB", blackCannyRGB)
    o = cv.add(img,black,mask=blackCanny)
    # cv.imshow("o", o)
    return o



def minify(img,W =37,H = 22):
    h, w,_ = img.shape
    wr = w / W
    hr = h / H
    if hr > wr:
        r = hr
        h = H
        w = round(w / r)
    else:
        r = wr
        h = round(h / r)
        w = W
    # cv2.imshow("imgaaa",img)
    img2 = cv2.resize(img, (w, h), cv2.INTER_AREA)
    # cv2.imshow("img2",img2)
    return img2

def make(img,w=37,h=22,blur=3):
    if isinstance(img,str):
        img = cv2.imread(img,-1)
    # print(img)
    # cv2.imshow("raw",img)
    if (img.shape[2]) == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    if blur:
        edgeBlackImg = edgeBlack(img,blur)
    else:
        edgeBlackImg = img
    out = minify(edgeBlackImg, w, h)
    return out

if __name__ == '__main__':
    img = cv.imread("test.png")
    edgeBlackImg = edgeBlack(img)
    out = minify(edgeBlackImg,92,55)
    # out = minify(edgeBlackImg)
    cv2.imwrite("out.png",out)
    cv.waitKey(0)
