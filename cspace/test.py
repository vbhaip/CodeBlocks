import cv2
from cspaceSliders import FilterWindow

cap = cv2.VideoCapture(0)
ret, image = cap.read()
image = cv2.resize(image, ((int)(image.shape[1]/3), (int)(image.shape[0]/3)))
window = FilterWindow('Filter Window', image)
window.show(verbose=True)
