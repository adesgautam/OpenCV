
import cv2
import numpy as np
import time

img1 = cv2.imread("earth.jpg", 1)
img2 = cv2.imread("spacex.jpg", 1)

j=0
k = 1
while k>0:
	
	dst = cv2.addWeighted(img2, k, img1, j, 0)

	cv2.imshow('dst',dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	j+=0.2
	k-=0.2

