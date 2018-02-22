from services import *
import os
import json

from services import tv


def process_message(topic=None, message=None):
 # TODO: need to fix the dynamic loading of modules
    try:
        print "topic: " + topic
        print "status " + message
        module = None
        if("tv" in topic):
            module = tv

        #tv.kodi("",  "")
        #platform = topic.split("/")[1]
       # module = __import__("services." + platform)
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


