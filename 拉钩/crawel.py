"""
author:张鑫
date:2021/5/19 9:14
https://m.lagou.com/search.json?city=%E5%85%A8%E5%9B%BD&positionName=python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&pageNo=1&pageSize=15
content>page>result>[city,companyFullName,companyId,companyLogo,companyName,
createTime,positionId,positionName,salary]

"""
import pymongo
import json
import time
import random

database = pymongo.MongoClient('localhost', port=27017)
db = database['lagou']
crawel_list = db['crawel_list']


def response(flow):
    if 'm.lagou.com/search.json' in flow.request.url:
        for item in json.loads(flow.response.text)['content']['data']['page']['result']:
            crawels = {}
            time.sleep(random.randint(3, 5))
            # 公司所在城市
            city = item['city']
            crawels['city'] = city
            # 公司全称
            companyFullName = item['companyFullName']
            crawels['companyFullName'] = companyFullName
            # 公司编号
            companyId = item['companyId']
            crawels['companyId'] = companyId
            # 公司图标
            companyLogo = item['companyLogo']
            crawels['companyLogo'] = companyLogo
            # 公司名称
            companyName = item['companyName']
            crawels['companyName'] = companyName
            # 创建时间
            createTime = item['createTime']
            crawels['createTime'] = createTime
            # 职位编号
            positionId = item['positionId']
            crawels['positionId'] = positionId
            # 职位名称
            positionName = item['positionName']
            crawels['positionName'] = positionName
            # 薪水
            salary = item['salary']
            crawels['salary'] = salary

            count = crawel_list.count({'positionId': crawels['positionId']})

            if count == 0:
                print('**************************************')
                print(crawels)
                crawel_list.insert_one(crawels)
                print('**************************************')
            else:
                print('数据已存在')
