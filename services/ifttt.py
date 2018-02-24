import requests

def trigger(topic=None, details=None):
    url = "https://maker.ifttt.com/trigger/" + str(details) +"/with/key/dUtzt_YIPoeVmj3DuemRom"
    print url
    r = requests.post(url)
    print r.status_code




