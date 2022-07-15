# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 18:23
# @Author  : hertx
# @Software: PyCharm
# @File    : vip_jx.py
import os.path
import time
from urllib.parse import urljoin
from hertx.httpx import Http
import execjs
from my_thread import ThreadX

http = Http()
http.ignore_status = False


#
def m1907(url):
    with open(r'js/encode.js', 'r') as f:
        ctx1 = execjs.compile(f.read())
        encrypt = ctx1.call('get')
        print(encrypt)
        s1ig = encrypt.get('s1ig')
        z = encrypt.get('z')
    url = url + '&s1ig={}&g='.format(s1ig)
    r = http.get(f'https://a1.m1907.cn:404/api/v/?z={z}&jx={url}', verify=False)
    print(r)
    print(r.json)
    data = r.json.get('data')[0]

    print(data['name'])
    for i in data['source']['eps']:
        print(i['name'], i['url'])
    return r.json


# if __name__ == '__main__':
#     m1907('完美世界')


def 下载文件(url, index):
    r = http.get(url)
    with open(f'video/{index}.mp4', 'wb') as f:
        f.write(r.content)


# if __name__ == '__main__':
#     play_list = m3u8.load('https://new.qqaku.com/20220624/jlr0e6O4/index.m3u8')
#     print(play_list.playlists)
#     url2 = urljoin('https://new.qqaku.com/20220624/jlr0e6O4/index.m3u8', '/20220624/jlr0e6O4/1100kb/hls/playlist_up.m3u8')
#     play_list = m3u8.load(url2)
#     for index, segment in enumerate(play_list.segments):
#         ur = segment.uri
#         print(ur)
if __name__ == '__main__':
    url = 'https://s7.fsvod1.com/20220707/9vE4tWFf/index.m3u8'
    url2 = ''

    r = http.get(url)
    print(r)
    # ext_m3u = r.text.strip()
    # for line in ext_m3u.split('\n'):
    #     if not line.startswith('#'):
    #         url2 = urljoin(url, line)
    # # print(url2)
    # r = http.get(url2)
    # ext_m3u = r.text.strip()
    # # print(ext_m3u)
    # index = 0
    # for item in ext_m3u.split('\n'):
    #     if not item.startswith('#'):
    #         print(urljoin(url, item), index)
    #         # if index == 0:
    #         ThreadX(下载文件, urljoin(url, item), index)
    #         index += 1
