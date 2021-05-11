#this script simulates the connected wearable device
#to be run as a seperate container
# TODO : decide on data format to send
# TODO : generate random values fitting data format


import paho.mqtt.client as mqtt
import json
import random
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

def on_message(client, userdata, msg):
    #continue
    print('Recieved Message')
    print(msg.payload.decode("utf-8"))


# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("client", "Client1234")

# connect to HiveMQ Cloud on port 8883
client.connect("bca34a4c6dda4adc808decdcbc2a56b5.s1.eu.hivemq.cloud", 8883)

device_id="1"

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic"+device_id)

#temperature is taken in celcius
data={'hr':random.randrange(75,200),'spo2_level':random.uniform(0,1),'body_temperature':random.randrange(35,40),'hours_of_sleep':random.randrange(6,10)}
data=json.dumps(data)

# publish data to the topic "my/test/topic/device_id"
client.publish("my/test/topic"+device_id,data)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()