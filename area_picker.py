import numpy as np
import cv2


def nothing(x):
	pass

cap = cv2.VideoCapture('DirivingVideo.mp4')

width  = int(cap.get(3))
height = int(cap.get(4))

cv2.namedWindow("point_picker")
cv2.createTrackbar("TLx", "point_picker", 0, width, nothing)
cv2.createTrackbar("TLy", "point_picker", 0, height, nothing)
cv2.createTrackbar("TRx", "point_picker", 0, width, nothing)
cv2.createTrackbar("TRy", "point_picker", 0, height, nothing)
cv2.createTrackbar("BLx", "point_picker", 0, width, nothing)
cv2.createTrackbar("BLy", "point_picker", 0, height, nothing)
cv2.createTrackbar("BRx", "point_picker", 0, width, nothing)
cv2.createTrackbar("BRy", "point_picker", 0, height, nothing)

while(cap.isOpened()):

	ret, frame = cap.read()
	if not ret:
		cap = cv2.VideoCapture("DirivingVideo.mp4")
		continue
		
	TLx = cv2.getTrackbarPos('TLx', 'point_picker')
	TLy = cv2.getTrackbarPos('TLy', 'point_picker')
	TRx = cv2.getTrackbarPos('TRx', 'point_picker')
	TRy = cv2.getTrackbarPos('TRy', 'point_picker')
	BLx = cv2.getTrackbarPos('BLx', 'point_picker')
	BLy = cv2.getTrackbarPos('BLy', 'point_picker')
	BRx = cv2.getTrackbarPos('BRx', 'point_picker')
	BRy = cv2.getTrackbarPos('BRy', 'point_picker')

	cv2.line(frame, (TLx, TLy), (TRx, TRy), (0,255,0), 2)
	cv2.line(frame, (TRx, TRy), (BRx, BRy), (0,255,0), 2)
	cv2.line(frame, (BRx, BRy), (BLx, BLy), (0,255,0), 2)
	cv2.line(frame, (BLx, BLy), (TLx, TLy), (0,255,0), 2)

	cv2.imshow('Original',frame)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()