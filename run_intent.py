import ahlogger
from services.hue_service import HueService
from services.lifx_service import LifxService
from services.mopidy_service import MopidyService
from services.rmBroadLinkService import RMBroadLInk
import platform
import services.dash
import json

if __name__ == "__main__":

   services = RMBroadLInk(ip="192.168.0.17")
  # services.clear_tracklist()
   services.turn_on_bt_audio()



   # button_name = "andex"
   # MQTT_MSG = json.dumps({"name": button_name, "bulb_name": "bedroom"})
   #
   # print(platform.python_version())
   # service = HueService('192.168.0.10')
   # message = {}
   # message['name'] = 'kitchen'
   # value = service.get_function(message)
   # value()