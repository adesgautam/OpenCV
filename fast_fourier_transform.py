
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
	# ret, thresh = cv2.threshold(gray, 100, 230, cv2.THRESH_BINARY)

	# Take fast fourier transform of image
	f = np.fft.fft2(gray)

	# Shift by N/2 in x and y directions 
	fshift = np.fft.fftshift(f)
	magnitude_spectrum = 20*np.log(np.abs(fshift))

	# store for showing
	o_fshift = fshift

	# Get Image Shape
	rows, cols = frame.shape[0], frame.shape[1]
	# Get the middle point
	rrows, ccols = int(rows/2), int(cols/2)
	msize = 10

	# Mask (High Pass Filter)
	fshift[rrows-msize:rrows+msize, ccols-msize: ccols+msize] = 1

	# Mask (Low Pass Filter)
	# mask = np.zeros((rows, cols), np.uint8)
	# mask[rrows-msize : rrows+msize, ccols-msize : ccols+msize] = 1
	# fshift = mask*o_fshift

	# Inverse FFT shift of the masked FFT shift
	ifshift = np.fft.ifftshift(fshift)
	# Inverse FFT
	iff = np.fft.ifft2(ifshift)
	
	cv2.imshow('Original', gray)
	cv2.imshow('FFT', np.uint8(f))
	cv2.imshow('FFT Shift', np.uint8(o_fshift))
	cv2.imshow('Inverse FFT Shift', np.uint8(ifshift))
	cv2.imshow('Inverse FFT', np.uint8(iff))
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release webcam
vid.release()
# Close all windows 
cv2.destroyAllWindows()






