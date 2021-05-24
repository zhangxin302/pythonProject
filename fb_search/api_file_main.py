# -*- coding:utf-8 -*-
# @FileName  :api_file_main.py
# @Time      :2021/01/25
# @Author    :pylemon
"""
api 接口文件提取
"""
import json
import os
import re
import sys
from time import sleep

from jsonpath import jsonpath
from loguru import logger

#os.path.dirname(__file__)获取当前文件的目录
# E:/Projects/fb_selenium
# os.path.abspath(__file__)获取当前文件绝对路径（完整路径）
# E:\Projects\fb_selenium\api_file_main.py
# os.path.dirname(os.path.abspath(__file__))
# E:\Projects\fb_selenium
file_path = os.path.dirname(os.path.abspath(__file__))
# 修改运行路径
sys.path.append(file_path)
sys.path.insert(0, os.path.dirname(file_path))  # 修改模块的导入

from tools.extract import Extract
from settings import REDIS

API_FILE_PATH = os.path.join(file_path, 'api_file')

# LOG_FILE = os.path.join(LOG_DIR, "log_{time}.log")
LOG_FILE = os.path.join(file_path, "api_facebook_main.log")
logger.add(LOG_FILE, rotation="100MB", retention=1, encoding='utf-8')


class APIFile:

    def __init__(self):
        self.logger = logger
        self.redis = REDIS
        self.extract = Extract

    def get_all_file(self):
        file_name_all = os.listdir(API_FILE_PATH)
        file_all = {"comment": dict(), "post": dict()}
        for file_name in file_name_all:
            if not file_name.endswith('.json'):
                continue
            elif file_name.startswith('comment_'):
                article_id = re.compile('comment_(\d+)_').findall(file_name)[0]
                comment_li = file_all['comment'].get(article_id)
                comment_li = [] if not comment_li else comment_li
                comment_li.append(file_name)
                file_all['comment'][article_id] = comment_li


            elif file_name.startswith('post_'):
                user_id = re.compile('post_([\s\S]+?)_\d+\.\d+\.json').findall(file_name)[0]
                post_li = file_all['post'].get(user_id)
                post_li = [] if not post_li else post_li
                post_li.append(file_name)
                file_all['post'][user_id] = post_li
            else:
                continue
        return file_all

    def extract_post_api(self, user_id, post_file_name):
        """提取贴子 api """
        post_path = os.path.join(API_FILE_PATH, post_file_name)
        with open(post_path, 'r', encoding='utf-8') as f:
            post_api_json = json.load(f)

        post_li = self.extract.parse_post(post_api_json)
        # self.logger.debug('api 提取到贴子：{}, {}'.format(user_id, len(post_li)))
        if not post_li:
            return
        public_author_msg = self.redis.get('fb:user_'+user_id)
        if not public_author_msg:
            # self.logger.error('api redis 公共主页获取失败： {}'.format(user_id))
            return
        public_author_msg = json.loads(public_author_msg.decode())
        self.logger.debug('api redis 公共主页获取成功： {}'.format(user_id))
        for post_data in post_li:
            post_data.update(public_author_msg)
            self.redis.set('fb:post_{}_{}'.format(user_id, post_data.get('post_id')), json.dumps(post_data), ex=60*30)

        print(json.dumps(post_li, ensure_ascii=False))

        # 清除本地文件
        self.logger.debug('api 公共主页保存成功，清理本地文件：{},  {}'.format(user_id, post_file_name))
        self.clear_file(post_path)

        # edges_li = post_api_json.get('data').get('node').get('timeline_feed_units').get('edges')
        # edges_li = [] if not edges_li else edges_li
        # nodes_li = [i.get('node') for i in edges_li]
        # for node in nodes_li:
        #     comet_sections = node.get('comet_sections')
        #     comet_sections = dict() if not comet_sections else comet_sections

    def clear_file(self, path):

        try:
            os.remove(path)
            pass
        except:
            pass

    def extract_comment_api(self, post_id, comment_file_name):
        all_comment_li = []

        post_key = self.redis.keys('fb:post_*_{}'.format(post_id))
        if not post_key:
            # self.logger.error('api post_id redis get error: {}'.format(post_key))
            return all_comment_li

        comment_file_path = os.path.join(API_FILE_PATH, comment_file_name)
        with open(comment_file_path, 'r', encoding='utf-8') as f:
            comment_json = json.load(f)
        comment_data_li = self.extract.parse_comment_json(comment_json)
        if not comment_data_li:
            return all_comment_li
        post_data = json.loads(self.redis.get(post_key[0].decode()).decode())
        for comment_data in comment_data_li:
            # post_id = comment_data.get('post_id')
            comment_data.update(post_data)
            all_comment_li.append(comment_data)
            # print(json.dumps(comment_data,ensure_ascii=False))
        self.clear_file(comment_file_path)
        return all_comment_li

    def start(self):
        file_all = self.get_all_file()
        # print(json.dumps(file_all))

        # 第一步 提取帖子
        post_file_msg = file_all.get('post')
        for user_id, post_file_name_li in post_file_msg.items():
            for post_file_name in post_file_name_li:
                # self.logger.debug('开始解析贴子：{}'.format(post_file_name))
                self.extract_post_api(user_id, post_file_name)
        # 提取评论
        comment_file_msg = file_all.get('comment')
        all_comment_li = []
        for post_id, comment_file_name_li in comment_file_msg.items():
            for comment_file_name in comment_file_name_li:
                # self.logger.debug('开始解析评论：{}'.format(comment_file_name))
                comment_data_li = self.extract_comment_api(post_id, comment_file_name)
                all_comment_li += comment_data_li

        if all_comment_li:
            # 保存评论
            all_comment_li = list({json.dumps(i) for i in all_comment_li})
            self.redis.lpush('fb:save', *all_comment_li)

if __name__ == '__main__':
    while True:
        try:
            APIFile().start()
        except:
            pass
        sleep(1)