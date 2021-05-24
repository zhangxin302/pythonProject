"""
author:张鑫
date:2021/5/7 14:56
http://api.gifshow.com/rest/n/comment/list/v2?mod=samsung%28SM-G977N%29&lon=101.565154&country_code=CN&kpn=KUAISHOU&oc=GENERIC&egid=DFP55AA6907F09537569993D8BD50A44166F0E60631348DC1DBB3AE228ECDDD9&hotfix_ver=&sh=1600&appver=6.9.2.11245&max_memory=128&isp=CMCC&browseType=1&kpf=ANDROID_PHONE&did=ANDROID_9f1f47b29747b286&net=WIFI&app=0&ud=0&c=GENERIC&sys=ANDROID_5.1.1&sw=900&ftt=&language=zh-cn&iuid=&lat=30.998662&did_gt=1620369457795&ver=6.9
作者名字：rootComments>author_name
评论：rootComments>content
作者id：rootComments>author_id
评论时间：rootComments>time
"""
import json
import random
import time
import pymongo

database = pymongo.MongoClient('localhost', port=27017)
db = database['kuaishou']
comments_list = db['comments_list']


def response(flow):
    if 'api.gifshow.com/rest/n/comment/list/v2' in flow.request.url:
        for item in json.loads(flow.response.text)['rootComments']:
            comments = {}
            comments['author_name'] = item['author_name']
            comments['content'] = item['content']
            comments['author_id'] = item['author_id']
            comments['time'] = item['time']
            results = comments_list.count({'author_name': comments['author_name'], 'content': comments['content']})
            if results == 0:
                print('************************************')
                print(comments)
                comments_list.insert(comments)
                print('************************************')
                results += 1
                continue
            else:
                print('数据已存在')
