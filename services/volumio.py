import json
import requests

def playlist(topic=None, details=None):
    ip = None
    all_details = json.loads(details)

    ip = all_details.get('ip')
    name = all_details.get('playlist')

    url = "http://" +str(ip) + "/api/v1/commands/?cmd=playplaylist&name=" + str(name)
    print url
    r = requests.get(url)
    print r.status_code


    print ""
