"""
https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=2783187&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1
https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=2783187&score=0&sortType=6&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1
https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=2783187&score=0&sortType=6&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1
https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=2783187&score=0&sortType=6&page=3&pageSize=10&isShadowSku=0&rid=0&fold=1
"""
from a_公司项目.京东评论数据.chi import get_ua
from a_公司项目.京东评论数据.chi import cooies
import requests
import re
import json
import time
import random
from fake_useragent import UserAgent
from openpyxl import Workbook
import csv
class JD():

    def __init__(self):
        self.headers = {
            "user-agent": get_ua()
        }
        self.s = 1
        self.f = open('酒.csv', 'w', encoding='utf-8')
        self.csv_writer = csv.writer(self.f)
        self.csv_writer.writerow(['内容', '评论时间', '用户名', 'id', '产品名', '购买类型'])
    # 第一页内容
    def one_html(self):
        #######https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100010617336&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=60109284815&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        header = {
            'User-Agent': get_ua(),
            'Cookie': cooies()
        }
        t = requests.get(url, headers=header).text
        # json1 = re.findall(r'fetchJSON_comment98\((.*?)}\)', html1)[0]+"}"
        # t = re.search(r'(?<=fetchJSON_comment98\().*(?=\);)', t).group(0)
        t = re.findall(r'fetchJSON_comment98\((.*?)}\)', t)[0]+"}"
        print(t)
        j = json.loads(t)
        commentSummary = j['comments']
        for comment in commentSummary:
            list1 = []
            c_content = comment['content']
            list1.append(c_content)
            c_time = comment['creationTime']
            list1.append(c_time)
            c_name = comment['nickname']
            list1.append(c_name)
            c_id = comment['id']
            list1.append(c_id)
            c_referenceName = comment['referenceName']
            list1.append(c_referenceName)
            c_productColor = comment['productColor']
            list1.append(c_productColor)
            print(list1)
            self.csv_writer.writerow(list1)
        print("第", self.s, "页")
        self.s += 1
        time.sleep(random.randint(10, 12))

    # 其他页数据
    def get_html(self):
        for i in range(99):
            two_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=60109284815&score=0&sortType=6&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(
                i)
            print(two_url)
            t = requests.get(two_url, headers=self.headers).text
            t = re.search(r'(?<=fetchJSON_comment98\().*(?=\);)', t).group(0)
            j = json.loads(t)
            commentSummary = j['comments']
            for comment in commentSummary:
                list1 = []
                c_content = comment['content']
                list1.append(c_content)
                c_time = comment['creationTime']
                list1.append(c_time)
                c_name = comment['nickname']
                list1.append(c_name)
                c_id = comment['id']
                list1.append(c_id)
                c_referenceName = comment['referenceName']
                list1.append(c_referenceName)
                c_productColor = comment['productColor']
                list1.append(c_productColor)
                print(list1)
                self.csv_writer.writerow(list1)
            print("第", self.s, "页")
            self.s += 1
            time.sleep(random.randint(11, 14))


if __name__ == '__main__':
    j = JD()
    j.one_html()
    j.get_html()