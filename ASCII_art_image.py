import numpy as np
import cv2

im = cv2.imread("zz.jpg",0)
im = cv2.resize(im,(128,84))
im2 = np.zeros_like(im,dtype=np.uint8)
im2[im<64] = 0
im2[im>=64] = 1
im2[im>=128] = 2
im2[im>=192] = 3
foo = open("zz.txt",'w')

for i in im2:
    for j in i:
        foo.write(" " if j==0 else "." if j==1 else "*" if j==2 else "@")
    foo.write("\n")


