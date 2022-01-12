import requests
import AniParse
aniurl = str()

def download(path):
    video = bytes()
    url = '/'.join(path.split('/')[:-1])
    name = aniurl.split('/')[-1].split('.')[0] + '-episode-' + series + '-' +  _quality + '.ts'
    if path[:4] == 'http':
        playlist = requests.get(path).text
        playlist = playlist.split('\n')[:-1]
        for i in playlist:
            if path.split('/')[2] == 'static.libria.fun':
                while True:
                    parsed_data = AniParse.parse(aniurl)
                    path = parsed_data[int(series)][_quality]
                    playlist = requests.get(path).text
                    playlist = playlist.split('\n')[:-1]
                    if  path.split('/')[2] != 'static.libria.fun':
                        break
            if i[0] != '#':
                print('Downloading:', url + '/' + i)
                fragment = requests.get(url + '/' + i).content
                video += fragment
        print('Writing...')
        file = open(name, 'wb')
        file.write(video)
        file.close()
        print('Done!')


while True:
    video = bytes()
    aniurl = input('Input anime page url: ')
    series = input('Series: ')
    parsed_data = AniParse.parse(aniurl)
    low, high = parsed_data[int(series)].keys()
    _quality = input(f'Quality: {low} or {high}: ')
    if len(series) == 1:
        url = parsed_data[int(series)][_quality]
        download(url)
