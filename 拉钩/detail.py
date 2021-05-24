"""
author:张鑫
date:2021/5/19 11:50
https://m.lagou.com/wn/jobs/8815045.html
props>pageProps>jd>[city,companyAddress,companyFeature,companyId,companyName,companySize
district,education,financeStage,industryField,jobNature,nameInitial,positionAdvantage,positionDetail
positionName,publisherName,salary,workAddress,workAddressPrefix,workAddressSuffix,workYear]
"""
# 导入相关模块
import pandas as pd
import pymongo
import json
import requests
import time
import random

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['lagou']
crawel_list = db['crawel_list']

# 读取数据
data = pd.DataFrame(list(crawel_list.find()))

# 需要显示的数据
data = data[['positionId']]

# 导入成csv
data.to_csv('crawel.csv')

# 输出结果

for data in data.values:
    time.sleep(random.randint(1, 5))
    data = str(data).replace('[', '').replace(']', '')

    print(data)
