"""
author:张鑫
date:2021/5/13 11:41
"""
# !/usr/bin/env python
"""
web端   抖老板 投放视频抓取
https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-04-23%2000:00&end_time=2021-04-23%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page=1&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67
https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-04-25%2000:00&end_time=2021-04-25%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=1&page=1&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67
首页  https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-04-23%2000:00&end_time=2021-04-23%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page=1&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67
详情  https://api.doulaoban.com/v1/task/plas/task_detail?id=6292411&status=0&time_type=pay_time&start_time=2020-08-21%2000:00&end_time=2020-08-22%2023:59&index_ids=4,6,13,15,30,36,41,47,67,42,35&grading=5&goods_id=

"""
from loguru import logger
import requests
import time
import re
import json
import schedule

# from flask import Flask
from base.mysql_db import MySQLPipeline


#
def mysql():
    # new_time=time.strftime("%H:%M", time.localtime())

    # mon = (time.strftime("%m-%d",time.localtime()))
    # new_time = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    dt = time.strftime("%Y-%m-%d")

    mysql = MySQLPipeline()
    # app = Flask(__name__)

    headers = {
        "cookie": "Hm_lvt_95f29f66fe1210be4b5158abc33863ee=1618982380,1619059458,1619061523,1620292354; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmRvdWxhb2Jhbi5jb20vbG9naW4iLCJpYXQiOjE2MjAyOTIzNjgsImV4cCI6MTYyMTUwMTk2OCwibmJmIjoxNjIwMjkyMzY4LCJqdGkiOiJxOUJXdXBTaldnaVJhbVpVIiwic3ViIjoyNDEzMjYsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEiLCJjb21wYW55IjoyMDYyNjMsImNvbXBhbnlfdXNlciI6MjQxMzI2LCJmcm9tIjoid2ViIn0.9L7hbBBeRHXPk0wW7T5kWbnrgUK2qikUAHLcZ3jCkxI; Hm_lpvt_95f29f66fe1210be4b5158abc33863ee=1620370248",
        "referer": "https://zs.doulaoban.com/Monitor_plus",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }

    # @app.route('/jim')
    # def hello():
    num = 0
    # for page in range(1,2016, +1):
    for page in range(1, 5, +1):
        logger.warning(f"当前是第 {page} 页")
        # https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-05-11%2000:00&end_time=2021-05-11%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page=3&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67
        url = f"https://api.doulaoban.com/v1/task/plas/task_list?is_open_comment=&goods_id=&query_user=&start_time=2021-05-11%2000:00&end_time=2021-05-11%2023:59&order=&by=&aweme_ids=&order_site_id=&site_id=&status=&page={page}&paginate=15&time_type=creat_time&index_ids=4,6,12,13,15,30,36,41,47,67"
        response = requests.get(url, headers=headers)

        logger.info(f"请求状态{response.status_code}")

        res = response.json()
        req_code = res.get("code")

        if req_code != 1000:
            logger.error("请求错误,状态码不对")
            logger.error(f"{res} \n\n")
            exit()
        data_len = len(res["data"]["data"])
        logger.info(f"当前数据长度为{data_len}")
        if data_len < 5:
            logger.info(res)

        for crawl_list in res["data"]["data"]:
            num += 1
            # task_u_id = crawl_list['task_u_id']
            id = crawl_list["id"]
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
            # print(id,desc,video_play_url)
            # count = ["play_increment+cost+shopping_click+shopping_price+shop_price+used_price+used_order+used_price_roi+used_one_price+used_order_price"]
            # print(id,desc,video_play_url,play_increment,cost,shopping_click,shopping_price,shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price)
            print(
                f"id{id},标题{desc},视频链接{video_play_url},Dou+播放增量{play_increment},时段消耗{cost},购物车点击量{shopping_click},购物车单价{shopping_price},进店单价{shop_price},有效的{used_price},有效单数{used_order},ROI{used_price_roi},有效单笔价{used_one_price},有效出单成本{used_order_price}")
            mysql.list_sql(id, desc, video_play_url, play_increment, cost, shopping_click, shopping_price, shop_price,
                           used_price, used_order, used_price_roi, used_one_price, used_order_price, create_time,
                           created_at)

            # doumysql.list_sql(id, desc, video_play_url,play_increment,cost,shopping_click,shopping_price,shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price)
            # doumysql.close_spider()
            #         url2 = f"https://api.doulaoban.com/v1/task/plas/task_detail?id=8319056&status=0&time_type=pay_time&start_time=2021-05-10%2000:00&end_time=2021-05-11%2023:59&index_ids=4,6,13,15,12,14,30,36,41,47,67,42,35&grading=5&goods_id="
            url2 = f"https://api.doulaoban.com/v1/task/plas/task_detail?id={id}&status=1&time_type=pay_time&start_time={dt} 00:00&end_time={dt} 23:59&index_ids=4,6,13,15,30,36,41,47,67,42,35&grading=2&goods_id="
            response2 = requests.get(url=url2, headers=headers)
            res2 = response2.content.decode()
            content2 = re.sub("\s", "", res2)
            content2 = json.loads(content2)
            if content2['code'] == 1000:
                for detail in content2['data']['list']:
                    t_id = ["id"]
                    # dou_task_id = detail['dou_task_id']
                    show_time = detail["show_time"]
                    play_count = detail["play_count"]
                    start_time = detail["start_time"]  # 开始时间 "2021-04-28 09:40:00"
                    end_time = detail["end_time"]  # 结束时间  "2021-04-28 09:50:00"
                    play_all_count = detail["play_all_count"]  # 播放量
                    play_increment = detail["play_increment"]  # 投放增量
                    cost = detail["cost"]  # 投放消耗
                    shopping_price = detail["shopping_price"]  # 购物车单价
                    # shopping_click = detail["shopping_click"]   # 购物车点击量
                    # shop_visit_count = detail["shop_visit_count"]  # 店铺引流量
                    shop_price = detail["shop_price"]  # 进店单价
                    used_price = detail["used_price"]  # 有效的
                    used_order = detail["used_order"]  # 有效单数
                    used_price_roi = detail["used_price_roi"]  # ROI
                    used_one_price = detail["used_one_price"]  # 有效单笔价
                    used_order_price = detail["used_order_price"]  # 有效出单成本
                    used_income_roi = detail["used_income_roi"]  # 有效佣金ROI
                    all_order = detail["all_order"]  # 全部单数
                    count2 = [
                        "play_count" + "play_all_count" + "play_increment" + "cost" + "shopping_price" + "shop_price" + "used_price" + "used_order" + "used_price_roi" + "used_one_price" + "used_order_price" + "used_income_roi" + "all_order"]
                    print(
                        f"日期{show_time},开始时间{start_time},结束时间{end_time},总数{play_count},播放量{play_all_count},投放增量{play_increment},投放消耗{cost},购物车单价{shopping_price},,进店单价{shop_price},有效的{used_price},有效单数{used_order},ROI{used_price_roi},有效单笔价{used_one_price},有效出单成本{used_order_price},有效佣金ROI{used_income_roi},有效单数{all_order}")
                    # mysql.list_sql(id, desc, video_play_url, play_increment, cost, shopping_click, shopping_price, shop_price, used_price, used_order, used_price_roi, used_one_price, used_order_price)
                    # mysql.detail_sql(show_time, play_count, play_all_count, play_increment, cost,
                    #            shopping_price, shop_price, used_price, used_order, used_price_roi,
                    #            used_one_price, used_order_price, used_income_roi, all_order)
                    mysql.detail_sql(t_id, show_time, start_time, end_time, play_count, play_all_count, play_increment,
                                     cost, shopping_price,
                                     shop_price, used_price, used_order, used_price_roi, used_one_price,
                                     used_order_price,
                                     used_income_roi, all_order)
            logger.info("sleep 5 s")
            time.sleep(1)
    mysql.close_spider()


if __name__ == '__main__':
    while 1:
        schedule.every(10).minutes.do(mysql)
        schedule.run_pending()
        time.sleep(10)









