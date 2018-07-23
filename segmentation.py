
import cv2
import numpy as np

img1 = cv2.imread("water_coins.jpg", 1)

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 140, 255, cv2.THRESH_BINARY_INV)

# noise removal
kernel = np.ones((3,3), dtype=np.uint8)
erosion = cv2.erode(mask, kernel, iterations=10)

# background
bg = cv2.dilate(erosion, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(erosion, cv2.DIST_L2, 5)
ret, fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# Finding unknown region
fg = np.uint8(fg)
unknown = cv2.subtract(bg, fg)

ret, markers = cv2.connectedComponents(fg)

markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(img1, markers)
img1[markers == -1] = [0,0,255]

cv2.imshow('output', img1)
# cv2.imshow('erosion', erosion)
# cv2.imshow('bg', bg)
# cv2.imshow('dist_transform', dist_transform)
# cv2.imshow('fg', fg)
# cv2.imshow('markers', markers)
# cv2.imshow('unknown', unknown)

cv2.waitKey(0)
cv2.destroyAllWindows()