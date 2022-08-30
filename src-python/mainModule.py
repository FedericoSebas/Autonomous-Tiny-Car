from MotorModule import Motor
from LaneModule import getLaneCurve
import cv2
 
##################################################
motor = Motor(2,3,4,17,22,27)
##################################################
 
def main():
 
    img = cv2.VideoCapture(https://192.168.0.123/video)
    curveVal= getLaneCurve(img,1)
 
    sen = 1.3  # SENSITIVITY
    maxVAl= 1 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.132: curveVal=0
    else:
        if curveVal>-0.14: curveVal=0
    motor.move(0.20,-curveVal*sen,0.05)
    cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()