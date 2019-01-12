import cv2
import numpy as np

#  Capturing video through webcam
cap = cv2.VideoCapture(0)

while(1):
    _, img = cap.read()

    # Converts the colour to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Range of white
    white_lower = np.array([90, 25, 160], np.uint8)
    white_upper = np.array([30, 200, 255], np.uint8)

    # Finding the range of white
    white = cv2.inRange(hsv, white_lower, white_upper)

    # Generates kernal for the dilation
    kernal = np.ones((5, 5), "uint8")

    white = cv2.dilate(white, kernal)
    res = cv2.bitwise_and(img, img, mask=white)

    # Tracking the White
    (contours, hierarchy) = cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "WHITE colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))
        cv2.imshow("Whitecolour", white)
        cv2.imshow("Colour Tracking", img)
        cv2.imshow("white", res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
