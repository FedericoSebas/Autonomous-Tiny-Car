import random
import time
from paho.mqtt import client as mqtt_client


broker = 'ip'
port = 1883
topic = "motor/autonomy/turn"
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


def publish(client,msg):
    time.sleep(0.0001)
    # msg = getTurn()
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def Mqtt():
    client = connect_mqtt()
    client.loop_start()
    return client
