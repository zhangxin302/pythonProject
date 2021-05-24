"""
author:张鑫
date:2021/5/7 15:33
"""
from hashlib import md5

"""
author:张鑫
date:2021/4/19 15:57
"""

import requests, json, pymongo, time

from tools.headers import headers
from tools.转变时间戳 import time_turn

database = pymongo.MongoClient('localhost', port=27017)
db = database['qqmusic']
comments_list = db['comments_list']

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=137106212&g_tk=1176323532&loginUin=1247371788&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=106318183&cmd=8&needmusiccrit=0&pagenum=1&pagesize=25&lasthotcommentid=song_106318183_2097521454_1605715065_396340163_1617634003&domain=qq.com&ct=24&cv=10101010'
response = requests.get(url=url, headers=headers, verify=False)
html = response.json()['comment']['commentlist']

for item in html:
    comments = {}
    # 昵称
    comments['nick'] = item['nick']
    # 评论
    comments['rootcommentcontent'] = item['rootcommentcontent']
    # 时间
    comments['time'] = item['time']
    results = comments_list.count({'nick': comments['nick']})
    print(results)
    if results == 0:
        print('**********************************************')

        print(comments)
        comments_list.insert(comments)

        print('**********************************************')
        results += 1
        continue
    else:
        print('数据已存在')
