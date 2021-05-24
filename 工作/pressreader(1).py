"""
第一页
#越南
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers={}&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers={}&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
#柬埔寨
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=6203%2C9gr2%2C9ws1%2C9vnr%2C9hm7%2C9vyu%2C9vyv%2C9kw9&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals=
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=20&pageSize=20&totals=
# 文章页
https://www.pressreader.com/api/articles/GetItems?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&articles=281689732619992%2C281483574217857%2C281668257700644%2C281878711203332%2C281779926953224%2C281835761418633%2C281805696700151%2C281479279216826%2C281960314943381%2C281706912129156%2C281513637842267%2C281526522737886%2C281556588593995%2C281852941234907%2C282054804517796%2C281857236206447%2C281724088023206%2C281711207006417%2C281496454358096%2C281956020504987&pages=&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search
# 具体文章url
https://www.pressreader.com/api/articles/GetArticle?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&key=281689732619992&viewType=search
https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=281689732619992&pageSize=20&totals=
"""

import requests
from fake_useragent import UserAgent
import time
import random
import csv

f = open('南非英文杂志.csv', 'a', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['区域', '媒体名称', '发布时间', '标题', '文章', '国家'])

headers = {
    "user-agent": UserAgent().random,
    # "cookie": "__cfduid=dab90f2fac93475d2881ae946f33d8b0f1618477581; lng=zh; AProfile=+YFwOAe9XxbKL/ZFQL7MdnbpOFQGAQAkCAAAAAAAAJmKWt0=; _ga=GA1.2.2125254992.1618477623; _fbp=fb.1.1618477625040.773840126; _hjid=1ae40699-f888-4850-9fa5-3013add9c00b; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2021-04-26%2011%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pressreader.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2021-04-26%2011%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pressreader.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; _gid=GA1.2.2004167064.1619409336; _hjTLDTest=1; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F89.0.4389.90%20Safari%2F537.36; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.pressreader.com%2Fsearch%3Fquery%3DChina%2520poverty%26newspapers%3D1105%252C5796%252C7415%252C9393%252C9395%252C9396%252C9427%252C9429%252C9432%252C9433%252C9434%252C9hpz%252C9f77%252C9hsw%252C9vpg%252C9gve%252C9hrv%252C9k58%252C9gh9%252C9gss%252C9ic9%252C9gf5%252C9geu%252C9j71%252C9yhe%252C9yhg%252C9yhf%252C9xa2%252C9vri%252C9blq%252C9yhh%252Csalg%252C9yrm%252C9aaf%252C9vrl%252C9kag%252C9knw%252C9wud%252C9akw%252C9yhd%26languages%3Den%26in%3DALL%26date%3DAnytime%26hideSimilar%3D0%26type%3D2%26state%3D2"
}

# url = "https://www.pressreader.com/api/search/GetArticles?accessToken=Icm3hIpmPlJ6Le3Y2gyonJdsRj7fDVmRQXMy9KkRJQ06cxPXU--V6d9_sEnDXSvxEtPXMftzyoDQxfEcY-bdRg!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=9d46%2C9fak%2C9aa3%2C9vq1&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals="
# html = requests.get(url=url, headers=headers).json()
# count = 84

# if count % 20 != 0:
#     page_sum = count // 20 + 1
# else:
#     page_sum = count // 20
# print(count, page_sum)

