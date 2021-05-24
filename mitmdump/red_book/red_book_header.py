from lxml import etree
import requests
import re

from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().random
}

url = 'https://www.xiaohongshu.com/explore'

response = requests.get(url=url, headers=headers)

html = response.text
# print(html)
results = etree.HTML(html)

titles = re.findall(r'"title":"(.*?)"', html)[14:]

names = re.findall(r'"nickname":"(.*?)"', html)
times = re.findall(r'"time":"(.*?)"', html)
likes = re.findall(r'"likes":([0-9]{1,})', html)

print(titles,names,times,likes)

dic1 = {}
list1 = []
# for i in range(len(titles)):
#     dic1['title'] = titles[i]
#     dic1['name'] = names[i]
#     dic1['time'] = times[i]
#     dic1['like'] = likes[i]
#     list1.append(dic1)
#     dic1 = {}
# print(list1)