import paho.mqtt.client as mqtt
import json

from messaging.messager_processor import process_message


class HomeMessager():

    pi_ip = None

    def __init__(self, ip = None):
        self.pi_ip = ip

    def launch(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.pi_ip)
        client.loop_forever()

    def on_message(self, client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)
        process_message(message.topic, message.payload)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        print("subscribing to home/#")
        client.subscribe("home/#")

def start_process(ip= None):
    messager = HomeMessager(ip)
    messager.launch()