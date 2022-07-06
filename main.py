import cv2
import numpy as np
import pyautogui
import os

#os.system("sudo apt-get install scrot")

SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("video.avi", fourcc, 20.0, (SCREEN_SIZE))


while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break


cv2.destroyAllWindows()
out.release()


