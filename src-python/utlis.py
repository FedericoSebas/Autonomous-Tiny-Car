import cv2
import numpy as np

def thresholding(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([46,0,0])
    upperWhite = np.array([179,255,255])
    maskWhite = cv2.inRange(imgHsv,lowerWhite,upperWhite)
    return maskWhite

def valTrackbars(initialTracbarVals=[],wT=270, hT=480):
    widthTop = initialTracbarVals[0]
    heightTop = initialTracbarVals[1]
    widthBottom = initialTracbarVals[2]
    heightBottom = initialTracbarVals[3]
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def warpImg(img,points,w,h,inv=False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2,pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp

def getHistogram(img,minPer=0.1,region=1):
    if region == 1:
        histValues = np.sum(img,axis=0)
    else:
        histValues = np.sum(img[img.shape[0]//region:,:],axis=0)

    maxValue = np.max(histValues)
    minValue = minPer*maxValue

    indexArray = np.where(histValues>=minValue)
    basePoint = int(np.average(indexArray))

    imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for x,intensity in enumerate(histValues):
        cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(255,0,255),1)
        cv2.circle(imgHist,(basePoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
    return basePoint,imgHist
