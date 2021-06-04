"""
author:张鑫
date:2021/6/3 15:29
发酵甜果酒
https://aweme.snssdk.com/aweme/v2/shop/search/aggregate/shopping/?os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=160101&dpi=320&uuid=351564272622119&app_name=aweme&version_name=16.1.0&ts=1622707352&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=16109900&channel=tengxun_1128_0512&_rticket=1622707352307&device_platform=android&iid=3642043920823015&version_code=160100&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&is_android_pad=0&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v2/shop/search/aggregate/shopping/?os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=160101&dpi=320&uuid=351564272622119&app_name=aweme&version_name=16.1.0&ts=1622706373&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=16109900&channel=tengxun_1128_0512&_rticket=1622706374474&device_platform=android&iid=3642043920823015&version_code=160100&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&is_android_pad=0&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v2/shop/search/aggregate/shopping/?os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=160101&dpi=320&uuid=351564272622119&app_name=aweme&version_name=16.1.0&ts=1622709782&cpu_support64=false&app_type=normal&appTheme=light&ac=wifi&host_abi=armeabi-v7a&update_version_code=16109900&channel=tengxun_1128_0512&_rticket=1622709782526&device_platform=android&iid=3642043920823015&version_code=160100&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&is_android_pad=0&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
"""
# 导入模块
import requests
import re
import time
import random
import pymongo
import json

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douyin']
rum_list = db['rum_list']


# 获取数据


def response(flow):
    if 'aweme.snssdk.com/aweme/v2/shop/search/aggregate/shopping/' in flow.request.url:
        for item in json.loads(flow.response.text)['items']:
            print(item)
            rums = {}
            rums['level'] = item['level']
            rums['goods_ratio'] = item['product_info']['attach_info']['goods_ratio']
            time.sleep(random.randint(1, 3))
            rums['commodity_type'] = item['product_info']['commodity_type']
            rums['gid'] = item['product_info']['gid']
            rums['h5_url'] = item['product_info']['h5_url']
            rums['img'] = item['product_info']['img']
            rums['name'] = item['product_info']['name']
            rums['platform_name'] = item['product_info']['platform_name']
            rums['promotion_id'] = item['product_info']['promotion_id']
            rums['schema'] = item['product_info']['schema']
            rums['schema_type'] = item['product_info']['schema_type']
            rums['show_price'] = item['product_info']['show_price']
            rums['tag_infos'] = item['product_info']['tag_infos']
            rums['result_type'] = item['result_type']
            rums['users'] = item['users']
            count = rum_list.count_documents({'promotion_id': rums['promotion_id']})
            if count == 0:
                print('****************************')
                print(rums)
                rum_list.insert_one(rums)
                print('****************************')
            else:
                print('数据已存在')
