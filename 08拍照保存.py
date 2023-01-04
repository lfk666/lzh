import cv2

cap=cv2.VideoCapture(0)

falg=1
num=1

while(cap.isOpened()):
    ret_flag,Vshow = cap.read()
    cv2.imshow("Capture_Test",Vshow)
    k=cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite("D:/python/opencv/"+str(num)+".jpg",Vshow)
        print("success to save"+str(num)+".jpg")
        print("-------------")
        num +=1
    elif k== ord(" "):
        break
cap.release()
cv2.destroyAllWindows()