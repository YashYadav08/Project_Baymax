#this script simulates the connected wearable device ( device_id = 1 )

import paho.mqtt.client as mqtt
import json
import random
import time


def on_message(client, userdata, msg):
    #continue
    print('Recieved Message')
    print(msg.payload.decode("utf-8"))



client = mqtt.Client()                                                      # client object
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)                           # enable TLS

client.username_pw_set("client", "Client1234")                              # set username and password

client.connect("bca34a4c6dda4adc808decdcbc2a56b5.s1.eu.hivemq.cloud", 8883) # connect to HiveMQ Cloud on port 8883

device_id="1"


client.subscribe("my/test/device"+device_id)                                # subscribe to the topic "my/device/topic"


def publishData():
    # NOTE : all metrics are imperial
    data = {'hr':random.randrange(50,200),
            'blood_oxygen_level':random.uniform(0,1),
            'body_temperature':random.randrange(35,40),
            'blood_pressure_systolic':random.randrange(60,90),
            'blood_pressure_diastolic':random.randrange(90,140)
            }

    data=json.dumps(data)
    
    client.loop_start()                                                         #starts a background thread to handle the network traffic
    
    client.publish("my/test/device"+device_id,data)                             # publish data to the topic "my/test/device+device_id"

    client.loop_stop()                                                          # stops the background thread

if __name__=="__main__": 
    while True:
        time.sleep(10)
        publishData()
        