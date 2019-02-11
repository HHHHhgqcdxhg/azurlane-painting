import cv2,os

VideoWriter = cv2.VideoWriter(
    "./chm.avi",
    cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 15,
    (1280, 720))

CWD = os.path.dirname(os.path.abspath(__file__))

videoPicsPath = os.path.realpath(os.path.join(CWD,"outputs/chm/o"))

ps = [cv2.imread(os.path.join(videoPicsPath,f"{x}.png")) for x in range(13)]

for f in range(2158):
    # if not f % 2 == 0:
    #     continue
    print(f)
    # im = cv2.imread(os.path.join(videoPicsPath,f"{f}.png"))
    VideoWriter.write(ps[f%13])
VideoWriter.release()
cv2.destroyAllWindows()





