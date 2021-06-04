"""
author:张鑫
date:2021/5/28 14:31
"""
# 导入模块
from fastapi import FastAPI
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douyin']
comments = db['comments']
zuopin = db['zuopin']

app = FastAPI()


@app.get('/logins/zuopin')
def root():
    zuopin_list = []
    for zuopins in db.zuopin.find({}, {'share_url': 1, 'nickname': 1, 'author_user_id': 1,
                                       'create_time': 1, 'desc': 1, "_id": 0}):
        zuopin_list.append(zuopins)
    return zuopin_list


@app.get('/logins/comments')
def root():
    comments_list = []

    for comments in db.zuopin.find({}, {'text': 1, 'create_time': 1, "_id": 0}):
    # for comments in db.zuopin.find({}, {'create_time': 1, "_id": 0}):
        comments_list.append(comments)
    return comments_list
