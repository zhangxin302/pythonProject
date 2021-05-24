"""
author:张鑫
date:2021/5/4 19:44
data>list>(index_show,order,title,title_icon)
https://api.bilibili.com/pgc/season/index/result?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&area=-1&build=6140500&c_locale=zh_CN&channel=yingyongbao&copyright=-1&is_finish=-1&mobi_app=android&order=3&page=1&pagesize=21&platform=android&s_locale=zh_CN&season_month=-1&season_status=-1&season_type=1&season_version=-1&sort=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&style_id=-1&ts=1620440132&type=0&year=-1&sign=de5f771bb37b191b2b8776aca5b71d6f
https://api.bilibili.com/pgc/season/index/result?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&area=-1&build=6140500&c_locale=zh_CN&channel=yingyongbao&copyright=-1&is_finish=-1&mobi_app=android&order=3&page=2&pagesize=21&platform=android&s_locale=zh_CN&season_month=-1&season_status=-1&season_type=1&season_version=-1&sort=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&style_id=-1&ts=1620439618&type=0&year=-1&sign=5ed522045365d227a09547d48e1162ad
https://api.bilibili.com/pgc/season/index/result?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&area=-1&build=6140500&c_locale=zh_CN&channel=yingyongbao&copyright=-1&is_finish=-1&mobi_app=android&order=3&page=3&pagesize=21&platform=android&s_locale=zh_CN&season_month=-1&season_status=-1&season_type=1&season_version=-1&sort=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&style_id=-1&ts=1620439623&type=0&year=-1&sign=5ec3f501f61821fa39a9dcf582defe84
https://api.bilibili.com/pgc/season/index/result?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&area=2&build=6140500&c_locale=zh_CN&channel=yingyongbao&copyright=-1&is_finish=-1&mobi_app=android&order=3&page=1&pagesize=21&platform=android&s_locale=zh_CN&season_month=-1&season_status=-1&season_type=1&season_version=-1&sort=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&style_id=-1&ts=1620128335&type=0&year=-1&sign=58e7df38ebf42669079a54556ba59b97
"""
import pymongo
import time
import random
import json

database = pymongo.MongoClient('localhost', port=27017)
db = database['bilibili']
cartoon_list = db['cartoon_list']


def response(flow):
    if 'api.bilibili.com/pgc/season/index/result' in flow.request.url:
        for item in json.loads(flow.response.text)['data']['list']:
            time.sleep(random.randint(1, 5))
            cartoon = {}
            cartoon['title'] = item['title']
            cartoon['title_icon'] = item['title_icon']
            cartoon['index_show'] = item['index_show']
            cartoon['order'] = item['order']
            # results = cartoon_list.count({'title': cartoon['title']})
            # if results == 0:
            print('**********************************')
            print(item)
            cartoon_list.insert(cartoon)
            print(cartoon)
            print('**********************************')
            #     results += 1
            # else:
            #     print('数据已存在')
