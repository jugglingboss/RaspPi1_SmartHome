import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
#print("sending 2...")
publish.single("Blinds", "2",hostname="localhost")


client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "darkness");
client.disconnect();