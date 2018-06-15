
import cv2
import numpy as np

def nothing(x):
    pass

# capture from webcam
vid = cv2.VideoCapture(0)

cv2.namedWindow('trackbarsL')
cv2.namedWindow('trackbarsU')

# create lower trackbars for color change
cv2.createTrackbar('LH','trackbarsL',0,179,nothing)
cv2.createTrackbar('LS','trackbarsL',0,255,nothing)
cv2.createTrackbar('LV','trackbarsL',0,255,nothing)

# create upper trackbars for color change
cv2.createTrackbar('UH','trackbarsU',0,179,nothing)
cv2.createTrackbar('US','trackbarsU',0,255,nothing)
cv2.createTrackbar('UV','trackbarsU',0,255,nothing)

while vid.isOpened():
	ret, frame = vid.read()
	# resize frame
	frame = cv2.resize(frame, (800,450))
	# flip frames
	frame = cv2.flip(frame,1)

	frame = cv2.medianBlur(frame, 5)

	# convert to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	if ret == True:

		# lower trackbars
		lh = cv2.getTrackbarPos('LH','trackbarsL')
		ls = cv2.getTrackbarPos('LS','trackbarsL')
		lv = cv2.getTrackbarPos('LV','trackbarsL')

		# upper trackbars
		uh = cv2.getTrackbarPos('UH','trackbarsU')
		us = cv2.getTrackbarPos('US','trackbarsU')
		uv = cv2.getTrackbarPos('UV','trackbarsU')

		# set range
		lower = np.uint8([[[lh,ls,lv]]])
		upper = np.uint8([[[uh,us,uv]]])

		# convert lower and upper to HSV
		lower = cv2.cvtColor(lower, cv2.COLOR_BGR2HSV)
		upper = cv2.cvtColor(upper, cv2.COLOR_BGR2HSV)
		
		mask = cv2.inRange(hsv, lower, upper)
		res = cv2.bitwise_and(frame, frame, mask= mask)	
		
		# show coloured
		# cv2.imshow('original',frame)
		# show mask
		cv2.imshow('mask', mask)
		# show output
		cv2.imshow('output',res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()




