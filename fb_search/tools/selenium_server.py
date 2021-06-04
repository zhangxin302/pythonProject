import os
import re
import sys
from time import sleep

from lxml import etree
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.path.dirname(__file__))
from fb_search.tools.extract_time import handle_pub_time
from fb_search.tools.utils import check_pub_time
from fb_search.tools.logger_server import logger


class SeleniumServer:

    def __init__(self):
        """
        selenium 插件服务，用于加载页面，操作页面服务
        """
        self.logger = logger

        driver_exe_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
        driver_js_path = os.path.join(os.path.dirname(__file__), 'stealth.min.js')
        print(driver_exe_path)
        print(driver_js_path)

        chrome_options = Options()
        # chrome_options.add_argument(r'--proxy-server=http://127.0.0.1:8888')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_argument(r'--user-data-dir=E:\Projects\+Jonathen Charm')  # 配置文件1
        chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36')
        # with open(driver_js_path) as f: js = f.read()

        self.driver = Chrome(driver_exe_path, options=chrome_options)
        # 去标识，反爬虫
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})

        self.wait_driver = WebDriverWait(self.driver, 30)  # 等待元素
        self.driver.set_page_load_timeout(60)  # 页面加载超时等待

    def loads_post(self, e_day=7):
        """
        根据帖子的过期时间下拉
        :param e_day:
        :return:
        """

        # 贴子时间
        epr_num = 5  # 过期的贴子数量
        for_num = 30  # 循环的的数量
        while True:
            if epr_num < 1:
                break
            if for_num < 1:
                break
            # 过期贴子 大于5   循环次数大于30 就停止下拉

            # 检测过期时间
            pub_time_tag_li = self.driver.find_elements_by_xpath('//div[@class="buofh1pr"]/div[1]/div[2]')

            for pub_time_tag in pub_time_tag_li:
                pub_time_text = pub_time_tag.text.strip()
                if not pub_time_text:
                    continue

                self.logger.debug('pub_time_text: {}, epr_num: {}, for_num: {}'.format(pub_time_text, epr_num, for_num))
                pub_time = handle_pub_time(pub_time_text)
                if not pub_time:
                    epr_num -= 1
                    continue
                if not check_pub_time(pub_time, e_day):
                    epr_num = 5
                else:
                    epr_num -= 1

                if epr_num < 1:
                    break
                if for_num < 1:
                    break

            try:
                self.driver.execute_script("window.scrollTo(0, {});".format(20000 * (for_num + 1)))
            except:
                pass
            sleep(2)
            for_num -= 1
        sleep(5)

    def click_sort_button(self):
        """点击排序"""
        button_xpath = '//div[@role="article" and @aria-posinset]//div[@role="button"]/span[@dir="auto"]'
        button_li = self.driver.find_elements_by_xpath(button_xpath)
        for button_msg in button_li:
            button_text = button_msg.text
            if '最' in button_text:
                # 最相关评论
                # 点击排序
                self.logger.debug('点击： {}'.format(button_text))
                actions = ActionChains(self.driver)
                actions.move_to_element(button_msg)
                actions.perform()
                sleep(1)
                actions.click()
                actions.perform()
                sleep(5)
                input()

                # 点击 由新到旧
                span_li = self.driver.find_elements_by_xpath('//div[@data-pagelet="root"]/div[@role="menu"]//span[@dir="auto"]')
                for span in span_li:
                    if '由新到旧' in span.text:
                        self.logger.debug('点击： {}'.format(span.text))
                        actions = ActionChains(self.driver)
                        actions.move_to_element(span)
                        actions.perform()
                        sleep(1)
                        actions.click()
                        actions.perform()
                        sleep(5)
                        break
                break
        input()

    def click_more_comment(self, post_id="10158991236280429"):

        # 获取xpath
        html = etree.HTML(self.driver.page_source)
        selenium_xpath = ''
        more_index = 0
        for posinset in range(1, 100):
            post_div_xpath_base = '//div[@role="article" and @aria-posinset="{}"]'.format(posinset)
            post_div = html.xpath(post_div_xpath_base)
            if not post_div:
                continue
            post_div = post_div[0]
            # 确认贴子
            comment_url_li = post_div.xpath('.//ul//a[contains(@href, "?comment_id=")]/@href')
            comment_url_li = [] if not comment_url_li else comment_url_li
            is_post = list(filter(lambda x: str(post_id) in x, comment_url_li))
            if is_post:
                self.logger.debug('找到贴子的div: {}'.format(post_id))
                # 找到评论位置
                span_li = post_div.xpath('.//span[@dir="auto"]')
                span_li = [] if not span_li else span_li
                span_li.reverse()
                for _index, span in enumerate(span_li):
                    span_text = ''.join(span.xpath('.//text()')).strip()
                    if re.compile('^其他\d+[,\d]*条评论?|^更多评论?|^\d+[,\d]*条回复?').findall(span_text):
                        self.logger.debug('找到更多评论的位置 {} : {}'.format(span_text, _index))
                        selenium_xpath = post_div_xpath_base
                        more_index = _index
                        break

                break
        for i in range(10):
            if selenium_xpath:
                js_text = """
                        function _clike(xpath_msg) {
                    var click_li = [];
                    var result = document.evaluate(xpath_msg, document);
                    var tag = result.iterateNext();
                    while (tag){
                        var tag_text = tag.innerText
                        console.log(tag_text);
                        is_more_tag = tag_text.match(/^其他\d+[,\d]*条评论?|^更多评论?|^\d+[,\d]*条回复?/)
                        if (is_more_tag){
                            console.log("评论按钮：   " + tag_text)
                            click_li.push(tag)
                        }
                        tag = result.iterateNext();
                    }
                    if (click_li){
                        const click_tag = click_li[click_li.length-1];
                        console.log("js 点击： "+ click_tag.innerText)
                        // debugger;
                        click_tag.scrollIntoView();
    
                        click_tag.click();
                    }
                }
                _clike('%s');
                        """
                js_text = js_text % (selenium_xpath + '//span[@dir="auto"]')

                try:
                    self.driver.execute_script(js_text)
                except:
                    pass
                sleep(2)
        # 不管用
        # if selenium_xpath:
        #     input('----')
        #     self.logger.debug('执行点击更多评论')
        #     post_div = self.driver.find_element_by_xpath(selenium_xpath)
        #     span_tag_li = post_div.find_elements_by_xpath('.//span[@dir="auto"]')
        #     span_tag_li.reverse()
        #     actions = ActionChains(self.driver)
        #     more_span = span_tag_li[more_index]
        #     self.logger.info(more_span.text)
        #     actions.move_to_element(more_span)
        #     actions.perform()
        #     sleep(5)
        #     more_span.click()
        #     sleep(5)
        #     input()

    def close_driver(self):
        try:
            self.driver.close()
        except:
            pass
        try:
            self.driver.quit()
        except:
            pass


if __name__ == '__main__':
    S = SeleniumServer()
    S.driver.get('https://www.facebook.com/')
    input()

