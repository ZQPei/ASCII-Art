import numpy as np
import cv2
import os

import time 
time.sleep(5)
vdo = cv2.VideoCapture("F:/Downloads/The.Incredibles.2004.BluRay.iPad.720p.AAC.4Audio.x264-HDSPad/The.Incredibles.2004.BluRay.iPad.720p.AAC.4Audio.x264-HDSPad.mp4")
#vdo.set(cv2.CAP_PROP_POS_FRAMES,20000)
while vdo.grab():
    os.system("cls")
    _,im = vdo.retrieve()
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im = cv2.resize(im,(120,45))
    im2 = np.zeros_like(im,dtype=np.uint8)
    im2[im<64] = 0
    im2[im>=64] = 1
    im2[im>=128] = 2
    im2[im>=192] = 3
    for i in im2:
        for j in i:
            print(" " if j==0 else "." if j==1 else "*" if j==2 else "@", end="")
        print()
