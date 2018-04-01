import logging
from pathlib import Path



home_dir = home = str(Path.home()) + "/alexa-home.log"
logging.basicConfig(filename=home_dir,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def log(message):
     logging.debug(str(message))