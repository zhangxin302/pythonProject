"""
author:张鑫
date:2021/5/26 17:15
https://m.guazi.com/zz/buy/
"""
from tools.headers import headers

"""
@Project -> File   ：WebCrawler -> 瓜子二手车.py
@IDE    ：PyCharm
@Author ：Mr. Lvkun
@Date   ：2021/5/26 14:30
"""
from fake_useragent import UserAgent
import time
from requests import request
from lxml import etree
from pymongo import MongoClient


# client = MongoClient(host='127.0.0.1', port=27017)
# # 验证
# client.admin.authenticate('root', '123456')
# # 指定数据库
# mydb = client['guazi1']
# # 存放数据的数据库表名
# post = mydb['data']

# headers = {
#     'User-Agent': UserAgent().random
# }


def ceshi():
    for i in range(1, 51):
        url = f"https://www.guazi.com/zz/buy/o{i}/"
        response = request('get', headers=headers, url=url,verify=False).text
        root = etree.HTML(response)
        li_list = root.xpath("//ul[@class='carlist clearfix js-top']/li")
        for item in li_list:
            title = item.xpath(".//h2[@class='t']/text()")
            price = item.xpath(".//div[@class='t-price']/p/text()")

            data = {
                "title": title[0],
                "price": price[0]
            }
            print(data)
        #     post.insert_one(data)
        # client.close()


if __name__ == '__main__':
    start_time = time.time()
    ceshi()
    print(time.time() - start_time)
