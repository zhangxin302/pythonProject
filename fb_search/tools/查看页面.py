# -*- coding: utf-8 -*-
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import re
import time
from tools.extract_time import handle_pub_time
import hashlib
name = input('输入启动名称')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument(r'--user-data-dir=E:\Projects\+639957919351')  # 配置文件1
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(920, 1200)
wait = WebDriverWait(driver, 10)
# driver.get("https://www.facebook.com/search/posts/?q=新冠疫情")
# sleep(random.randint(10,15))
# html = etree.HTML(driver.page_source)
# div_list = html.xpath('//div[@role="article"]/div/div')
# div_num=int(len(div_list))
# for num in range(1,div_num+1):
#     xpath_rule='//div[@role="feed"]/div/div[{}]//div[@role="article"]/div/div/div/div/div[3]/a'.format(num)
#     driver.find_element_by_xpath(xpath_rule).click()
#     sleep(5)
#     driver.execute_script("window.scrollTo(0,{});".format(random.randint(3000, 9000)))
#     print(driver.current_url)
#     driver.back()
# driver.close()

# https://twitter.com/today_not_good/status/1078494831188402176  # 回复
# https://twitter.com/adam_lee1984/status/1078492080559845376  # 主题贴
# driver.get('http://bbs.bato.cn/forum.php?mod=post&action=newthread&fid=497')
# driver.get('http://cpf110.com/code-l/index.php')
url=' https://www.facebook.com/MFAofficeHK/posts/1337799716594833'
driver.get(url)
sleep(5)
html=etree.HTML(driver.page_source)
divlist=html.xpath('//div[@role="main"]/div[4]/div[1]')[0]
post_data_li = []
postdic={}
# 主贴作者信息
div2=divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[2]')[0]
ir_authors=div2.xpath('./div/div[2]//div/div[1]//text()')[0]  # 作者的名字(ir_authors)
urltime_text="".join(div2.xpath('./div/div[2]//div/div[2]//text()'))
ir_urltime=handle_pub_time(urltime_text.replace("=",'').split('·')[1].strip())   # 文章发布时间
ir_sid=re.findall("\d{10,}",url)[0]              # 作者的id(ir_sid)
ir_content = "".join(divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[3]/div[1]//text()'))
ir_title = ir_content[:60] if len(ir_content) > 60 else ir_content  # 文章的标题(ir_title)
# 评论数据（包含主贴转赞评）
div4=divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[4]')[0]
# 主贴转赞评
zzp=div4.xpath('./div/div/div[1]/div/div[1]//text()')
try:
    ir_nresrved1=re.findall('\d+',zzp[4])[0] # 文章分享数(ir_nresrved1)
except:
    ir_nresrved1=""
try:
    ir_nresrved2="".join(re.findall('\d+',zzp[2]))
except:
    ir_nresrved2=""  # 文章点赞数(ir_nresrved2)
try:
    ir_nresrved3 = re.findall('\d+', zzp[3])[0]  # 文章评论数(ir_nresrved3)
except:
    ir_nresrved3=""
postdic["ir_authors"]=ir_authors
postdic["ir_urltime"]=ir_urltime
postdic["ir_urldate"]=int(time.time())
postdic["ir_url"]=url
postdic["ir_sid"]=ir_sid
postdic["ir_content"]=ir_content
postdic["ir_title"]=ir_title
postdic["ir_nresrved1"]=ir_nresrved1
postdic["ir_nresrved2"]=ir_nresrved2
postdic["ir_nresrved3"]=ir_nresrved3
postdic["ir_ispost"] =1   # 1为主贴 2为评论
postdic["ir_area"]=1      #1为国外  2为国内
postdic["ir_mediatype"] = 8
postdic["ir_mediasource"] ="facebook"
postdic["ir_firsturl"] =url
postdic["ir_md5"] =hashlib.md5(url.encode(encoding='UTF-8')).hexdigest()
post_data_li.append(postdic)
#评论数据
try:
    commen_list=div4.xpath('.//div/div/div[2]/ul/li')
    for i in commen_list:
        try:
            commendic = {}
            commnet_authors = i.xpath('./div/div/div[2]//a//span[@dir="auto"]/text()')[0]

            comment_textdiv=i.xpath('.//div[@role="article"]/div[2]/div')
            if len(comment_textdiv)<2:
                comment_content ="".join(i.xpath('.//div[@role="article"]/div[2]/div[1]//div[@dir="auto"]//text()'))
                try:
                    img_list=i.xpath('.//div[@role="article"]/div[2]/div[1]//div[@dir="auto"]//img')
                    for img in img_list:
                        comment_content+=img.xpath("./@alt")[0]
                except:
                    pass
            else:
                comment_content=""
                try:
                    img_list = i.xpath('.//div[@role="article"]/div[2]/div[2]//img')
                    for img in img_list:
                        comment_content+=img.xpath("./@src")[0]
                except:
                    pass
            print("评论作者名：", commnet_authors,"*********评论内容:",comment_content)
            # commnet_url = i.xpath('.//div[@role="article"]/div[2]//li[3]/a/@href')[0]
            # try:
            #     commnet_urltime=handle_pub_time(i.xpath('//div[@role="article"]/div[2]//li[3]/a//text()')[0].strip())
            # except:
            #     print("时间转换错误，提取时间为————————————————————",i.xpath('//div[@role="article"]/div[2]//li[3]/a//text()')[0].strip())
            # commendic["ir_authors"] = commnet_authors
            # commendic["ir_urltime"] = commnet_urltime
            # commendic["ir_urldate"] = int(time.time())
            # commendic["ir_url"] = commnet_url
            # commendic["ir_sid"] =""
            # commendic["ir_content"] = comment_content
            # commendic["ir_title"] = ir_content
            # commendic["ir_nresrved1"] =""
            # commendic["ir_nresrved2"] =""
            # commendic["ir_nresrved3"] =""
            # commendic["ir_ispost"] = 2  # 1为主贴 2为评论
            # commendic["ir_area"] = 1  # 1为国外  2为国内
            # commendic["ir_mediatype"] = 8
            # commendic["ir_mediasource"] = "facebook"
            # commendic["ir_firsturl"] = url
            # commendic["ir_md5"] = hashlib.md5(commnet_url.encode(encoding='UTF-8')).hexdigest()
            # post_data_li.append(commendic)
        except:
            continue
except:
    print("没有评论数据")

print(post_data_li)
driver.close()
sleep(1000)
