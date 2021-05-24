"""
author:张鑫
date:2021/5/20 17:45
create_time=1621085617
digg_count=86
reply_count=21
score=3.6596672390725473
text=坚决抵制日漫，抵制二次元，抵制日本畸形文化输出，文化侵略，毒害我们的青少年小孩子，瓦解我们的意志，破坏我们的风气！
user_name=自由阵地
"""
import re
import requests
import json
import time
import random
def response(flow):
    if 'ib.snssdk.com/article/v4/tab_comments/'in flow.request.url:
        for item in json.loads(flow.response.text)['data']['comments']:
            create_time = item['create_time']
            digg_count = item['digg_count']
            reply_count = item['reply_count']
            score = item['score']
            text = item['text']
            user_name = item['user_name']
            print(create_time)
            print(digg_count)
            print(reply_count)
            print(score)
            print(text)
            print(user_name)
