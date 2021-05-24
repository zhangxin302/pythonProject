"""
author:张鑫
date:2021/4/25 9:56
"""
import random
import time

'''
https://aweme.snssdk.com/aweme/v2/comment/list/?aweme_id=6959089428203703593&cursor=80&count=20&insert_ids&address_book_access=1&gps_access=1&forward_page_type=1&channel_id=0&city=513300&hotsoon_filtered_count=0&hotsoon_has_more=1&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAzGjXk31Qh9dvtuNf4-wsCK7yn6oOcox6Jwa1cBts_l4&item_type=0&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1620436648&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1620436648769&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007 
https://aweme.snssdk.com/aweme/v2/comment/list/?aweme_id=6959089428203703593&cursor=180&count=20&insert_ids&address_book_access=1&gps_access=1&forward_page_type=1&channel_id=0&city=513300&hotsoon_filtered_count=0&hotsoon_has_more=1&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAzGjXk31Qh9dvtuNf4-wsCK7yn6oOcox6Jwa1cBts_l4&item_type=0&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1620436794&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1620436795813&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007 

'''
import pymongo, pymysql
import requests, json, mitmdump

client = pymongo.MongoClient('localhost', port=27017)
db = client['douyin']
douyin_comment = db['comments']


# response 响应结果
# flow字节流
def response(flow):
    if 'https://aweme.snssdk.com/aweme/v2/comment/list/' in flow.request.url:
        for item in json.loads(flow.response.text)['comments']:
            comments={}
            comments['text'] = item['text']
            comments['create_time'] = item['create_time']
            comments['nickname'] = item['user']['nickname']
            print('********************************************')
            douyin_comment.insert(comments)
            print(comments)

            print('********************************************')


