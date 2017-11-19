
import paho.mqtt.client as paho
import random


def get_names(names):
    with open(names) as f:
        names = f.read()
    return names.split("\n")

def print_skull():
    
    print('''

       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \

            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
'''
)

class MQTTChat:
    def __init__(self):
        self.names = get_names("names.txt")
    
    def on_connect(self, client, userdata, flags, rc):

        print("Group chat connected with server")

    def on_disconnect(self, client, userdata, rc):
        print("Super chat Closed")
        print("Disconnected")

    def on_message(self, client, userdata, msg):
        name = random.sample(self.names, 1)
        print("{}:  {}".format(name[0], msg.payload.decode("utf-8")))

def main():

    print ("Welcome to SuperChat")
    print ("#"*15)
    print_skull()
    mqtt = MQTTChat()
    client = paho.Client(protocol=paho.MQTTv31)
    client.on_connect = mqtt.on_connect
    client.on_disconnect = mqtt.on_disconnect
    client.on_message = mqtt.on_message

    client.connect("192.168.0.21", 1883, 60)
    client.subscribe('superchat', qos=0)
    client.loop_forever()

if __name__ == "__main__":
    main()

# Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)

