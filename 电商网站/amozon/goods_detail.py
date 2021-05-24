"""
author:张鑫
date:2021/5/10 9:31
https://www.amazon.cn/b?node=1519395071&pf_rd_r=CG8JXQ4NM8CR1QZWYWV2&pf_rd_p=bdf28247-c4f5-4084-8653-cb25630e3151&pd_rd_r=c7df14ac-ed58-4da2-b31e-186b53a60a20&pd_rd_w=P9AwD&pd_rd_wg=PlnCV&ref_=pd_gw_unk
<img class="s-image" src="https://images-cn.ssl-images-amazon.cn/images/I/71fIYYUMSoL._AC_UL320_.jpg"
alt="Huawei 华为 P40 Pro 智能手机，256GB 内存，8GB RAM，腮红金"
<span class="a-icon-alt">4.7 颗星，最多 5 颗星</span>
<span>购海外购商品满300元免运费</span>
<span class="a-offscreen">¥4,700.98</span>
"""
import re
from bs4 import BeautifulSoup

import requests

headers = {
    'cookie': 'session-id=462-7691734-6727513; ubid-acbcn=462-4201526-6080054; session-token="Q4s6gLR8eKptN5i+SMo/h/NHur6gzLluJGGWfxx34sl3LX5UQVtiQaK/+Dz3JXTyGBqAdguAtUtijXHlhwS6lw5e7TYRXpseAHa7CqrD1wkXnBrmY3CKJ7FwIbNeeLmvhUzUyV4J2D/nh1uOjVBA58ZnRyO9LeXEQ+jKIoCCUrLb187ja30qW61gAnAct3A97tJLq48L8jdn0xb727+F3br2lOviuI4+y6SvXt/W4wI="; x-acbcn="VSICvdadQqFqlWWVLUw9Q@6I7tLhe@J@3QrqUJ3pk6y4zKhDrCRS4kCMOuzcGRNH"; at-main=Atza|IwEBIIZc3nxq5u0KVgU-EbppX01u69yhhWNUxAP7nWmnrgzpE9VbdxaE1Tk9iEPgNbLScn7plmTodE8CG6Oo-5k6GlfE2nUZPvSknAd4hG8iS9LgwYrYUhHVgWKecSLdp7WcaWGsUjkbB9Iejt62rvDGu6KdR3kmO8cw6cO0x48l3_KavxUHHHW_Mq6eUhOe_Xd7E9XaEx1LRQo3_IjysUrNJ-jPayPDKUH6hgu2zH5vEiksUbPUdYJ8Sj8Mn9FtTqWKpo8; sess-at-main="vTFwOC7UV7xsXEOgkBiF5rLXPDZEQlA/wFgL/rbeCts="; sst-main=Sst1|PQGHfeQmHwV5jOqELnrxAf7WCVhBJ3MjbmiFFwEKaHHScIZ3xUnTodI3mnPZlDWqOzqx97mQQ0NF6vJDtzV6Jo5YRrm-fq6Uw0Oc3uw6tJyowV0H2PETcLvF-ifp4aOok2CcyxWq4dKMulkHOQwuSY5Qfp1fNHnx5FUMi2dpb2eWofWvhvNYzOhqDsdlDNNPdnmTEYRrwHC58m_tMzsLtP1R_TIdROwt0cz3_CCWwe88JgKCnOoHwOJyxt6I2Gp1QXPJDhn4w8J6q2Aym_zZNjmkVsEx4ceJrM4arcWQOrEPaz4; lc-acbcn=zh_CN; i18n-prefs=CNY; session-id-time=2082787201l; csm-hit=tb:DAJDQVB44MRAPTJ8Q6BP+s-WPRS63RNB92834M50PCJ|1620611867767&t:1620611867767&adb:adblk_no',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    'Referer': 'https://www.amazon.cn/b?node=1519395071&pf_rd_r=CG8JXQ4NM8CR1QZWYWV2&pf_rd_p=bdf28247-c4f5-4084-8653-cb25630e3151&pd_rd_r=c7df14ac-ed58-4da2-b31e-186b53a60a20&pd_rd_w=P9AwD&pd_rd_wg=PlnCV&ref_=pd_gw_unk',
}

url = 'https://www.amazon.cn/dp/B08MTXHCC2/ref=sr_1_79?dchild=1&pf_rd_i=1519395071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=0b8e6baa-7be1-4374-9059-a2430f0bf76c%2C0b8e6baa-7be1-4374-9059-a2430f0bf76c&pf_rd_r=29DMER63MAZ1G8S639FN%2C29DMER63MAZ1G8S639FN&pf_rd_s=merchandised-search-left-4&pf_rd_t=101&qid=1620612321&s=amazon-global-store&sr=1-79 '

html = requests.get(url=url, headers=headers, verify=False).content.decode()

results = BeautifulSoup(html, 'lxml')

name = results.select('meta')[2].get('content')

score = results.select('span#priceblock_ourprice')[0].text

preferential = results.select('span#price-shipping-message')[0].text

color = results.select('span.selection')[0].text
# 承诺
promise = results.select('span.a-list-item')[18:]

# 技术指标
skill = results.select('th.a-color-secondary ')
# 技术细节
detail = results.select('td.a-size-base')
# 购买提示
cue = results.select('span.a-color-secondary')
# 配送信息
msg = results.select('div.a-spacing-base')
preferential = re.sub('\s', '', preferential)
color = re.sub('\s', '', color)
for item2 in msg[3:10]:
    item2 = re.sub('\s', '', item2.text)
print(f"配送信息：{item2}")
print(f"商品名称：{name}")
print(f"评分：{score}")
print(f"产品优惠：{preferential}")
print(f"颜色：{color}")
for item in promise:
    item = re.sub('\s', '', item.text)
    print(f"承诺:{item}")
for item3 in skill:
    print(f"技术指标：{item3.text}")
for item4 in detail:
    print(f"技术细节：{item4.text}")
for item5 in cue:
    print(f"购买提示：{item5.text}")
