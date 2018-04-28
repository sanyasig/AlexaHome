import ahlogger
from services.rmBroadLinkService import RMBroadLInk

if __name__ == "__main__":
   broadlink = RMBroadLInk('192.168.0.17')
   broadlink.toggle_power()
