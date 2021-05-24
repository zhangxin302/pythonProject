"""
author:张鑫
date:2021/4/9 11:54
"""
import json

import pymysql
from bs4 import BeautifulSoup
import requests, random, time
import xlwt
from tools.headers import headers

for i in range(1, 3):
    if i == 1:
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=72342821969&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    if i == 2:
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=72342821969&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
    response = requests.get(url, headers=headers)
    html = response.content.decode('gbk')
    html = html.replace("fetchJSON_comment98(", "")
    html = html.replace(");", "")
    html = json.loads(html)
    list1 = []

    worksheed = ["评价"]
    for item in html["comments"]:
        item = item["content"]
        print(item)

        db = pymysql.connect(user='root', password='zhangxin941021', database='jd')

        cursor = db.cursor()
        sql = """
        insert into jd values(%s)
        """
        cursor.execute(sql,item)
        db.commit()
        db.close()

