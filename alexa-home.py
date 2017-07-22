import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import messaseManager


app = Flask(__name__)
ask = Ask(app, "/alexa/home")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.route('/alexa')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Skills Kit, you can say hello'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Hello world'
    return statement(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('FIREAPPP',  convert={'App': str, 'Action': str})
def lauch_app(App, Action):
    action_word = "stop:"+App

    if Action in ["start", "lauch", "turnon", "turn on"]:
        action_word = "start:" + App

    messaseManager.send("home/adb", action_word)
    speech_text = 'app launching!'
    return statement(speech_text).simple_card('FIREAPPP', speech_text)

@ask.intent('PCOFF')
def shutdown_PC():
    messaseManager.send("home/pc", "off")
    speech_text = 'Turinng off your laptop'
    return statement(speech_text).simple_card('PCOFF', speech_text)

@ask.intent('PLAY')
def shutdown_PC():
    messaseManager.send("home/adb", "play")
    speech_text = 'ok'
    return statement(speech_text).simple_card('PLAY', speech_text)


@ask.intent('PAUSE')
def shutdown_PC():
    messaseManager.send("home/adb", "pause")
    speech_text = 'ok'
    return statement(speech_text).simple_card('PAUSE', speech_text)





@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
