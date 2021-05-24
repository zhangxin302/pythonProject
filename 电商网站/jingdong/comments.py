"""
author:张鑫
date:2021/5/8 14:43

"""
import requests
import json
import pymongo
import time
import random
import re
import schedule

from tools.headers import headers

database = pymongo.MongoClient('localhost', port=27017)
db = database['jingdong']
comments = db['comments']


def jd_comments():
    url = 'https://search-x.jd.com/Search?callback=jQuery9050829&area=1&enc=utf-8&keyword=%E6%AF%8D%E4%BA%B2%E8%8A%82%E7%A4%BC%E7%89%A9&adType=7&page=1&ad_ids=291%3A33&xtest=new_search&_=1620456234422'
    html = requests.get(url=url, headers=headers).content.decode()
    html = html.replace('jQuery9050829(', '').replace(')', '')
    for item in json.loads(html)['291']:
        time.sleep(random.randint(1, 5))
        goods = {}
        goods['ad_title'] = item['ad_title']
        goods['ad_title'] = str(goods['ad_title']).replace('<font class="skcolor_ljg">', '').replace('</font>', '')

        goods['image_url'] = item['image_url'] + 'https://img14.360buyimg.com/n7/'
        goods['pc_price'] = item['pc_price']
        goods['sku_price'] = item['sku_price']
        goods['shop_name'] = item['shop_link']['shop_name']
        goods['comment_num'] = item['comment_num']
        goods['spu_id'] = item['spu_id']
        results = comments.count({"spu_id": item['spu_id']})
        if results == 0:
            print(goods['ad_title'])
            comments.insert_one(goods)
            results += 1
            continue
        else:
            print('订单已存在')


if __name__ == '__main__':
    while 1:
        # 没分钟执行一次jd_comments
        schedule.every().minute.do(jd_comments)
        # 执行所有函数
        schedule.run_pending()
        # 休眠20秒
        time.sleep(20)
