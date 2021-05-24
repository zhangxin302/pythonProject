"""
author:张鑫
date:2021/5/19 15:38
"""

# 导入模块
import time
import pymongo
import random
import re
import pandas as pd
import numpy as np

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douyin']
comments = db['comments']

# 读取数据
data = pd.DataFrame(list(comments.find()))

# 确定输出字段
data = data[['create_time', 'text']]

# 输出结果
print(data)

# 输出成csv文件
# data.to_csv('抖音评论.csv')

# 输出成字典
# data.to_dict()

# 输出成Excel
# data.to_excel('抖音评论.xls')


# 输出成网页(乱码)
# data.to_html('抖音.html')
