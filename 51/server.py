"""
author:张鑫
date:2021/5/22 16:05
https://51f.xyz/api/info/list?type=all&cityCode=110000&page=2&perPage=24&sort=publish
"""
# 导入模块
import json
import re
import time
import random
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
yellow = database['yellow']
five_list = yellow['five_list']


# 求解
def response(flow):
    if '51f.xyz/api/info/list' in flow.request.url:
        for item in json.loads(flow.response.text)['data']:
            print(item)
            fives = {}
            # 城市编号
            city_code = item['city_code']
            fives['城市编号'] = city_code
            #
            # 地区
            cityCodeReadable = item['cityCodeReadable']
            fives['地区'] = cityCodeReadable

            # 价钱
            consume_lv = item['consume_lv']
            fives['价钱'] = consume_lv

            # 封面图片
            cover_picture = item['cover_picture']
            fives['封面图片'] = 'https://image.yefengliu.com/info/picture/'+cover_picture

            # 发布时间
            created_at = item['created_at']
            fives['发布时间'] = created_at

            # 顾客描述
            desc = item['desc']
            fives['顾客描述'] = desc

            # 年龄
            girl_age = item['girl_age']
            fives['年龄'] = girl_age

            # 颜值
            girl_beauty = item['girl_beauty']
            fives['颜值'] = girl_beauty

            # id
            id = item['id']
            fives['id'] = id

            # 题目
            title = item['title']
            fives['题目'] = title

            print('**********************************')
            print(fives)
            five_list.insert_one(fives)
            print('**********************************')
