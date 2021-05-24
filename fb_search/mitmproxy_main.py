# -*- coding: utf-8 -*-
# @Time : 2021/1/24 21:41
# @Author : python
# @File : mitmproxy_main.py
# @Project : fb_selenium

# 获取 路径
import json
import os
import re
import sys
from time import sleep, mktime, localtime, time
from tools.extract import Extract
from tools.connect_mysql import Connect_Mysql


file_path = os.path.dirname(os.path.abspath(__file__))
# 修改运行路径
sys.path.append(file_path)
sys.path.insert(0, os.path.dirname(file_path))  # 修改模块的导入

API_FILE_PATH = os.path.join(file_path, 'api_file')

def response(flow):
    # flow.request.headers['User-Agent'] = 'MitmProxy'
    # 如果打开这个就退出服务
    # print('关闭拦截器')
    if 'httpbin.org/ip' in flow.request.url:
        print('hello')
        print(flow.request.headers)
        print(flow.request.headers.get('Host'))
        print(type(flow.request.headers.get('Host')))
        print('='*30)
        print('关闭拦截器')
        sys.exit()
    # if 'posts/' in flow.request.url and '/?q=' not in flow.request.url:
    #     if flow.response.text:
    #         response_text =flow.response.text
    #         datas=Extract.parse_post(response_text)
    #         Connect_Mysql.Save_Data(datas)
    # if '/groups/' in flow.request.url:
    #     if flow.response.text:
    #         response_text =flow.response.text
    #         datas=Extract.parse_post(response_text)
    #         Connect_Mysql.Save_Data(datas)
    # if 'permalink.php?story_fbid' in flow.request.url and '/?q=' not in flow.request.url:
    #     if flow.response.text:
    #         response_text =flow.response.text
    #         datas=Extract.parse_post(response_text)
    #         Connect_Mysql.Save_Data(datas)
    # if '/videos/' in flow.request.url:
    #     if flow.response.text:
    #         response_text =flow.response.text
    #         datas=Extract.parse_post(response_text)
    #         Connect_Mysql.Save_Data(datas)
    # if '/photos/' in flow.request.url:
    #     if flow.response.text:
    #         response_text =flow.response.text
    #         datas=Extract.parse_post(response_text)
    #         Connect_Mysql.Save_Data(datas)










if __name__ == '__main__':

    while True:
        try:
            os.system('mitmdump -s mitmproxy_main.py -p 8888')
        except Exception as e:
            print(e)
            break
        #     pass
        # try:
        #     print('服务重启中。。。')
        # except:
        #     pass
    # os.system('mitmdump -s server.py -p 8888')