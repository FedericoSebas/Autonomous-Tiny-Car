import WebcamModule as wM
import DataCollectedModule as dcM
import MqttControllerModule as mcM
import cv2
from time import sleep
axis = ""
turn = 0
joyValLeft = []
joyValRight = []
record = 2

def Main(client):
    global joyValLeft
    global joyValRight
    global speed
    global axis
    global turn
    global record
    while True:
        joyValLeft,joyValRight = mcM.subscribe(client)
        if joyValLeft and joyValLeft[0] >= 90 and joyValLeft[0] <= 270:
            axis = "left"
            turn = joyValLeft[1] / -100
            #mcM.publish(client,turn)    
        if joyValLeft and joyValLeft[0] < 90 and joyValLeft[0] >= 0:
            axis = "right"
            turn = joyValLeft[1] / 100
            #mcM.publish(client,turn)    
        if joyValLeft and joyValLeft[0] <= 360 and  joyValLeft[0] > 270:
            axis = "right"
            turn = joyValLeft[1] / 100
            #mcM.publish(client,turn)    
        if record == 2 and joyValRight and joyValRight[0] > 0 and joyValRight[0] <= 180:
            dcM.createFolder()
            print('Recording Started ...')
            record = 1
        if record == 1 and joyValRight and joyValRight[0] > 180 and joyValRight[0] <= 360:
            record = 0
            speed = 0
        if record == 1:
            img = wM.getImg(size=[270,480])
            dcM.saveData(img,turn)
            speed = 205
        elif record == 0:
            dcM.saveLog()
            record = 2
        # motor.move(speed,turn)
        # cv2.waitKey(1)

if __name__ == "__main__":
    client = mcM.Mqtt()
    Main(client)



