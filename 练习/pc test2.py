from os import mkdir
import requests
import re
import xlwt
from bs4 import BeautifulSoup


# 爬虫主函数
def reptile(i, page):
    sum = 0
    # 进入网页
    for a in range(page):
        sum += 1
        i += 1
        html = joinHtml(i)

        # 爬取数据
        listUrl = reptileDate(html)

        # 保存数据
        saveDate(listUrl, sum)


# 获取html
def joinHtml(i):
    url = 'https://www.2dcf2c4e713a979f.com/tupian/'
    url = url + str(i) + '.html'  # 拼接url
    headers = {
        'authority': 'www.2dcf2c4e713a979f.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.2dcf2c4e713a979f.com/tupian/list-%E4%BA%9A%E6%B4%B2%E5%9B%BE%E7%89%87-7.html',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_ga=GA1.2.578238296.1620110856; _gid=GA1.2.1235106727.1620110856',
    }

    response = requests.get(url, headers=headers)  # 进入网站
    html = response.content.decode()  # 解码
    # print(html) #测试
    return html


# 爬取数据
def reptileDate(html):
    listUrl = []  # 存放图片地址
    soup = BeautifulSoup(html, 'html.parser')  # 对网页进行解析
    for item in soup.find_all('img'):  # 分别获取img标签内容
        # print(item)#测试
        item = str(item)
        result = re.search(r'.*data-original="(.*)" src=.*', item)
        result = result.group(1)
        listUrl.append(result)
        # print(result)#测试
    return listUrl


# 保存
def saveDate(listUrl, sum):
    url = 'D:\hkd\\'
    url = url + str(sum) + '.xlsx'  # 得到url
    xlsx = xlwt.Workbook()  # 创建excel表格
    sht1 = xlsx.add_sheet('Sheet1')
    sum = 0
    for i in listUrl:  # 写入url
        sht1.write(sum, 0, i)
        sum += 1
    xlsx.save(url)


if __name__ == '__main__':
    try:
        mkdir('D:\\hkd')
        reptile(106170, 100)
    except:
        reptile(106170, 100)
