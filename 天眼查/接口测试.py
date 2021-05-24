import requests
import json
import math
import pandas as pd

headers = {
    'Authorization': "50a24654-3189-4430-a675-8db802ce822f",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

com_lst = open('com_lst.txt', 'r', encoding='utf-8').read().split('\n')


def bzxr():
    '''
    被执行人
    :return:
    '''
    data_lst = []
    for com in com_lst:
        url = f'https://open.api.tianyancha.com/services/v4/open/zhixinginfo.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        if json.loads(response.text)['reason'] == '无数据':
            continue
        else:
            count = json.loads(response.text)['result']['total']
            page_sum = math.ceil(count / 50)
            for p in range(1, page_sum + 1):
                url = f'https://open.api.tianyancha.com/services/v4/open/zhixinginfo.json?name={com}&pageNum={p}'
                response = requests.get(url, headers=headers, verify=False)
                items = json.loads(response.text)['result']['items']
                data_lst += items
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./联易融POC第二部分tyc被执行人数据_20200707.xlsx')


def lssxr():
    '''
    历史失信人
    :return:
    '''
    data_lst = []
    for com in com_lst:
        url = f'http://open.api.tianyancha.com/services/v4/open/past/dishonest.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        if json.loads(response.text)['reason'] == '无数据':
            continue
        else:
            count = json.loads(response.text)['result']['total']
            page_sum = math.ceil(count / 50)
            for p in range(1, page_sum + 1):
                url = f'http://open.api.tianyancha.com/services/v4/open/past/dishonest.json?name={com}&pageNum={p}'
                response = requests.get(url, headers=headers, verify=False)
                items = json.loads(response.text)['result']['items']
                data_lst += items
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./联易融POC第二部分tyc历史失信人tyc数据_20200707.xlsx')


def lsbzxr():
    '''
    历史被执行人
    :return:
    '''
    data_lst = []
    for com in com_lst:
        url = f'http://open.api.tianyancha.com/services/v4/open/past/zhixing.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        if json.loads(response.text)['reason'] == '无数据':
            continue
        else:
            count = json.loads(response.text)['result']['total']
            page_sum = math.ceil(count / 50)
            for p in range(1, page_sum + 1):
                url = f'http://open.api.tianyancha.com/services/v4/open/past/zhixing.json?name={com}&pageNum={p}'
                response = requests.get(url, headers=headers, verify=False)
                items = json.loads(response.text)['result']['items']
                data_lst += items
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./联易融POC第二部分tyc历史被执行人数据_20200707.xlsx')


def sxr():
    '''
    失信人
    :return:
    '''
    data_lst = []
    for com in com_lst:
        url = f'https://open.api.tianyancha.com/services/v4/open/dishonest.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        if json.loads(response.text)['reason'] == '无数据':
            continue
        else:
            count = json.loads(response.text)['result']['total']
            page_sum = math.ceil(count / 50)
            for p in range(1, page_sum + 1):
                url = f'https://open.api.tianyancha.com/services/v4/open/dishonest.json?name={com}&pageNum={p}'
                response = requests.get(url, headers=headers, verify=False)
                items = json.loads(response.text)['result']['items']
                data_lst += items
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./联易融POC第二部分tyc失信人数据_20200707.xlsx')


def xzcf():
    '''
    行政处罚
    :return:
    '''
    data_lst = []
    for com in com_lst:
        print(com)
        url = f'http://open.api.tianyancha.com/services/v4/open/punishmentInfo.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        print(response.text)
        input()
        if json.loads(response.text)['reason'] == '无数据':
            data = {}
            data['是否查询到'] = '否'
        else:
            name = json.loads(response.text)['result']['name']
            data = {}
            data['现用名'] = name
            data['是否查询到'] = '是'
            if com == name:
                data['是否为现用名'] = '是'
            else:
                data['是否为现用名'] = '否'
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./快手被分析对象行政处罚信息公司检索数据_天眼查_20200708.xlsx')


def gsxx():
    '''
    工商信息
    :return:
    '''
    data_lst = []
    for com in com_lst:
        print(com)
        url = f'http://open.api.tianyancha.com/services/v4/open/baseinfoV3.json?name={com}&pageNum=1'
        response = requests.get(url, headers=headers, verify=False)
        if json.loads(response.text)['reason'] == '无数据':
            data = {}
            data['检索公司'] = com
            data['是否查询到'] = '否'
        else:
            name = json.loads(response.text)['result']['name']
            data = {}
            data['检索公司'] = com
            data['现用名'] = name
            data['是否查询到'] = '是'
            if com == name:
                data['是否为现用名'] = '是'
            else:
                data['是否为现用名'] = '否'
        print(data)
        data_lst.append(data)
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./公司检索数据_天眼查_20200730.xlsx')


def ggxx():
    '''
    工商信息
    :return:
    '''
    data_lst = []
    for com in com_lst[:1]:
        com = '北京百度网讯科技有限公司'
        print(com)
        url = f'https://open.api.tianyancha.com/services/v4/open/changeinfo.json?name={com}'
        response = requests.get(url, headers=headers, verify=False)
        print(response.text)
        input()
        if json.loads(response.text)['reason'] == '无数据':
            data = {}
            data['检索公司'] = com
            data['是否查询到'] = '否'
        else:
            name = json.loads(response.text)['result']['name']
            data = {}
            data['检索公司'] = com
            data['现用名'] = name
            data['是否查询到'] = '是'
            if com == name:
                data['是否为现用名'] = '是'
            else:
                data['是否为现用名'] = '否'
        print(data)
        data_lst.append(data)
    ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
    ds.to_excel('./公司检索数据_天眼查_20200730.xlsx')


def zzq():
    '''
    著作权
    :return:
    '''
    data_lst = []
    for com in com_lst:
        print(com)
        for p in range(1, math.ceil(307 / 20) + 1):
            url = f'http://open.api.tianyancha.com/services/v4/open/copyReg?name={com}&pageNum={p}'
            response = requests.get(url, headers=headers, verify=False)
            items = json.loads(response.text)['result']['items']
            for item in items:
                data = {}
                data['regnum'] = item.get('regnum')
                print(data)
                data_lst.append(data)
            ds = pd.DataFrame(data_lst, index=range(1, len(data_lst) + 1))
            ds.to_excel('./北京百度网讯科技有限公司著作权_天眼查_20200923.xlsx')


zzq()
