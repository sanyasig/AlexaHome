from services.firestrick_service import FireStick
import json

def restart(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    stick.restart()

def kodi(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    #stick.turn_off_youtube()
    stick.turn_on_kodi()

def youtube(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    stick.turn_on_youtube()