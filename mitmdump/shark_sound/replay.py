"""
author:张鑫
date:2021/4/30 9:54
notice_lists>notice_list_v2>comment>text
https://aweme.snssdk.com/aweme/v1/notice/multi/?group_list=%5B%7B%22count%22%3A1%2C%22group%22%3A64%7D%2C%7B%22notice_id%22%3A6956156199398425631%2C%22create_time%22%3A1619690400%2C%22count%22%3A1%2C%22group%22%3A83%7D%2C%7B%22notice_id%22%3A6951573735023936542%2C%22create_time%22%3A1618539405%2C%22count%22%3A1%2C%22group%22%3A84%7D%5D&app_version=15.2.0&is_new_notice=1&fetch_all=0&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1619766644&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1619766644381&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://aweme.snssdk.com/aweme/v1/notice/multi/?group_list=%5B%7B%22count%22%3A1%2C%22group%22%3A64%7D%2C%7B%22notice_id%22%3A6956156199398425631%2C%22create_time%22%3A1619690400%2C%22count%22%3A1%2C%22group%22%3A83%7D%2C%7B%22notice_id%22%3A6951573735023936542%2C%22create_time%22%3A1618539405%2C%22count%22%3A1%2C%22group%22%3A84%7D%5D&app_version=15.2.0&is_new_notice=1&fetch_all=0&os_api=22&device_type=SM-G977N&ssmix=a&manifest_version_code=150201&dpi=320&uuid=351564272622119&app_name=aweme&version_name=15.2.0&ts=1619749072&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15209900&channel=aweGW&_rticket=1619749072870&device_platform=android&iid=3413328874713982&version_code=150200&cdid=3697952e-3f20-4137-920b-99fe588f4c6e&openudid=9f1f47b29747b286&device_id=456997632486734&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
"""
import json
import time
import random
import requests
import pymongo

db = pymongo.MongoClient('localhost', port=27017)
database = db['douyin']
replay = database['replay']


def response(flow):
    if 'aweme.snssdk.com/aweme/v1/notice/multi/' in flow.request.url:
        for item in json.loads(flow.response.text)['notice_lists']:
            time.sleep(random.randint(1, 5))

            print('*****************************************')
            for i in item['notice_list_v2']:
                print(i)
                # replays = {}
                # replays['text'] = i['text']
                # replays['nickname'] = i['user']['comment']
                #
                # print(replays)
                # replay.insert(replays)
            # text = item['text']
            #
            # print(item['notice_list_v2'][0]['comment']['text'])

            print('******************************************')
