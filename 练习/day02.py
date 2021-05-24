import requests
from fake_useragent import UserAgent
import time
import random
import csv

import pymysql
import os

os.environ['http_proxy'] = 'http://127.0.0.1:1080'
os.environ['https_proxy'] = 'https://127.0.0.1:1080'
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='123456',
#                      database='press1',
#                      charset='utf8'
# )
from urllib3.util import timeout

db = pymysql.connect(host='localhost', user='root', password='zhangxin941021', database='press1', charset='utf8')
cursor = db.cursor()
ins = '''insert into pressreader values(%s,%s,%s,%s,%s)'''

# f = open('越南英文杂志','w',encoding='utf-8')
# csv_writer = csv.writer(f)
# csv_writer.writerow(['id','标题','发布时间','内容'])

# headers = {
# "cookie":"__cfduid=de26a59b28f814c9f43fc33baf25bb5911616989793; lng=zh; AProfile=L5lTOAdoBhBFoZgvTr8Ltn+3KZ5KAQAkCAAAAAAAAHiLpN0=; _ga=GA1.2.2081882240.1616989796; _gid=GA1.2.538258213.1616989796; _hjid=fcce81cd-2c65-4d06-a50e-697b18bf5b5b; _fbp=fb.1.1616989798838.1371493273; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.pressreader.com%2Fsearch%3Fquery%3DChina%2520poverty%26newspapers%3D9011%252C9hmc%252C9hmd%252C9hzl%252Cf672%26languages%3Den%26date%3DAnytimes%26hideSimilar%3D0%26type%3D2%26state%3D1; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0",
# "sec-ch-ua":'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
# "sec-ch-ua-mobile":"?0",
# "sec-fetch-dest":"document",
# "sec-fetch-mode":"navigate",
# "sec-fetch-site":"cross-site",
# "sec-fetch-user":"?1",
# "upgrade-insecure-requests":"1",
# "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
# }
headers = {

    "user-agent": UserAgent().random
}

# 第一次出要获取 多少页
# url = "https://www.pressreader.com/api/search/GetArticles?accessToken=danJVlA6ihusZe58NwOtponz7dXXCIWUgZPBJn4wVFERjjYLcy7ubIdbmaPtSlwEthcGm4arryZ8FGyAOZcEUQ!!&searchText=+%22China+poverty%22&searchAuthor=&range=Anytimes&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals="
url = "https://www.pressreader.com/api/search/GetArticles?accessToken=vvn8AQhonuhjI2qi9T5kODs4S_Y8lXqsJJ31uZQKfCoc1rcWmaE5CImTm0xgZZgoI-vtyFfUVhK61qqpgT3kVA!!&searchText=+%22China+poverty%22&searchAuthor=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals="
proxies = {'http': 'http://127.0.0.1:1080', 'https': 'http://127.0.0.1:1080'}
s = requests.Session()
s.trust_env = False
html = s.get(url=url, headers=headers, verify=False, proxies=proxies, timeout=(30, 60)).json()

count = html['TotalFoundArticles']
print("总杂志数：", count)
# 页数

if count % 20 != 0:
    page_sum = count // 20 + 1
else:
    page_sum = count // 20
