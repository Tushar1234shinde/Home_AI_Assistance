import cv2
import tempfile
import os

def capture_frame():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Warning: Could not open webcam")
        return None
    
    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        print("Warning: Could not capture frame")
        cap.release()
        return None
    
    # Release the webcam
    cap.release()
    
    # Save the frame to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    cv2.imwrite(temp_file.name, frame)
    
    return temp_file.name

if __name__ == "__main__":
    image_path = capture_frame()
    print(f"Frame captured and saved to: {image_path}")