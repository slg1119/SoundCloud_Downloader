__author__ = 'RokHyung Son'
# -*- coding: utf-8 -*-
import urllib
import json
import os


soundcloudurl = raw_input("SoundCloud URL: ")


def finduser():
    try:
        url = json.load(urllib.urlopen('http://api.soundcloud.com/resolve.json?url=' + soundcloudurl + '&client_id=YOUR_CLIENT_ID'))
        usercode = url['uri']
        print usercode
        return usercode
    except KeyError:
        print 'Please input right url'
        exit()

def dwn():
    url = json.load(urllib.urlopen(finduser() + '/tracks.json?client_id=YOUR_CLIENT_ID'))
    for parsing in url:
        if 'errors' in url:
            parsing = json.load(urllib.urlopen(finduser() + '?client_id=YOUR_CLIENT_ID'))
        print 'Download mp3file'
        title = parsing['title']
        stream_url = parsing['stream_url'] + '?client_id=YOUR_CLIENT_ID'
        target = open('tmp.mp3', "wb")
        print 'Downloading:' + title
        urllib.urlretrieve(stream_url,'tmp.mp3')
        os.rename('tmp.mp3', title+'.mp3')

dwn()