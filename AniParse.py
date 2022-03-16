import requests
from bs4 import BeautifulSoup
import re
def parse(url):
    print('Parsing html: '+url)
    data = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    tags = soup.find_all(text=re.compile('Playerjs'))
    for tag in tags[0].split(',')[2:-2]:
        try:
            if ''.join(tag.split('"download":')[0].split('{"id"')[0].split('"title"')[0].split('"file":"')).split('"poster"')[0].replace('"', '').replace(r'\/\/', '//').replace(r'\/', '/') != '':
                url = ''.join(tag.split('"download":')[0].split('{"id"')[0].split('"title"')[0].split('"file":"')).split('"poster"')[0].replace('"', '').replace(r'\/\/', '//').replace(r'\/', '/').split('https://')[1]
                quality = ''.join(tag.split('"download":')[0].split('{"id"')[0].split('"title"')[0].split('"file":"')).split('"poster"')[0].replace('"', '').replace(r'\/\/', '//').replace(r'\/', '/').split('https://')[0][1:-1]
                sernum = url.split('/')[5]
                data.setdefault(sernum, [])
                data[sernum].append({quality:'https://' + url})
        except:
            pass
    
    return data


def format_data(data, sernum):
    num = 0
    quality = []
    url = []
    for i in data[sernum]:
        quality += i.keys()
        url.append(i[quality[num]])
        num += 1
    return (quality, url)
