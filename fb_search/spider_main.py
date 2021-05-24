# _*_ coding:utf-8 _*_  
import json
import os
import sys
from time import sleep
from lxml import etree
import random
import redis
sys.path.append(os.path.dirname(__file__))

from tools.logger_server import logger
from tools.selenium_server import SeleniumServer
from tools.extract import Extract
from tools.connect_mysql import Save_Data

from settings import REDIS, EPR_TIME


class FB:

    def __init__(self):

        self.selenium = SeleniumServer()
        self.driver = self.selenium.driver
        self.redis = REDIS

        self.logger = logger
        self.extract = Extract()

        self.epr_time = EPR_TIME


    def start(self, keyword):
        """程序的入口
        :param keyword 搜索的关键字
        """
        self.logger.debug('start: {}'.format(keyword))

        # 打开关键字搜索结果帖子
        home_url = 'https://www.facebook.com/search/posts/?q={}'.format(keyword)
        try:
            self.driver.get(home_url)
        except:
            pass
        sleep(random.randint(10,15))
        html = etree.HTML(self.driver.page_source)
        div_list = html.xpath('//div[@role="article"]/div/div')
        div_num = int(len(div_list))
        try:
            for num in range(1, div_num + 1):
                xpath_rule = '//div[@role="feed"]/div/div[{}]//div[@role="article"]/div/div/div/div/div[3]/a'.format(num)
                self.driver.find_element_by_xpath(xpath_rule).click()
                sleep(random.randint(2,5))
                post_url=self.driver.current_url
                self.logger.debug('进入详情页: {}'.format(post_url))
                try:
                    post_data_li=Extract.parse_post(self.driver.page_source,post_url,keyword)
                    Save_Data(post_data_li)
                    self.driver.execute_script("window.scrollTo(0,{});".format(random.randint(3000,9000)))
                except:
                    self.driver.refresh()
                    sleep(random.randint(2, 5))
                    try:
                        post_data_li = Extract.parse_post(self.driver.page_source, post_url,keyword)
                        Save_Data(post_data_li)
                        self.driver.execute_script("window.scrollTo(0,{});".format(random.randint(3000, 9000)))
                    except:
                        self.logger.debug('详情页: {}数据解析错误'.format(post_url))
                sleep(random.randint(2,5))

                self.driver.back()
                sleep(random.randint(2,6))

            self.selenium.close_driver()
        except:
            self.logger.debug('关键字: {}搜索结果的详情页链接匹配错误'.format(keyword))
            self.selenium.close_driver()

if __name__ == '__main__':
    # facebook 公共主页的信息
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    while True:
        if r.scard("keyword")==0:
            print("暂无关键字数据抓取")
            break
        else:
            keyword=r.spop("keyword").decode("utf-8")
            try:
                fb_server = FB()
                fb_server.start(keyword)
                sleep(random.randint(60*4, 60*8))
            except:
                sleep(random.randint(30*1, 30*3))
                continue
    # keyword_list=["疫苗","疫情","新冠","口罩"]
    # for keyword in keyword_list:
    #     fb_server = FB()
    #     fb_server.start(keyword)
    #     sleep(random.randint(60*4, 60*8))
