from services.firestrick_service import FireStick
from services.rmBroadLinkService import RMBroadLInk
import time
import  json

def kodi(topic=None, details=None):
    ## turm on tv
    RMBroadLInk().toggle_power()
    time.sleep(10)
    FireStick().turn_on_kodi()
    print ("in tv platform")

def youtube(topic=None, details=None):
    ## turm on tv
    RMBroadLInk().toggle_power()
    time.sleep(10)
    FireStick().turn_on_kodi()
    print ("in tv platform")

def itself(topic=None, details=None):
    my_dict = json.loads(details)
    new_state = my_dict.get("state", None)
    if ("on" in new_state):
        RMBroadLInk().toggle_power()
    else :
        RMBroadLInk().toggle_power()
