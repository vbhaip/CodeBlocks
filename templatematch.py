import numpy as np
import cv2
import format_obj

AREA_THRESHOLD = 15000
COLORS = ["PINK", "GREEN"]

#this defines the threshold for the hsv_mask

low_pink_hsv = np.array([142, 94, 0])
high_pink_hsv = np.array([255, 255, 255])

low_green_hsv = np.array([43, 69, 74])
high_green_hsv = np.array([101, 184, 255])

low_yellow_hsv = np.array([28, 143, 0])
high_yellow_hsv = np.array([84, 219, 255])

low_orange_hsv = np.array([0, 209, 60])
high_orange_hsv = np.array([132, 255, 255])



def getContours(raw_frame, color):
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	if(color == "PINK"):
		mask_hsv = cv2.inRange(hsv, low_pink_hsv, high_pink_hsv)
	elif(color == "GREEN"):
		mask_hsv = cv2.inRange(hsv, low_green_hsv, high_green_hsv)
	elif(color == "YELLOW"):
		mask_hsv = cv2.inRange(hsv, low_yellow_hsv, high_yellow_hsv)
	elif(color == "ORANGE"):
		mask_hsv = cv2.inRange(hsv, low_orange_hsv, high_orange_hsv)

	contours, _ = cv2.findContours(mask_hsv,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	return contours

def getFeatures(frame, c, color):


	M = cv2.moments(c)

	#this gives details for the smallest bounding box needed, NOTE: DOESN'T ACCOUNT FOR ROTATION
	x, y, w, h = cv2.boundingRect(c)

	#gets the angle of rotation of the bounding box, if its too large, then we should give error
	(_,_),(_,_),angle = cv2.fitEllipse(c)

	#gets perimeter, use this to find out length of contour
	perimeter = cv2.arcLength(c,True)

	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)

	#gets number of points that are needed for for the contour
	points = len(approx)

	# print("x,y ",x,",",y)
	# print("angle ", angle)
	# print("perimeter ", perimeter)
	# print("points ", len(approx))

	# print("\n")

	cv2.drawContours(frame, c, -1, (255, 0, 0), 3)

	return (x, y, color, points)


def getBoxArray(frame):

	box_arr = []
	for color in COLORS:
		contours = getContours(frame, color)
		for c in contours:
			if cv2.contourArea(c) > AREA_THRESHOLD:
				box_arr.append(getFeatures(frame, c, color))

	return box_arr


cap = cv2.VideoCapture(1)



while(True):

	ret, frame = cap.read()
	frame = cv2.flip(frame, -1)
	# blur = cv2.GaussianBlur(frame, (25, 25), 0)
	
	arr = getBoxArray(frame)

	# print(arr)
	# print("\n\n")
	obj = format_obj.format_objects(arr)
	# print(obj)
	# print("\n")

	obj.evaluate()


	# cv2.imshow('mask',mask_hsv)
	cv2.imshow('frame', frame)


	if cv2.waitKey(500) & 0xFF == ord('q'):
		break

