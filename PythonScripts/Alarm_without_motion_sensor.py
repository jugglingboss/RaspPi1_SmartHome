import time
import random
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


while True:
    
    x=True
    while x==True:
        file=open('/var/www/html/Data.txt')
        lines = file.readlines()
        if len(lines) != 3:
            print(len(lines))
            print(datetime.datetime.now())
            file.close()
        else:
            x=False
            


    Alarm = lines[2].split(":")
    #print(lines[2])
    if Alarm[0]=="Off":
        Alarm=["26","99"]


    hourtm = datetime.datetime.now()

    if hourtm.hour==int(Alarm[0]):
        if hourtm.minute==int(Alarm[1]):
            print("blinds")
            publish.single("Blinds", "0",hostname="localhost")
            client = mqtt.Client()
            client.connect("localhost",1883,60)
            client.publish("topic/test", "cycle");
            client.disconnect()
            time.sleep(60)


