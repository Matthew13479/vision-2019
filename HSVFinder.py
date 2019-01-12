import cv2
import numpy as np


def nothing(x):
    pass

#  Capturing video through webcam
capture = cv2.VideoCapture(0)

# Creating the adjustments window
cv2.namedWindow("Adjustments")

# Creating the Trackbars
cv2.createTrackbar("L - H", "Adjustments", 0, 179, nothing)
cv2.createTrackbar("L - S", "Adjustments", 0, 255, nothing)
cv2.createTrackbar("L - V", "Adjustments", 0, 255, nothing)
cv2.createTrackbar("H - H", "Adjustments", 179, 179, nothing)
cv2.createTrackbar("H - S", "Adjustments", 255, 255, nothing)
cv2.createTrackbar("H - V", "Adjustments", 255, 255, nothing)


while True:
    _, frame = capture.read()

    # Converts the colour to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Adjustments")
    l_s = cv2.getTrackbarPos("L - S", "Adjustments")
    l_v = cv2.getTrackbarPos("L - V", "Adjustments")
    h_h = cv2.getTrackbarPos("H - H", "Adjustments")
    h_s = cv2.getTrackbarPos("H - S", "Adjustments")
    h_v = cv2.getTrackbarPos("H - V", "Adjustments")

    # Range of colour
    lowColour = np.array([l_h, l_s, l_v])
    highColour = np.array([h_h, h_s, h_v])
    mask = cv2.inRange(hsv, lowColour, highColour)

    cv2.imshow("Original", frame)
    cv2.imshow("HSV Finder", mask)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

# White HSV values are:
# Lower 90,25,160
# Higher 30, 200, 255
