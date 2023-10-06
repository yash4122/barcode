import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from pyzbar.pyzbar import decode
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Decode barcodes in the frame
    barcodes = decode(frame)

    # Loop over the detected barcodes
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Get barcode polygon points
        points = barcode.polygon

        # Convert the points to a NumPy array
        points = np.array(points, dtype=np.int32)

        # Draw a bounding box around the barcode
        cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        # Display the barcode data on the frame
        text = f"{barcode_type}: {barcode_data}"
        cv2.putText(frame, text, (points[0][0], points[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Barcode Scanner", frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
