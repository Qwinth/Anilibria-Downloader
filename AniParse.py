import requests
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import unquote
def parse(url):
    print('Parsing html: '+url)
    data = {}
    urlhigh = str()
    qualityhigh = str()
    urllow = str()
    qualitylow = str()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    tags = soup.find_all(text=re.compile('Playerjs'))
    for tag in tags[0].split(',')[2:-2]:
        try:
            if ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[1] != ' ':
                try:
                    urlhigh = ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[1].split('//')[1].split("'")[0]
                    qualityhigh = ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[1].split('//')[0]
                    if qualityhigh == '[1080p]':
                        num = int(urlhigh.split('/')[4].split('-')[0])
                    else:
                        num = int(urlhigh.split('/')[4])
                except:
                    pass
        except:
            if ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[0] != ' ':
                try:
                    urllow = ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[0].split('//')[1].split("'")[0]
                    num = int(urllow.split('/')[4].split('-')[0])
                    qualitylow = ''.join(tag.split('download:')[0].split('}')[0].split('file:')[0].split("{'title':")[0].split('\n')).split(" 'file':'")[0].split('//')[0]
                    
                except:
                    pass
        if urlhigh and urllow:
            data[num] = {qualityhigh[1:-1]:'http://' + urlhigh, qualitylow[1:-1]:'http://' + urllow}
    return data
