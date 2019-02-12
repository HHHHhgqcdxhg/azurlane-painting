import cv2
import numpy as np
import time
import paint
# import draw
# import draw2


def old():
    cap = cv2.VideoCapture('videos/chm.flv')
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            try:
                o = paint.drawRandBg(frame, blur=None)
                o.save(f"outputs/chm/{i}.png", "PNG")
            except:
                pass
            i += 1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def makeVideo(inputVideoPath: str, output: str, cutFrames: int = 1, w: int = 1, h: int = 1, blur: int = 0):
    """
    :param input:输入视频的路径
    :param output:输出视频的路径,请以".avi"结尾
    :param cutFrames:抽帧频率,比如填1的话,则原视频每一帧都会处理后加入新视频中;填2的话,原视频每2帧会有一帧处理后加入新视频中
    :param w:横向画板数
    :param h:纵向画板数
    :param blur:控制线条加粗,设为0的话不做加粗处理.不为0的话只能填单数,即1,3,5,7等.某些情况下线条加粗比较符合像素风,请按需取用
    :return:
    输出的视频没有音频轨道没有原视频对比,请放入其他剪辑软件中自行添加.另,如果w和h调的特别大的话,视频分辨率会超级高.
    """
    inVideo = cv2.VideoCapture(inputVideoPath)
    inFps = inVideo.get(cv2.CAP_PROP_FPS)
    outFps = inFps / cutFrames
    framesCount = int(inVideo.get(cv2.CAP_PROP_FRAME_COUNT))

    outVideo = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), outFps,
                               (37 * 20 * w + 278 + 262, 22 * 20 * h + 110 + 170))
    if (inVideo.isOpened() == False):
        print("Error opening video stream or file")
    i = 0
    while (inVideo.isOpened()):
        ret, frame = inVideo.read()
        if ret == True:
            if i % cutFrames == 0:
                try:
                    o = paint.drawN(frame,w=w,h=h, blur=blur)
                    img = cv2.cvtColor(np.asarray(o), cv2.COLOR_RGB2BGR)
                except:
                    pass
                else:
                    outVideo.write(img)
                print(f"{i:>10} of {framesCount} frames handdled")
            i += 1
        else:
            break
    inVideo.release()
    outVideo.release()


if __name__ == '__main__':
    makeVideo("videos/sjw.mp4", "sjw.avi",1,4,4)



