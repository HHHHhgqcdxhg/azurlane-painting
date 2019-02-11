import os,cv2



leftArea = (0,0,278,720)
rightArea = (1018,0,1280,720)

def cut(img,area):
    return img[area[1]:area[3],area[0]:area[2]]

CWD = os.path.dirname(os.path.abspath(__file__))
imgDPath = os.path.realpath(os.path.join(CWD,"./blhx_raw/tmp"))

imgsPath = os.listdir(imgDPath)

leftPath = os.path.realpath(os.path.join(CWD,"./blhx_raw/left"))
rightPath = os.path.realpath(os.path.join(CWD,"./blhx_raw/right"))
i = 0
for imgPath in imgsPath:
    imgRealPath = os.path.join(imgDPath, imgPath)
    if "left" in imgPath or "right" in imgPath:
        os.remove(imgRealPath)
        continue

    img = cv2.imread(imgRealPath)
    left = cut(img,leftArea)
    right = cut(img,rightArea)
    cv2.imwrite(os.path.join(leftPath,f"{i}.jpg"), left)
    cv2.imwrite(os.path.join(rightPath,f"{i}.jpg"), right)
    i += 1


