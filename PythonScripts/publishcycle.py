import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "cycle");
client.disconnect();

