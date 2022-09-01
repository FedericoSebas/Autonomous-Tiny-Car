import cv2
import utlis
 
cap = cv2.VideoCapture('http://192.168.0.111:9003/video')
 
def getImg(display= False,size=[720,1280]):
    intialTrackBarVals = [102, 80, 20, 214 ]
    utlis.initializeTrackbars(intialTrackBarVals)
    success, img = cap.read()
    img = cv2.resize(img,(480,240))
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)
