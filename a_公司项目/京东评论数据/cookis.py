# coding=gbk


"""
sum
"""
from a_��˾��Ŀ.������������.chi import get_ua
from a_��˾��Ŀ.������������.chi import cooies
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
from openpyxl import Workbook
import csv

f = open('���͹���.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['Ʒ����', '�۸�', '��Ʒ����', '��Ʒ���', '����', '��Ʒë��', '��Ʒ����', '�ƾ���', '��װ���', '����', '��ζ', '���ó���', '�ӹ�����'])

sum = 0

header = {
    'User-Agent': get_ua(),
    'Cookie': cooies()
}

url = 'https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E'
content = requests.get(url, headers=header).text
# print(content)
xpath_obj = etree.HTML(content)
li_list = xpath_obj.xpath("//ul[@class='gl-warp clearfix']/li//div[@class='gl-i-wrap']/div[@class='p-img']/a/@href")
# print(li_list)
# //ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()
prices = xpath_obj.xpath('//ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()')
print(prices)

url2 = 'https:{}'
ye = 0
for u in li_list:

    url3 = url2.format(u)
    sum += 1
    print(url3, "*****��", sum, "������************")
    time.sleep(random.randint(11, 15))
    datas = requests.get(url3, headers=header).text
    data = etree.HTML(datas)
    # ��ȡ����ҳ����
    lists = data.xpath("//ul[@class='parameter2 p-parameter-list']/li")
    print(len(lists))
    k = 1
    dict_data = {}
    list_data = []
    name = data.xpath('//div[@class="sku-name"]/text()')[0].replace(' ', '')
    list_data.append(name)
    list_data.append(prices[ye])
    ye += 1
    for lis in lists:

        ziduan = lis.xpath("./text()")[0]
        # print(k, ziduan)
        jian = ziduan.split('��')[0]
        zhi = ziduan.split('��')[1]
        dict_data[jian] = zhi

        if k == 1:
            if '��Ʒ����' not in dict_data:
                dict_data['��Ʒ����'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 2:
            if '��Ʒ���' not in dict_data:
                dict_data['��Ʒ���'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 3:
            if '����' not in dict_data:
                dict_data['����'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 4:
            if '��Ʒë��' not in dict_data:
                dict_data['��Ʒë��'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 5:
            if '��Ʒ����' not in dict_data:
                dict_data['��Ʒ����'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 6:
            if '�ƾ���' not in dict_data:
                dict_data['�ƾ���'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 7:
            if '��װ���' not in dict_data:
                dict_data['��װ���'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 8:
            if '����' not in dict_data:
                dict_data['����'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 9:
            if '��ζ' not in dict_data:
                dict_data['��ζ'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 10:
            if '���ó���' not in dict_data:
                dict_data['���ó���'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        if k == 11:
            if '�ӹ�����' not in dict_data:
                dict_data['�ӹ�����'] = '��'
                list_data.append('��')
                dict_data[jian] = zhi
        list_data.append(zhi)
        k += 1
    print(list_data)
    csv_writer.writerow(list_data)
# https://item.jd.com/10031229063891.html
#       //item.jd.com/10027299539889.html
two_url = 'https://search.jd.com/search?keyword=%E6%9E%9C%E9%85%92&suggest=1.rem.0.base&wq=%E6%9E%9C%E9%85%92&ev=2460_144161%5E2449_144155%5E&pvid=aac1d2338b644535b0e2a1aad4134b60&page={}&s={}&click=0'

for i in range(3, 44):
    page = i
    s = (i - 1) * 30 + 1
    # print(i,(i-1)*30+1)
    o_url = two_url.format(page, s)
    # print(o_url)
    time.sleep(random.randint(10, 12))
    content = requests.get(o_url, headers=header).text
    # print(content)
    xpath_obj = etree.HTML(content)
    li_list = xpath_obj.xpath("//ul[@class='gl-warp clearfix']/li//div[@class='gl-i-wrap']/div[@class='p-img']/a/@href")
    prices = xpath_obj.xpath('//ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]/strong/i/text()')

    # print(li_list)
    ye = 0
    o_url2 = 'https:{}'
    time.sleep(random.randint(11, 15))

    for u in li_list:
        try:
            o_url3 = o_url2.format(u)
            sum += 1
            print(o_url3, "*****��", sum, "������************")
            time.sleep(random.randint(11, 15))
            datas = requests.get(o_url3, headers=header).text
            data = etree.HTML(datas)
            # ��ȡ����ҳ����
            lists = data.xpath("//ul[@class='parameter2 p-parameter-list']/li")

            k = 1
            dict_data = {}
            list_data = []
            name = data.xpath('//div[@class="sku-name"]/text()')[0].replace(' ', '')
            list_data.append(name)
            list_data.append(prices[ye])
            ye += 1
            for lis in lists:
                ziduan = lis.xpath("./text()")[0]
                # print(k, ziduan)
                jian = ziduan.split('��')[0]
                zhi = ziduan.split('��')[1]
                dict_data[jian] = zhi
                if k == 1:
                    if '��Ʒ����' not in dict_data:
                        dict_data['��Ʒ����'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 2:
                    if '��Ʒ���' not in dict_data:
                        dict_data['��Ʒ���'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 3:
                    if '����' not in dict_data:
                        dict_data['����'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 4:
                    if '��Ʒë��' not in dict_data:
                        dict_data['��Ʒë��'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 5:
                    if '��Ʒ����' not in dict_data:
                        dict_data['��Ʒ����'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 6:
                    if '�ƾ���' not in dict_data:
                        dict_data['�ƾ���'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 7:
                    if '��װ���' not in dict_data:
                        dict_data['��װ���'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 8:
                    if '����' not in dict_data:
                        dict_data['����'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 9:
                    if '��ζ' not in dict_data:
                        dict_data['��ζ'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 10:
                    if '���ó���' not in dict_data:
                        dict_data['���ó���'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                if k == 11:
                    if '�ӹ�����' not in dict_data:
                        dict_data['�ӹ�����'] = '��'
                        list_data.append('��')
                        dict_data[jian] = zhi
                list_data.append(zhi)
                k += 1
            print(list_data)
            csv_writer.writerow(list_data)
        except Exception as e:
            print("����", e)
            continue