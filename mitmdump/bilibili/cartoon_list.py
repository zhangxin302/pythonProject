"""
author:张鑫
date:2021/5/8 10:18
"""
import json
import requests
import time
import random

from tools.headers import headers

url = 'https://api.bilibili.com/pgc/season/index/result?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&area=-1&build=6140500&c_locale=zh_CN&channel=yingyongbao&copyright=-1&is_finish=-1&mobi_app=android&order=3&page=3&pagesize=21&platform=android&s_locale=zh_CN&season_month=-1&season_status=-1&season_type=1&season_version=-1&sort=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&style_id=-1&ts=1620439623&type=0&year=-1&sign=5ec3f501f61821fa39a9dcf582defe84'
html = requests.get(url=url,headers=headers,verify=False).json()

for item in html['data']['list']:
    title = item['title']
    order = item['order']
    print(title)
    print(order)
