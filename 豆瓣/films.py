"""
author:张鑫
date:2021/5/25 9:19
1-20：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
21-40：https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20
"""
# 导入模块
from urllib.parse import unquote, quote
import json
import requests
import time
import random
import pymongo


# 连接数据库
from tools.headers import headers

database = pymongo.MongoClient('localhost', port=27017)
db = database['douban']
films_list = db['films_list']

# 获取网页
for i in range(20):
    time.sleep(random.randint(3, 8))
    url = f'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={20 * i}'
    html = requests.get(url=url, headers=headers, verify=False).json()
    for item in html['subjects']:
        films = {}
        # 豆瓣评分
        rate = item['rate']
        films['豆瓣评分'] = rate
        # 电影名
        title = item['title']
        films['电影名'] = title
        # 详情链接
        url = item['url']
        films['详情链接'] = url
        # 封面链接
        cover = item['cover']
        films['封面链接'] = cover
        # 电影编号
        id = item['id']
        films['电影编号'] = id
        # 是否新上映
        is_new = item['is_new']
        films['是否新上映'] = is_new

        # 判断是否已存在与数据库
        count = films_list.count_documents({'电影编号': films['电影编号']})
        if count == 0:
            time.sleep(random.randint(5,15))
            print('*************************************')
            print(films)
            films_list.insert_one(films)
            print('*************************************')
        else:
            print('数据已存在')
