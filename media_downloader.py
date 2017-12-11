# get valid title https://api.themoviedb.org/3/search/movie?api_key=6185e808668fae673a5665b757c6d099&query=Jack+Reacher
import requests
import json
import urllib
from bs4 import BeautifulSoup, Tag
import transmissionrpc
from threading import Thread
import subprocess

from urllib3.util import request


def download_title(title):

    print("get actual name")
    # get torrent file
    details = send_http_requuest("https://api.themoviedb.org/3/search/movie?api_key=6185e808668fae673a5665b757c6d099&query="+title, 0, 0)
    title = details['results'][0]['title']
    year =  details['results'][0]['release_date'].split('-')[0]
    print  title + " " + year
    t_magent = getSkyTorrentMagent(title, year)
    tc = transmissionrpc.Client('192.168.0.17', port=9091, user='nani', password='nanipi')
    tc.add_torrent(t_magent)
    print tc.get_torrents()

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

def get_telugu_list():
    base_url = 'http://www.movierulz.ms/telugu-movie/'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "lxml")

    for tag in soup.find_all("dd"):
        if (isinstance(tag, Tag) & tag.attrs.has_key('class')):
            if('wp-caption-text' in tag.attrs['class']):
                test = tag.contents[0]
                print test.replace("(Telugu)", "").strip()

def clear_youttube_playlist():
        test_key = "AIzaSyC9H0Gl5cbgX_vniQ39D0ABFiN4xf8to8Y"
        base_url = "https://www.googleapis.com/youtube/v3/playlistItems?maxResults=50&playlistId=PL7Wn10dWKB2zYQvjdAX7HshQ3xYIRC-zE&part=snippet&key=" + test_key
        song_list = send_http_requuest(base_url, 0, 0)
        for items in song_list['items']:
            video_id = items['snippet']['resourceId']['videoId']


def download_youtube_playlist():
    t = Thread(target=send_download_request, args=(9,))
    t.start()
    return "Downloading"

def send_download_request(i):
    p = subprocess.Popen('ssh -t nani@192.168.0.22 python /home/nani/work/getYoutube_playlist.py', shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()


