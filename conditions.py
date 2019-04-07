import datetime
import cv2


cap = cv2.VideoCapture(1)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def check_time():
    return datetime.datetime.now().minute % 2 == 0

def ret_false():
    return False

def ret_true():
    return True

def check_face():
	ret, image = cap.read()

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w] # face region of image
		roi_color = image[y:y+h, x:x+w]

	cv2.imshow("Faces", image)
	cv2.waitKey(1000)
	return len(faces) > 0
