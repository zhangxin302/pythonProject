"""
author:张鑫
date:2021/5/14 14:23
"""
import json
import requests
import re

from tools.headers import headers

url = 'https://p.3.cn/prices/mgets?callback=jQuery6712862&type=1&area=1_2800_55811_0&pdtk=&pduid=16209731728481737821774&pdpin=&pin=null&pdbp=0&skuIds=J_100016780992%2CJ_10020516389634%2CJ_48267736346%2CJ_100004325476%2CJ_72308063731%2CJ_10026121674907%2CJ_100009477910%2CJ_10020380288289%2CJ_68752491808%2CJ_10023428359778&ext=11100000&source=item-pc'

html = requests.get(url=url, headers=headers).content.decode()

# # 原价
op = re.findall('"op":"(.*?)","cbf":"', html)[0]
print(f"原价：{op}")
# # 特价
p = re.findall('"p":"(.*?)","op":"', html)[0]
print(f"特价：{p}")
