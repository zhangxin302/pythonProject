"""
author:张鑫
date:2021/5/12 14:30
"""
import json
import random
import time

import pymongo
import requests
# import pymongo

import schedule

from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random,
}


#
# hotel_list = [
#     {
#
#         'poiId': 75548,
#         'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvgPNZCEFEbMOWPgXOYEjdFKxbFmzsu2EVAbYGkE9+c6bH6EWcT9mwgMMhg2iTlnV5U7JyMoxP16wPhPAubMTDjyQCSm8GBiNSrBmMoIPS82mg8kub4PH/us9AoxkkQ0rxipGaYnMHt9+eoJm9FtuJgRETJdRz1xYOAQQovsST5YXQ==',
#     },
#     {
#
#         'poiId': 193123202,
#         'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvi5ijmy54xl/rRWS+a/2Tm/P5SWrOrXbGsX2iUv7eGoHFmW3F5MroqTmt0scBcgyz9UWELNzLKSGgBgw6cp3qt3XvGX+c2v9urYn8DwF5L5blhoHyMiM6lOy3F2AvaGBG/U+GxOYbSlBp0jLGyp40g+kYGoIxQT5K5uGrrtfHxTTw=='
#     },
#     {
#
#         'poiId': 41273222,
#         # 'X-FOR-WITH':''
#         'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvg7FQnnwBWei9LkGvzfvS/yo3GN6Zp9UIclMGy0wA3/RpoGmjojIee41QCP6+a9bT7EZa83iyqQE2egXaU8i1H6Uq3sGZDN9ZpbuUQYevscAbmweNGBpXgpxpxAOaCE0hqJHJTm/8pZyBE3nVblPGlpRvOyamNBe8GvS3MTgMwQjA=='
#     },
#     #     {
#     #         'poiId':,
#     #         'X-FOR-WITH':''
#     # },
#     {
#         'poiId': 877592431,
#         'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvhKm/a19UcToa6iTxYbyCeesRRlqWw+aMLIERhku9PCegh7szcuW9pbkZ2an2pEIYgWJtRuk9V3IX1x6z2ZGh4PFHLg28wMqxNQfVZt31bsxqv7vuoGV5fY9iglF1SmZsoKqGanVPieVq/jvQnDUtnIbHRXFcgpcZkWWGtnVSsOzg=='    },
# ]
# database = pymongo.MongoClient('localhost',port=27017)
# db = database['meituan']
# hotels = db['hotels']
# for i in hotel_list:
#
#     time.sleep(random.randint(1, 5))
#     hotels_list = {}
#     url = f'https://ihotel.meituan.com/group/v2/poi/detail/service?utm_medium=pc&version_name=999.9&poiId={i["poiId"]}&X-FOR-WITH={i["X-FOR-WITH"]}'
#
#     html = requests.get(url=url, headers=headers, verify=False).json()['data']
#
#     # 酒店服务
#     service = html['serviceIconsInfo']['serviceIcons']
#     for item1 in service:
#         attrDesc = item1['attrDesc']
#         hotels_list['attrDesc']=attrDesc
#         imgUrl = item1['imgUrl']
#         hotels_list['imgUrl'] = imgUrl
#         # print(f"酒店服务：{item1['attrDesc']},服务链接：{item1['imgUrl']}")
#     # 酒店介绍
#     introduce = html['hotelIntroInfo']
#     for item2 in introduce['poiExtendsInfos']:
#         attrDesc = item2['attrDesc']
#         attrValue = item2['attrValue']
#         hotels_list['attrDesc'] = attrDesc
#         hotels_list['attrValue'] = attrValue
#         # print(f"酒店介绍：{item2['attrDesc']},详情：{item2['attrValue']}")
#
#     for item3 in introduce['poiExtendsInfosDesc']:
#         hotels_list['item3']=item3
#
#         # print(f"酒店开业时间：{item3}")
#
#     # print(f"酒店内部介绍：{introduce['poiDesc']}")
#         poiDesc = introduce['poiDesc']
#         hotels_list['poiDesc'] = poiDesc
#
#     # 设施服务
#     Facilities = html['hotelFacilitiesRuleInfo']['hotelFacilitiesInfo']['serviceIconsInfo']['serviceIcons']
#
#     for item5 in Facilities:
#         attrDesc = item5['attrDesc']
#         hotels_list['attrDesc'] = attrDesc
#         imgUrl = item5['imgUrl']
#         hotels_list['imgUrl'] = imgUrl
#         # print(f"设施服务：{item5['attrDesc']},详情：{item5['imgUrl']}")
#     # 订房必读
#     read = html['hotelFacilitiesRuleInfo']['hotelRuleInfo']['checkInAndOutList']
#     for item6 in read:
#         attrRuleName = item6['attrRuleName']
#         hotels_list['attrRuleName'] = attrRuleName
#         attrValueDesc = item6['attrValueDesc']
#         hotels_list['attrValueDesc'] = attrValueDesc
#         # print(f"必读项：{item6['attrRuleName']},详情：{item6['attrValueDesc']}")
#
#     # 订房必读2
#     read2 = html['hotelFacilitiesRuleInfo']['roomBookingModelV2']['dataCellModels']
#     for item7 in read2:
#         title = item7['title']
#         hotels_list['title'] = title
#         contents = item7['contents']
#         hotels_list['contents'] = contents
#         # print(f"标题：{item7['title']},链接：{item7['icon']},内容:{item7['contents']}")
#
#     # 交通信息
#     traffic = html['trafficIntroInfo']
#     # 地铁
#     subway = traffic['subwayStations']
#     for item9 in subway:
#         print(f"地铁站：{item9['name']}")
#         print(f"距离信息：{item9['distanceDesc']}")
#         print(f"直线距离：{item9['distance']}")
#         print(f"经度：{item9['longitude']}")
#         print(f"维度：{item9['latitude']}")
#     # 火车
#     train = traffic['railwayStations']
#     for item10 in train:
#         print(f"火车站：{item10['name']}")
#         print(f"距离信息：{item10['distanceDesc']}")
#         print(f"直线距离：{item10['distance']}")
#         print(f"经度：{item10['longitude']}")
#         print(f"维度：{item10['latitude']}")
#         latitude = item10['latitude']
#         hotels_list['latitude'] = latitude
#     # 机场
#     train = traffic['airports']
#     for item11 in train:
#         print(f"机场：{item11['name']}")
#         print(f"距离信息：{item11['distanceDesc']}")
#         print(f"直线距离：{item11['distance']}")
#         print(f"经度：{item11['longitude']}")
#         print(f"维度：{item11['latitude']}")
#     # 位置
#     addr = traffic['addr']
#     print(f'位置：{addr}')
#     # 推荐理由
#     season = html['multiplePoiFeature']
#     print(f'酒店名字：{season["poiName"]}')
#     print(f'酒店类型：{season["hotelStar"]}')
#     print(f'类型介绍：{season["starExplain"]}')
#     poiName = season["poiName"]
#     hotels_list['poiName'] = poiName
#     starExplain = season["starExplain"]
#     hotels_list['starExplain'] = starExplain
#     hotels.insert(hotels_list)
#     print(hotels_list)

