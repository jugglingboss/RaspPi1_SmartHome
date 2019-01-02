import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
#print("sending 0...")
publish.single("Blinds", "0",hostname="localhost")

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "cycle");
client.disconnect();