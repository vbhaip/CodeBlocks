import numpy as np
import cv2


low_pink_hsv = np.array([142, 94, 0])
high_pink_hsv = np.array([255, 255, 255])

low_green_hsv = np.array([43, 69, 74])
high_green_hsv = np.array([101, 184, 255])

low_yellow_hsv = np.array([28, 143, 0])
high_yellow_hsv = np.array([84, 219, 255])





cap = cv2.VideoCapture(1)



while(True):

	ret, frame = cap.read()

    # print(type(frame))

	# frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))

	blur = cv2.GaussianBlur(frame, (25, 25), 0)

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	mask_hsv = cv2.inRange(hsv, low_yellow_hsv, high_yellow_hsv)
	# ret,thresh = cv2.threshold(imgray,127,255,0)
	_, contours, _ = cv2.findContours(mask_hsv,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	#image = cv2.drawContours(frame, [contours], -1, (0,255,0), 3)

	for c in contours:
		if cv2.contourArea(c) > 2000:
	 		cv2.drawContours(frame, c, -1, (255, 0, 0), 3)

	cv2.imshow('mask',mask_hsv)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
# print('done')