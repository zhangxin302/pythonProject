"""
author:张鑫
date:2021/4/12 9:20
"""
import requests
from utils.headers import headers_with_ChromeUA
from lxml import etree

url = "http://gztianyou.wx.520163.com/logic/trace_route.aspx?lcode=21040865193 "
Referer="http://gztianyou.wx.520163.com/logic/order_list_acct.aspx?code=043s09ll2wbzP64zBFml2o9EUp2s09ly&state=gztianyou2"
response = requests.get(url,Referer,headers=headers_with_ChromeUA)
html_str = response.content.decode()
root = etree.HTML(html_str)
li_list = root.xpath("//div[@class='container-fluid']")
print(type(li_list))
for li in li_list:
    cover_url = str(li.xpath(".//div[@class='col-xs-8  ']/text()")).replace("\\","").replace(" ","").replace("rn","").replace("'","").replace(",","").replace("[","").replace("]","")
    num = li.xpath(".//div[@class='col-xs-8  ']/b/text()")[0]
    # content =str(li.xpath(".//div[@class='media-body']/p[@class='color6']/text()")).replace(" ","").replace("\\","").replace("rn","").replace("[","").replace("]","").replace("'","")
    content=str(li.xpath(".//div[@class='media-body']/p/text()")).replace(" ","").replace("\\","").replace("rn","").replace("'","")
    print(type(content))
    print(content)