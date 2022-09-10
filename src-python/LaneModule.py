import cv2
import numpy as np
import utlis
curveList = []
avgVal = 10
def getLaneCurve(img):
    # step1
    imgResult = img.copy()
    imgThres = utlis.thresholding(img)

    #step 2
    hT,wT,c=img.shape
    initialTrackBarVals = [20, 343, 0, 480]
    points = utlis.valTrackbars(initialTrackBarVals)
    imgWarp = utlis.warpImg(imgThres,points,wT,hT)

    #step 3 
    midPoint, imgHist = utlis.getHistogram(imgWarp,minPer=0.5,region=4)
    basePoint, imgHist = utlis.getHistogram(imgWarp,minPer=0.9)
    curveRaw = basePoint-midPoint

    #step 4
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))

    #step 5
    imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT,inv = True)
    imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
    imgInvWarp[0:hT//3,0:wT] = 0,0,0
    imgLaneColor = np.zeros_like(img)
    imgLaneColor[:] = 0, 255, 0
    imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
    imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
    midY = 450
    cv2.putText(imgResult,str(curve),(wT//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
    cv2.line(imgResult,(wT//2,midY),(wT//2+(curve*3),midY),(255,0,255),5)
    cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY-25), (wT // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
    for x in range(-30, 30):
        w = wT // 20
        cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
                (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)

    # cv2.imshow('Thres',imgWarp)
    # cv2.imshow('Vid',imgResult)
    # cv2.imshow('Hist',imgHist)
    
    curve = curve/100

    if curve>1:curve== 1
    if curve<-1:curve ==-1

    return curve
