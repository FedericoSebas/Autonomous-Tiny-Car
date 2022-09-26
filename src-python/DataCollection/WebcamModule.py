import cv2

cap = cv2.VideoCapture('http://192.168.10.101:8000/video')

def getImg(size=[270,480]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    return img
