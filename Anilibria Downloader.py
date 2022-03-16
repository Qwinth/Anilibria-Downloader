# by Mr.Qwinth
import os
import urllib
import AniParse
import ffmpy
aniurl = str()
foldpath = str()
headers = {'User-Agent':'Anilibria Downloader'}
def download(path, pn):
    video = bytes()
    url = '/'.join(path.split('/')[:-1])
    name = (aniurl.split('/')[-1].split('.')[0] + '_episode_' + pn + '_' +  _quality).replace('-', '_')
    if path[:4] == 'http':
        playlist = urllib.request.urlopen(urllib.request.Request(path, headers=headers)).read().decode()
        playlist = playlist.split('\n')[:-1]
        for i in playlist:
            if i[0] != '#':
                print('Downloading:', url + '/' + i)
                fragment = urllib.request.urlopen(urllib.request.Request(url + '/' + i, headers=headers)).read()
                video += fragment
        print('Writing...')
        try:
            file = open(foldpath + name + '.ts', 'wb')
        except:
            os.remove(foldpath + name + '.ts')
            file = open(foldpath + name + '.ts', 'wb')
        file.write(video)
        file.close()
        #subprocess.call(['attrib', '+h', foldpath + name + '.ts'])      
        print('Correcting and converting...')
        ffmpy.FFmpeg(inputs={foldpath + name + '.ts': None}, outputs={foldpath + name + '.mp4': None}).run()
        os.remove(foldpath + name + '.ts')
        print('Done!')


while True:
    video = bytes()
    aniurl = input('Input anime page url: ')
    series = input('Series: ')
    foldpath = input('Save to: ') + '/'
    parsed_data = AniParse.parse(aniurl)
    
    if '-' in series:
        _quality = input(f'Quality {" ".join(AniParse.format(parsed_data, series.split("-")[0])[0])}: ')
        for i in range(int(series.split('-')[0]), int(series.split('-')[1]) + 1):
            format_data = AniParse.format_data(parsed_data, str(i))
            url = format_data[1][format_data[0].index(_quality)]
            download(url, str(i))

    elif ',' in str(series):
        _quality = input(f'Quality {" ".join(AniParse.format(parsed_data, series.split(",")[0])[0])}: ')
        for i in range(int(series.split(',')[0]), int(series.split(',')[1]) + 1):
            format_data = AniParse.format_data(parsed_data, str(i))
            url = format_data[1][format_data[0].index(_quality)]
            download(url, str(i))

    else:
        format_data = AniParse.format_data(parsed_data, series)
        _quality = input(f'Quality {" ".join(format_data[0])}: ')
        url = format_data[1][format_data[0].index(_quality)]
        download(url, series)
