# -*- coding=utf-8 -*-
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
from selenium.webdriver.common.keys import Keys


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
        # 打开首页
        home_url = 'https://www.facebook.com'
        try:
            self.driver.get(home_url)
        except:
            pass
        sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath('//input[@type="search"]').send_keys(keyword)
        sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath('//input[@type="search"]').send_keys(Keys.ENTER)
        # 打开关键字搜索结果帖子
        # key_url = 'https://www.facebook.com/search/posts/?q={}'.format(keyword)
        # try:
        #     self.driver.get(key_url)
        # except:
        #     pass
        sleep(random.randint(1,3))
        #
        try:
            self.driver.find_element_by_xpath('//div[@aria-label="筛选条件"]/div/div[2]/div[1]/div/div/div/div[2]/div[2]').click()
        except:
            self.driver.find_element_by_xpath('//ul[@role="listbox"]/li[last()]').click()
            sleep(random.randint(1, 3))
            self.driver.find_element_by_xpath(
                '//div[@aria-label="筛选条件"]/div/div[2]/div[1]/div/div/div/div[2]/div[2]').click()
        sleep(random.randint(3, 6))
        html = etree.HTML(self.driver.page_source)
        div_list = html.xpath('//div[@role="article"]/div/div')
        div_num = int(len(div_list))
        try:
            for num in range(1, div_num + 1):
                try:
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
                except:
                    continue

            self.selenium.close_driver()
        except:
            self.logger.debug('关键字: {}搜索结果的详情页链接匹配错误'.format(keyword))
            self.selenium.close_driver()

