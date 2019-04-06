import numpy as np
import cv2


AREA_THRESHOLD = 2000


#this defines the threshold for the hsv_mask

low_pink_hsv = np.array([142, 94, 0])
high_pink_hsv = np.array([255, 255, 255])

low_green_hsv = np.array([43, 69, 74])
high_green_hsv = np.array([101, 184, 255])

low_yellow_hsv = np.array([28, 143, 0])
high_yellow_hsv = np.array([84, 219, 255])

low_orange_hsv = np.array([0, 209, 60])
high_orange_hsv = np.array([132, 255, 255])



cap = cv2.VideoCapture(1)



while(True):

	ret, frame = cap.read()

    # print(type(frame))

	# frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))

	blur = cv2.GaussianBlur(frame, (25, 25), 0)

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	mask_hsv = cv2.inRange(hsv, low_orange_hsv, high_orange_hsv)
	# ret,thresh = cv2.threshold(imgray,127,255,0)
	_, contours, _ = cv2.findContours(mask_hsv,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	#image = cv2.drawContours(frame, [contours], -1, (0,255,0), 3)

	for c in contours:
		if cv2.contourArea(c) > AREA_THRESHOLD:

			#(original image, list of contours, which contour (-1 means all of them), rgb vals, thickness)
			cv2.drawContours(frame, c, -1, (255, 0, 0), 3)


			M = cv2.moments(c)

			#this gives details for the smallest bounding box needed, NOTE: DOESN'T ACCOUNT FOR ROTATION
			x, y, w, h = cv2.boundingRect(c)

			#gets the angle of rotation of the bounding box, if its too large, then we should give error
			(_,_),(_,_),angle = cv2.fitEllipse(cnt)

			#gets perimeter, use this to find out length of contour
			perimeter = cv2.arcLength(cnt,True)

			#gets number of points that are needed for for the contour
			points = len(c)

			print("x,y " + x "," + y)
			print("angle " + angle)
			print("perimeter " + perimeter)
			print("points " + points)








	cv2.imshow('mask',mask_hsv)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
# print('done')



import numpy as np
import cv2 as cv
cap = cv.VideoCapture('video/noChessBoard.MOV')
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0,255,(100,3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
cv.imwrite('frame1.png', old_frame)
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
# Create a mask image for drawing purposes
print('starting')
'''
mask = np.zeros_like(old_frame)
frame1 = old_frame
ret, frame2 = cap.read()
gray1, gray2 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY), cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

p1 = cv.goodFeaturesToTrack(gray1, mask=None, **feature_params)
p2, st, err = cv.calcOpticalFlowPyrLK(gray1, gray2, p1, None, **lk_params)

if len(p1) != len(p2):
    print('oopsie!')
disp1 = frame1
for p in p1:
    a, b = p[0]
    disp1 = cv.circle(disp1, (a, b), 11, (0, 0, 255), -1)
disp1 = cv.resize(disp1, (int(disp1.shape[1]/3), int(disp1.shape[0]/3)))
disp1 = cv.flip(disp1, -1)
disp2 = frame2
for p in p2:
    a, b = p[0]
    disp2 = cv.circle(disp2, (a, b), 11, (0, 0, 255), -1)
disp2 = cv.resize(disp2, (int(disp2.shape[1]/3), int(disp2.shape[0]/3)))
disp2 = cv.flip(disp2, -1)
#cv.imshow('mask1', disp1)
#cv.imshow('mask2', disp2)
#k = cv.waitKey(100000) & 0xff
#cv.destroyAllWindows()

E, mask = cv.findEssentialMat(p1, p2, 1.0, (0., 0.), cv.RANSAC, 0.999, 3.0)
points, rvec, tvec, mask = cv.recoverPose(E, p1, p2)
disp1 = frame1

objp = np.array([[0, 0, 0], [0, 2, 0], [2, 0, 0], [2, 2, 0]])
focalLength = frame1.shape[1]
camMat = np.array([[focalLength, 0, frame1.shape[1]//2], [0, focalLength, frame1.shape[0]//2], [0, 0, 1]])
distCoef = np.array([0, 0, 0, 0])
print(camMat)
imgp = cv.projectPoints(objp, rvec, tvec, camMat, distCoef)

cv.imshow('mask', mask)
k = cv.waitKey(100000) & 0xff
cv.destroyAllWindows()


cv.waitKey(100000)
'''
while 1:
    mask = np.zeros_like(old_frame)
    ret, frame = cap.read()
    p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    if ret:
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        blur = cv.GaussianBlur(frame, (25, 25), 0)
        #cv.imshow('blur', blur)
        hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
        # HSV limits
        lower_hsv = np.array([0, 29, 77])
        upper_hsv = np.array([34, 74, 166])
        mask_hsv = cv.inRange(hsv, lower_hsv, upper_hsv)

        #approx_simple only stores points connecting the line, but approx_none saves all the points
        contours, _ = cv.findContours(mask_hsv, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv.contourArea(c) > 30000:
                M = cv.moments(c)
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                cv.drawContours(frame, c, -1, (255, 0, 0), 3)
                cv.circle(frame, (cX, cY), 15, (0, 0, 255), -1)
                cv.circle(mask_hsv, (cX, cY), 15, (0, 0, 255), -1)

        img = cv.add(frame, mask)
        img = cv.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
        m = mask_hsv#cv.add(mask_hsv, mask)
        m = cv.resize(m, (int(m.shape[1]/3), int(m.shape[0]/3)))
        img = cv.flip(img, -1)
        m = cv.flip(m, -1)
        cv.imshow('frame',img)
        cv.imshow('mask',m)
        k = cv.waitKey(3000) & 0xff
        if k == 27:
            break
cv.destroyAllWindows()
cap.release()
print('done')