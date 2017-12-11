from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from dateutil import parser


try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_home_controller_events():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    page_token = None

    while True:
        events = service.events().list(calendarId='gpkf2puham77c5gn8ra8e4t7r4@group.calendar.google.com', pageToken=page_token).execute()
        message = ""
        for event in events['items']:
            e_date = None
            start = event["start"]
            if start.has_key("dateTime"):
                e_date = start["dateTime"]
            if start.has_key("date"):
                e_date = start["date"]
            e_summary = event["summary"]
            parsed_date = parser.parse(e_date)
            weekday = parsed_date.strftime("%A")
            day = parsed_date.day
            month = parsed_date.strftime("%B")
            message =  message + "on " + weekday + " " + str(day) + " " + month + " there is  " + e_summary + ". \n"

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return message
