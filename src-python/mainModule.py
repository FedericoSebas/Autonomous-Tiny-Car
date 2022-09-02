from LaneModule import getLaneCurve
import WebcamModule

##################################################
# This will be sent to a MCU
##################################################

def getTurn():
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1)

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
    return -curveVal*sen
    
