
import cv2
import numpy as np

img = cv2.imread("earth.jpg", 1)

# blue value at [300,300]
print(img[300,300,0])

# set white at a region
img[300:350,300:350] = [255,255,255]

# access RED value
print(img.item(300,300,2))

# modify RED value
img.itemset((400,400,2), 150) 
print(img.item(400,400,2))

# get image shape
print(img.shape)

# get image size
print(img.size)

# get image dtype
print(img.dtype)

# ROI
img[100:200, 200:300] = img[200:300, 200:300]

# Make border
BLUE = [170,50,100]
constant= cv2.copyMakeBorder(img,30,30,30,30, cv2.BORDER_CONSTANT, value=BLUE)

cv2.imshow('image',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()
