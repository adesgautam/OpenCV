
import cv2
import numpy as np

# capture from webcam
vid = cv2.VideoCapture(0)

while vid.isOpened():
	ret, frame = vid.read()
	# resize frame
	frame = cv2.resize(frame, (600,350))
	# flip frames
	coloured = cv2.flip(frame,1)
	# convert BGR to GRAY
	gray = cv2.cvtColor(coloured, cv2.COLOR_BGR2GRAY)

	# Threshold image
	ret, thresh = cv2.threshold(gray, 100, 230, cv2.THRESH_BINARY)

	# Find Contours 
	image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	# Draw all Contours 
	contours = cv2.drawContours(coloured, contours, -1, (0,0,255), 2)
	
	# cv2.imshow('BINARY', image)
	cv2.imshow('Contours', contours)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()











