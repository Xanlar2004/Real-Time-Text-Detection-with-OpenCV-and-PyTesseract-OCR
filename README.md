<!DOCTYPE html>
<html>

<head>
  <h1>Real-Time Text Detection with OpenCV and PyTesseract OCR</h1>
</head>

<body>
  <h2>Introduction</h2>
  <p>This project implements a real-time text detection system in Python using OpenCV and PyTesseract OCR. It captures live video feed or static images, identifies text regions, and extracts the
     recognized text. This technology is highly useful in automating tasks like document scanning, license plate recognition, and real-time translation. Key features include:<br>
     1. Real-Time Detection: Identifies and tracks text in live video streams or images.<br>
     2. Image Preprocessing: Applies image processing techniques to enhance text detection accuracy.<br>
     3. Character Recognition: Utilizes OCR to recognize characters and draw bounding boxes around detected text.<br></p>
  
  <h2>Requirements</h2>
  <p>Python Libraries:<br>
     Numpy: For numerical computation.<br>
     cv2 (OpenCV): For image processing and detection.<br>
     PyTesseract: For Optical Character Recognition (OCR).<br>
     PIL: For handling image file formats.<br></p>

  <h2>Installation</h2>
  <p>Set Up Python Environment: Ensure Python is installed.<br>
     Install Packages: <code>pip install numpy opencv-python pytesseract pillow</code><br>
     Run the Code: Open the code in VS Code or any preferred IDE. Execute <code>text_detection.py</code>.<br></p>
  
  <h2>Code Explanation</h2>
  <p>This Python script processes images or live video to detect and extract text.<br>
     1. Imports: Imports necessary libraries like OpenCV, PyTesseract, and NumPy.<br>
     2. Image Preprocessing: Converts images to grayscale and applies edge detection for enhanced text localization.<br>
     3. Text Detection: Utilizes PyTesseract OCR to extract characters and draw bounding boxes around detected text regions.<br>
     4. Display: Shows the output image with bounding boxes in real-time.</p>
  
</body>

</html>
