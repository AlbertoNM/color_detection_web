import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    if ret:
        
        cv2.imshow('test', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()