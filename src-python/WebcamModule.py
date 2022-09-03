import cv2
import utlis
from LaneModule import getLaneCurve
import LaneModule
#cap = cv2.VideoCapture('http://192.168.0.111:9003/video')
 
#def getImg(display= False,size=[720,1280]):
    #intialTrackBarVals = [102, 80, 20, 214 ]
    #utlis.initializeTrackbars(intialTrackBarVals)
 #   success, img = cap.read()
  #  img = cv2.resize(img,(480,240))
   # return img

#cap = cv2.VideoCapture(0)
 
#def getImg(display= False,size=[480,240]):
   # intialTrackBarVals = [102, 80, 20, 214 ]
    #utlis.initializeTrackbars(intialTrackBarVals)
#    _, img = cap.read()
 #   img = cv2.resize(img,(size[0],size[1]))
  #  if display:
   #     cv2.imshow('IMG',img)
    #return img

#if __name__ == '__main__':
 #while True:
#    img = getImg(True)

#if __name__ == '__main__':
def getTurn():
    cap = cv2.VideoCapture('http://192.168.0.111:9003/video')
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

#import cv2

#cap = cv2.VideoCapture("http://192.168.43.134:9003/video")

#def getImg(display= False,size=[480,240]):
#    frameCounter = 0
    #while True:
#    frameCounter += 1
 #   if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
  #      cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
   #     frameCounter = 0
    #_, img = cap.read()
   # img = cv2.resize(img,(size[0],size[1]))
    #if display:
        #cv2.imshow('IMG',img)
    #return img

#if __name__ == '__main__':
 #   while True:
  #      img = getImg(True)
