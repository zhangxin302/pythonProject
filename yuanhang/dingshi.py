"""
@Project -> File   ：WebCrawler -> 3.py
@IDE    ：PyCharm
@Author ：Mr. Lvkun
@Date   ：2021/5/13 11:28
"""
import random

import requests
from fake_useragent import UserAgent
import re
import time
import pymongo


class HomeLinkSpider(object):
    # 初始化
    def __init__(self):
        self.database = pymongo.MongoClient('localhost', port=27017)
        self.db = self.database['report']
        self.people_report_list = self.db['people_report_list']
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.people_report = {}
        self.url = 'https://ib.snssdk.com/api/news/feed/v47/?last_ad_show_interval=-1&cached_item_num=3&ad_ui_style' \
                   '=%7B%22van_package%22%3A350000010%7D&refer=1&refresh_reason=0&count=20&max_behot_time=1620786034' \
                   '&last_refresh_sub_entrance_interval=1620786694&cp=6f0c92b73ae06q1&plugin_enable=4&loc_mode=5' \
                   '&tt_from=pre_load_more&lac=4527&cid=28883&client_extra_params=%7B%22ad_download%22%3A%7B' \
                   '%22space_unoccupied%22%3A56758388%2C%22space_cleanable%22%3A0%7D%2C%22last_ad_position%22%3A-1%2C' \
                   '%22playparam%22%3A%22codec_type%3A7%22%7D&iid=229152404021512&device_id=456997632486734&ac=wifi' \
                   '&mac_address=80%3AFA%3A5B%3A72%3AD3%3A1E&channel=lite2_tengxun&aid=35&app_name=news_article_lite' \
                   '&version_code=800&version_name=8.0.0&device_platform=android&ab_version=668904%2C2678438%2C668907' \
                   '%2C2648775%2C2678479%2C668903%2C2678473%2C1859937%2C668908%2C2678483%2C668905%2C2678447%2C668906' \
                   '%2C2678455&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=SM-G977N' \
                   '&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=351564272622119&openudid' \
                   '=9f1f47b29747b286&manifest_version_code=8000&resolution=900*1600&dpi=320&update_version_code' \
                   '=80006&_rticket=1620786694280&plugin_state=3616896348189&sa_enable=0&tma_jssdk_version=1.87.0.7' \
                   '&rom_version=22&cdid=16d9b212-e738-448e-a960-920b360286f2 '
    # 获取网页
    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers, verify=False).json()
        while 1:
            for item in html['data']:
                time.sleep(random.randint(1, 5))
                print(item)
                return item

    def task1(self):
        item = self.get_html()
        people_report = self.people_report
        people_report_list = self.people_report_list
        return self.sign_report(item, people_report, people_report_list)

    # 解析文本
    def sign_report(self, item, people_report, people_report_list):
        titles = item['content']
        # print(title,type(title))

        title = str(re.findall('"abstract":"(.*)","action_list"', titles)).replace(
            '","action_extra":"{\\"channel_id\\": 0}',
            '').replace(
            "']", ''
        ).replace("['", '')
        people_report['title'] = title
        article_url = str(re.findall('"article_url":"(.*)","article_version"', titles)).replace("['", "").replace("']",
                                                                                                                  "")
        people_report['article_url'] = article_url
        if people_report_list['title'] == people_report['article_url']:
            print('数据已存在')
            # continue
        else:
            print('********************************')

            people_report_list.insert(people_report)
            print(f"标题：{title}")
            print(f"题目链接：{article_url}")
            print(people_report)

            print('********************************')


if __name__ == '__main__':
    # 开始时间
    start = time.time()
    # 类实例化
    home_link_spider = HomeLinkSpider()
    # 调用类中函数
    home_link_spider.task1()
    # 结束时间
    end = time.time()
    # 时间差
    print("耗时：{}秒".format(end - start))
