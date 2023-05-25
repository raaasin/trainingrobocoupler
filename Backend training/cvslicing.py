import cv2 as cv
img=cv.imread("teja.jpg")

img[250:300,50:550]=(0,255,0)
part=img[80:230,270:390]
img[0:150,0:120]=part
resize=cv.resize(img,(800,600))
cv.imshow("window",resize)
cv.waitKey(0)
cv.destroyAllWindows()
