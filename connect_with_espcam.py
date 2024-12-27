import cv2

# ESP32-CAM URL (replace with the URL provided by your ESP32-CAM)
ESP32_CAM_URL = "http://<ESP32-CAM-IP>/video"

# Create a QRCodeDetector object
detector = cv2.QRCodeDetector()

# Open the ESP32-CAM video stream
cap = cv2.VideoCapture(ESP32_CAM_URL)

if not cap.isOpened():
    print("Error: Unable to access the ESP32-CAM stream.")
    exit()

print("Press 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture the frame.")
        break

    # Detect and decode the QR code
    value, points, _ = detector.detectAndDecode(frame)

    # If a QR code is detected
    if value:
        print(f"QR Code Detected: {value}")
        # Draw bounding box around the QR code
        if points is not None:
            points = points.astype(int)
            for i in range(len(points)):
                cv2.line(frame, tuple(points[i][0]), tuple(points[(i+1) % len(points)][0]), (0, 255, 0), 3)

    # Display the video feed with bounding box (if any)
    cv2.imshow("ESP32-CAM QR Code Scanner", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release the video stream and close the window
cap.release()
cv2.destroyAllWindows()
