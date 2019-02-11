import cv2, math
import numpy as np


class Draw:
    # @staticmethod
    # def rgb2hsv(r, g, b):
    #     r, g, b = r / 255.0, g / 255.0, b / 255.0
    #     mx = max(r, g, b)
    #     mn = min(r, g, b)
    #     df = mx - mn
    #     if mx == mn:
    #         h = 0
    #     elif mx == r:
    #         h = (60 * ((g - b) / df) + 360) % 360
    #     elif mx == g:
    #         h = (60 * ((b - r) / df) + 120) % 360
    #     # elif mx == b:
    #     else:
    #         h = (60 * ((r - g) / df) + 240) % 360
    #     if mx == 0:
    #         s = 0
    #     else:
    #         s = df / mx
    #     v = mx
    #     return h/255, s, v

    @staticmethod
    def rgb2hsv(r, g, b):
        mx = max(r, g, b)
        mn = min(r, g, b)
        v = max(r, g, b)
        s = (mx - mn) / mx
        if (r == mx):
            h = 60 * (g - b) / (mx - mn)
            # pass
        elif (g == mx):
            h = 60 * (b - r) / (mx - mn) + 120
        # if (b == mx):
        else:
            h = 60 * (r - g) / (mx - mn) + 240
        if (h < 0):
            h += 360
        return h/360, s, v/255

    @staticmethod
    def HSVDistance(hsv_1, hsv_2):
        H_1, S_1, V_1 = hsv_1
        H_2, S_2, V_2 = hsv_2
        h = 100 * math.cos(30 / 180 * math.pi)
        r = 100 * math.sin(30 / 180 * math.pi)
        x1 = r * V_1 * S_1 * math.cos(H_1 * 2 * math.pi)
        y1 = r * V_1 * S_1 * math.sin(H_1 * 2 * math.pi)
        z1 = h * (1 - V_1)
        x2 = r * V_2 * S_1 * math.cos(H_2 * 2 * math.pi)
        y2 = r * V_2 * S_1 * math.sin(H_2 * 2 * math.pi)
        z2 = h * (1 - V_2)
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        return dx ** 2 + dy ** 2 + dz ** 2

    @staticmethod
    def RGBDistance(rgb_1, rgb_2):
        # print("RGBDistance")
        r0,g0,b0 = rgb_1[0],rgb_1[1],rgb_1[2]
        r1,g1,b1 = rgb_2[0],rgb_2[1],rgb_2[2]
        dr = r0 - r1
        dg = g0 - g1
        db = b0 - b1
        r = (r0 + r1) / 2
        res = 2 * dr * dr + 4 * dg * dg + 3*db*db + (r * (dr *dr - db * db)) / 256
        return res
        # rmean = (r0 + r1 ) / 2
        # r = r0 - r1
        # g = g0 - g1
        # b = b0 - b1
        # rmean,r,g,b =  int(rmean),int(r),int(g),int(b)
        # return math.sqrt((((512 + rmean) * r * r) >> 8) + 4 * g * g + (((767 - rmean) * b * b) >> 8))


        # return sum(((rgb_1[x] - rgb_2[x]) ** 2 for x in range(3)))

    def findNearestColorFromRGBRaw(self, rgb):
        # print(rgb[:3] == (255,211,115))
        if rgb.__len__() == 4 and rgb[-1] == 0:
            return 1
        if rgb.__len__() == 4:
            rgb = rgb[:3]
        nearestI = 0
        nearesrDistance = self.RGBDistance(rgb, self.colorsI[0])
        for i in range(1, self.colorsI.__len__() - 1):
            d = self.RGBDistance(rgb, self.colorsI[i])
            if d < nearesrDistance:
                nearestI = i
                nearesrDistance = d
        # if(rgb[0] == 255 and rgb[1] ==211 and rgb[2] ==115):
        if(rgb[0] == 255):
            print(rgb)
            print(nearestI)
        return nearestI

    def findNearestColor(self, hsv):
        minKey = 0
        minValue = self.HSVDistance(hsv, self.colorsHSVI[0])
        for k in range(1, self.colorsHSVI.__len__()):
            v = self.colorsHSVI[k]
            distance = self.HSVDistance(hsv, v)
            if distance < minValue:
                minValue = distance
                minKey = k
        return minKey

    def findNearestColorFromRGBA(self, color):
        if color.__len__() == 4:
            a = color[3]
            if a == 0:
                return self.colorsI.__len__() - 1
            else:
                r, g, b, _ = color
        else:
            r, g, b = color
        hsv = self.rgb2hsv(r, g, b)
        return self.findNearestColor(hsv)

    def __new__(cls, *args, **kwargs):
        cls.colors = {
            "black": (49, 40, 41),
            "white": (255, 255, 255),
            "yellow": (255, 211, 115),
            "green": (115, 255, 173),
            "blue": (115, 130, 255),
            "red": (247, 105, 90),
            "pink": (255, 215, 198),
            "gray": (181, 174, 165)
        }

        def _(color, pos=(0, 0), cls=cls):
            if isinstance(color, str):
                color = cls.colors[color]
            if isinstance(color, int):
                color = cls.colorsI[color]
            pixels = np.zeros((20, 20, 3), dtype=np.uint8)
            pixels[:, :, :3] = color
            return pixels

        cls.drawOne = _

        cls.colors = {k: np.array(v) for k, v in cls.colors.items()}
        # print("colors", cls.colors)
        cls.colorsI = [cls.colors[c] for c in cls.colors]
        # print("colorsI", cls.colorsI)
        # cls.colorsHSV = {k: cls.rgb2hsv(v[0], v[1], v[2]) for k, v in cls.colors.items()}
        # cls.colorsHSVI = [cls.colorsHSV[c] for c in cls.colorsHSV]

        # print("colors", cls.colors)
        # print("colorsI", cls.colorsI)

        cls.pixels = {k: cls.drawOne(v) for k, v in cls.colors.items()}
        cls.pixelsI = [cls.pixels[p] for p in cls.pixels]
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        pass

    def analyseImg(self, img):
        if isinstance(img, str):
            if img[-3:] == "png":
                img = cv2.imread(img, -1)
            else:
                img = cv2.imread(img)
        h, w, _ = img.shape
        wr = w / 37
        hr = h / 22
        if hr > wr:
            r = hr
            h = 22
            w = round(w / r)
        else:
            r = wr
            h = round(h / r)
            w = 37
        img = cv2.resize(img, (w, h), cv2.INTER_AREA)
        # cv2.imshow("rawIm",img)
        imgFollow = np.zeros((22, 37), dtype=np.uint8)
        imgFollow.fill(self.colorsI.__len__() - 1)
        # print(imgFollow)
        presetX = math.floor((37 - w) / 2)
        presetY = math.floor((22 - h) / 2)
        for x in range(w):
            for y in range(h):
                # pNearest = self.findNearestColorFromRGBA(img[y, x])
                pNearest = self.findNearestColorFromRGBRaw(img[y, x,::-1])
                # print(pNearest)
                # print(self.colorsI[pNearest])
                imgFollow[presetY + y, presetX + x] = pNearest
                r, g, b = self.colorsI[pNearest]
                img[y, x, :3] = (r, g, b)
                # print(img[y, x, :3])
                # print(imgFollow[presetY + y, presetX + x])
        return img, imgFollow

    def smallImgToCanvas(self, img):
        target = np.zeros((440, 740, 3))
        target[:20, :20, :] = (255, 0, 0)
        cv2.imshow("tmp", target)
        return target

    def imgFollow2Canvas(self, imgFollow):
        target = np.zeros((440, 740, 3), dtype=np.uint8)
        for y in range(22):
            for x in range(37):
                # print("self.pixelsI[int(imgFollow[y, x])]",self.pixelsI[int(imgFollow[y, x])])
                target[y * 20:(y * 20 + 20), x * 20:x * 20 + 20] = self.pixelsI[int(imgFollow[y, x])]
                # print("target[y * 20:(y * 20 + 20), x * 20:x * 20 + 20]",target[y * 20:(y * 20 + 20), x * 20:x * 20 + 20])

        # print(target[:,8:10,:])
        # cv2.imshow("tmpb", target)
        # target[:, :, :] = target[:, :, :]
        # print(target[15:20,8:10,:])
        # cv2.imshow("tmpa", target)
        return target

    def colorDef(self):
        pass


