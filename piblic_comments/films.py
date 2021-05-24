"""
author:张鑫
date:2021/5/20 10:30
https://m.maoyan.com/ajax/movieOnInfoList?token=&optimus_uuid=14CF28D0B91311EB9B76EBFB0987B06C0389F1EE08884031AB2A42411C25D506&optimus_risk_level=71&optimus_code=10
https://m.maoyan.com/ajax/movieOnInfoList?token=&optimus_uuid=14CF28D0B91311EB9B76EBFB0987B06C0389F1EE08884031AB2A42411C25D506&optimus_risk_level=71&optimus_code=10
https://m.maoyan.com/ajax/moreComingList?token=&movieIds=1250964%2C1302134%2C1221%2C1278054%2C1297907%2C1241385%2C1284360%2C343568%2C1383416%2C1250700&optimus_uuid=14CF28D0B91311EB9B76EBFB0987B06C0389F1EE08884031AB2A42411C25D506&optimus_risk_level=71&optimus_code=10
https://m.maoyan.com/ajax/moreComingList?token=&movieIds=1329156%2C1217041%2C1370268%2C1302373%2C1249328%2C1302015&optimus_uuid=14CF28D0B91311EB9B76EBFB0987B06C0389F1EE08884031AB2A42411C25D506&optimus_risk_level=71&optimus_code=10
https://m.maoyan.com/ajax/moreComingList?token=&movieIds=1329156%2C1217041%2C1370268%2C1302373%2C1249328%2C1302015&optimus_uuid=14CF28D0B91311EB9B76EBFB0987B06C0389F1EE08884031AB2A42411C25D506&optimus_risk_level=71&optimus_code=10
movieList>[id,nm,rt,showInfo,showst,star,version,wish]
"""
# 导入模块
import json
import time
import random
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['public_comments']
film_list = db['film_list']


# 请求网页
def response(flow):
    if 'm.maoyan.com/ajax/moreComingList' in flow.request.url:

        for item in json.loads(flow.response.text)['coming']:
            films = {}
            time.sleep(random.randint(1, 5))

            id = item['id']
            if id is not None:
                films['电影id'] = id
            else:
                print('暂无id')

            sc = item['sc']
            if id is not None:
                films['评分'] = sc
            else:
                print('暂无评分')

            nm = item['nm']
            if id is not None:
                films['电影名'] = nm
            else:
                print('暂无电影名')

            rt = item['rt']
            if id is not None:
                films['上映时间'] = rt
            else:
                print('暂无上映时间')

            showInfo = item['showInfo']
            if id is not None:
                films['播放信息'] = showInfo
            else:
                print('暂无播放信息')

            showst = item['showst']
            if id is not None:
                films['展厅'] = showst
            else:
                print('暂无展厅')
            try:
                star = item['star']
                films['主演'] = star
            except:
                print('暂无主演')

            wish = item['wish']
            if id is not None:
                films['望眼欲穿'] = wish
            else:
                print('暂无人想看')
            # 查看电影名这个字段在数据库中的数量
            count = film_list.count({'电影名': films['电影名']})
            if count == 0:
                print('******************************************')
                print(films)
                film_list.insert_one(films)
                count += 1
                print('******************************************')
            else:
                print('数据已存在')

        # for item in json.loads(flow.response.text)['coming']:
        #     films = {}
        #     time.sleep(random.randint(1, 5))
        #     id = item['id']
        #     films['电影id'] = id
        #
        #     nm = item['nm']
        #     films['电影名'] = nm
        #
        #     rt = item['rt']
        #     films['上映时间'] = rt
        #
        #     showInfo = item['showInfo']
        #     films['播放信息'] = showInfo
        #
        #     showst = item['showst']
        #     films['展厅'] = showst
        #
        #     star = item['star']
        #     films['主演'] = star
        #
        #     wish = item['wish']
        #     films['望眼欲穿'] = wish
        #
        #     count = film_list.count({'id': films['电影id']})
        #     if count == 0:
        #         print('******************************************')
        #         print(films)
        #         film_list.insert_one(films)
        #         print('******************************************')
        #     else:
        #         print('数据已存在')
