"""
author:张鑫
date:2021/5/19 16:26
https://druidv6.if.qidian.com/argus/api/v1/topBooks/get?site=11&topId=0&categoryId=-1&pageIndex=1&pageSize=20
https://druidv6.if.qidian.com/argus/api/v1/topBooks/get?site=11&topId=0&categoryId=-1&pageIndex=50&pageSize=20
Author,AuthorId,BookId,BookLevel,BookName,BookStatus,CategoryId,CategoryName,Description,ExtraName
ExtraValue,TopNo,WordsCount
"""

# 导入模块
import pymongo
import json
import time
import random

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['qidian']
zuopin_list = db['zuopin_list']


# 请求页面

def response(flow):
    if 'druidv6.if.qidian.com/argus/api/v1/topBooks/get' in flow.request.url:
        for item in json.loads(flow.response.text)['Data']:
            zuopins = {}
            time.sleep(random.randint(3, 5))
            Author = item['Author']
            zuopins['作者'] = Author

            AuthorId = item['AuthorId']
            zuopins['作者编号'] = AuthorId

            BookId = item['BookId']
            zuopins['作品编号'] = BookId

            BookLevel = item['BookLevel']
            zuopins['作品等级'] = BookLevel

            BookName = item['BookName']
            zuopins['书名'] = BookName

            BookStatus = item['BookStatus']
            zuopins['作品状态'] = BookStatus

            CategoryId = item['CategoryId']
            zuopins['题材编号'] = CategoryId

            CategoryName = item['CategoryName']
            zuopins['题材名称'] = CategoryName

            Description = item['Description']
            zuopins['描述'] = Description

            ExtraName = item['ExtraName']
            zuopins['打赏物'] = ExtraName

            ExtraValue = item['ExtraValue']
            zuopins['打赏数量'] = ExtraValue

            TopNo = item['TopNo']
            zuopins['作品排名'] = TopNo

            WordsCount = item['WordsCount']
            zuopins['总字数'] = WordsCount

            count = zuopin_list.count_documents({'BookName': zuopins['书名']})
            print(count)
            if count == 0:
                print('***********************************************')
                print(zuopins)
                zuopin_list.insert_one(zuopins)
                print('***********************************************')
                count += 1
            else:
                print('作品已存在')
