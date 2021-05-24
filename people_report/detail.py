# 导入模块
import json
import time
import requests
import random
import re
from bs4 import BeautifulSoup
from tools.headers import headers
import pandas as pd
import pymongo

# 连接数据库
database = pymongo.MongoClient('localhost', port=27017)
db = database['report']
people_report_list = db['people_report_list']
detail_list = db['detail_list']

# 获取数据库数据
data = pd.DataFrame(list(people_report_list.find()))
# 获取所需字段
data = data['article_url']
data = data.values
for data in data[:-3]:
    print(data)
url = 'http://m.news.cctv.com/2020/11/23/ARTImvP4IgohSC3sO5Paon5O201123.shtml'
html = requests.get(url=url, headers=headers, verify=False).content.decode()
content = BeautifulSoup(html, 'lxml')
content = content.select('div.col_w660')[0]
content = str(content)
# for item in content:
#     print(type(str(item)))
# 标题
title = re.findall('<!--repaste.title.begin-->(.*?)<!--repaste.title.end-->', content)[0]
# 发布单位
company = re.findall('<a href="http://news.cntv.cn/mobile/" target="_blank">(.*?)</a>', content)[0]
# 来源
referce = re.findall('<i>(.*?)</i>', content)[0]
# 正文
html = '''
<span style="font-size: 16px;">“小康路上一个都不能少”，这是习近平总书记反复提及的庄严承诺。</span><br/></p>
<p><span style="font-size: 16px;">从民族地区到革命老区，习近平一路风雨，脚步不停，看基础设施、看公共服务，着眼大局、精准定位，开出一张张“脱贫药方”。</span></p>
<p><span style="font-size: 16px;">“老区在全国建小康的征程中要同步前进，一个也不能少”；“脱贫、全面小康、现代化，一个民族都不能少”。十八大以来，贫困地区基本生活条件明显改善，具备条件的建制村全部通硬化路，深度贫困村地区通宽带比例达到98%。国家教育经费也持续向贫困地区倾斜，10.8万所义务教育薄弱学校的办学条件得到改善。</span></p>
<p><span style="font-size: 16px;">为了不让任何一个贫困群众掉队，不遗漏任何一个脱贫指标，习近平总书记亲自指挥、精准部署，全国上下同心协力。最便捷的基础设施、最普惠的扶贫政策，惠及每一个脱贫路上的困难群众，中华民族“战胜贫困”的夙愿正在变为现实。</span></p>
<p><span style="font-size: 16px;"><br/></span></p>
<p><span style="font-size: 16px;"></span></p>
<p style="white-space: normal;"><span style="font-size: 16px;"><span style="caret-color: rgb(127, 127, 127); color: rgb(127, 127, 127);">系列时政微视频·变迁｜总书记指挥打赢世纪脱贫攻坚战｜近期内容&gt;&gt;</span></span></p>
<p style="white-space: normal;"><span style="color:#7f7f7f;font-size:16px">第一集《一往情深》&gt;&gt;</span><span style="caret-color: rgb(127, 127, 127); font-size: 16px; color: rgb(31, 73, 125);"><a _href="http://api.cportal.cctv.com/api/newsInsert/ywnr.html?id=Artidz4qVDJsGt7Dc1dVNBks201123&amp;preview=1&amp;version=724" href="http://api.cportal.cctv.com/api/newsInsert/ywnr.html?id=Artidz4qVDJsGt7Dc1dVNBks201123&amp;preview=1&amp;version=724" target="_self">点击查看</a></span></p>
<p><font color="#7f7f7f" size="3"><span style="caret-color: rgb(127, 127, 127);">第二集《最后的攻坚》<span style="caret-color: rgb(127, 127, 127); color: rgb(127, 127, 127);">&gt;&gt;</span></span></font><a _href="http://api.cportal.cctv.com/api/newsInsert/ywnr.html?id=ArtiNpolrlXQP5EHUEOSQu9J201123&amp;preview=1&amp;version=724" href="http://api.cportal.cctv.com/api/newsInsert/ywnr.html?id=ArtiNpolrlXQP5EHUEOSQu9J201123&amp;preview=1&amp;version=724" target="_self"><font color="#7f7f7f" size="3"><span style="caret-color: rgb(127, 127, 127); color: rgb(31, 73, 125);">点击查看</span></font></a></p>
'''

pre = re.compile('>(.*?)<')
content = ''.join(pre.findall(html))
content = str(content).replace('&gt;','')
print(f"标题：{title}")
print(f"发布单位：{company}")
print(f"来源：{referce}")
print(f"内容：{content}")
