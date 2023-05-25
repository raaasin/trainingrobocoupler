import cv2 as cv
img = cv.imread('teja.jpg')
resize=cv.resize(img,(200,200))
cv.imshow('window',resize)
cv.waitKey(0)
cv.destroyAllWindows(0)
