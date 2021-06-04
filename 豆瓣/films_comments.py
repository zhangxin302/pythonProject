"""
author:张鑫
date:2021/5/25 9:59
https://movie.douban.com/subject/26662159/comments?status=P
https://movie.douban.com/subject/26662159/comments?start=20&limit=20&status=P&sort=new_score
https://movie.douban.com/subject/26662159/comments?start=40&limit=20&status=P&sort=new_score
"""
# 导入模块
import requests
import re
import time
import random
import pymongo
import pandas as pd
from bs4 import BeautifulSoup
from tools.headers import headers
from lxml import etree

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douban']
films_list = db['films_list']
comments_list = db['comments_list']

# # 获取网页
# # 读取数据
# data = pd.DataFrame(list(films_list.find()))
# # 需要读取的字段
# data = data['电影编号']
# data = data.values
# for item in data:
#     comments = {}
#     time.sleep(random.randint(1, 3))
#     url = f'https://movie.douban.com/subject/{item}/comments?status=P'
#     html = requests.get(url=url, headers=headers).content.decode()
#     results = BeautifulSoup(html, 'lxml')
#     results = results.select('div.mod-bd')
#     for item in results:
#         time.sleep(random.randint(1, 3))
#         # 昵称
#         time.sleep(random.randint(1, 3))
#         nickname = item.select('span.comment-info>a')
#         for nickname in nickname:
#             nickname=nickname.text
#             comments['nickname'] = nickname
#         # 评星
#         # comments_start = re.findall('span class="(.*?)"title',item)
#         # 有用
#
#         time.sleep(random.randint(1, 3))
#         useful = item.select('span.votes')
#         for useful in useful:
#             useful=useful.text
#             comments['useful'] = useful
#         # 评论时间
#         time.sleep(random.randint(1, 3))
#         comments_time = item.select('span.comment-time')
#         for comments_time in comments_time:
#             comments_time = re.sub('\s', '', comments_time.text)
#             comments['comments_time']=comments_time
#
#
#         # 评论内容
#         time.sleep(random.randint(1, 3))
#         comments_content = item.select('p.comment-content')
#         for comments_content in comments_content:
#             comments_content = re.sub('\s', '', comments_content.text)
#             comments['评论内容']=comments_content
#             print('************************************')
#             print(comments)
#             print('************************************')

# # 获取网页
# # 读取数据
data = pd.DataFrame(list(films_list.find()))
# 需要读取的字段
data = data['电影编号']
data = data.values

for item in data:
    for i in range(100):
        url = f'https://movie.douban.com/subject/{item}/comments?start={20 * i}&limit=20&status=P&sort=new_score'
        print(url)
        # url = 'https://movie.douban.com/subject/26662159/comments?status=P'
        html = requests.get(url=url, headers=headers).content.decode()
        tree = etree.HTML(html)
        nickname = tree.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/a/text()')
        comments_start = tree.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/span[2]/@class')
        userful = tree.xpath('//*[@id="comments"]/div/div[2]/h3/span[1]/span/text()')
        comments_time = tree.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/span[3]/@title')
        comments_content = tree.xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
        # print(dict(zip(nickname,comments_start)))
        for i in range(len(comments_time)):
            time.sleep(random.randint(1, 5))
            comments = {}
            # nickname = nickname[i]

            comments['昵称'] = nickname[i]

            # comments_start = comments_start[i]
            comments['星级'] = comments_start[i]

            # userful = userful[i]
            comments['有用'] = userful[i]

            # comments_time = comments_time[i]
            comments['评论时间'] = comments_time[i]

            # comments_content = comments_content[i]
            comments['评论内容'] = comments_content[i]
            print('**********************************')
            print(comments)
            comments_list.insert_one(comments)

            print('**********************************')
