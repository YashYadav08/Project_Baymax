#NOTE : This script handles :
# 1. real time processing of data from device for all users registered in the database(Done)
# 2. pushing notifications to emergency contacts with location
# 3. writing data to database at regular intervals(Done)
# 4. classification of detectable critical situations(stroke,seizure,all other such cases we can detect from available sensors)
# NOTE : this code(functionality) runs in the mobile device (yes,we should have made an app but for now this is ok)

import paho.mqtt.client as mqtt
import json
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import date
from call import call


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('Recieved message!')
    conn = psycopg2.connect(database="sensor_data2", user="postgres", password="Ironman@3142", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    data=msg.payload.decode("utf-8")
    data=json.loads(data)
    print(data)    



    today = date.today()
    d = today.strftime("%d/%m/%Y")

    print(type(d))
    file1 = open("data.txt","r")  
    user_id = file1.read() 
    file1.close() 

    cur.execute("INSERT INTO HEALTH_DATA2 (USER_ID,HR,BLOOD_OXYGEN_LEVEL,TEMPERATURE,BP_SYSTOLIC,BP_DIASTOLIC,DATE_TIME) \
      VALUES ({},{},{},{},{},{},{})".format(user_id,data['hr'],data['blood_oxygen_level'],data['body_temperature'],data['blood_pressure_systolic'],data['blood_pressure_diastolic'],d));    

    condition = ""
    to_number = "+919057014880"     #modify this to get nearest ambulance number
    
    conn2 = psycopg2.connect(database="User_Data2", user="postgres", password="Ironman@3142", host="127.0.0.1", port="5432")
    cur2 = conn.cursor()
    cur2.execute("SELECT * from User_Data2 where USER_ID={}".format(user_id))
    rows = cur2.fetchall()
    user_age = rows[0]['AGE']
    user_name = rows[0]['NAME']
    call_needed = False

    if data['hr']>=(220-user_age):
        condition = "Tachycardia"
        call_needed = True 
    elif data['hr']<40:
        condition = "Bradycardia"
        call_needed = True
    elif data['blood_oxygen_level']<0.6:
        condition = "Hypoxemia"
        call_needed = True
    elif data['body temperature']<35:
        condition = "Hypothermia"
        call_needed = True
    elif data['body temperature']>42:
        condition = "Hyperthermia"
        call_needed = True
    elif data['blood_pressure_systolic']<90 or data['blood_pressure_diastolic']<60:
        condition = "Hypotension"
        call_needed = True
    elif data['blood_pressure_systolic']>140 or data['blood_pressure_diastolic']<90:
        condition = "Hypertension"
        call_needed = True
    if call_needed:
        location = ""           #find location
        message = "Alert! User {} is suffering from {} at location {}".format(user_name,condition,location)
        call(to_number,message)
    
    conn.commit()
    conn.close()
    print('Insertion Complete!')
    
    file1 = open("data.txt","w")  
    file1.write(str(int(user_id)+1)) 
    file1.close() 


if __name__=="__main__":
    client = mqtt.Client()                                                      # client object
    client.on_message = on_message

    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)                           # enable TLS

    client.username_pw_set("client", "Client1234")                              # set username and password

    client.connect("bca34a4c6dda4adc808decdcbc2a56b5.s1.eu.hivemq.cloud", 8883) # connect to HiveMQ Cloud on port 8883

    device_id="1"

    client.subscribe("my/test/device"+device_id)                                # subscribe to the topic "my/device/topic"

    client.loop_forever()                                                       # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
