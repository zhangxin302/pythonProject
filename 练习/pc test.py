from bs4 import BeautifulSoup
import os
import urllib.request, urllib.error
import xlwt
import sqlite3


def reptile_silisili(url, savepath):
    # url:需要爬取的网页
    # 爬取网页
    datelist=getDate(url,)

    # 分析数据
    # 保存数据
    saveDate(savepath=savepath)


# 爬取网页
def getDate(url,baseurl):
    for i in range(5):   #循环获取每一页的html
        url=url+str(i)
        html=askUrl(url)
    #正则解析数据
        soup=BeautifulSoup(html,'html.parser') #对网页进行解析
        for item in soup.find(r'a',herf='/anime/2555.html'):
            print(item)









    getlist = []

    return getlist


def askUrl(url):
    #定义头部信息
    head = {
        'User-Agent': ' Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'}
    resquest = urllib.request.Request(url, headers=head)
    html=''
    try:
        #获取并解码html
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')

    except urllib.error.URLError as x:
        if hasattr(x,'code'):
            print(x.code)
        if hasattr(x,'reason'):
            print(x.reason)
    return html





# 保存路径
def saveDate(savepath):
    savepath = 'd:/ani/animation.xls'


if __name__ == '__main__':
    url = 'http://www.silisili.in/anime/202101/'
    getDate(url,1)

