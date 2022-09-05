import cv2
import utlis
from LaneModule import getLaneCurve
import LaneModule

def getTurn():
    cap = cv2.VideoCapture('http://ip:port/video')
    #utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    #while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    success, img = cap.read()
    img = cv2.resize(img,(480,240))
    curve = getLaneCurve(img,2)
    #print(curve)
    #cv2.imshow('Vid',img)
    cv2.waitKey(1)
    curveVal= getLaneCurve(img,0)
    

    sen = 1.3  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    # print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    cv2.waitKey(1)
    return -curveVal*sen

