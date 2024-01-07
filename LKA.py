import numpy as np
import cv2


def nothing(x):
	pass

kernel = np.ones((5,5),np.uint8)

cv2.namedWindow("tracker")
cv2.createTrackbar("HH", "tracker", 0, 255, nothing)
cv2.createTrackbar("SH", "tracker", 0, 255, nothing)
cv2.createTrackbar("VH", "tracker", 0, 255, nothing)
cv2.createTrackbar("HL", "tracker", 0, 255, nothing)
cv2.createTrackbar("SL", "tracker", 0, 255, nothing)
cv2.createTrackbar("VL", "tracker", 0, 255, nothing)

cap = cv2.VideoCapture('DirivingVideo.mp4')

while(cap.isOpened()) and True:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	HH = cv2.getTrackbarPos("HH", "tracker")
	SH = cv2.getTrackbarPos("SH", "tracker")
	VH = cv2.getTrackbarPos("VH", "tracker")
	HL = cv2.getTrackbarPos("HL", "tracker")
	SL = cv2.getTrackbarPos("SL", "tracker")
	VL = cv2.getTrackbarPos("VL", "tracker")

	lowerHSVValue = np.array([HL, SL, VL])
	higherHSVValue = np.array([HH, SH, VH])

	mask = cv2.inRange(hsv, lowerHSVValue, higherHSVValue)

	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow("masked", mask)
	cv2.imshow("filterd", res)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()