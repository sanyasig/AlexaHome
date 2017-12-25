from services import Utils
from services.firestrick_service import FireStick


def process_message(topic=None, message=None):
    print "topic: " + topic
    print "mesage: " + message

    service = Utils.getService(topic)
    execution = service.get_function(message)

    if(execution != None):
        result =  execution()
        print result


