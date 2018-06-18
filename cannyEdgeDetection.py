
import cv2
import numpy as np

# capture from webcam
vid = cv2.VideoCapture(0)

while vid.isOpened():
	ret, frame = vid.read()
	# resize frame
	frame = cv2.resize(frame, (600,350))
	# flip frames
	frame = cv2.flip(frame,1)
	# convert BGR to GRAY
	original = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Threshold image
	ret, frame = cv2.threshold(original, 100, 230, cv2.THRESH_BINARY)

	# Laplacian Filter (image, minVal, maxVal)
	canny = cv2.Canny(frame, 100, 100)

	cv2.imshow('BINARY', frame)
	cv2.imshow('Canny', canny)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()











