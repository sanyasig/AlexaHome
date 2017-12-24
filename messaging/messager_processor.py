from services.firestrick_service import FireStick


def process_message(topic=None, message=None):
    print "topic: " + topic
    print "mesage: " + message
    if topic == "home/adb":
        topic_adb(message)


def topic_adb(message=None):

    firestick = FireStick("192.168.0.6 ")
    split_message = message.split("_")

    if split_message.length > 1:
        if(split_message[1] == "youtube"):
            if split_message[2] == "on" :
                print "turing on youtube"
                firestick.turn_on_youtube()
            else:
                print "turing off youtube"
                firestick.turn_off_youtube()

        elif(split_message[1] == "kodi"):
            if split_message[2] == "on" :
                print "turing on kodi"
                firestick.turn_on_kodi()
            else:
                print "turing off kodi"
                firestick.turn_off_kodi()
