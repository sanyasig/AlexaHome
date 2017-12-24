import subprocess

class FireStick():

    ip = None

    stop_kodi="adb shell am force-stop org.xbmc.kodi"
    start_kodi="adb shell am start -n org.xbmc.kodi/.Splash"
    start_youtube="adb shell am start -n org.chromium.youtube_apk/.YouTubeActivity"
    stop_youtube="adb shell am force-stop org.chromium.youtube_apk"

    def __init__(self, ip = None):
        self.ip = ip

    def restart(self):
        print "restarting Firestick"
        self.reconnect()
        self.run_bash_command("adb reboot")
        self.dissconnect()

    def turn_on_youtube(self):
        self.reconnect()
        self.run_bash_command(self.stop_kodi)
        self.run_bash_command("sleep 1")
        self.run_bash_command(self.start_youtube)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_off_youtube(self):
        self.reconnect()
        self.run_bash_command(self.stop_youtube)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_on_kodi(self):
        self.reconnect()
        self.run_bash_command(self.stop_youtube)
        self.run_bash_command("sleep 1")
        self.run_bash_command(self.start_kodi)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_off_kodi(self):
        self.reconnect()
        self.run_bash_command(self.stop_kodi)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def run_bash_command(self, bashCommand):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

    def reconnect(self):
        self.run_bash_command("adb kill-server")
        self.run_bash_command("adb start-server")
        self.run_bash_command("adb connect " + self.ip)

    def dissconnect(self):
        self.run_bash_command("adb kill-server")