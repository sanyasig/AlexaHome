import ahlogger
from services.hue_service import HueService
from services.lifx_service import LifxService
from services.rmBroadLinkService import RMBroadLInk
import platform
import services.dash

if __name__ == "__main__":
   print(platform.python_version())

   service =  HueService('192.168.0.10')
   message = {}
   message['name'] = 'kitchen'

   value = service.get_function(message)
   value()
