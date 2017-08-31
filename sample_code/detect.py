"""
This file demos method to detect and visualize an object from:
- An image file
- A live capture stream
"""

import dlib, cv2

detector = dlib.simple_object_detector("detector.svm")

"""
Detect from an image file
"""
image_path = 'image path'
img = cv2.imread(image_path)

dets = detector(img)
for det in dets:
    p1 = (det.left(), det.top())
    p2 = (det.right(), det.bottom())
    color = (0, 0, 255) # Red
    cv2.rectangle(camera_frame, p1, p2, color)
    cv2.imshow('Eyeglasses', camera_frame)
    cv2.waitKey(0)

# ========================================= #

"""
Detect from a live stream
"""
camera_number = 0
camera = cv2.VideoCapture()
camera.open(camera_number)
if camera.isOpened() is not True:
    print("Could not access camera")
    exit()
else:
    print("Camera ready")

width, height = 640, 480
fps = 10

camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
camera.set(cv2.CAP_PROP_FPS, fps)

while True:
    capture_success, camera_frame = camera.read()

    if capture_success:
        dets = detector(camera_frame)
        if len(dets) == 0:
            cv2.putText(camera_frame, msg_no_glasses, msg_coor, cv2.FONT_HERSHEY_SIMPLEX, 1.0, font_color, 2)
        else:
            for det in dets:
                p1 = (det.left(), det.top())
                p2 = (det.right(), det.bottom())
                color = (0, 0, 255) # Red
                cv2.rectangle(camera_frame, p1, p2, color)
        cv2.imshow('Eyeglasses', camera_frame)
        key = cv2.waitKey(1000 // fps)
    if key == 27: # Escape key
        break
