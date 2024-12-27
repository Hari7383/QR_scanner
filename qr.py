import cv2

# Load the image containing the QR code
image = cv2.imread('ig.jpg')

# Create a QRCodeDetector object
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
value, points, _ = detector.detectAndDecode(image)

if value:
    print(f"QR Code Detected: {value}")
    # Optionally draw a bounding box around the QR code
    if points is not None:
        points = points.astype(int)
        for i in range(len(points)):
            cv2.line(image, tuple(points[i][0]), tuple(points[(i+1) % len(points)][0]), (0, 255, 0), 3)
else:
    print("No QR Code detected.")

# Display the image
cv2.imshow('QR Code Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
