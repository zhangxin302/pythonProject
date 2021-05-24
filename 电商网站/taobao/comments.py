"""
author:张鑫
date:2021/5/8 11:53
 https://aldcdn.tmall.com/recommend.htm?appId=03067&itemId=615711429594&vid=0&curPage=1&step=100&categoryId=50006584&sellerId=3193724813&shopId=182455847&brandId=107380&refer=&callback=jsonpAldTabWaterfall
 https://rate.tmall.com/list_detail_rate.htm?itemId=615711429594&spuId=1607629875&sellerId=3193724813&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvQ9vPvB%2BvjQCkvvvvvjiWPFzU1jnbR2SOtjD2PmPOgjnHR2MhQji8n2SvzjggvpvhvvvvvUvCvv147sSzhr147DiF%2Fn%2F%2BvpvEvvB4vDDXvCAI39hvCvvhvvmevpvhvvmv9d9Cvm9vvvvvphvvvvvvvcHvpvFbvvv2vhCv2UhvvvWvphvWgvvvvQCvpvs9uvhvmvvv9bQgH86zkvhvC99vvOCtop9CvhQUuTIvC0ugQfzCHEB%2Bm7zUaNoQdox%2Fgjxl%2Bb8rJmc6khzBRBH%2BCNoxfJmK5zHmsnF9TE9XwHsXS47BhC3qVUcnDOmOejIUDajxALwpvvhvC9vhvvCvpvgCvvpvvvvvRvhvCvvvvvm%2BvpvEvv38v9phvC9idvhvhovUm9UjCQvOzkeSI2BvAxZ1dvhvHmQhQUVa5pvwJkeSULELKXhH6LIt&needFold=0&_ksTS=1621218850440_507&callback=jsonp508
"""
import json
import random
import schedule
import requests
import time
import re
import pymongo

# def connect_mongo():


databasse = pymongo.MongoClient('localhost', port=27017)
db = databasse['taobao']
comments_list = db['comments_list']

headers = {
    'authority': 'rate.tmall.com',
    'method': 'GET',
    'path': '/list_detail_rate.htm?itemId=615711429594&spuId=1607629875&sellerId=3193724813&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098#E1hvUQvWvPOvjQCkvvvvvjiWPFzU1jEHn2FhzjEUPmPWljYER2dW1j3CPszOtj0+vpvEvUmweEQvvUV2dvhvhpovFUMPvvmvbAZNcrjBR4Ie39hvCvmvphmevpvhvvCCB29CvvpvvhCv29hvCvvvvvvUvpCWvJ4h3CzUd3wgKFnfIWoZHd8rwk/gQfutnCBQ7fmxdBeKHsCHs4hZVEp7EcqWaXTAdByaWXxrV4TJRAYVyOvOHd8rwos6D40Xd3ODNu9Cvv9vvhhggJF4/O9CvvOCvhE2tWmgvpvIvvCvpvvvvvvvvh89vvvCJpvvByOvvUhQvvCVB9vv9BQvvhXVvvmCjvvCvvOv9hCvvvm+vpvZ3O2t/5+vvvU2EBYaAOZzWuvTnhO=&needFold=0&_ksTS=1621219785851_495&callback=jsonp496',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'cna=NqUCGfAF6AUCAS/xSOAkAhz/; lid=琵琶湖畔琵琶语; enc=ND37NPC1FMD+1wRhL4PZYeDn1E1HhKx+8sVBzLtyntcqkSabh9+p9Pbm2WuXSYEQLhd79BtvOc0BQb5JxDK2Yg==; hng=CN|zh-CN|CNY|156; _m_h5_tk=eec545745d538e3e090e7b8a859218be_1620985787238; _m_h5_tk_enc=28e8543b5ef32a24ff9efffc1b3b262f; t=2ca4aff55d54517434823682c5bee2ee; tracknick=\u7435\u7436\u6E56\u7554\u7435\u7436\u8BED; lgc=\u7435\u7436\u6E56\u7554\u7435\u7436\u8BED; _tb_token_=540ff6e56b7e; cookie2=1dee15782652bd6fc8389f03d4c45e03; xlly_s=1; x5sec=7b22726174656d616e616765723b32223a2265656135303161633666313634353765623236306536663561323632346235314349697268345547454c333736655439767279626f67456f416a447475662f632f762f2f2f2f3842227d; dnk=\u7435\u7436\u6E56\u7554\u7435\u7436\u8BED; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw==&cookie21=URm48syIYB3rzvI4Dim4&pas=0&existShop=false&cookie15=UIHiLt3xD8xYTw==&cookie14=Uoe2zEWovjySvw==; uc3=vt3=F8dCuwgmnjZew1fWQJI=&id2=UU6m3S9L75CWkA==&lg2=VT5L2FSpMGV7TQ==&nk2=pmoa7JSc4Giae7tjR6I=; _l_g_=Ug==; uc4=nk4=0@pKV37AeEU+e7xpYy2vwv4frv7CVUWmo5Kg==&id4=0@U2xrcMQ9NFFn/nOJDeff67YrLf87; unb=2672538657; cookie1=BxUALBFNkgard4saE/r4FkORlDLtEg6XVieLZGS1qs4=; login=true; cookie17=UU6m3S9L75CWkA==; _nk_=\u7435\u7436\u6E56\u7554\u7435\u7436\u8BED; sgcookie=E1008JM+dtDk3oR0gzkqKR2dcIYPMhFMza5jHg32SnFRvw6qsaMiQ24uJgXPRL6NWWkMOD7AVp1SYj4DRUGUmhblmQ==; sg=语7b; csg=22fcdfd2; isg=BHR0pKXCqAZTqDyXYyDr8VhVRTLmTZg3QKLBBA7VlP-DeRTDNlwQxgs_-bGhgdCP; tfstk=crLRBsXx5xDuBG1v_3nmRW1-s1KRZDPRK76LJb1O8xlifO4diXTMWhsiV65KEjC..; l=eBQ6KvfHjcT1P8zXBO5aPurza77T3IRb4sPzaNbMiInca6hl6FNbfNCCcPFJJdtjgt1FTetyq4hFHRLHR3A0mkfQ7_5LaCRKnxf..',
    'referer': 'https://detail.tmall.com/item.htm?id=615711429594&ali_refid=a3_431358_1007:121664695:J:182455847_0_100:1679f88edf46b6957be9604fa8c7fdc6&ali_trackid=85_1679f88edf46b6957be9604fa8c7fdc6&spm=a21bo.21814703.201876.17&scm=1007.34127.211940.0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'
}
data = {
    'itemId': '615711429594',
    'spuId': '1607629875',
    'sellerId': '3193724813',
    'order': '3',
    'currentPage': '1',
    'append': '0',
    'content': '1',
    'tagId': '',
    'posi': '',
    'picture': '',
    'groupId': '',
    'ua': '098#E1hvUQvWvPOvjQCkvvvvvjiWPFzU1jEHn2FhzjEUPmPWljYER2dW1j3CPszOtj0+vpvEvUmweEQvvUV2dvhvhpovFUMPvvmvbAZNcrjBR4Ie39hvCvmvphmevpvhvvCCB29CvvpvvhCv29hvCvvvvvvUvpCWvJ4h3CzUd3wgKFnfIWoZHd8rwk/gQfutnCBQ7fmxdBeKHsCHs4hZVEp7EcqWaXTAdByaWXxrV4TJRAYVyOvOHd8rwos6D40Xd3ODNu9Cvv9vvhhggJF4/O9CvvOCvhE2tWmgvpvIvvCvpvvvvvvvvh89vvvCJpvvByOvvUhQvvCVB9vv9BQvvhXVvvmCjvvCvvOv9hCvvvm+vpvZ3O2t/5+vvvU2EBYaAOZzWuvTnhO=needFold: 0',
    '_ksTS': '1621219785851_495',
    'callback': 'jsonp496',
}

