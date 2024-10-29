<!DOCTYPE html>
<html>

<head>
  <h1>Real-Time Text Detection with OpenCV and PyTesseract OCR</h1>
</head>

<body>
  <h2>Introduction</h2>
  <p>This project implements a real-time text detection system in Python using OpenCV and PyTesseract OCR. It captures live video feeds or static images, identifies text regions, and extracts the
     recognized text. This technology is highly useful in automating tasks like document scanning, license plate recognition, and real-time translation. Key features include:<br>
     1. Real-Time Detection: Identifies and tracks text in live video streams or images.<br>
     2. Image Preprocessing: Applies image processing techniques to enhance text detection accuracy.<br>
     3. Character Recognition: Utilizes OCR to recognize characters and draw bounding boxes around detected text.<br></p>
  
  <h2>Requirements</h2>
  <p>Python Libraries:<br>
     - Numpy: For numerical computations and array handling.<br>
     - cv2 (OpenCV): For basic image processing tasks.<br>
     - PIL: For opening, manipulating, and saving image file formats.<br>
     - Pytesseract: For extracting text from images.<br>
     - Time: For handling time-related tasks and measuring intervals.<br></p>

  <h2>Installation</h2>
  <p>To set up the environment:<br>
     - Download and install Visual Studio Code (or your preferred IDE).<br>
     - Ensure Python is installed.<br>
     - Install required packages: <code>pip install numpy opencv-python pillow pytesseract</code><br>
     - Open Visual Studio Code or any preferred IDE and create a file named <code>text-detection.py</code>.<br>
     - Run the application.<be></p>

  <h2>Code Explanation</h2>
  <p>This Python script detects text from images. Here’s a breakdown of the code:<br>
     1. Imports: Import required libraries for numerical computations, image processing, and OCR.<br>
     2. Image Reading and Conversion: Load the image file (ensure it is in your directory) and convert it from BGR to RGB format.<br>
     3. Character Detection: Use PyTesseract to detect characters and their bounding box coordinates.<br>
     4. Processing and Drawing Boxes: Iterate through the detected characters, split their details, and draw rectangles around each character to indicate detection.<br>
     5. Displaying the Image: Use OpenCV to display the image with rectangles drawn around detected text, and wait for a key press to close the window.<br></p>

</body>

</html>