draw = Draw()
if __name__ == '__main__':
    # print(draw)
    # print(draw.colorsHSV)
    im, imFollow = draw.analyseImg("test6.png")
    cv2.imwrite("im.jpg", im)
    # print(im)
    # cv2.imshow("im", cv2.resize(im, (785, 783)))
    # print(imFollow)
    img = draw.imgFollow2Canvas(imFollow)
    cv2.imwrite("out.png", img)
    cv2.imshow("out.png", img)
    cv2.imshow("out2.png", img[:, :, ::-1])
    # cv2.imshow("x",draw.pixelsI[7])
    # print(draw.findNearestColorFromRGBRaw((253, 197, 210)))
    cv2.waitKey(0)
    # print(draw.rgb2hsv(255,2,198))
    # print(imFollow)

    # print(draw.smallImgToCanvas(im))
    # c = draw.findNearestColorFromRGBA((255,255,255))
    # print(c)
# # 图片的分辨率为200*300，这里b, g, r设为随机值，注意dtype属性
# b = np.random.randint(0, 255, (200, 300), dtype=np.uint8)
# print(b)
# g = np.random.randint(0, 255, (200, 300), dtype=np.uint8)
# r = np.random.randint(0, 255, (200, 300), dtype=np.uint8)
#
# # 合并通道，形成图片
# img = cv2.merge([b, g, r])
#
# # 显示图片
# cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyWindow('test')
