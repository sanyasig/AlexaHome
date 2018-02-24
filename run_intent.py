import data_manager
from messaging import mqtt_publish
from services import ifttt

if __name__ == "__main__":
   ifttt.trigger("", "socket1-on")
