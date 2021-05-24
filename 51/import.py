"""
author:张鑫
date:2021/5/22 18:18
"""
import pymongo
import pandas as pd

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
yellow = database['yellow']
five_list = yellow['five_list']

# 导出数据
data = pd.DataFrame(list(five_list.find()))

# 需要导出的字段
data = data['封面图片']
url = 'https://image.yefengliu.com/info/picture/'
data = url+data
# 保存成xls
data.to_excel('five.xls')
