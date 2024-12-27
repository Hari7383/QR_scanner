import cv2

detector = cv2.QRCodeDetector()
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Failed to capture the frame.")
        break

    value, points, _ = detector.detectAndDecode(frame)

    if value:
        print(f"QR Code Detected: {value}")
        if points is not None:
            points = points.astype(int)
            for i in range(len(points)):
                cv2.line(frame, tuple(points[i][0]), tuple(points[(i+1) % len(points)][0]), (0, 255, 0), 3)

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        print("Exiting...")
        break

cam.release()
cv2.destroyAllWindows()