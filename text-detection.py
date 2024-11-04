import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

# Set the dimensions for the video frame
frame_width = 640
frame_height = 480

# Initialize video capture from the specified camera index with given frame dimensions.
def initialize_video_capture(camera_index=0):
    video_capture = cv2.VideoCapture(camera_index)
    video_capture.set(3, frame_width)
    video_capture.set(4, frame_height)
    return video_capture

# Captures a screenshot of the specified bounding box.
def capture_screen(bbox=(300, 300, 1500, 1000)):
    screen_capture = np.array(ImageGrab.grab(bbox))
    return cv2.cvtColor(screen_capture, cv2.COLOR_RGB2BGR)

# Main function to run the text detection program.
def main():
    video_capture = initialize_video_capture()
    
    while True:
        start_time = cv2.getTickCount()
        ret, image = video_capture.read()
        
        if not ret:
            print("Failed to capture image")
            break
        
        # Uncomment the line below to use screen capture instead of webcam
        # image = capture_screen()

        # Processes the image to detect text and draw bounding boxes around detected characters.
        h_img, w_img, _ = image.shape
        boxes = pytesseract.image_to_boxes(image)

        for box in boxes.splitlines():
            box_details = box.split(' ')
            if len(box_details) == 5:
                char, x, y, w, h = box_details[0], int(box_details[1]), int(box_details[2]), int(box_details[3]), int(box_details[4])
                cv2.rectangle(image, (x, h_img - y), (w, h_img - h), (50, 50, 255), 2)
                cv2.putText(image, char, (x, h_img - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

        # Calculates and displays the FPS on the image.
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - start_time)
        cv2.putText(image, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 230, 20), 2)

        # Show the result in a window
        cv2.imshow("Result", image)

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
