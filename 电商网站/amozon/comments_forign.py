"""
author:张鑫
date:2021/5/11 14:34
"""

import requests
import random
import time
from bs4 import BeautifulSoup
import pymongo
import schedule

database = pymongo.MongoClient('localhost', port=27017)
db = database['amazon']
comments_forign_list = db['comments_forign_list']
headers = {
    'cookie': 'session-id=135-1303361-3230510; sp-cdn="L5Z9:CN"; skin=noskin; ubid-main=134-2361675-3800957; x-main="ZJjKCYD4WlxNSIlDL7PlwNn9ZzU3o?Mh@mn4FfSd0XYXcX5pUdh1xyRpoT2Kq5xL"; at-main=Atza|IwEBIL3MCP8cpo_5WiawBV5k_oh2lLLQCN0-NcyVJL74IoqyWsx1rLf-gQ9hzTWbPMc_fc8WvsOkQF6dLizGR3IJ-6gxU2HiPiqDzjOxfYyy5auVvAneBXfM8g4fHJ9sVDQaigbSLN9nKm6ZcbBQr4kXTJXTeZ0n2HYAbVW3MsFvG_UkxSOq4RyYHQ8BQIbW9sJv-pyYpC41sJO-VQMAAGo7zKp4; sess-at-main="hiMfw7kh6eO2O6ma/IYV/UpKw0uI+ya6jbxltUJma30="; sst-main=Sst1|PQGqONyzq7vSboNiwCCUSJiGCXNPJ9Hea9X-_QQy9DFNJpvDHeK0Dme1jAJiSZ0rlugHofufhuP_b7Ra3spM6V37ij-EI7xr6EuDasBx1nb-WzMMCrY-LqdKF2lsFcEYyZvn_Z9gKdXim-4uDgdnElsIVqOpXmCO-5k8g05o7jZufk0Iw2kBmW7p8oH84CXeYgrCr0WpkbjHZqV39q85oTzU34K5iv2Gyyhkr94bydBpbHELYDEkM_S6rY3qFfx89piRR4ANLyY42AcCN1QvzUZI0oPrOTDuhO16oul48-6cqQg; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; session-token="2S7lCMitousGs2An7Yq3DDTSEKGFVZmU626xZd0OOIs6ECmc23W4k/cpMFlAs5Sh64gWUCAW6ySoZx1lYQ6DE5zxyMfmwsW9PSX0QCnKK6Qh2XMKzPsEAENn3cZu6KDiQlesFILY93trDm3BIaspIPuS4WeMaM2Frmum0cWl/wqKPdGv08Do9E1wqG9QayXaYNUN7joIXYKUFnMUtEWRag=="; csm-hit=tb:s-8FAW9692VC9Q0B96MTTF|1620714652514&t:1620714653026&adb:adblk_no',
    'referer': 'https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-Count/product-reviews/B00MNV8E0C/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
}


def amozon_coments_forign():
    for i in range(100):
        time.sleep(random.randint(1, 5))
        url = f'https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-Count/product-reviews/B00MNV8E0C/ref=cm_cr_arp_d_paging_btm_next_{i}?ie=UTF8&reviewerType=all_reviews&pageNumber={i}'

        html = requests.get(url=url, headers=headers, verify=False).content.decode()

        results = BeautifulSoup(html, 'lxml')

        results = results.select('div#cm_cr-review_list')

        for item in results:

            time.sleep(random.randint(1, 5))
            # 买家
            names = item.select('div.a-profile-content>span.a-profile-name')

            for name in names:
                comments_forign = {}
                # time.sleep(random.randint(1, 5))
                name = str(name.text).replace('.', '-')
                comments_forign['name'] = name
                # print(comments_forign)
                # print(f"买家：{name}")

                # 评分
            scores = item.select('span.a-icon-alt')
            for score in scores:
                # time.sleep(random.randint(1, 5))
                score = str(score.text).replace('.', '-')
                comments_forign['score'] = score
                # print(comments_forign)

            # print(f"评分：{score}")

            # 总评
            short_comments = item.select('a>span')
            for short_comment in short_comments:
                # time.sleep(random.randint(1, 5))
                short_comment = str(short_comment.text).replace('.', '-')
                comments_forign['short_comment'] = short_comment
            # print(f"总评：{short_comment}")

            # 评论时间和地点
            date_ways = item.select('span[class="a-size-base a-color-secondary review-date"]')
            for date_way in date_ways:
                # time.sleep(random.randint(1, 5))
                date_way = str(date_way.text).replace('.', '-')
                comments_forign['date_way'] = date_way
            # print(f"评论时间和地点：{date_way}")

            # 评论正文
            comments = item.select('span[class="a-size-base review-text review-text-content"]>span')
            for comment in comments:
                # time.sleep(random.randint(1, 5))
                comment = str(comment.text).replace('<br>', '').replace('.', '-').replace('\n', '')
                comments_forign['comment'] = comment
            # print(f"评论正文：{comment}")

            # 多少人认为有用
            usefuls = item.select('span[class="a-size-base a-color-tertiary cr-vote-text"]')
            for useful in usefuls:
                # time.sleep(random.randint(1, 5))
                useful = str(useful.text).replace('.', '-')
                comments_forign['useful'] = useful
        count = comments_forign_list.count({'comment': comments_forign['comment']})
        if count == 0:
            print('**************************************')
            print(comments_forign)
            print('**************************************')
            comments_forign_list.insert_one(comments_forign)
            count += 1
        else:
            print('数据已存在')
            print(comments_forign['name'])


if __name__ == '__main__':
    while 1:
        schedule.every(5).seconds.do(amozon_coments_forign)
        schedule.run_pending()
        time.sleep(20)