class Hotel:
    def __init__(self):
        self.hotels_list = {}
        self.hotel_list = [
            {

                'poiId': 75548,
                'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvgPNZCEFEbMOWPgXOYEjdFKxbFmzsu2EVAbYGkE9+c6bH6EWcT9mwgMMhg2iTlnV5U7JyMoxP16wPhPAubMTDjyQCSm8GBiNSrBmMoIPS82mg8kub4PH/us9AoxkkQ0rxipGaYnMHt9+eoJm9FtuJgRETJdRz1xYOAQQovsST5YXQ==',
            },
            {

                'poiId': 193123202,
                'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvi5ijmy54xl/rRWS+a/2Tm/P5SWrOrXbGsX2iUv7eGoHFmW3F5MroqTmt0scBcgyz9UWELNzLKSGgBgw6cp3qt3XvGX+c2v9urYn8DwF5L5blhoHyMiM6lOy3F2AvaGBG/U+GxOYbSlBp0jLGyp40g+kYGoIxQT5K5uGrrtfHxTTw=='
            },
            {

                'poiId': 41273222,
                # 'X-FOR-WITH':''
                'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvg7FQnnwBWei9LkGvzfvS/yo3GN6Zp9UIclMGy0wA3/RpoGmjojIee41QCP6+a9bT7EZa83iyqQE2egXaU8i1H6Uq3sGZDN9ZpbuUQYevscAbmweNGBpXgpxpxAOaCE0hqJHJTm/8pZyBE3nVblPGlpRvOyamNBe8GvS3MTgMwQjA=='
            },

            {
                'poiId': 877592431,
                'X-FOR-WITH': 'x/9q1QUUZKFfU41iyjPEDA9Q736VmZB1I2licJlwVvhKm/a19UcToa6iTxYbyCeesRRlqWw+aMLIERhku9PCegh7szcuW9pbkZ2an2pEIYgWJtRuk9V3IX1x6z2ZGh4PFHLg28wMqxNQfVZt31bsxqv7vuoGV5fY9iglF1SmZsoKqGanVPieVq/jvQnDUtnIbHRXFcgpcZkWWGtnVSsOzg=='},
        ]

    def connect_mongo(self):
        self.database = pymongo.MongoClient('localhost', port=27017)
        self.db = self.database['meituan']
        self.hotels = self.db['hotels']
        return self.hotels

    def get_html(self):
        hotel_list = self.hotel_list
        for i in hotel_list:
            time.sleep(random.randint(1, 5))
            url = f'https://ihotel.meituan.com/group/v2/poi/detail/service?utm_medium=pc&version_name=999.9&poiId={i["poiId"]}&X-FOR-WITH={i["X-FOR-WITH"]}'

            self.task(url)

    def task(self, url):
        html = requests.get(url=url, headers=headers, verify=False).json()['data']
        hotels_list = self.hotels_list
        hotels = self.connect_mongo()
        return self.analy_html(html, hotels_list, hotels)

        # print(self.analy_html(html, hotels_list))

    def analy_html(self, html, hotels_list, hotels):
        # 酒店服务
        service = html['serviceIconsInfo']['serviceIcons']
        for item1 in service:
            attrDesc = item1['attrDesc']
            self.hotels_list['attrDesc'] = attrDesc
            imgUrl = item1['imgUrl']
            self.hotels_list['imgUrl'] = imgUrl
            print(f"酒店服务：{item1['attrDesc']},服务链接：{item1['imgUrl']}")
        # 酒店介绍
        introduce = html['hotelIntroInfo']
        for item2 in introduce['poiExtendsInfos']:
            attrDesc = item2['attrDesc']
            attrValue = item2['attrValue']
            hotels_list['attrDesc'] = attrDesc
            hotels_list['attrValue'] = attrValue
            print(f"酒店介绍：{item2['attrDesc']},详情：{item2['attrValue']}")

        for item3 in introduce['poiExtendsInfosDesc']:
            hotels_list['item3'] = item3

            print(f"酒店开业时间：{item3}")

            # print(f"酒店内部介绍：{introduce['poiDesc']}")
            poiDesc = introduce['poiDesc']
            hotels_list['poiDesc'] = poiDesc

        # 设施服务
        Facilities = html['hotelFacilitiesRuleInfo']['hotelFacilitiesInfo']['serviceIconsInfo']['serviceIcons']

        for item5 in Facilities:
            attrDesc = item5['attrDesc']
            hotels_list['attrDesc'] = attrDesc
            imgUrl = item5['imgUrl']
            hotels_list['imgUrl'] = imgUrl
            print(f"设施服务：{item5['attrDesc']},详情：{item5['imgUrl']}")
        # 订房必读
        read = html['hotelFacilitiesRuleInfo']['hotelRuleInfo']['checkInAndOutList']
        for item6 in read:
            attrRuleName = item6['attrRuleName']
            hotels_list['attrRuleName'] = attrRuleName
            attrValueDesc = item6['attrValueDesc']
            hotels_list['attrValueDesc'] = attrValueDesc
            print(f"必读项：{item6['attrRuleName']},详情：{item6['attrValueDesc']}")

        # 订房必读2
        read2 = html['hotelFacilitiesRuleInfo']['roomBookingModelV2']['dataCellModels']
        for item7 in read2:
            title = item7['title']
            hotels_list['title'] = title
            contents = item7['contents']
            hotels_list['contents'] = contents
            print(f"标题：{item7['title']},链接：{item7['icon']},内容:{item7['contents']}")

        # 交通信息
        traffic = html['trafficIntroInfo']
        # 地铁
        subway = traffic['subwayStations']
        for item9 in subway:
            print(f"地铁站：{item9['name']}")
            print(f"距离信息：{item9['distanceDesc']}")
            print(f"直线距离：{item9['distance']}")
            print(f"经度：{item9['longitude']}")
            print(f"维度：{item9['latitude']}")
        # 火车
        train = traffic['railwayStations']
        for item10 in train:
            print(f"火车站：{item10['name']}")
            print(f"距离信息：{item10['distanceDesc']}")
            print(f"直线距离：{item10['distance']}")
            print(f"经度：{item10['longitude']}")
            print(f"维度：{item10['latitude']}")
            latitude = item10['latitude']
            hotels_list['latitude'] = latitude
        # 机场
        train = traffic['airports']
        for item11 in train:
            print(f"机场：{item11['name']}")
            print(f"距离信息：{item11['distanceDesc']}")
            print(f"直线距离：{item11['distance']}")
            print(f"经度：{item11['longitude']}")
            print(f"维度：{item11['latitude']}")
        # 位置
        addr = traffic['addr']
        print(f'位置：{addr}')
        # 推荐理由
        season = html['multiplePoiFeature']
        print(f'酒店名字：{season["poiName"]}')
        print(f'酒店类型：{season["hotelStar"]}')
        print(f'类型介绍：{season["starExplain"]}')
        poiName = season["poiName"]
        hotels_list['poiName'] = poiName
        starExplain = season["starExplain"]
        hotels_list['starExplain'] = starExplain
        poiName = season["poiName"]
        if hotels['poiName'] == poiName:
            hotels.insert(hotels_list)
            print(hotels_list)
        else:
            print('数据已存在')


if __name__ == '__main__':
    while 1:
        hotel = Hotel()
        hotel.get_html()
        schedule.every(5).seconds.do(hotel.task)
        schedule.run_pending()
        time.sleep(10)
