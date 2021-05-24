"""
author:张鑫
date:2021/5/11 9:38
https://www.amazon.com/s?k=amazonbasics&pd_rd_r=020174fd-7223-496b-93a8-90fb85c2bf60&pd_rd_w=qAPd3&pd_rd_wg=N0Ao5&pf_rd_p=fef24073-2963-4c6b-91ab-bf7eab1c4cac&pf_rd_r=PEZ8M3FS4VWQPWWWSKC1&ref=pd_gw_unk
"""
import re

import requests
import time
import random
import pymongo
from bs4 import BeautifulSoup
from numpy.ma import count

database = pymongo.MongoClient('localhost', port=27017)
db = database['amozon']
goods_forign = db['goods_forign']
headers = {
    'Referer': 'Referer: https://www.amazon.com/?ref_=nav_custrec_signin&claim_type=EmailAddress&new_account=1&',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56",
    'Cookie': 'session-id=135-1303361-3230510; sp-cdn="L5Z9:CN"; skin=noskin; ubid-main=134-2361675-3800957; session-token="wmj4t/uItWwai/pQqRYAr+vIU739pDeK6xldXY4pEwrTKY6SfueC8bzErUFmamaCTW5T7SSFIIOxoB7GZf1NHLY+hZ/y7HFWgVhiSMMeqjkAZW7oylBNbTyBq3SPfLIVxhD2EeM1sf/Jp3Kw6x3zl+k395ZXOazAJikxyk7Y70VVzzsFaJwdxgAlT78ZQhfZqzW4h2CTP5cwurFV5nQUpGwLvSKNdWf1KxNUJOjI9aQ="; x-main="ZJjKCYD4WlxNSIlDL7PlwNn9ZzU3o?Mh@mn4FfSd0XYXcX5pUdh1xyRpoT2Kq5xL"; at-main=Atza|IwEBIL3MCP8cpo_5WiawBV5k_oh2lLLQCN0-NcyVJL74IoqyWsx1rLf-gQ9hzTWbPMc_fc8WvsOkQF6dLizGR3IJ-6gxU2HiPiqDzjOxfYyy5auVvAneBXfM8g4fHJ9sVDQaigbSLN9nKm6ZcbBQr4kXTJXTeZ0n2HYAbVW3MsFvG_UkxSOq4RyYHQ8BQIbW9sJv-pyYpC41sJO-VQMAAGo7zKp4; sess-at-main="hiMfw7kh6eO2O6ma/IYV/UpKw0uI+ya6jbxltUJma30="; sst-main=Sst1|PQGqONyzq7vSboNiwCCUSJiGCXNPJ9Hea9X-_QQy9DFNJpvDHeK0Dme1jAJiSZ0rlugHofufhuP_b7Ra3spM6V37ij-EI7xr6EuDasBx1nb-WzMMCrY-LqdKF2lsFcEYyZvn_Z9gKdXim-4uDgdnElsIVqOpXmCO-5k8g05o7jZufk0Iw2kBmW7p8oH84CXeYgrCr0WpkbjHZqV39q85oTzU34K5iv2Gyyhkr94bydBpbHELYDEkM_S6rY3qFfx89piRR4ANLyY42AcCN1QvzUZI0oPrOTDuhO16oul48-6cqQg; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; csm-hit=tb:s-S3ZZ3AJ9GJZYXPTAQ6MV|1620696783388&t:1620696783779&adb:adblk_no',
}

url = 'https://www.amazon.com/s?k=amazonbasics&pd_rd_r=020174fd-7223-496b-93a8-90fb85c2bf60&pd_rd_w=qAPd3&pd_rd_wg=N0Ao5&pf_rd_p=fef24073-2963-4c6b-91ab-bf7eab1c4cac&pf_rd_r=PEZ8M3FS4VWQPWWWSKC1&ref=pd_gw_unk '

html = requests.get(url=url, headers=headers, verify=False).content.decode()

results = BeautifulSoup(html, 'lxml')

results = results.select('div.s-main-slot')

# print(results)
for item in results:
    time.sleep(random.randint(1, 5))
    goods = {}
    item1 = item.select('span.a-size-base-plus')
    for name in item1:
        time.sleep(random.randint(1, 5))

        print(f"商品名称：{name.text}")

    item2 = item.select('span.a-icon-alt')
    for score in item2:
        time.sleep(random.randint(1, 5))

        print(f"商品评分：{score.text}")

        # 评论数
    item3 = item.select('a.a-link-normal>span.a-size-base')
    for counts in item3:
        time.sleep(random.randint(1, 5))

        if '$' in counts.text:
            print('暂无评论')
        else:
            print(f"评论数：{counts.text}")

    # 价格
    price = item.select('div[class="a-section a-spacing-medium"]')
    for item in price:
        time.sleep(random.randint(1, 5))
        if "$" not in item.text:
            print('商品价格：暂无定价')
        else:
            # item4 = item.select('span.a-price>span.a-offscreen')
            item4 = item.select('div.a-row a-size-base a-color-base')
            # print(item4)
            for price in item4:
                price = str(price.text)
                print(price)

                if count(price) == 2:
                    price = price[0]
            print(f"商品价格：{price}")
print(f"商品名称：{name.text}\n商品评分：{score.text}\n评论数：{counts.text}\n商品价格：{price.text}\n")
print(price)
print(type(str(price)))
price = price.text
price.replace('$', '')
price = price.values
goods[price].replace()
goods_forign.insert(goods)
print(goods)