# url = f'https://rate.tmall.com/list_detail_rate.htm?itemId={data["itemId"]}&spuId={data["spuId"]}&sellerId={data["sellerId"]}&order={data["order"]}&currentPage={data["currentPage"]}&append={data["append"]}&content={data["content"]}&tagId={data["tagId"]}&posi={data["posi"]}&picture={data["picture"]}&groupId={data["groupId"]}&ua={data["ua"]}&needFold={data["needFold"]}&_ksTS={data["_ksTS"]}&callback={data["callback"]}'
url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=615711429594&spuId=1607629875&sellerId=3193724813&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvUQvWvPOvjQCkvvvvvjiWPFzU1jEHn2FhzjEUPmPWljYER2dW1j3CPszOtj0%2BvpvEvUmweEQvvUV2dvhvhpovFUMPvvmvbAZNcrjBR4Ie39hvCvmvphmevpvhvvCCB29CvvpvvhCv29hvCvvvvvvUvpCWvJ4h3CzUd3wgKFnfIWoZHd8rwk%2FgQfutnCBQ7fmxdBeKHsCHs4hZVEp7EcqWaXTAdByaWXxrV4TJRAYVyOvOHd8rwos6D40Xd3ODNu9Cvv9vvhhggJF4%2FO9CvvOCvhE2tWmgvpvIvvCvpvvvvvvvvh89vvvCJpvvByOvvUhQvvCVB9vv9BQvvhXVvvmCjvvCvvOv9hCvvvm%2BvpvZ3O2t%2F5%2BvvvU2EBYaAOZzWuvTnhO%3D&needFold=0&_ksTS=1621219785851_495&callback=jsonp496'
html = requests.get(url=url, headers=headers, verify=False).content.decode()

html = html.replace('jsonp496(', '').replace(')', '')

html = json.loads(html)
print(html)
for item in html['rateDetail']['rateList']:
    comments = {}
    # 买家昵称
    displayUserNick = item['displayUserNick']
    comments['displayUserNick'] = displayUserNick
    # 评论时间
    rateDate = item['rateDate']
    comments['rateDate'] = rateDate

    # 评论内容
    rateContent = item['rateContent']
    comments['rateContent'] = rateContent

    # 商家回复
    reply = item['reply']
    comments['reply'] = reply

    # 商品详情
    auctionSku = item['auctionSku']
    comments['auctionSku'] = auctionSku

    # 订单编号
    id = item['id']
    comments['id'] = id

    results = comments_list.count({'id': comments['id']})
    if results == 0:
        print('*********************************************')
        print(comments)
        comments_list.insert_one(comments)
        print('*********************************************')
        results += 1
    else:
        print('数据已存在')

