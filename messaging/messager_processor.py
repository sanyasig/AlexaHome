from services import *
import os
import json
import ahlogger

from services import tv, ifttt, firetv, dash, volumio, alerts, audio


def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        ahlogger.log("topic: " + topic)
        ahlogger.log("status " + str(message))

        if("tv" in topic):
            module = tv
        if ("ifttt" in topic):
            module = ifttt
        if ("firetv" in topic):
            module = firetv
        if ("dash" in topic):
            module = dash
        if ("volumio" in topic):
            module = volumio
        if ("alerts" in topic):
            module = alerts
        if ("audio" in topic):
            module = audio

        func = getattr(module, topic.split("/")[2])
        func(topic, message)

    except :
        ahlogger.log("Cannto find service")

    # ahlogger.log "mesage: " + message
    # service = Utils.getService(topic)
    # execution = service.get_function(message)
    # execution = service.get_function(message)
    #
    # if(execution != None):
    #     result =  execution()
    #     ahlogger.log result


