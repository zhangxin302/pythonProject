"""
author:张鑫
date:2021/6/1 10:13
https://aweme.snssdk.com/aweme/v2/shop/promotion/comments/?product_id=3473193580594635989&cursor=0&count=10&stat_id=-1&tag_id=14&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1622513917&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1622513918989&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v2/shop/promotion/comments/?product_id=3473193580594635989&cursor=60&count=10&stat_id=-1&tag_id=14&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1622515502&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1622515502943&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v2/shop/promotion/comments/?product_id=3473193580594635989&cursor=70&count=10&stat_id=-1&tag_id=14&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1622515527&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1622515528153&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v2/shop/promotion/comments/?product_id=3414010100376074813&cursor=30&count=10&stat_id=-1&tag_id=14&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1622516556&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1622516556890&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
"""
# 导入模块
import json
import re
import time
import random
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douyin']
weixun_drink = db['weixun_drink']


# 获取信息
def response(flow):
    if 'https://aweme.snssdk.com/aweme/v2/shop/promotion/comments/' in flow.request.url:
        for item in json.loads(flow.response.text)['comments']:
            # time.sleep(random.randint(3, 10))

            comments = {}
            # 用户编号
            user_id = item['user_id']
            comments['用户编号'] = user_id
            # 用户昵称
            user_name = item['user_name']
            comments['用户昵称'] = user_name
            # 软件编号
            app_id = item['app_id']
            comments['软件编号'] = app_id
            # 评论时间
            comment_time = item['comment_time']
            comments['评论时间'] = comment_time
            # 评论内容
            content = item['content']
            comments['评论内容'] = content
            # 订单id
            id = item['id']
            comments['订单id'] = id
            # 点赞数
            likes = item['likes']
            comments['点赞数'] = likes
            # 等级
            rank = item['rank']
            comments['等级'] = rank
            # 逻辑等级
            rank_logistic = item['rank_logistic']
            comments['逻辑等级'] = rank_logistic
            # 商品等级
            rank_product = item['rank_product']
            comments['商品等级'] = rank_product
            # 商城等级
            rank_shop = item['rank_shop']
            comments['商城等级'] = rank_shop
            # 商家回复
            shop_reply = item['shop_reply']
            comments['商家回复'] = shop_reply
            count = weixun_drink.count_documents({'订单id': comments['订单id']})
            if count == 0:
                print('******************************')
                print(comments)
                weixun_drink.insert_one(comments)
                print('******************************')
            else:
                print('数据已存在')
