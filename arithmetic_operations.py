
import cv2
import numpy as np

img1 = cv2.imread("earth.jpg", 1)
img2 = cv2.imread("spacex.jpg", 1)

ls = 50

bg = img2[0:ls,0:ls]

img1 = cv2.resize(img1, (ls,ls))

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# for pizza.jpg
# ret, mask = cv2.threshold(img2gray, 243, 255, cv2.THRESH_BINARY)
# for earth.jpg
ret, mask = cv2.threshold(img2gray, 3, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)	

# for pizza.jpg
# img2_bg = cv2.bitwise_and(bg,bg,mask = mask)
# img1_fg = cv2.bitwise_and(img1,img1,mask = mask_inv)

# for earth.jpg
img2_bg = cv2.bitwise_and(bg,bg,mask = mask_inv)
img1_fg = cv2.bitwise_and(img1,img1,mask = mask)

img2[0:ls,0:ls] = img1_fg + img2_bg

cv2.imshow('dst',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


