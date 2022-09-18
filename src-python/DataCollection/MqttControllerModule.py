import random
from paho.mqtt import client as mqtt_client


broker = 'ip'
port = 1883
JoyLeft_TurnTopic = "motor/autonomy/left"
JoyRight_MenuTopic = "motor/autonomy/right"
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
        if len(msg.JoyLeft_TurnTopic ) != 0:
            print(f"Received `{msg.payload.decode()}` from `{msg.JoyLeft_TurnTopic }` JoyLeft_TurnTopic ")
            Turn = msg.payload.decode().split()
        if len(msg.JoyRight_MenuTopic) != 0:
            print(f"Received `{msg.payload.decode()}` from `{msg.JoyRight_MenuTopic}` JoyRight_MenuTopic")
            Menu = msg.payload.decode().split()
    client.subscribe(JoyLeft_TurnTopic )
    client.subscribe(JoyRight_MenuTopic)
    client.on_message = on_message
    return Turn,Menu

def Mqtt():
    client = connect_mqtt()
    client.loop_start()
    return client
