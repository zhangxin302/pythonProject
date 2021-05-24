# -*- coding:utf-8 -*-
# @FileName  :api.py
# @Time      :2021/01/25
# @Author    :pylemon
import json
import re

from jsonpath import jsonpath

with open('api01', 'r', encoding='utf-8-sig') as f:
    response_text = f.read()
if response_text.startswith('{"data":{"node":{"__typename":"Page"'):
    _index = response_text.find('{"label":"CometFeedStoryVideoAttachmentVideoPlay')
    json_text = response_text[:_index]
    try:
        json_content = json.loads(json_text)
    except:
        json_content = dict()
    actors_li = jsonpath(json_content, '$..actors')
    actors_li = [] if not actors_li else actors_li
    user_id = None

    for actors in actors_li:
        if not isinstance(actors, list):
            continue

        for actor in actors:
            # {
            # "__typename": "Page",
            # "__isActor": "Page",
            # "id": "46251501064",
            # "__isEntity": "Page",
            # "url": "https://www.facebook.com/tsaiingwen/",
            # "category_type": "POLITICIAN"
            # }
            url = actor.get('url')
            if not url:
                continue
            user_num_id = actor.get('id')  # 公共主页的 用户数字id

            _user_id = re.compile('www.facebook.com/([\s\S]+?)/').findall(url)
            user_id = _user_id[0] if _user_id else None
            if user_id:
                break
        if user_id:
            break
    print(user_id)