k = 0
for page in range(page_sum):
    time.sleep(random.randint(9, 11))
    pages = page * 20
    id_url = "https://www.pressreader.com/api/search/GetArticles?accessToken=vvn8AQhonuhjI2qi9T5kODs4S_Y8lXqsJJ31uZQKfCoc1rcWmaE5CImTm0xgZZgoI-vtyFfUVhK61qqpgT3kVA!!&searchText=+%22China+poverty%22&searchAuthor=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals="
    ids_url = id_url.format(pages)
    print(ids_url)
    html = requests.get(url=ids_url, headers=headers).json()
    # print(html['Items'])
    lines = html['Items']
    list_id = []
    sum = 0
    for line in lines:
        try:
            regionid = line['RegionId']
            list_id.append(regionid)
            sum += 1
            # print(regionid)
        except Exception as e:
            print("id为空获取下一条")
            continue

    print(list_id)
    print("共", sum, "个id")
    try:
        print("获取内容")
        if len(list_id) == 20:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14], list_id[15], list_id[16], list_id[17],
                                 list_id[18], list_id[19])
        elif len(list_id) == 19:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14], list_id[15], list_id[16], list_id[17], list_id[18])

        elif len(list_id) == 18:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14], list_id[15], list_id[16], list_id[17])
        elif len(list_id) == 17:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14], list_id[15], list_id[16])
        elif len(list_id) == 16:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14], list_id[15])
        elif len(list_id) == 15:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13],
                                 list_id[14])
        elif len(list_id) == 14:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12],
                                 list_id[13])
        elif len(list_id) == 13:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11], list_id[12])
        elif len(list_id) == 12:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10], list_id[11])
        elif len(list_id) == 11:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9], list_id[10])
        elif len(list_id) == 10:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5],
                                 list_id[6],
                                 list_id[7], list_id[8], list_id[9])
        elif len(list_id) < 10:
            url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
            one_url = url.format(list_id[0], list_id[1], list_id[2], list_id[3], list_id[4], list_id[5])

        # url = "https://www.pressreader.com/api/articles/GetItems?accessToken=kpD5Rre5jMvw_rbP8dUym9XGstk0bHZApu5pGf3WZAxpRvcP4qW7zldhKCHPfNqlGLMuQlqwBOtvxyq0nLORtg!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A6329821_4%2CissueId%3A7035674_4%2CissueId%3A7508498_13&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
        # one_url = url.format(list_id[0],list_id[1],list_id[2],list_id[3],list_id[4],list_id[5],list_id[6],list_id[7],list_id[8],list_id[9],list_id[10],list_id[11],list_id[12],list_id[13],list_id[14])

        html = requests.get(url=one_url).json()
        print(html)
        # html = html.json.loads()
        lines = html['Articles']

        for line in lines:
            list_data = []
            # print(line)
            # 所需要的内容 标题 作者 发布时间 正文内容 样本数量
            id = line['Id']
            Title = line['Title']
            times = line['Issue']['Date']
            texts = line['Blocks']
            Countrycode = line['Countrycode']
            list_Text = []
            for text in texts:
                Text = text['Text']
                list_Text.append(Text)
            m = ' '.join(list_Text)
            # print(id,"===",Title,"===",times,"===",m)
            list_data.append(id)
            list_data.append(Title)
            list_data.append(times)
            list_data.append(m)
            list_data.append(Countrycode)
            print(list_data)
            cursor.execute(ins, list_data)
            # 3.提交到数据库执行
            db.commit()
            # csv_writer.writerow(list_data)
    except Exception as e:
        print("有误")
        continue
print("获取完毕")
cursor.close()
db.close()
# break
# except:
#     print("Connection refused by the server..")
#     print("Let me sleep for 5 seconds")
#     print("ZZzzzz...")
#     time.sleep(5)
#     print("Was a nice sleep, now let me continue...")
#     continue

# if len(list_id) <= 17:
#     one_url = "https://www.pressreader.com/api/articles/GetItems?accessToken=vvn8AQhonuhjI2qi9T5kODs4S_Y8lXqsJJ31uZQKfCoc1rcWmaE5CImTm0xgZZgoI-vtyFfUVhK61qqpgT3kVA!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A7532200_4%2CissueId%3A6329821_4%2CissueId%3A7035674_4&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
#     one_url = url.format(list_id[0],list_id[1],list_id[2],list_id[3],list_id[4],list_id[5],list_id[6],list_id[7],list_id[8],list_id[9],list_id[10],list_id[11],list_id[12],list_id[13],list_id[14],list_id[15])
#     html = requests.get(url=one_url).json()
#     print(html)
#     html = html.json.loads()
#     lines = html['Articles']
#     for line in lines:
#         # print(line)
#         # 所需要的内容 标题 作者 发布时间 正文内容 样本数量
#         id = line['Id']
#         Title = line['Title']
#         times = line['Issue']['Date']
#         texts = line['Blocks']
#         list_Text = []
#         for text in texts:
#             Text = text['Text']
#             list_Text.append(Text)
#         print(id,"===",Title,"===",times,"===",list_Text)
#     times.sleep(random.randint(1, 3))
# else:
#     one_url = "https://www.pressreader.com/api/articles/GetItems?accessToken=vvn8AQhonuhjI2qi9T5kODs4S_Y8lXqsJJ31uZQKfCoc1rcWmaE5CImTm0xgZZgoI-vtyFfUVhK61qqpgT3kVA!!&articles={}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}%2C{}&pages=issueId%3A7532200_4%2CissueId%3A6329821_4%2CissueId%3A7035674_4&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search"
#     one_url = url.format(list_id[0],list_id[1],list_id[2],list_id[3],list_id[4],list_id[5],list_id[6],list_id[7],list_id[8],list_id[9],list_id[10],list_id[11],list_id[12],list_id[13],list_id[14],list_id[15],list_id[16],list_id[17])
#     html = requests.get(url=one_url).json()
#     # print(html)
#     # html = html.json.loads()
#     lines = html['Articles']
#     for line in lines:
#         # print(line)
#         # 所需要的内容 标题 作者 发布时间 正文内容 样本数量
#         id = line['Id']
#         Title = line['Title']
#         times = line['Issue']['Date']
#         texts = line['Blocks']
#         list_Text = []
#         for text in texts:
#             Text = text['Text']
#             list_Text.append(Text)
#         print(id,"===",Title,"===",times,"===",list_Text)
#         times.sleep(random.randint(1, 3))
