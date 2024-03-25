import cv2

camera_1 = cv2.VideoCapture(0)
camera_2 = cv2.VideoCapture(6)

while camera_1.isOpened():
    ret_1, frame_1 = camera_1.read()
    ret_2, frame_2 = camera_2.read()
    
   

    cv2.imshow('camera_1', frame_1)
    cv2.imshow('camera_2', frame_2)

    if cv2.waitKey(10) & 0xFF == ord('q'):  # press q or ESC to quit. You probably need to hit the screen first
        break

camera_2.release()
camera_2.release()
cv2.destroyAllWindows()
