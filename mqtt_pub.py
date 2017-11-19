import time
import paho.mqtt.client as paho

from quotes import get_quotes

QOS = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnected")
    time.sleep(5)

def on_publish(client, userdata, mid):
    print ("Message published")

    
client = paho.Client(protocol=paho.MQTTv31)
#client = paho.Client(client_id="foogoo", clean_session=True, userdata=None, protocol=paho.MQTTv31)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    message = get_quotes()
    (rc, mid) = client.publish("quotes", message, qos=QOS)
    time.sleep(3)

