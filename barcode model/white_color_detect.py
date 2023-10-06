import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_white = np.array([0,0,168])
    upper_white = np.array([172,111,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Filtered Result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
