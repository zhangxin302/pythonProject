"""
author:张鑫
date:2021/5/20 15:30
"""
# 导入模块
from selenium import webdriver
import re
import time
import random
import requests
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['selenium']
catoon_list = db['catoon_list']
# while 1:
# 使用谷歌浏览器
driver = webdriver.Chrome()
for i in range(1, 11):
    time.sleep(random.randint(3, 5))

    # 请求网页
    driver.get(f'https://www.bilibili.com/v/anime/finish/#/all/default/0/{i}/')
    # 页面最大化
    driver.maximize_window()
    # 鼠标滑动
    driver.execute_script('window.scrollTo(1000,2000)')
    # 等页面加载
    time.sleep(random.randint(10, 15))
    # 点击下一页
    driver.find_element_by_css_selector(
        '#videolist_box>div.vd-list-cnt>div.pager.pagination>ul>li.page-item.next>button').click()
    # 显示网页源码
    html = driver.page_source

    # 解析页面
    print(f"第{i}页")
