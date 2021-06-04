# coding=gbk


"""
sum
"""
from a_公司项目.京东评论数据.chi import get_ua
from a_公司项目.京东评论数据.chi import cooies
from a_公司项目.京东评论数据.chi import cooies1
import requests
import random
from lxml import etree
import time
import random
from fake_useragent import UserAgent
from openpyxl import Workbook
import csv
from fake_useragent import UserAgent

f = open('发酵国酒.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['品牌名', '价格', '商品名称', '商品编号', '店铺', '商品毛重', '商品产地', '酒精度', '包装规格', '容量', '口味', '加工工艺', '加工工艺'])

sum = 0

header = {
    'User-Agent': get_ua(),
    'Cookie': cooies()
}
header1 = {
    'User-Agent': UserAgent().random,
    # 'Cookie': cooies1()
}

# url = 'https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E'
# content = requests.get(url, headers=header).text
# # print(content)
# xpath_obj = etree.HTML(content)
# li_list = xpath_obj.xpath("//ul[@class='gl-warp clearfix']/li//div[@class='gl-i-wrap']/div[@class='p-img']/a/@href")
# # print(li_list)
# # //ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()
# prices = xpath_obj.xpath('//ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()')
# print(prices)
#
# url2 = 'https:{}'
# ye = 0
# for u in li_list:
#
#     url3 = url2.format(u)
#     sum += 1
#     print(url3, "*****第", sum, "条数据************")
#     time.sleep(random.randint(20, 25))
#     datas = requests.get(url3, headers=header1).text
#     data = etree.HTML(datas)
#     # 获取详情页数据
#     lists = data.xpath("//ul[@class='parameter2 p-parameter-list']/li")
#     print(len(lists))
#     k = 1
#     dict_data = {}
#     list_data = []
#     try:
#         name = data.xpath('//div[@class="sku-name"]/text()')[0].replace(' ', '')
#         print(name)
#     except Exception as e:
#         name = '同商品名称'
#     list_data.append(name)
#     list_data.append(prices[ye])
#     ye += 1
#     for lis in lists:
#
#         ziduan = lis.xpath("./text()")[0]
#         jian = ziduan.split('：')[0]
#         zhi = ziduan.split('：')[1]
#         dict_data[jian] = zhi
#         print(jian, zhi)
#         if k == 1:
#             if '商品名称' not in dict_data:
#                 dict_data['商品名称'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 2:
#             if '商品编号' not in dict_data:
#                 dict_data['商品编号'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 3:
#             if '店铺' not in dict_data:
#                 dict_data['店铺'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 4:
#             if '商品毛重' not in dict_data:
#                 dict_data['商品毛重'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 5:
#             if '商品产地' not in dict_data:
#                 dict_data['商品产地'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 6:
#             if '酒精度' not in dict_data:
#                 dict_data['酒精度'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 7:
#             if '包装规格' not in dict_data:
#                 dict_data['包装规格'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 8:
#             if '容量' not in dict_data:
#                 dict_data['容量'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 9:
#             if '口味' not in dict_data:
#                 dict_data['口味'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 10:
#             if '适用场景' not in dict_data:
#                 dict_data['适用场景'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         if k == 11:
#             if '加工工艺' not in dict_data:
#                 dict_data['加工工艺'] = '空'
#                 list_data.append('空')
#                 dict_data[jian] = zhi
#         list_data.append(zhi)
#         k += 1
#     print(list_data)
# # https://item.jd.com/10031229063891.html
# #       //item.jd.com/10027299539889.html
two_url = 'https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page={}&s={}&click=0'
# 跑到270，修改为（30,44）
for i in range(20, 30):
    page = i
    s = (i - 1) * 30 + 1
    # print(i,(i-1)*30+1)
    o_url = two_url.format(page, s)
    # print(o_url)
    time.sleep(random.randint(12, 15))
    content = requests.get(o_url, headers=header).text
    # print(content)
    xpath_obj = etree.HTML(content)
    li_list = xpath_obj.xpath("//ul[@class='gl-warp clearfix']/li//div[@class='gl-i-wrap']/div[@class='p-img']/a/@href")
    prices = xpath_obj.xpath('//ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()')

    # print(li_list)
    ye = 0
    o_url2 = 'https:{}'

    for u in li_list:

        o_url3 = o_url2.format(u)
        sum += 1
        print(o_url3, "*****第", sum, "条数据************")
        time.sleep(random.randint(15, 20))
        datas = requests.get(o_url3, headers=header1).text
        data = etree.HTML(datas)
        # 获取详情页数据
        lists = data.xpath("//ul[@class='parameter2 p-parameter-list']/li")

        k = 1
        dict_data = {}
        list_data = []
        try:
            name = data.xpath('//div[@class="sku-name"]/text()')[0].replace(' ', '')
            print(name)
        except Exception as e:
            name = '同商品名称'
        list_data.append(name)
        list_data.append(prices[ye])
        ye += 1
        for lis in lists:
            ziduan = lis.xpath("./text()")[0]
            # print(k, ziduan)
            jian = ziduan.split('：')[0]
            zhi = ziduan.split('：')[1]
            dict_data[jian] = zhi
            if k == 1:
                if '商品名称' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 2:
                if '商品编号' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 3:
                if '店铺' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 4:
                if '商品毛重' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 5:
                if '商品产地' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 6:
                if '酒精度' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 7:
                if '包装规格' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 8:
                if '容量' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 9:
                if '口味' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 10:
                if '适用场景' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            if k == 11:
                if '加工工艺' not in dict_data:
                    list_data.append('空')
                    dict_data[jian] = zhi
            list_data.append(zhi)
            k += 1
        print(list_data)

"""
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=1&s=1&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=3&s=61&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=5&s=117&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=7&s=180&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=9&s=241&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=11&s=300&click=0
https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page=45&s=1318&click=0
"""
