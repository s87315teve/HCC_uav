# coding=utf-8
import cv2
import time

cap=cv2.VideoCapture("udp://192.168.10.1:?")

while True:
	isFrame, frame=cap.read()

	if isFrame:
		cv2.imshow("UAV video",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
