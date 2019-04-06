import numpy as np
import cv2


low_pink_hsv = np.array([202, 154, 0])
high_pink_hsv = np.array([255, 255, 255])

low_green_hsv = np.array([43, 69, 74])
high_green_hsv = np.array([101, 184, 255])

low_yellow_hsv = np.array([44, 80, 254])
high_yellow_hsv = np.array([62, 177, 255])





cap = cv2.VideoCapture(1)



while(True):

	ret, frame = cap.read()

    # print(type(frame))

	# frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))

	blur = cv2.GaussianBlur(frame, (25, 25), 0)

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	l = np.array([0,0,0])
	h = np.array([100,255,255])
	mask_hsv = cv2.inRange(hsv, low_green_hsv, high_green_hsv)
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


# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('video/noChessBoard.MOV')
# # params for ShiTomasi corner detection
# feature_params = dict( maxCorners = 100,
#                        qualityLevel = 0.3,
#                        minDistance = 7,
#                        blockSize = 7 )
# # Parameters for lucas kanade optical flow
# lk_params = dict( winSize  = (15,15),
#                   maxLevel = 2,
#                   criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# # Create some random colors
# color = np.random.randint(0,255,(100,3))
# # Take first frame and find corners in it
# ret, old_frame = cap.read()
# cv.imwrite('frame1.png', old_frame)
# old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
# # Create a mask image for drawing purposes
# print('starting')
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
# while 1:
#     mask = np.zeros_like(old_frame)
#     ret, frame = cap.read()
#     p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
#     if ret:
#         frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#         blur = cv.GaussianBlur(frame, (25, 25), 0)
#         #cv.imshow('blur', blur)
#         hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
#         # HSV limits
#         lower_hsv = np.array([0, 29, 77])
#         upper_hsv = np.array([34, 74, 166])
#         mask_hsv = cv.inRange(hsv, lower_hsv, upper_hsv)
#         contours, _ = cv.findContours(mask_hsv, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#         for c in contours:
#             if cv.contourArea(c) > 30000:
#                 M = cv.moments(c)
#                 cX = int(M['m10'] / M['m00'])
#                 cY = int(M['m01'] / M['m00'])
#                 cv.drawContours(frame, c, -1, (255, 0, 0), 3)
#                 cv.circle(frame, (cX, cY), 15, (0, 0, 255), -1)
#                 cv.circle(mask_hsv, (cX, cY), 15, (0, 0, 255), -1)

#         img = cv.add(frame, mask)
#         img = cv.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
#         m = mask_hsv#cv.add(mask_hsv, mask)
#         m = cv.resize(m, (int(m.shape[1]/3), int(m.shape[0]/3)))
#         img = cv.flip(img, -1)
#         m = cv.flip(m, -1)
#         cv.imshow('frame',img)
#         cv.imshow('mask',m)
#         k = cv.waitKey(3000) & 0xff
#         if k == 27:
#             break
# cv.destroyAllWindows()
# cap.release()
# print('done')