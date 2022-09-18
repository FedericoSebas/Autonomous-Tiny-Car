import cv2
 
cap = cv2.VideoCapture('video or webcam')
 
def getImg(display,size=[270,480]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display is True:
        cv2.imshow('video',img)
    return img
