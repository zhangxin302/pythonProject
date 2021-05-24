"""
author:张鑫
date:2021/5/10 14:21

https://www.amazon.cn/s?i=communications&rh=n%3A665002051&fs=true&page=2&qid=1620627585&ref=sr_pg_1
https://www.amazon.cn/s?i=communications&rh=n%3A665002051&fs=true&page=3&qid=1620628390&ref=sr_pg_3
https://www.amazon.cn/s?i=communications&rh=n%3A665002051&fs=true&page=4&qid=1620628411&ref=sr_pg_4
https://www.amazon.cn/s?i=communications&rh=n%3A665002051&fs=true&page=5&qid=1620628436&ref=sr_pg_4
"""
from bs4 import BeautifulSoup
import time
import requests
import random
import re

headers = {
    'cookie': 'session-id=462-7691734-6727513; ubid-acbcn=462-4201526-6080054; x-acbcn="VSICvdadQqFqlWWVLUw9Q@6I7tLhe@J@3QrqUJ3pk6y4zKhDrCRS4kCMOuzcGRNH"; at-main=Atza|IwEBIIZc3nxq5u0KVgU-EbppX01u69yhhWNUxAP7nWmnrgzpE9VbdxaE1Tk9iEPgNbLScn7plmTodE8CG6Oo-5k6GlfE2nUZPvSknAd4hG8iS9LgwYrYUhHVgWKecSLdp7WcaWGsUjkbB9Iejt62rvDGu6KdR3kmO8cw6cO0x48l3_KavxUHHHW_Mq6eUhOe_Xd7E9XaEx1LRQo3_IjysUrNJ-jPayPDKUH6hgu2zH5vEiksUbPUdYJ8Sj8Mn9FtTqWKpo8; sess-at-main="vTFwOC7UV7xsXEOgkBiF5rLXPDZEQlA/wFgL/rbeCts="; sst-main=Sst1|PQGHfeQmHwV5jOqELnrxAf7WCVhBJ3MjbmiFFwEKaHHScIZ3xUnTodI3mnPZlDWqOzqx97mQQ0NF6vJDtzV6Jo5YRrm-fq6Uw0Oc3uw6tJyowV0H2PETcLvF-ifp4aOok2CcyxWq4dKMulkHOQwuSY5Qfp1fNHnx5FUMi2dpb2eWofWvhvNYzOhqDsdlDNNPdnmTEYRrwHC58m_tMzsLtP1R_TIdROwt0cz3_CCWwe88JgKCnOoHwOJyxt6I2Gp1QXPJDhn4w8J6q2Aym_zZNjmkVsEx4ceJrM4arcWQOrEPaz4; lc-acbcn=zh_CN; i18n-prefs=CNY; session-token="NC7E9+RQcUXQUMN8v9Wwrxo/Dcg1MIv1Jwi646KDGwCxdEZhWXF/Exm9FJFT9o390+ZXlnim4SBqakmkKqKDJGZwyi6SCumSXpc0SClmp3Sdbn4o070vme5eHcYHEuW2jzcxmPi1aESklMJN6XN5LMztTEddsNfyTuHKMWDe1MnU6TAYD7iE2Mg65QXlEq5Q0yB+dIjF38BBgnWh9gYFSQ=="; session-id-time=2082787201l; csm-hit=tb:s-XXYQAE46PB3GNBY4BSXX|1620975038831&t:1620975039432&adb:adblk_no',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
}

i = 'communications'
rh = '665002051'
fs = 'true'
page = 5
qid = 1620628436
ref = 'sr_pg_4'
url = f'https://www.amazon.cn/s?i={i}&rh=n%3A{rh}&fs={fs}&page={page}&qid={qid}&ref={ref}'

html = requests.get(url=url, headers=headers, verify=False).content.decode()

# 方法一
# results = BeautifulSoup(html, 'lxml')
#
# results = results.select('div.a-section')[5:156]
# for item in results:
#
#     time.sleep(random.randint(1,5))
#     # print(item)
#     names = item.select('img.s-image')
#     for name in names:
#         name = name.get('alt')
#         if len(name) == 0:
#             pass
#         else:
#             print(f"产品名称：{name}")
#     # # 评分
#     scores = item.select('span.a-icon-alt')
#     for score in scores:
#         if score is None:
#             print('暂无评分')
#         else:
#             print(f"评分：{score.text}")
#     # # 价格
#     price = item.select('span.a-offscreen')
#     if price is None:
#         print('暂无定价')
#     else:
#         for price in price:
#             print(f"价格：{price.text}")
#     #
#     # # 优惠
#     youhui = item.select('div.a-row>span')
#     if youhui == []:
#         pass
#     else:
#         for youhui in youhui:
#
#             print(f"优惠信息：{youhui.text}")
#     #
#     # # 是否是海外购
#     buy = item.select('img.s-image')
#     # print(buy)
#     if buy==[]:
#         pass
#     for a in buy:
#         b = a.get('alt')
#         if b =="":
#             print('海外购')
#         else:
#             pass

# 方法二
# 产品名
name = re.findall('srcset="" alt="(.*?)" data-image-index="97"', html)[0]
# 价格
price = re.findall('<span class="a-offscreen">(.*?)</span><span aria-hidden="true">', html)[0]
# 优惠
youhui = re.findall(
    '<div class="a-row a-size-base a-color-secondary s-align-children-center"><span>(.*?)</span></div><div class="a-row a-size-base a-color-secondary">',
    html)[0]

print(name)
print(price)
print(youhui)
