import random
from paho.mqtt import client as mqtt_client
from time import sleep


broker = '192.168.10.160'
port = 1883
JoyLeft_TurnTopic = "motor/rc/left"
JoyRight_MenuTopic = "motor/rc/right"
TurnTopic = "motor/rc/turn"
Turn = []
Menu = []
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
#username = 'CERTERO-motor'
#password = 'CERTERO-motor'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.tls_set(tls_version=mqtt_client.ssl.PROTOCOL_TLS)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    global Turn
    global Menu
    def on_message(client, userdata, msg):
        global Turn
        global Menu
        if msg.topic == JoyLeft_TurnTopic:
             print(f"Received `{msg.payload.decode()}` from `{msg.topic}` JoyLeft_TurnTopic ")
             Turn = msg.payload.decode().split()
        if msg.topic == JoyRight_MenuTopic:
             print(f"Received `{msg.payload.decode()}` from `{msg.topic}` JoyRight_MenuTopic")
             Menu = msg.payload.decode().split()
    client.subscribe(JoyLeft_TurnTopic )
    client.subscribe(JoyRight_MenuTopic)
    client.on_message = on_message
    Turn = list(map(int,Turn))
    Menu = list(map(int,Menu))
    client.loop_start()
    return Turn,Menu

def Mqtt():
    client = connect_mqtt()
    return client
if __name__ == "__main__":
    client = Mqtt()
    while True:
        subscribe(client)
        if Turn or Menu:
            print(Turn)
            print(Menu)