if __name__ == '__main__':
    # facebook 公共主页的信息
    # r = redis.StrictRedis(host='localhost', port=6379, db=1)
    # while True:
    #     if r.scard("keyword")==0:
    #         print("暂无关键字数据抓取")
    #         break
    #     else:
    #         keyword=r.spop("keyword").decode("utf-8")
    #         try:
    #             fb_server = FB()
    #             fb_server.start(keyword)
    #             sleep(random.randint(60*4, 60*8))
    #         except:
    #             sleep(random.randint(30*1, 30*3))
    #             continue
    keyword_list=['NPC', 'CPPCC', 'two sessions', "the National People's Congress", "the Chinese People's Political Consulative Conference", 'delegate to NPC', 'member of CPPCC', 'the NPC standing Committee', 'the Standing Committee of  the CPPCC National Committee', '兩會', '全國人民代表大會', '中華人民共和國全國人民代表大會', '中國人民政治協商會議', '兩會時間', '中國人民政治協商會議全國委員會常務委員會', '两会', '全国人民代表大会', '中华人民共和国全国人民代表大会', '中国人民政治协商会议', '两会时间', '中国人民政治协商会议全国委员会常务委员会', '全国人民代表大会常务委员会', '全國人民代表大會常務委員會', '政協委員', '政協提案']
    # keyword_list=['光大信用卡', '光大+信用卡', '浦发+信用卡', '招商+信用卡', '中信+信用卡', '广发+信用卡', '兴业+信用卡', '民生+信用卡', '广发信用卡', '广发银行信用卡', '民生信用卡', '民生银行信用卡中心', '浦发银行信用卡', '浦发银行信用卡中心', '兴业银行信用卡', '兴业银行信用卡百科', '兴业银行信用卡中心', '招商银行信用卡', '招商银行信用卡中心', '中信银行信用卡', '中信银行信用卡中心', '平安+信用卡', '平安银行信用卡官方微博', '光大+信用卡+延后', '光大+信用卡+延期', '光大+信用卡+还款', '光大+信用卡+撤费', '光大+信用卡+歧视', '光大+信用卡+差异', '315消费宝', '啄木鸟投诉', '法律快车', '投诉直通车', '找法网', '华律网', '律图网', '110网', '中顾法律网', '中国质量万里行', '信用卡', '光大银行信用卡', '光大+信用卡+生孩子', '光大+信用卡+大出血', '光大+信用卡+坐月子', '光大银行+生孩子', '光大银行+大出血', '光大银行+坐月子', '光大银行+bug', '光大信用卡+bug', '光大信用卡+积分bug', '光大银行+8倍积分', '光大银行+8倍+积分', '光大银行+积分+bug', '光大银行+积分', '光大银行+积分bug', '光大信用卡+积分+bug', '光大信用卡+8倍积分', '光大信用卡+8倍+积分', '光大信用卡+积分', '光大+bug', '光大+积分bug', '光大+8倍积分', '电子认证', '在线诉讼', '在线仲裁', '存证', '电子证据', 'v2x', '车路协同', '电子劳动合同', '身份验证', '电子证照', 'V2X', '电子签名', '电子签约', '电子合同', '数字证书', 'ssl证书', '实名认证', '电子签章', 'TrustAsia', '上上签', '法大大', 'E签宝', '契约锁', '数字认证', 'CFCA', '亚洲诚信', '浙江葫芦娃', '数安时代', '天威诚信', '天诚安信', '天威诚信+陈韶光', '天威诚信+唐志红', '天威诚信+李延昭', 'e签宝', '全球能源互联网', '全球能源互联网发展合作组织', '刘振亚', 'Global Energy Internet', 'Global Energy Interconnection', 'Global Energy Interconnection Development and Cooperation Organization', 'GEIDCO', '全球能源互聯網', '全球能源互聯網發展合作組織', '劉振亞', 'GEI', '印度地球政策中心', '尼泊尔国际问题研究所', '关注环境发展和研究组织', '梅蒂斯全球意识网', '埃及伊纳雅资本有限公司', '阿尔及利亚爱途比商业信息公司', '埃及常青公司', '哥伦比亚人权网络基金会', '平民社会组织网', '澳大利亚达沃斯论坛', '澳大利亚基础设施伙伴关系', '南亚环境论坛', '达沃斯全球风险论坛', '维森林国际组织', '印度伊斯兰工商会', '澳大利亚新南威尔士大学', '莫纳什大学', '卧龙岗大学', '欧洲亚洲事务研究所', '贝鲁特美国大学', '美国环保协会', '环境可持续扶轮社行动小组', '地球再利用行动组织', '墨西哥自然保护协会南部分会', '多米尼加盈实基金会', '绿色星球', '印度乌达雅组织', '拯救地球柬埔寨', '拯救气候', '西纳姆青年慈善基金会', '治愈星球全球组织', '世界海洋委员会', '加拿大皇家银行财富管理中心', '美慈组织', '气候行动运动组织', '斯泰特咨询有限公司', '比利时旋转传媒', '伊格罗数字媒体公司', 'Itqan 可持续发展组织', '青年发展行动组织', '跨国社会人文技术思想基金组织', '全球能源网络协会', '国际塞勒姆妇女组织', '妇女环境计划布基纳法索代表处', '尼日尔青年环境志愿者组织', '乌班图青年发展组织', '艾玛斯国际信托组织', '荣誉殿堂基金', '尼泊爾國際問題研究所', '關注環境發展和研究組織', '梅蒂斯全球意識網', '埃及伊納雅資本有限公司', '阿爾及利亞愛途比商業資訊公司', '哥倫比亞人權網路基金會', '平民社會組織網', '澳大利亞達沃斯論壇', '澳大利亞基礎設施夥伴關係', '南亞環境論壇', '達沃斯全球風險論壇', '維森林國際組織', '印度伊斯蘭工商會', '澳大利亞新南威爾士大學', '莫納什大學', '臥龍崗大學', '歐洲亞洲事務研究所', '貝魯特美國大學', '美國環保協會', '環境可持續扶輪社行動小組', '地球再利用行動組織', '墨西哥自然保護協會南部分會', '多明尼加盈實基金會', '綠色星球', '印度烏達雅組織', '拯救氣候', '西納姆青年慈善基金會', '治癒星球全球組織', '世界海洋委員會', '加拿大皇家銀行財富管理中心', '美慈組織', '氣候行動運動組織', '斯泰特諮詢有限公司', '比利時旋轉傳媒', '伊格羅數位媒體公司', 'Itqan 可持續發展組織', '青年發展行動組織', '跨國社會人文技術思想基金組織', '全球能源網路協會', '國際賽勒姆婦女組織', '婦女環境計畫布吉納法索代表處', '尼日爾青年環境志願者組織', '烏班圖青年發展組織', '艾瑪斯國際信託組織', '榮譽殿堂基金', 'Terre Policy Center', 'Institute for International Relations-Nepal', 'Nepal-Institute for International Relations', 'Concern for Environmental Development And Research', 'Metis Global Awareness Network', 'Global Awareness Network', 'Enara Capital Limited', 'Sarl I2b Algeria', 'Evergreen Egypt United', 'Fundacion Red Colombiana Para La Defensa De Los Dh', 'Reseau Communautaire Pir Le\xa0Pauvre', 'ADC Forum', 'Infrastructure Partnership Australia', 'South Asian Forum for Environment', 'Global Risk Forum GRF Davos', 'WeForest', 'Indo-OIC Islamic Chamber of Commerce and Industry', 'The University of New South Wales', ' Sydney', 'Monash University', 'University of Wollongong', 'European Institute for Asian Studies', 'The American University of Beirut', 'Environmental Defense Fund', 'Environmental Sustainability Rotarian Action Group', 'Reusa Misión Planeta A.C.', 'Pronatura Sur', 'Fundacion Plenitud', 'Green Planet', 'UDYAMA', 'Save the Earth Cambodia', 'Save The Climate', 'Sadayanodai Ilaignar Narpani Mandram', 'Heal the Planet Global Organisation', 'World Ocean Council', 'Royal Bank of Canada Wealth Management Center', 'Mercy Corps', 'Climate Action Campaign', 'Stantec Consulting Ltd', 'Revolve Media', 'PT Ieglo Digital Kreasi', 'ItQan', 'Action for Youth Development Association', 'Ideology Fund', 'Global Energy Network Institute', 'NGO Femmes de Salem Internationale', 'Women Environmental Programme-Burkina', 'Ubuntu Youth in Development', 'Emmaus International Trust', 'The Performance Theater', 'Enara Capital', 'RCP-Network', 'InfraPshipAust', 'GRF Davos', 'UNSW Sydney', 'Misión planeta', 'Fundación Plenitud', 'RBC Wealth Management', 'MercyCorps', 'ONG Femmes de Salem', 'WEP-BF', 'Emmaus Trust', 'GEI+Energy Interconnection', '秀域', '加盟', '健康推广大使', '中国女篮', '女篮国家队', '马拉松', '奥运会', '美业+O2O', '美业+电商', '医美', '美业+社交', '张玉珊', '环球捕手+李潇', '肖尚略', '美容+美丽田园', '修身堂', '克丽缇娜', '思妍丽', '河狸家', '环球捕手', '微店+云集', '电商+云集', '李晓宁', '秀域+美容', '秀域+保健', '秀域+护肤', '秀妮儿内衣', '秀域+科技', '秀域+纤体塑形', '秀域+点阵波', '秀域+超V', '秀域+肩颈复苏', '秀域+亚健康调理', '秀域+医美', '秀域+微整形', '秀域+水光针', '秀域+祛斑', '秀域+激素脸', '秀域+青春痘', '秀域+抗衰', '秀域+注射美容', '秀域+减肥', '秀域+古方减肥', '秀域美容', '秀域+健康', '秀域+亚健康服务', '春语医美', '春语医疗美容', '春语微整形', '海医悦美', '秀域+健康科技', '秀域+大健康', '秀域+健康管理', '秀域+健康管家', '斑马会员', '扶贫', '医疗', '食品', '美妆', '大宝护手霜', '叮当快药', '教育', '人大代表', '东江湖', '武当山', '东江湖', '石牛山', '两会', '人大代表', '政协委员', '全国人民代表大会', ' 中华人民共和国全国人民代表大会', '中国人民政治协商会议', '两会时间', '全国人民代表大会常务委员会', '中国人民政治协商会议全国委员会常务委员会', '人大提案', '政协提案', '古武当山', '邯郸+武当山', '武安+武当山', '石牛山+福建', '石牛山+德化', '石牛山+水口镇', '中华人民共和国全国人民代表大会', '档案管理', '电子档案', '信息化', '信息安全', '窃取', '防范', '简单密码', '信息泄露', '加密', '安全产品', '网络安全', '高校信息维护', '队伍建设']

    for keyword in keyword_list:
        fb_server = FB()
        fb_server.start(keyword)
        sleep(random.randint(60*4, 60*8))
