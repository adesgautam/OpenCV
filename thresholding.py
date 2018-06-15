

import cv2
import numpy as np

img = cv2.imread("book.jpg", 1)
img = cv2.resize(img, (400,600))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, res1 = cv2.threshold(gray, 110, 230, cv2.THRESH_BINARY)
ret, res2 = cv2.threshold(gray, 110, 230, cv2.THRESH_BINARY_INV)
ret, res3 = cv2.threshold(gray, 110, 230, cv2.THRESH_TRUNC)
ret, res4 = cv2.threshold(gray, 110, 230, cv2.THRESH_TOZERO)
ret, res5 = cv2.threshold(gray, 110, 230, cv2.THRESH_TOZERO_INV)

cv2.imshow('BIN', res1)
cv2.imshow('BIN_INV', res2)
cv2.imshow('TRUNC', res3)
cv2.imshow('TOZERO', res4)
cv2.imshow('TOZERO_INV', res5)

res6 = cv2.adaptiveThreshold(gray, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)
cv2.imshow('ADAPTIVE_GAUSSIAN', res6)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
ret, res7 = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('OTSU', res7)

cv2.waitKey(0)
cv2.destroyAllWindows()