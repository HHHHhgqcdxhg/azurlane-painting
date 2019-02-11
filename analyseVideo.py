import cv2
import numpy as np
import time
import paint
import draw
import draw2

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
# cap = cv2.VideoCapture('videos/点兔S1NCOP.mp4')
# cap = cv2.VideoCapture('videos/mezy.flv')
# cap = cv2.VideoCapture('videos/ssNCOP.mkv')
# cap = cv2.VideoCapture('videos/wy2.mp4')
cap = cv2.VideoCapture('videos/chm.flv')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
i = 0
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # print(frame)
    # if i % 2 == 0:
    try:
      # cv2.imwrite(f"outputs/mezy_raw/raw/{i}_raw.jpg", frame)
      # o = paint.drawRandBg(frame,blur=None)
      # o = paint.draw4mult(frame,blur=None)
      o = paint.drawRandBg(frame,blur=None)
      # o = draw2.draw(frame,37*4,22 * 4,blur=0)
      # cv2.imwrite(f"outputs/ss/{i}.png",o)
      o.save(f"outputs/chm/{i}.png","PNG")
    except:
      pass
    i += 1
    # Display the resulting frame
    # cv2.imshow('Frame',frame)
    # time.sleep(5)

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
