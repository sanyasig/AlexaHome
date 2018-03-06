from services import *
import os
import json

from services import tv, ifttt, firetv, dash, volumio


def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        print "topic: " + topic
        print "status " + message

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

        func = getattr(module, topic.split("/")[2])
        func(topic, message)

    except :
        print "Cannto find service"

    # print "mesage: " + message
    # service = Utils.getService(topic)
    # execution = service.get_function(message)
    # execution = service.get_function(message)
    #
    # if(execution != None):
    #     result =  execution()
    #     print result


