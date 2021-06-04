"""
author:张鑫
date:2021/5/25 17:08
"""
# 导入模块
import random

import pandas as pd
import requests
import re
import time
import pymongo
# from tools.headers import headers
from lxml import etree

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['douban']
films_list = db['films_list']
films_detail = db['films_detail']

# 读取数据库
data = pd.DataFrame(list(films_list.find()))
# 需要读取的字段
data = data['电影编号']
# 去值
data = data.values
headers = {
    'cookie': 'bid=pCT6bPGqfyk; douban-fav-remind=1; __gads=ID=847cef97bc9ad4bf-22b24b2a62c60072:T=1615624472:RT=1615624472:S=ALNI_MZj1DYzXd6ydunwJpC284hp2Zz8FQ; __utmz=30149280.1615624473.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); ll="108288"; __utmc=30149280; __utmz=223695111.1621906252.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; _vwo_uuid_v2=D711CE1E49B4A0F9D55E8C1DDFE1B93AC|bfea9f50d0e7f99abe0bf5c052224c44; ap_v=0,6.0; __utma=30149280.1754853929.1615624473.1621931804.1622192107.6; __utma=223695111.1946521424.1621906252.1621931804.1622192107.5; __utmb=223695111.0.10.1622192107; _pk_ses.100001.4cf6=*; dbcl2="238891706:tB5vhbviXYw"; ck=Qv9L; push_noty_num=0; push_doumail_num=0; __utmt=1; __utmv=30149280.23889; __utmb=30149280.10.10.1622192107; _pk_id.100001.4cf6=7b5f41c04f0a3f5d.1621906252.5.1622193321.1621932522.',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4503.5 Safari/537.36'
}
for data in data:
    time.sleep(random.randint(1, 3))
    detail_list = {}
    url = f'https://movie.douban.com/subject/{data}/?tag=%E7%83%AD%E9%97%A8&from=gaia'
    print(url)
    html = requests.get(url=url, headers=headers).content.decode()

    tree = etree.HTML(html)
    # try:
    # 导演
    edtor = str(tree.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')).replace('[', '').replace(']', '')
    detail_list['导演'] = edtor
    # except:
    #     print('暂无导演')
    # try:
    # 编剧
    time.sleep(random.randint(1, 3))
    binaju = str(tree.xpath('//*[@id="info"]/span/span[2]/a/text()')).replace('[', '').replace(']', '')
    detail_list['编剧'] = binaju
    # except:
    #     print('暂无导演')
    # try:
    # 主演
    zhuyan = str(tree.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')).replace('[', '').replace(']', '')
    detail_list['主演'] = zhuyan
    # except:
    #     print('暂无主演')
    # try:
    # 类型
    time.sleep(random.randint(1, 3))
    style = str(tree.xpath('//*[@id="info"]/span/text()')[4:6]).replace('[', '').replace(']', '')
    detail_list['类型'] = style
    # except:
    #     print('暂无类型')
    # try:
    # 制片国
    country = str(tree.xpath('//*[@id="info"]/text()')[8]).replace('[', '').replace(']', '')
    detail_list['制片国'] = country
    # except:
    #     print('暂无制片国')
    try:
        # 语言
        lang = str(tree.xpath('//*[@id="info"]/text()')[10]).replace('[', '').replace(']', '')
        detail_list['语言'] = lang
    except:
        print('暂无语言')
    try:
        # 上映时间
        times = str(tree.xpath('//*[@id="info"]/span/text()')[11]).replace('[', '').replace(']', '')
        detail_list['上映时间'] = times
    except:
        print('暂无上映时间')

    # 片长
    try:
        time.sleep(random.randint(1, 3))
        long = str(tree.xpath('//*[@id="info"]/span[14]/text()')).replace('[', '').replace(']', '')
        detail_list['片长'] = long
    except:
        print('暂无片长')
    # try:
    # 别名
    time.sleep(random.randint(1, 3))
    extra_name = str(tree.xpath('//*[@id="info"]/text()')[-4]).replace('[', '').replace(']', '')
    detail_list['别名'] = extra_name
    # except:
    #     print('暂无别名')
    # try:
    #     # imdb.replace('[','').replace(']','')
    #     imdb = str(tree.xpath('//*[@id="info"]/text()')[-2]).replace('[', '').replace(']', '')
    #     detail_list['imdb'] = imdb
    # except:
    #     print('暂无imdb')
    count = films_detail.count_documents({'别名': detail_list['别名']})
    if count == 0:

        print('*******************************************')
        print(detail_list)
        films_detail.insert_one(detail_list)
        print('*******************************************')
    else:
        print('数据已存在')
