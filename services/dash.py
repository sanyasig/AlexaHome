import config_parser
from services import ifttt, volumio
from services.hue_service import HueService
from services.lifx_service import LifxService

def fiesta(topic=None, details=None):
    #ifttt.trigger("", "socket1-on")
    volumio.playlist(topic, details)

def andrex(topic=None, details=None):
    service = LifxService()
    message = {}
    message['mac'] = 'd0:73:d5:11:cd:17'
    value = service.get_function(message)
    value()

def on(topic=None, details=None):
    service = HueService('192.168.0.10')
    message = {}
    message['name'] = 'kitchen'
    value = service.get_function(message)
    value()