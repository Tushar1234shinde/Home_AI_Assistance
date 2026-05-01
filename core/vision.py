import cv2
import tempfile
import os
import atexit

_camera = None


def release_camera():
    global _camera
    if _camera is not None:
        _camera.release()
        _camera = None


def get_camera():
    global _camera
    if _camera is None:
        _camera = cv2.VideoCapture(0)
    return _camera


atexit.register(release_camera)

def capture_frame():
    cap = get_camera()
    if not cap.isOpened():
        print("Warning: Could not open webcam")
        release_camera()
        return None

    ret, frame = cap.read()
    if not ret:
        print("Warning: Could not capture frame")
        release_camera()
        return None

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    cv2.imwrite(temp_file.name, frame)
    
    return temp_file.name

if __name__ == "__main__":
    image_path = capture_frame()
    print(f"Frame captured and saved to: {image_path}")
