import configparser
import  os

config = 0;

def read_config():
    config = configparser.ConfigParser()
    print(config.sections())
    config.read(os.path.expanduser('~') + '/work/alexa_settings.ini')
    return config


def get_config(type):
    config = read_config()
    return {
        'youtube': config['youtube'],
        'b': 2,
    }[type]



