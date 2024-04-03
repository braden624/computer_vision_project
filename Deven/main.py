import cv2

Left_camera = cv2.VideoCapture(1)
Right_camera = cv2.VideoCapture(0)

while Left_camera.isOpened():
    ret_1, frame_1 = Left_camera.read()
    ret_2, frame_2 = Right_camera.read()
    
   

    cv2.imshow('Left_camera', frame_1)
    cv2.imshow('Right_camera', frame_2)

    if cv2.waitKey(10) & 0xFF == ord('q'):  # press q or ESC to quit. You probably need to hit the screen first
        break

Left_camera.release()
Right_camera.release()
cv2.destroyAllWindows()
