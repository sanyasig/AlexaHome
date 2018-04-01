import requests

import config_parser


def trigger(topic=None, details=None):
    key = config_parser.read_config().get('ifttt', 'key')
    url = "https://maker.ifttt.com/trigger/" + str(details) +"/with/key/" + str(key)
    print(url)
    r = requests.post(url)
    print(r.status_code)




