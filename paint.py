from draw2 import draw
from PIL import Image
import cv2
import copy
import os
import numpy as np
import random

CWD = os.path.dirname(os.path.abspath(__file__))
# generalPic = Image.open("blhx_raw/general.jpg").convert("RGB")
leftPath = os.path.realpath(os.path.join(CWD, "./blhx_raw/left"))
rightPath = os.path.realpath(os.path.join(CWD, "./blhx_raw/right"))
leftPics = [Image.open(os.path.join(leftPath, l)).convert("RGB") for l in os.listdir(leftPath)]
rightPics = [Image.open(os.path.join(rightPath, l)).convert("RGB") for l in os.listdir(rightPath)]
u = Image.open(os.path.realpath(os.path.join(CWD, "./blhx_raw/up.jpg"))).convert("RGB")
d = Image.open(os.path.realpath(os.path.join(CWD, "./blhx_raw/down.jpg"))).convert("RGB")


# def drawGeneral(imgPath, w=37, h=22, blur=3):
#     target = copy.copy(generalPic)
#     paint = draw(imgPath, w, h, blur)
#     # print(paint)
#     # cv2.imshow("paint",paint)
#     paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
#     paint_pil = Image.fromarray(paint.astype('uint8')).convert('RGB')
#
#     target.paste(paint_pil, (278, 109, 1018, 549))
#     # target.show()
#     return target


def drawRandBg(imgPath, w=37, h=22, blur=3):
    target = Image.new("RGB", (1280, 720))
    l = random.sample(leftPics, 1)[0]
    r = random.sample(rightPics, 1)[0]

    paint = draw(imgPath, w, h, blur)
    # print(paint)
    # cv2.imshow("paint",paint)
    # paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
    paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
    paint_pil = Image.fromarray(paint.astype('uint8')).convert('RGB')
    target.paste(l, (0, 0, 278, 720))
    target.paste(paint_pil, (278, 109, 1018, 549))
    target.paste(r, (1018, 0, 1280, 720))
    target.paste(u, (278, 0, 1019, 109))
    target.paste(d, (278, 550, 1019, 720))
    return target


def draw4mult(imgPath, blur=0):
    # target = Image.new("RGB", (1280 * 4, 720 * 4), "white")
    target = Image.new("RGB", (3238 + 262, 2040), "white")
    ls = random.sample(leftPics, 4)
    rs = random.sample(rightPics, 4)

    paint = draw(imgPath, 37 * 4, 22 * 4, blur)
    # print(paint)
    # cv2.imshow("paint",paint)
    # paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
    paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
    paint_pil = Image.fromarray(paint.astype('uint8')).convert('RGB')
    for x in range(4):
        target.paste(ls[x], (0, 440 * x, 278, 440 * x + 720))
        target.paste(rs[x], (3238, 440 * x, 3238 + 262, 440 * x + 720))
        target.paste(u, (278 + 741 * x, 0, 1019 + 741 * x, 109))
        # target.paste(d, (278 + 741 * x, 550, 1019 + 741 * x, 720))
        target.paste(d, (278 + 741 * x, 1870, 1019 + 741 * x, 2040))

    # target.paste(l, (0, 0, 278, 720))
    target.paste(paint_pil, (278, 109, 278 + 2960, 109 + 1760))
    # target.paste(r, (1018, 0, 1280, 720))
    # target.paste(u, (278, 0, 1019, 109))
    # target.paste(d, (278, 550, 1019, 720))
    return target


def randGetList(L: list):
    max = L.__len__() - 1
    r = random.randint(0, max)
    return L[r]


def drawN(imgPath, w=1, h=1, blur=0):
    """

    :param imgPath:输入图片的路径
    :param w:横向画板数
    :param h:纵向画板数
    :param blur:控制线条加粗,设为0的话不做加粗处理.不为0的话只能填单数,即1,3,5,7等.某些情况下线条加粗比较符合像素风,请按需取用
    :return: PIL图片对象
    """
    target = Image.new("RGB", (37 * 20 * w + 278 + 262, 22 * 20 * h + 110 + 170), "white")
    paint = draw(imgPath, 37 * w, 22 * h, blur)
    paint = cv2.cvtColor(paint, cv2.COLOR_BGR2RGB)
    paint_pil = Image.fromarray(paint.astype('uint8')).convert('RGB')

    lEdge = 278
    rEdge = 278 + 37 * 20 * w
    uEdge = 110
    dEdge = 22 * 20 * h + 110

    for x in range(w):
        target.paste(u, (278 + 741 * x, 0, 1019 + 741 * x, 109))
        target.paste(d, (278 + 741 * x, dEdge, 1019 + 741 * x, dEdge + 170))
    for y in range(h):
        target.paste(randGetList(leftPics), (0, 440 * y, 278, 440 * y + 720))
        target.paste(randGetList(rightPics), (rEdge, 440 * y, rEdge + 262, 440 * y + 720))
    target.paste(paint_pil, (lEdge, uEdge, rEdge, dEdge))
    return target


if __name__ == '__main__':
    # out = drawRandBg("testimg/D{AH`3(ZX0GOUZ4]G]A)LG3.png")
    # out = draw4mult("testimg/54_raw.jpg")
    # print("out")
    # out.show()
    # cv2.waitKey(0)
    import os
    t = drawN("C:\yuno.jpeg",5,5)
    t.show()
    # P = r'J:\projects\python_projects\zl-panting\outputs\chm'
    # op = r'J:\projects\python_projects\zl-panting\outputs\chm\o'
    # for x in range(13):
    #     out = drawRandBg(os.path.join(P, f"{x}.png"), blur=0)
    #     out.save(os.path.join(op, f"{x}.png"), "PNG")
        # cv2.imwrite(,out)
