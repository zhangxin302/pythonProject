import requests
from utils.headers import headers_with_ChromeUA
from lxml import etree

# 获取原始的html字符串
url = "http://test11.yupu.cn/wxxm/ydcx.asp?wxid=o-lKT536XTCHr6HN9JdGuctora4M&userid=280"
response = requests.get(url,headers=headers_with_ChromeUA)
html_str = response.content.decode()

root = etree.HTML(html_str)
li_list = root.xpath("//div[@class='centent']/div[@class='centent_1']/div[@class='weui_cells weui_bg']")
# print(len(li_list))
dic = {}
for li in li_list:
    cover_url = li.xpath("//div[@class='weui_cell']/div[@class='weui_cell_bd weui_cell_primary']/p/text()")[0]
    num = li.xpath("//div[@class='weui_cell']/div[@class='weui_cell_ft']/text()")[0]
    num1 = li.xpath("//div[@class='weui_cell']/div[@class='weui_cell_bd weui_cell_primary']/p[@style='width: auto;']/text()")
    content = li.xpath(("//div[@class='weui_cell']/div[@style='text-align: left;']/text()"))
    print(dict(zip(num1,content)))