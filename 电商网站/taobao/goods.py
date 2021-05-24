# """
# author:张鑫
# date:2021/5/21 9:36
# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210521&ie=utf8
# https://s.taobao.com/search?q=%E5%8D%8E%E4%B8%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.21814703.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
# https://s.taobao.com/search?q=%E6%9C%BA%E6%A2%B0%E5%B8%88&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210521&ie=utf8
# """
import datetime
import random
from urllib.parse import quote
from selenium import webdriver
import requests
import json
import time
from bs4 import BeautifulSoup

now_time = datetime.datetime.now().strftime('%Y-%m-%d').replace('-', '')
print(now_time)
# 输入需要搜索的商品
q = input('请输入需要搜索的商品：')
url = f'https://s.taobao.com/search?q={quote(q)}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_{now_time}&ie=utf8'
# 使用谷歌浏览器
driver = webdriver.Chrome()
# 请求网页
driver.get(url)
# 屏幕最大化
driver.maximize_window()
# 等待扫码登录淘宝
time.sleep(random.randint(10, 15))

# 网页源码
html = driver.page_source
# 返回源码
# print(html)
# 解析页面
results = BeautifulSoup(html, 'lxml')
results = results.select('div.m-itemlist')
# results = results.select('div[class="item J_MouserOnverReq  "]')
for item in results:
    for item in item:
        print(item)
        # 品牌
        name = item.select_one(
            '#mainsrp-itemlist>div>div>div:nth-child(1)>div:nth-child(45)>div.ctx-box.J_MouseEneterLeave.J_IconMoreNew>div.row.row-2.title').text
        # 店铺名
        dianpu = item.select_one(
            '#mainsrp-itemlist>div>div>div:nth-child(1)>div:nth-child(45)>div.ctx-box.J_MouseEneterLeave.J_IconMoreNew>div.row.row-3.g-clearfix>div.shop>a>span:nth-child(2)').text
        # 发货地
        arrive = item.select_one(
            '#mainsrp-itemlist>div>div>div:nth-child(1)>div:nth-child(45)>div.ctx-box.J_MouseEneterLeave.J_IconMoreNew>div.row.row-3.g-clearfix>div.location').text
        # 价格
        price = item.select_one(
            '#mainsrp-itemlist>div>div>div:nth-child(1)>div.item.J_MouserOnverReq.item-ad>div.ctx-box.J_MouseEneterLeave.J_IconMoreNew>div.row.row-1.g-clearfix>div.price.g_price.g_price-highlight>strong').text
        # 购买人数
        sum = item.select_one(
            '#mainsrp-itemlist>div>div>div:nth-child(1)>div.item.J_MouserOnverReq.item-ad>div.ctx-box.J_MouseEneterLeave.J_IconMoreNew>div.row.row-1.g-clearfix>div.price.g_price.g_price-highlight>strong').text
        print(f"品牌:{name}\n店铺名:{dianpu}\n发货地:{arrive}\n价格:{price}\n购买人数:{sum}\n")
