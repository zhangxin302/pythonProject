#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 13:52
# @Author  : yh
# @File    : demo1.py
# @Software: PyCharm
# @Desc    :
"""
https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-04-22%2000:00&end_time=2021-04-22%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page=30&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67
"""

import requests, json, re, datetime
# from base import mysql_help
# from base.mysql_help import MySQLPipeline

# new_time=time.strftime("%H:%M", time.localtime())
# new_time = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

# mysql = MySQLPipeline()

new_time = (datetime.datetime.now())




headers = {
    "cookie": "Hm_lvt_95f29f66fe1210be4b5158abc33863ee=1618982380,1619059458,1619061523,1620292354; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmRvdWxhb2Jhbi5jb20vbG9naW4iLCJpYXQiOjE2MjAyOTIzNjgsImV4cCI6MTYyMTUwMTk2OCwibmJmIjoxNjIwMjkyMzY4LCJqdGkiOiJxOUJXdXBTaldnaVJhbVpVIiwic3ViIjoyNDEzMjYsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEiLCJjb21wYW55IjoyMDYyNjMsImNvbXBhbnlfdXNlciI6MjQxMzI2LCJmcm9tIjoid2ViIn0.9L7hbBBeRHXPk0wW7T5kWbnrgUK2qikUAHLcZ3jCkxI; Hm_lpvt_95f29f66fe1210be4b5158abc33863ee=1620370248",
    "referer": "https://zs.doulaoban.com/Monitor_plus",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}
num = 0
for j in range(1,1950):
    url = f"https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-05-08%2000:00&end_time=2021-05-08%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page={j}&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67"
    # session = HTMLSession()
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    res = response.content.decode()
    content = re.sub("\s", "", res)
    content= json.loads(content)

    for crawl_list in content["data"]["data"]:
        num+=1
        dou_id = crawl_list["id"]
        desc = crawl_list["desc"]  # 标题
        video_play_url = crawl_list["video_play_url"]  # 视频链接
        play_increment = crawl_list["play_increment"]  # Dou+播放增量
        cost = crawl_list["cost"]  # 时段消耗
        shopping_click = crawl_list["shopping_click"]  # 购物车点击量
        shopping_price = crawl_list["shopping_price"]  # 购物车单价
        shop_price = crawl_list["shop_price"]  # 进店单价
        used_price = crawl_list["used_price"]  # 有效的
        used_order = crawl_list["used_order"]  # 有效单数
        used_price_roi = crawl_list["used_price_roi"]  # ROI
        used_one_price = crawl_list["used_one_price"]  # 有效单笔价
        used_order_price = crawl_list["used_order_price"]  # 有效出单成本
        create_time = crawl_list["create_time"]  # 创建时间
        created_at = crawl_list["created_at"]  # 结束时间
        print(
            f"id{dou_id},标题{desc},视频链接{video_play_url},Dou+播放增量{play_increment},时段消耗{cost},购物车点击量{shopping_click},购物车单价{shopping_price},进店单价{shop_price},有效的{used_price},有效单数{used_order},ROI{used_price_roi},有效单笔价{used_one_price},有效出单成本{used_order_price}")

        # mysql.list_sql(id, desc, video_play_url, play_increment, cost, shopping_click, shopping_price, shop_price,
        #                used_price, used_order, used_price_roi, used_one_price, used_order_price)


        url2 = f"https://api.doulaoban.com/v1/task/plas/task_detail?id={id}&status=1&time_type=pay_time&start_time=2021-05-14%2000:00&end_time=2021-05-14%2023:59&index_ids=4,6,13,15,30,36,41,47,67,42,35&grading=2&goods_id="
        # print(url2)
        response2= requests.get(url=url2,headers=headers)
        res2=response2.content.decode()
        content2 = re.sub("\s", "", res2)
        content2 = json.loads(content2)
        if content2['code'] == 1000:
            for detail in content2['data']['list']:
                detail_id = ["id"]
                # dou_task_id = detail['dou_task_id']
                show_time = detail["show_time"]
                play_count = detail["play_count"]
                start_time = detail["start_time"]  # 开始时间 "2021-04-28 09:40:00"
                end_time = detail["end_time"]  # 结束时间  "2021-04-28 09:50:00"
                play_all_count = detail["play_all_count"]  # 播放量
                play_increment = detail["play_increment"]  # 投放增量
                cost = detail["cost"]  # 投放消耗
                shopping_price = detail["shopping_price"]  # 购物车单价

                shop_price = detail["shop_price"]  # 进店单价
                used_price = detail["used_price"]  # 有效的
                used_order = detail["used_order"]  # 有效单数
                used_price_roi = detail["used_price_roi"]  # ROI
                used_one_price = detail["used_one_price"]  # 有效单笔价
                used_order_price = detail["used_order_price"]  # 有效出单成本
                used_income_roi = detail["used_income_roi"]  # 有效佣金ROI
                all_order = detail["all_order"]  # 全部单数
                shopping_click = detail["shopping_click"]  # 购物车点击量
                shop_visit_count = detail["shop_visit_count"]  # 店铺引流量
                print(f"日期{show_time},开始时间{start_time},结束时间{end_time},总数{play_count},播放量{play_all_count},投放增量{play_increment},投放消耗{cost},购物车单价{shopping_price},,进店单价{shop_price},有效的{used_price},有效单数{used_order},ROI{used_price_roi},有效单笔价{used_one_price},有效出单成本{used_order_price},有效佣金ROI{used_income_roi},有效单数{all_order},购物车点击量{shopping_click},店铺引流量{shop_visit_count}")
                  #     ,used_price_roi,used_one_price,used_order_price
                  # ,used_income_roi,all_order")


# mysql.close_spider()

# https://zs.doulaoban.com/Monitor_plusDetail?schedule_private_time=&itemAuthorId=1495780646716349&is_private=0&siteInfoId=1676548&siteInfoName=%E6%98%A5%E7%86%99%E5%AE%9D%E8%B4%9D%E5%84%BF&taskId=8449918&startTime=05-14%2012%3A10&endTime=&awemeId=6961988605573172491&commentIsOpen=0&goodsOrderType=1&desc=%E4%BF%9D%E5%AE%88%E5%A5%B3%E7%94%9F%E4%B9%9F%E8%83%BD%E7%A9%BF%E7%9A%84%E8%BF%90%E5%8A%A8%E8%83%8C%E5%BF%83%EF%BC%8C%E5%9B%A0%E4%B8%BA%E5%AE%83%E7%9C%9F%E7%9A%84%E5%A4%AA%E9%81%AE%E5%89%AF%E4%B9%B3%E4%BA%86%23%E5%87%8F%E8%82%A5%20%23%E7%98%A6%20%23%E6%98%BE%E7%98%A6%E7%A9%BF%E6%90%AD&taskStatus=1&tabType=timeMonitor