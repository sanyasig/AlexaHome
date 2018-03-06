import data_manager
from messaging import mqtt_publish
from services import ifttt, firetv, dash, volumio
import json

if __name__ == "__main__":
   MQTT_MSG = json.dumps({"playlist": "morning", "ip": "192.168.0.24"});
   volumio.playlist("", MQTT_MSG)
