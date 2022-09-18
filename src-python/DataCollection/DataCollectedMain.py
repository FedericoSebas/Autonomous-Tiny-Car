import WebcamModule as wM
import DataCollectedModule as dcM
import MqttControllerModule as mcM
import cv2
from time import sleep

record = 0
axis = ""
turn = 0

def Main(client):
    global speed
    global axis
    global turn
    while True:
        joyValLeft,joyValRight = mcM.subscribe(client)
            
        if joyValLeft[0] >= 90 and joyValLeft[0] <= 0 or joyValLeft[0] <= 360 and joyValLeft[0] >= 270:
            axis = "left"
            turn = joyValLeft[1] / -100
        if joyValLeft[0] > 180 and joyValLeft[0] < 270:
            axis = "right"
            turn = joyValLeft[1] / 100
        
        if joyValRight[0] >= 0 and joyValRight[0] <= 180:
            print('Recording Started ...')
            sleep(0.300)
            record = 1
        if record == 1:
            img = wM.getImg(True,size=[240,120])
            dcM.saveData(img,turn)
            speed = 205
        if joyValRight[0] > 180 and joyValRight[0] <= 360:
            dcM.saveLog()
            record = 0
            speed = 0
        # motor.move(speed,turn)
        cv2.waitKey(1)

if __name__ == "__main__":
    client = mcM.Mqtt()
    Main(client)
