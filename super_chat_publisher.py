import subprocess
import shlex
from paho.mqtt import client as paho

def execute_shell_with_stdout(command, exception=[]):
    command = shlex.split(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = p.communicate()
    exception.append(0)
    if p.returncode not in exception:
        raise OSError()
    return output, error

def on_connect(client, userdata, flags, rc):
    print (" I am conneting")

def on_disconnect(client, userdata, rc):
    print (" I am disconneting")

def on_getting(client , userdata, msg):
    if msg.payload == "poweroff":
        execute_shell_with_stdout("sudo reboot")

client = paho.Client(protocol=paho.MQTTv31)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_getting

client.connect("192.168.0.21", 1883, 60)
client.subscribe('home', qos=2)
client.loop_forever()
