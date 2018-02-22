import data_manager
from messaging import mqtt_publish

if __name__ == "__main__":
   print "runing a test intents"
   data_manager.toggel_state("main_tv")
   mqtt_publish.send("test", "asd")

