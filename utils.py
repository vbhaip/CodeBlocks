import numpy as np
import cv2
import imutils
import argparse
# https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = 'unidentified'
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04*peri, True)
        #approx is a contour that is a list of vertices
        #triangle = 3 vertices, rest follow
        if len(approx) == 3:
            shape = 'triangle'
        elif len(approx) == 4:
            shape = 'square'
        elif len(approx) == 5:
            shape = 'pentagon'
        else:
            shape = 'circle'
        return shape

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    '''ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    args = vars(ap.parse_args())
    frame = cv2.imread(args["image"])'''
    #load the image and resize it so that the shapes
    #can be approximated better
    resized = imutils.resize(frame, width=300)
    ratio = frame.shape[0]/float(resized.shape[0])
    #convert to grayscale, blur it slightly
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 126, cv2.THRESH_BINARY)[1]
    #find contours in threshhold image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    #loop over contours
    for c in cnts:
        #compute center of the contour, then detect
        #the name of the shape using only the contour
        peri = cv2.arcLength(c, True)
        print(peri)
        if peri > 1000: continue
        M = cv2.moments(c)
        cX = int((M["m10"] / (M["m00"]+1e-7)) * ratio)
        cY = int((M["m01"] / (M["m00"]+1e-7)) * ratio)
        print((cX, cY))
        shape = sd.detect(c)
        if shape == 'circle': continue
        #multiply the contour (x,y) coordinates by the resize
        #ratio then draw the contours and name the shape
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)
        #output image
        #cv2.imshow('frame', frame)
        cv2.waitKey(0)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
