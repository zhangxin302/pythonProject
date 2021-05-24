"""
author:张鑫
date:2021/5/14 16:02
"""
import json
import requests
import time
import random
import re

from tools.headers import headers

# url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.26.561c1b11AIDaPk&id=632121623416&ns=1&abbucket=16'
url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.26.561c1b11AIDaPk&id=632121623416&ns=1&abbucket=16#detail'
html = requests.get(url=url, headers=headers, verify=False).content.decode('gb18030')
print(html)
# 价格
price = re.findall('<em class="tb-rmb-num">(.*?)</em></strong>', html)
for price in price:
    price = str(price).split('-')

# print(f"原价：{price}")
price = float(price[0])
print(f"原价：{price}")
print('优惠方式：15元店铺优惠券，满8999元可用')
print('优惠方式：10元店铺优惠券，满4999元可用')
if price > 8999:
    price -= 15
elif 4999 < price < 8999:
    price -= 10
else:
    price -= 0
print(f"优惠价：{price}")
