import requests
from utils.headers import headers_with_ChromeUA

from bs4 import BeautifulSoup
from lxml import etree
import re

url = "http://www.wlhn.com/ht/so?code=wzlitong&no=2021040749185"
response = requests.get(url,headers=headers_with_ChromeUA)
html_str = response.content.decode()
root = etree.HTML(html_str)
li_list = root.xpath("//div[@id='infor']/ul[@id='trace']/li")
print(len(li_list))
for li in li_list:
    cover_url =li.xpath(".//em[@class='logistics-text']/text()")[0]
    time = str(li.xpath(".//span[@class='icon-12 logistics-time']/text()")).replace("\\","").replace("xa0","")
    date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", time)
    print(date_all)
