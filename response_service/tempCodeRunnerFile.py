def on_message(client, userdata, msg):
   data=msg.payload.decode("utf-8")
   data=json.loads(data)
   for key,val in data:
       print(key+' : '+val)
