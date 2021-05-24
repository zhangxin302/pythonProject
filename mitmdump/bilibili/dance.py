'''
data>new>[name,title,pubdate]
https://app.bilibili.com/x/v2/region/dynamic/child/list?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&build=6140500&c_locale=zh_CN&channel=yingyongbao&ctime=972980258&mobi_app=android&platform=android&pull=false&rid=20&s_locale=zh_CN&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&tag_id=0&ts=1620291589&sign=11ac6f060593527559a1d26030c0d527
https://app.bilibili.com/x/v2/region/dynamic/child/list?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&build=6140500&c_locale=zh_CN&channel=yingyongbao&ctime=417895771&mobi_app=android&platform=android&pull=false&rid=20&s_locale=zh_CN&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&tag_id=0&ts=1620291589&sign=439eced9004ac456307f67be5af2b307
https://app.biliapi.net/x/v2/region/dynamic/child/list?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&build=6140500&c_locale=zh_CN&channel=yingyongbao&ctime=289608827&mobi_app=android&platform=android&pull=false&rid=20&s_locale=zh_CN&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&tag_id=0&ts=1620294195&sign=d3157868cae437eb8cfea6ebf376eeae
https://app.biliapi.net/x/v2/region/dynamic/child/list?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&build=6140500&c_locale=zh_CN&channel=yingyongbao&ctime=289608827&mobi_app=android&platform=android&pull=false&rid=20&s_locale=zh_CN&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&tag_id=0&ts=1620294195&sign=d3157868cae437eb8cfea6ebf376eeae
https://app.biliapi.net/x/v2/region/dynamic/child/list?access_key=1c1c28ef37ba0b01717878a56b31eb51&appkey=1d8b6e7d45233436&build=6140500&c_locale=zh_CN&channel=yingyongbao&ctime=18849460&mobi_app=android&platform=android&pull=false&rid=20&s_locale=zh_CN&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.14.0%22%2C%22abtest%22%3A%22%22%7D&tag_id=0&ts=1620294277&sign=cd2b1f74f7ea0382c4d4d13e273edbd1
'''
import pymongo
import json
import random
import time

database = pymongo.MongoClient('localhost', port=27017)
db = database['bilibili']
dance_list = db['dance_list']


def response(flow):
    if 'app.bilibili.com/x/v2/region/dynamic/child/list'in flow.request.url:
        for item in json.loads(flow.response.text)['data']['new']:
            time.sleep(random.randint(1,5))
            dance = {}
            dance['name'] = item['name']
            dance['title'] = item['title']
            dance['pubdate'] = item['pubdate']
            print('*****************************************************')
            print(dance)
            dance_list.insert(dance)
            print('*****************************************************')

    elif 'app.biliapi.net/x/v2/region/dynamic/child/list'in flow.request.url:
        for item in json.loads(flow.response.text)['data']['new']:
            time.sleep(random.randint(1,5))
            dance = {}
            dance['name'] = item['name']
            dance['title'] = item['title']
            dance['pubdate'] = item['pubdate']
            print('*****************************************************')
            print(dance)
            dance_list.insert(dance)
            print('*****************************************************')
