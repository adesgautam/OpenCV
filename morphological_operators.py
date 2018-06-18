
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

	# Define kernel using cv2
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
	# kernel of 5x5
	# kernel = np.ones((3,3), np.uint8)

	# Erosion and dilation
	erosion = cv2.erode(frame, kernel, iterations=1)
	dilation = cv2.dilate(frame, kernel, iterations=1)

	# Opening(Erosion then Dilation) and Closing(Dilation then Erosion)
	opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)

	# Gradient(Dilation-Erosion)
	gradient = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)

	# cv2.imshow('Original', original)
	# cv2.imshow('BINARY', frame)
	cv2.imshow('Erosion', erosion)
	cv2.imshow('Dilation', dilation)
	# cv2.imshow('Opening', opening)
	# cv2.imshow('Closing', closing)
	cv2.imshow('Gradient', gradient)
	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()