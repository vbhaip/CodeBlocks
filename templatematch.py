import numpy as np
import cv2
import format_obj
import time

AREA_THRESHOLD = 10000
COLORS = ["PINK", "GREEN", "YELLOW", "RED"]

#this defines the threshold for the hsv_mask

low_pink_hsv = np.array([142, 50, 167])
high_pink_hsv = np.array([247, 255, 255])

low_green_hsv = np.array([60, 43, 126])
high_green_hsv = np.array([108, 141, 255])

low_yellow_hsv = np.array([30, 50, 50])
high_yellow_hsv = np.array([45, 255, 255])

low_orange_hsv = np.array([0, 209, 60])
high_orange_hsv = np.array([132, 255, 255])

low_red_hsv = np.array([0, 180, 0])
high_red_hsv = np.array([20, 255, 255])



def getContours(raw_frame, color):
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	if(color == "PINK"):
		mask_hsv = cv2.inRange(hsv, low_pink_hsv, high_pink_hsv)
	elif(color == "GREEN"):
		mask_hsv = cv2.inRange(hsv, low_green_hsv, high_green_hsv)
	elif(color == "YELLOW"):
		mask_hsv = cv2.inRange(hsv, low_yellow_hsv, high_yellow_hsv)
		cv2.imshow('hsv', mask_hsv)
		cv2.waitKey(30)
	elif(color == "ORANGE"):
		mask_hsv = cv2.inRange(hsv, low_orange_hsv, high_orange_hsv)
	elif(color == "RED"):
		mask_hsv = cv2.inRange(hsv, low_red_hsv, high_red_hsv)


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
	if color == "RED":
		cv2.drawContours(frame, c, -1, (0, 255, 0), 5)
	else:
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


def redInArr(array):
	for x in array:
		if x[2] == "RED":
			return True

	return False


def removeRed(array):
	return [i for i in array if i[2] != "RED"]

cap = cv2.VideoCapture(0)

# time.sleep(3)

while(True):

	arr = []

	while(not redInArr(arr)):
		ret, frame = cap.read()
		frame = cv2.flip(frame, -1)
		# blur = cv2.GaussianBlur(frame, (25, 25), 0)
		
		arr = getBoxArray(frame)
		frame = cv2.resize(frame, (960, 540))
		cv2.imshow('frame', frame)
		if cv2.waitKey(5) & 0xFF == ord('q'):
			break

	print("NO RED");
	while(redInArr(arr)):
		ret, frame = cap.read()
		frame = cv2.flip(frame, -1)
		# blur = cv2.GaussianBlur(frame, (25, 25), 0)
		
		arr = getBoxArray(frame)
		frame = cv2.resize(frame, (960, 540))
		cv2.imshow('frame', frame)
		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	print("YES RED")
	ret, frame = cap.read()
	frame = cv2.flip(frame, -1)
	# blur = cv2.GaussianBlur(frame, (25, 25), 0)
	
	arr = removeRed(getBoxArray(frame))

	frame = cv2.resize(frame, (960, 540))
	cv2.imshow('frame', frame)

	# print(arr)
	# print("\n\n")
	obj = format_obj.format_objects(arr)
	print(obj)
	print("\n")

	obj.evaluate()


	# cv2.imshow('mask',mask_hsv)


	if cv2.waitKey(500) & 0xFF == ord('q'):
		break

