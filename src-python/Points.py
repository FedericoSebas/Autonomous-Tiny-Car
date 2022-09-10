import cv2
import numpy as np

def thresholding(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([33,0,88])
    upperWhite = np.array([179,255,255])
    maskWhite = cv2.inRange(imgHsv,lowerWhite,upperWhite)
    return maskWhite

 
def warpImg(img,points,w,h,inv = False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp

def nothing(a):
    pass
 
def initializeTrackbars(initialTracbarVals,wT=270, hT=480):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top","Trackbars", initialTracbarVals[0],wT//2,nothing)
    cv2.createTrackbar("Height Top","Trackbars", initialTracbarVals[1], hT,nothing)
    cv2.createTrackbar("Width Bottom","Trackbars", initialTracbarVals[2],wT//2,nothing)
    cv2.createTrackbar("Height Bottom","Trackbars", initialTracbarVals[3], hT,nothing)


def valTrackbars(wT=270, hT=480):
    widthTop = cv2.getTrackbarPos("Width Top","Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top","Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom","Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom","Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def drawPoints(img,points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
    return img
    
if __name__ == '__main__':
    cap = cv2.VideoCapture('video')
    initialTrackBarVals = [51, 371, 0, 480]
    initializeTrackbars(initialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img,(270,480))
        imgCopy = img.copy()
        imgResult = img.copy()
        ## STEP 1
        imgThres = thresholding(img)

        ### STEP 2
        hT,wT, c = img.shape
        points = valTrackbars()
        imgWarp = warpImg(imgThres,points,wT,hT)
        imgWarpPoints = drawPoints(imgCopy,points)
        cv2.imshow('Vid1',imgWarpPoints)
        cv2.imshow('Vid2',imgWarp)
        cv2.waitKey(1)
