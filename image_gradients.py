
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
	ret, frame = cv2.threshold(original, 150, 230, cv2.THRESH_BINARY)

	# Laplacian Filter
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)

	# Sobel Filter on x-axis
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

	# Soble Filter on y-axis
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	cv2.imshow('BINARY', frame)
	cv2.imshow('Laplacian', laplacian)
	cv2.imshow('Sobelx', sobelx)
	cv2.imshow('Sobely', sobely)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()











