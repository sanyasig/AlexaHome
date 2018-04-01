
import paho.mqtt.publish as publish

def send(topic, message):
    print("sending " +message + " to " + topic)
    publish.single(topic, message, hostname="192.168.0.17")

