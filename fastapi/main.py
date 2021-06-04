"""
author:张鑫
date:2021/5/26 9:53
cd D:\pythonProject\fastapi
uvicorn main:app  --host=127.0.0.1 --port=8000 --reload
在浏览器输入127.0.0.1:8000
"""
# 导入fastapi模块
from typing import List

from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel

# 创建实例对象
# app = FastAPI()


# # 创建路径修饰器,必须是已有路径
# @app.get("/")
# # 编写路径操作函数
# async def root():
#     # 返回值，可以是列表，字典，或者字符串
#     return (1, 2)


# # 创建修饰器
# # /logins/{items}是api接口，写在端口后面
# @app.get('/logins/{items}')
# # 路径参数，如果确定类型。路径类型错误会报错
# def root(items:int):
#     return {items}


# # 只能使用类中的字段值
# class Kai_Sai_Er(str, Enum):
#     name = 'chuzihang'
#     age = 18
#     level = 'a'
#
#
# # 创建实例对象
# app = FastAPI()
#
#
# # 创建修饰器
# @app.get('/logins/{students}')
# # 参数值为函数中的内容
# def asd(students: Kai_Sai_Er):
#     return {'students': students}


# # 创建实例对象
# app = FastAPI()
#
#
# # 创建修饰器
# # file_path是一个路径
# @app.get('/file/{file_path:path}')
# # 描述路径参数
# def root(file_path):
#     # 返回参数值
#     return {file_path}


# app = FastAPI()


# @app.get('/login')
# num1和num2可以不写，取默认值
# /login?num1=1&num2=5,不取默认值的时候必须给一个固定值
# 可以和路径函数共用
# def root(num1: int = 2, num2: int = 5):
#     return [num1 * num2]
# @app.get('/login')
# def root(file_path: str = '/a'):
#     return (file_path)

#
# app = FastAPI()
#
#
# @app.get('/logins/')
# def root(q: str = None):
#     # 在/logins/加上？q=
#     # 如果q不存在，返回
#     returns = {'爱心小贴士': '别忘了输参数哦！'}
#     # 如果q存在，返回{'a': 'b'}和{q:q}
#     if q:
#         returns.update({q: q})
#     return returns
#

# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/logins/")
# # q的默认值是hello world，有参数是结果是参数值
# # 参数值是3到50位
# async def read_items(q: str = Query('hello world',
#                                     max_length=50, min_length=3,
#                                     # 参数别名
#                                     alias='rename'
#                                     )):
#     # 返回值为"items": 'Big preoject'
#     #        q:q
#     results = {"items": 'Big preoject'}
#     if q:
#         results.update({"q": q})  # 给字典results添加一个健值对{"q": q}
#     return results

# app = FastAPI()
#
#
# @app.get('/logins/')
# def root(
#         # 不输入参数时，输出值是['a', 'b']
#         # 有参数时，返回值在下面
#         # 两个同名参数，可以赋予不同的值
#         # q: List[str] = Query(['a', 'b'])
#         q: List[str] = Query([1,2])
# ):
#     returns = {'你好呀'}
#     if q:
#         returns = q
#     return returns

import pymongo

app = FastAPI()
database = pymongo.MongoClient('localhost', port=27017)
db = database['douyin']
zuopin = db['zuopin']


@app.get('/logins/zuopin')
def root():
    users = []
    for user in db.zuopin.find({}, {'share_url': 1, 'nickname': 1, 'author_user_id': 1,
                                    'create_time': 1, 'desc': 1, "_id": 0}):
        # for user in db.comments.find({'text':'@笑如春风沐 @趁黑摸条虾 @Y. @百事都可乐'}, {"_id": 0}):
        users.append(user)
    return users

