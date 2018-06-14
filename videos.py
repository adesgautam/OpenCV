

import cv2
import numpy as np

# capture from webcam
vid = cv2.VideoCapture(0)

# codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# write video to file
out = cv2.VideoWriter('output.avi',fourcc, 15.0, (int(vid.get(3)),int(vid.get(4))))

while vid.isOpened():
	ret, frame = vid.read()
	frame = cv2.flip(frame,1)
	if ret == True:
		out.write(frame)
		# convert to gray
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# show coloured
		cv2.imshow('frame',frame)
		
		# show gray 
		cv2.imshow('gray',gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
#release VideoWriter
out.release()
# Close all windows 
cv2.destroyAllWindows()


