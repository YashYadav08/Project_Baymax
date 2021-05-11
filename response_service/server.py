#NOTE : This script handles :
# 1. real time processing of data from device for all users registered in the database
# 2. pushing notifications to emergency contacts with location
# 3. writing data to database at regular intervals
# 4. multithreading for users(aysynchronousity)
# 5. classification of detectable critical situations(stroke,seizure,all other such cases we can detect from available sensors)
#  how to detect seizure 
# write an api to send data

import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('Recieved message')
    data=msg.payload.decode("utf-8")
    data=json.loads(data)
    print(data)     #change this to json
    



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

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic1")


# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()