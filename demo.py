# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 11:43
# @Author  : hertx
# @Software: PyCharm
# @File    : img.py
import requests
from hertx.interface.httpx import http, HTTP
from hertx.utils import func_run_times


@func_run_times()
def demo2():
    r = http.get('https://www.qqw21.com/')
    [print(i.get('src'), i.get('alt')) for i in r.xpath('//div[1]//div/ul//a/img')]
    # [print(i) for i in r.xpath('//div[1]//div/ul//a/img/@src')]
    # [print(i) for i in r.xpath('//div[1]/div/div/ul/li/a/img/@alt')]
    [print('https://www.qqw21.com' + i.get('href'), i.text) for i in r.xpath('//*[@id="nav"]//a')]

    [print(i) for i in r.xpath('//*[@id="nav"]//a/@href')]
    [print(i) for i in r.xpath('//*[@id="nav"]//a/text()')]


if __name__ == '__main__':
    demo2()
