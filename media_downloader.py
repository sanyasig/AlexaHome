# get valid title https://api.themoviedb.org/3/search/movie?api_key=6185e808668fae673a5665b757c6d099&query=Jack+Reacher
import requests
import json
import urllib
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup, Tag


def download_title(title):

    print("get actual name")
    # get torrent file
    details = send_http_requuest("https://api.themoviedb.org/3/search/movie?api_key=6185e808668fae673a5665b757c6d099&query="+title, 0, 0)
    title = details['results'][0]['title']
    year =  details['results'][0]['release_date'].split('-')[0]
    print  title + " " + year
    t_magent = getSkyTorrentMagent(title, year)
    print t_magent

    # need to get the torrents link
    return "adding title " + title + "to transmissions"

def send_http_requuest(url , params, type):
    print("sending http request")
    r = requests.get(url)

    if(r.status_code == 200):
        return json.loads(r.text)
    r.status_code


def getSkyTorrentMagent(title, year):
    base_url = "https://www.skytorrents.in"
    q_string = urllib.urlencode({ 'q' : title + ' ' + year})
    url = str(base_url) + "/search/all/ed/1/?l=en-us&" + q_string
    print url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for tag in soup.find_all("td"):
        a = tag.contents
        for each_c in a:
            if isinstance(each_c, Tag):
                if hasattr(each_c, 'attrs'):
                    if each_c.attrs.has_key("href"):
                        test  =  each_c.attrs['href']
                        if str(test).find("magnet:") != -1:
                            return each_c.attrs['href']

