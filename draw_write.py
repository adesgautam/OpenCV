
import cv2
import numpy as np

img = cv2.imread("earth.jpg", 0)

# draw line (image, start, end, BGR, thickness)
cv2.line(img,(20,30),(200,150),(0,255,5), 5)

# draw rectangle (image, start, end, BGR, thickness(-1 for fill))
cv2.rectangle(img, (100,100), (200,200), (255,0,0), 5)

# draw circle (image, centre, radius, BGR, thickness(-1 for fill))
cv2.circle(img, (250,250), 100, (255,255,255), 5)

# draw ellipse (image, centre, (major axis, minor axis), angle, startangle, endangle, color(0-255) ,thickness(-1 for fill))
cv2.ellipse(img, (300,300), (50,150), 180, 0, 180, 100, 5)

pts = np.array([[20,30],[40,50],[100,40],[80,80]], np.int32)
pts = pts.reshape((-1,1,2))
# draw polygon (image, points(shape(-1,1,2)), bool, BGR, thickness)
cv2.polylines(img, [pts], True, (0,255,255), 5)

# write text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()