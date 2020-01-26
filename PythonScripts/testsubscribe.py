import paho.mqtt.client as mqtt
import time
import datetime
# This is the Subscriber
path = '/var/www/html/Data.txt';
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "sunlight":
    print("sunlight")
    print(datetime.datetime.now())
    with open(path) as f:
        newText=f.read().replace('Blinds are Closed', 'Blinds are Opening')

    with open(path, "w") as f:
        f.write(newText)
        
    time.sleep(16)
    
    with open(path) as f:
        newText=f.read().replace('Blinds are Opening', 'Blinds are Opened')

    with open(path, "w") as f:
        f.write(newText)
    #client.disconnect()
  if msg.payload.decode() == "darkness":
    print ("darkness")
    print(datetime.datetime.now())
    with open(path) as f:
        newText=f.read().replace('Blinds are Opened', 'Blinds are Closing')

    with open(path, "w") as f:
        f.write(newText)
        
    time.sleep(12.9)
    
    with open(path) as f:
        newText=f.read().replace('Blinds are Closing', 'Blinds are Closed')

    with open(path, "w") as f:
        f.write(newText)
  if msg.payload.decode() == "cycle":
    print ("cycle")
    print(datetime.datetime.now())
    with open(path) as f:
        newText=f.read().replace('Blinds are Closed', 'Blinds are Opening')

    with open(path, "w") as f:
        f.write(newText)
        
    time.sleep(16)
    
    with open(path) as f:
        newText=f.read().replace('Blinds are Opening', 'Open on Cycle')

    with open(path, "w") as f:
        f.write(newText)
    time.sleep(300)
    
    with open(path) as f:
        newText=f.read().replace('Open on Cycle', 'Blinds are Closing')

    with open(path, "w") as f:
        f.write(newText)
    time.sleep(12.9)
    
    with open(path) as f:
        newText=f.read().replace('Blinds are Closing', 'Blinds are Closed')

    with open(path, "w") as f:
        f.write(newText)
client = mqtt.Client()
client.connect("10.0.0.200",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()