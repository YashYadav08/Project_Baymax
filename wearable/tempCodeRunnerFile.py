
client = mqtt.Client()                                                      # client object
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)                           # enable TLS

client.username_pw_set("client", "Client1234")                              # set username and password

client.connect("bca34a4c6dda4adc808decdcbc2a56b5.s1.eu.hivemq.cloud", 8883) # connect to HiveMQ Cloud on port 8883

device_id="1"

client.subscribe("my/test/device"+device_id)                                # subscribe to the topic "my/device/topic"
