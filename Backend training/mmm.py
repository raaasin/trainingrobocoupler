import cv2 as cv
vid = cv.VideoCapture(0)

while(True):
    ret,frame=vid.read(0)
    cv.imshow('my weiner',frame)

    if cv.waitKey(1) & 0xFF == ord('a'):
        break

vid.release()
cv.destroyAllWindows()
                                   
