import config_parser
from services import ifttt, volumio


def fiesta(topic=None, details=None):
    #ifttt.trigger("", "socket1-on")
    volumio.playlist(topic, details)