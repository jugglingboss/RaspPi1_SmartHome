#this is not in use, called stright from echo code
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
#print("sending 1...")
publish.single("relay", "6",hostname="localhost")