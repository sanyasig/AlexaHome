import broadlink
import time

import data_manager
from services.parent_service import ParentService

class RMBroadLInk(ParentService):

    def __init__(self, ip = None):
        self.ip = ip

    def get_function(self, message=None):
        split_message = message.split("_")
        return_fuction = None
        if len(split_message) > 1:
            if (split_message[1] == "tv"):
                if split_message[2] == "on":
                    print "turing on TV"
                    return_fuction = self.toggle_power
                else:
                    print "turing off youtube"
                    return_fuction = self.toggle_power

        return return_fuction

    def toggle_power(self):
        device = broadlink.rm(host=(self.ip, 80), mac=bytearray.fromhex("34ea344298bf"))
        print "Connecting to Broadlink device...."
        device.auth()
        time.sleep(1)
        print "Connected...."
        time.sleep(1)
        device.host
        codeData = "26008c009694133713371436141213121312131213121337133713371312141114111412131213121337131213121312131213121312133714111436143713371337133713371300060d949611391139113a111411141114111411141139113911391114111510151114111411141139111411141114111411141213113a1015103a1139113911391139113911000d05000000000000000000000000"
        device.send_data(codeData.decode('hex'))
        data_manager.toggel_state("main_tv")