k = 1165
# k = 247
for page in range(69, 150):
    time.sleep(random.randint(30, 35))
    pages = page * 20
    # 越南
    # id_url = "https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals="
    # 泰国
    # id_url = "https://www.pressreader.com/api/search/GetArticles?accessToken=Icm3hIpmPlJ6Le3Y2gyonJdsRj7fDVmRQXMy9KkRJQ06cxPXU--V6d9_sEnDXSvxEtPXMftzyoDQxfEcY-bdRg!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=9d46%2C9fak%2C9aa3%2C9vq1&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals="
    # 新加坡
    # id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=DSMcZSXSNXQ3o6KJSrV-FP1s80ZHX5YU3oLNFLj6RgGOJV0R-3NfatPMCPsHSP-xjPL5zVjGMzjQqPVeIV-jag!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1105%2C5796%2C7415%2C9393%2C9395%2C9396%2C9427%2C9429%2C9432%2C9433%2C9434%2C9hpz%2C9f77%2C9hsw%2C9vpg%2C9gve%2C9hrv%2C9k58%2C9gh9%2C9gss%2C9ic9%2C9gf5%2C9geu%2C9j71%2C9yhe%2C9yhg%2C9yhf%2C9xa2%2C9vri%2C9blq%2C9yhh%2Csalg%2C9yrm%2C9aaf%2C9vrl%2C9kag%2C9knw%2C9wud%2C9akw%2C9yhd&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
    # 赞比亚
    # id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=h1eKFA0BaMh84I89KPhhWn5uzUiwrBgld7856ktZHeX1f9OK6pulntTzSB1cx6PFPaB1i0g2CCsZtxBdrOEHiw!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=9hzp%2C9yb0%2Ceaam&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
    # 津巴布韦
    # id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=_HWk5PukF-9pZYDU4uOHjEBr9UQHjM7FeS66o6dX80EC5cdNfkhy0H_WMBcTl_vgum9dd7iMd3J1wrG63vK-Pg!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1729%2C9gm7%2C9efu%2C9gm4%2C9fa1%2C9gm9%2C9gk8%2C9gm3%2C9fa4%2C9gm2%2C9fa3&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
    # 纳米比亚 84篇
    # id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=NzlwtWUx3rMVy1H7HGSgXUXJiV11iTKvlwStCk7hX8KsmDmdnvU7MdUk6G4XxSqeUdytM7a4HjrzShdEbRq9bw!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=9faj%2C9gr0%2C9xz5&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
    # 南非
    id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=JgX5RuXjJkaFHWcgCL44rtQwFM_zIUP-rEgYzlEEJ4flKfHZfZlqsULJG5UxIw3TMMSgv313xt5KYkdLpVFrIA!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1106%2C1107%2C1113%2C1352%2C1457%2C1732%2C6256%2C6322%2C6323%2C6325%2C6402%2C6403%2C6510%2C6671%2C6985%2C6986%2C6987%2C6988%2C7035%2C7053%2C7067%2C7491%2C7528%2C7573%2C8147%2C8148%2C8231%2C8838%2C8839%2C9054%2C9674%2C9xve%2Csbf2%2Csbf1%2C9f08%2C9vqd%2C9go9%2C9vqe%2C9gad%2C9gqp%2C9gqt%2C9led%2C9alc%2C9kmj%2C9xui%2C9vlb%2C9ws3%2C9lc2%2C9vwn%2C9yll%2C9wub%2C9xy8%2C9yjs%2C9vw8%2C9gw9%2C9was%2C9afc%2C9f10%2C9fhe%2C9k29%2C9vqb%2Cefcj%2C9gae%2C9gqm%2C9f12%2C9a91%2C9feb%2C9f09%2C9klg%2C9f11%2C9gqn%2C9gqs%2C9d88%2C9wto%2C9fam%2C9fcm%2C9gmr%2Csbf4%2C9wb2%2C9ale%2Csghw%2C9ald%2C9f94%2C9f14%2C9gag%2C9faa%2C9yja%2Cefcp%2C9d90%2C9vxj%2C9luz%2C9xwz%2C9ib2%2C9vqg%2C9jcc%2C9afg%2C9yj4%2C9gaf%2C9alf%2Csbdh%2C9lvs%2C9jdu%2C9je4%2C9vlc%2C9fcr%2C9e9l%2C9alg%2C34s5%2Cs669%2C9a90%2C9lva%2C9ik4%2C9a92%2C9jby%2C9vkz%2C9kyj%2C9hv9%2Csf19%2C9kmk%2C9vqh%2C9d93%2Csbf3%2Csbf0%2C9lun%2C9xu4%2C9bcg%2C9baj%2C9ble%2C9ggn%2C9d92%2C9wtq%2C9vxw%2C9c20%2C9d99%2C9f20%2C9f21%2C9afd%2C9knv%2C9kn6&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
    ids_url = id_url.format(pages)
    print(ids_url)
    html = requests.get(url=ids_url, headers=headers).json()
    Items = html['Items']

    for item in Items:
        try:
            list = []
            uid = item['RegionId']
            # https://www.pressreader.com/api/articles/GetArticle?accessToken=DSMcZSXSNXQ3o6KJSrV-FP1s80ZHX5YU3oLNFLj6RgGOJV0R-3NfatPMCPsHSP-xjPL5zVjGMzjQqPVeIV-jag!!&key=284060552835887&viewType=search
            # two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=Icm3hIpmPlJ6Le3Y2gyonJdsRj7fDVmRQXMy9KkRJQ06cxPXU--V6d9_sEnDXSvxEtPXMftzyoDQxfEcY-bdRg!!&key={}&viewType=search'
            # two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=h1eKFA0BaMh84I89KPhhWn5uzUiwrBgld7856ktZHeX1f9OK6pulntTzSB1cx6PFPaB1i0g2CCsZtxBdrOEHiw!!&key={}&viewType=search'
            # two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=_HWk5PukF-9pZYDU4uOHjEBr9UQHjM7FeS66o6dX80EC5cdNfkhy0H_WMBcTl_vgum9dd7iMd3J1wrG63vK-Pg!!&key={}&viewType=search'
            # 纳米比亚
            # two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=NzlwtWUx3rMVy1H7HGSgXUXJiV11iTKvlwStCk7hX8KsmDmdnvU7MdUk6G4XxSqeUdytM7a4HjrzShdEbRq9bw!!&key={}&viewType=search'
            # 南非
            two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=JgX5RuXjJkaFHWcgCL44rtQwFM_zIUP-rEgYzlEEJ4flKfHZfZlqsULJG5UxIw3TMMSgv313xt5KYkdLpVFrIA!!&key={}&viewType=search'
            # 拼接详情页链接
            url1 = two_url.format(uid)
            time.sleep(random.randint(9, 11))
            print(url1)
            html = requests.get(url=url1, headers=headers).json()
            # 国家
            CountryCode = html['Issue']['CountryCode']
            list.append(CountryCode)
            # 媒体
            meiti = html['Issue']['Title']
            list.append(meiti)
            # 时间
            shijian = html['Issue']['Date']
            list.append(shijian)
            # 标题
            title = html['Title']
            list.append(title)
            # 文章
            texts = html['Blocks']
            list_Text = []
            for text in texts:
                Text = text['Text']
                list_Text.append(Text)
            m = ' '.join(list_Text)
            list.append(m)
            list.append('南非')
            print(list)
            csv_writer.writerow(list)
            k += 1
            # print("共", count, "页", "获取了第", k, "篇")
            print("共7121", "篇", "获取了第", k, "篇")
        except Exception as e:
            print("RegionId 为空，继续循环！")
            continue
