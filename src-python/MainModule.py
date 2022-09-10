from LaneModule import getLaneCurve
import WebcamModule
import MqttModule as mqtt
import cv2

def main(client):
 
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img)
 
    sen = 1.3  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    turn = -curveVal*sen
    mqtt.publish(client,turn)
    cv2.waitKey(1)

    # motor.move(0.20,-curveVal*sen,0.05)
     
 
if __name__ == '__main__':
    client = mqtt.Mqtt()
    while True:
        main(client)
