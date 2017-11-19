import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnected")

def on_message(client, userdata, msg):
    print ("Quotes of the day : {}".format(msg.payload))


client = paho.Client(protocol=paho.MQTTv31)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe('quotes', qos=0)
client.loop_forever()


