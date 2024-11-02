import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def captureScreen(bbox=(300, 300, 1500, 1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr

while True:
    timer = cv2.getTickCount()
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Uncomment the line below if you want to capture screen instead of webcam
    # img = captureScreen()

    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        if len(b) == 5:
            char, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
            cv2.putText(img, char, (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 230, 20), 2)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
