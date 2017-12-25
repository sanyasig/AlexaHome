import config_parser
from messaging.launcher import HomeMessager
import ssh as ssh
import paramiko, getpass, re, time

from services import Utils

if __name__ == "__main__":
   print "runing a test intents"
   Utils.execute_remote_command()