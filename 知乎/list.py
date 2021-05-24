import re
import time
import random
import requests
import pymongo
import schedule


# 封装成函数，方便调用
def host():
    # 连接数据库
    database = pymongo.MongoClient('localhost', port=27017)
    db = database['zhihu']
    content_list = db['content_list']
    # 请求头信息，防反扒
    headers = {
        'cookie': '_zap=29de0aed-13ed-4a77-8f0b-3b38230ffe85; d_c0="AKDbtpmrzRKPTpQLPgT_t5lKEDDDyRQQ2eM=|1615819946"; _xsrf=f933bfc6-7982-484b-80c7-6250088c35a0; captcha_session_v2="2|1:0|10:1621319796|18:captcha_session_v2|88:a2s1MGdsdEFBYjRYbHFGV0hjVUtuVVlHaWhDM2pQamZBK0FSM1pHQVErdXVYOENVcFpBY2F6N1VpRkdKNnU4TQ==|d22c57f45419ff9b70449ac4b52cdb71f3211b09117205594658ce9cc5b58986"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1619488507,1619488653,1619510797,1621319797; __snaker__id=BkxJn8b7ZDHWWOs4; gdxidpyhxdE=wTQWjh3dfzfr3onGI2zDZ9ZMhsKOBY\otXuZDKl2Qi9zG4igyYsBfyQJ85sulfZ0ucmJlHci3/mHRBgBio7pQlZohBxsZXIPwYqcC/4j2HwmItUBYPutDs4rpx0JUYqHsBVtPYbT5R\TLI7dW/nIbPOfC8jql4e6TaJJt4\qNhmrm0v7:1621320697887; _9755xjdesxxd_=32; YD00517437729195:WM_NI=3/1Qp6TxGOSDr9f24eCF6kTF23Fp0u291kgjtVj4W+ZqHZ824Cod6IncSIOyANC/X2+2TqO4lMW4U0nwJQZe68Cr1XI7YfsV9QTN8vh14c5nmqyaDs+NjsVNkIWpFj3hQ00=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d242928c9797b767aeb48eb7d55e978a8a85b53baff5bcb5b460a9ecaca4f32af0fea7c3b92af1f1ffb2f33e98a889b0d250b2e7aad3b76f819afa8cd74ef2ed8a91b37ff2e7ff8ce662b88aa6d5d6219aaf88bbbb3af89da185b543aebd9daace7383928dd0db3ae9ee9c92ce40b09399d5d83caea986b2d96ff6e88d93b4548be99787f25efb8f9cafbb7eaceffc84b866afafb782c779e992a694d546a9979991c562f1b89fd1b337e2a3; YD00517437729195:WM_TID=A7rd00Rm8RBEUQAEEFY/gj69DkH1pcTo; captcha_ticket_v2="2|1:0|10:1621319808|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfUUJTWjBYTERTcXhoRWN5NURSNGtHV0FMcjFSZTFQWVdIVkQ1YVNvbm1tZWZ2ODQwVkM5QlZJNzhKYS02T2tHbEkxTTY4R0hYRldXYjlLTjBObWh0QS5ybi5nT1h6anRJeXNPYk4ybkw2NWJ6dy44N3RWSVZPa1lWRUd2YkZtQTI3VmlKRGNJOElPSVZVVloxeWRHak1oRGxKaFFlZUE2NGRidEZlTnhkVEV0VEYwMDdST0RSdjVVajZLN3htU2JxNHNxLlhLXzhocjkuUnlMWWp3OHYyNWdhLnhBa3d5MVY0U0IyS1JuRTZaOXlrMmJvQ3FiNW0wT3dqUGZLSV9aMElWOW9RRVVuOVZ2VkYuOUVxMGFudktxbkRjTlRsMXk5Q3lhRVAxWC5rdVdyOFUtSVZndFkyeThvQ1RqT25OUUg4WGxuT3FzdDRrVjRWUXZHRzU3RndvZHFZeGtFVXdWLWxLN1Fza0dQOUFsSVlKdjAwb2UxSTI2bkYyZEZKYlVHcWtaR0p4a2suWTAuX1hQN0phX3BHOGVoQkhrVlFDZWhtZW1ZN2xHbTR4VEV4d2dyZkY0OG1uUWZxaS5GdVE5NlFxdG5fSXN0SUp0N05ZV3hQcGc5TXZYWkhEMVRRdGFlOUlOQUcwNndIclIuZHRaNFBlZzByTFJINWZaMyJ9|7a173a7a0ee6df7269779e9e4ead8327bf816ec7ea2a23a3dfd128b02b40018b"; z_c0="2|1:0|10:1621319832|4:z_c0|92:Mi4xNE9YV0tnQUFBQUFBb051Mm1hdk5FaVlBQUFCZ0FsVk5tSzZRWVFDMVdHQllqbUp2cjZqclgzbjBEQ0R2eUVpLVJn|c996162d2ecb005f1d9dbdab5152d544df2753012f352663262dcd6685eee9ee"; tst=r; SESSIONID=aUyMAl77sMButO0akqzxWSqt31A9R794AsdxcyhjcYb; JOID=VF0VC01frKvwEuebcFF_9DqPQlVkPfzas1OIqU8s4uyNaKioFOXLDp4R4ZZ2AUz5qjfveLFGiUZePNFXRzjv_6s=; osd=WlgXC0pRqanwFemeclF4-j-NQlJqOP7atF2Nq08r7OmPaK-mEefLCZAU45ZxD0n7qjDhfbNGjkhbPtFQST3t_6w=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1621322481; KLBRSID=fe78dd346df712f9c4f126150949b853|1621322494|1621319795',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4484.7 Safari/537.36'
    }
    # 请求网页
    for i in range(100):
        url = f'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=92c468eadb1055479435f4b6d42d86fa&desktop=true&page_number={i}&limit=6&action=down&after_id={6 * i + 5}&ad_interval=-1'

        html = requests.get(url=url, headers=headers).json()
        # try-except：手动抛出错误
        try:
            # 解析网页
            for item in html['data']:
                contents = {}
                time.sleep(random.randint(3, 5))
                # id
                id = item['id']
                contents['id'] = id
                # 作者
                author = item['target']['question']['author']['name']
                contents['作者'] = author

                # 题目
                title = item['target']['question']['title']
                contents['题目'] = title
                # 创建时间
                created = item['target']['question']['created']
                contents['创建时间'] = created
                # 回复数
                answer_count = item['target']['question']['answer_count']
                contents['回复数'] = answer_count
                # 赞同数
                follower_count = item['target']['question']['follower_count']
                contents['赞同数'] = follower_count
                # 评论数
                comment_count = item['target']['question']['comment_count']
                contents['评论数'] = comment_count
                # 发表时间

                created_time = item['created_time']
                contents['发表时间'] = created_time

                # 更新时间
                time.sleep(random.randint(1, 3))
                updated_time = item['updated_time']
                contents['更新时间'] = updated_time

                # 内容
                time.sleep(random.randint(1, 3))
                content = item['target']['content']
                pre = re.compile('>(.*?)<')
                content = ''.join(pre.findall(content))
                contents['内容'] = content
                count = content_list.count_documents({'id': contents['id']})
                # 判断爬取的数据是否存在于数据库中
                if count == 0:
                    print('*******************************************')
                    time.sleep(random.randint(3, 5))
                    print(contents)
                    content_list.insert_one(contents)
                    print('*******************************************')
                else:
                    print('数据已存在')
        except Exception as e:
            print(e)
            print('师傅被妖怪抓走了！！！！！！')
            arrive_time = time.sleep(random.randint(3, 5))
            print(f'大师兄还有{arrive_time}秒到达战场！！！！！！！')
            continue


# 主函数，只在本脚本中调用
if __name__ == '__main__':
    while 1:
        # 2秒执行一次
        schedule.every(2).seconds.do(host)
        # 执行所有函数
        schedule.run_pending()
        # 休眠
        time.sleep(5)
