# """
# 第一页
# #越南
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers={}&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers={}&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
# #柬埔寨
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=6203%2C9gr2%2C9ws1%2C9vnr%2C9hm7%2C9vyu%2C9vyv%2C9kw9&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals=
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals=
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=20&pageSize=20&totals=
# # 文章页
# https://www.pressreader.com/api/articles/GetItems?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&articles=281689732619992%2C281483574217857%2C281668257700644%2C281878711203332%2C281779926953224%2C281835761418633%2C281805696700151%2C281479279216826%2C281960314943381%2C281706912129156%2C281513637842267%2C281526522737886%2C281556588593995%2C281852941234907%2C282054804517796%2C281857236206447%2C281724088023206%2C281711207006417%2C281496454358096%2C281956020504987&pages=&socialInfoArticles=&comment=LatestByAll&options=1&viewType=search
# # 具体文章url
# https://www.pressreader.com/api/articles/GetArticle?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&key=281689732619992&viewType=search
# https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=281689732619992&pageSize=20&totals=
# """
#
# import json
#
#
#
# import requests
# from fake_useragent import UserAgent
# import time
# import random
# import csv
#
# f = open('南非英文杂志.csv', 'w', encoding='utf-8')
#
# csv_writer = csv.writer(f)
# csv_writer.writerow(['区域', '媒体名称', '发布时间', '标题', '文章', '国家'])
#
# header = {
#     "user-agent": UserAgent().random,
#     'cookie':'uuid_tt_dd=10_8043419840-1618720225762-906214; __gads=ID=68561d0183eb4f57-22c688ef74c7001d:T=1618720229:S=ALNI_MYduBEdpFO7fL7PzsyhxTiL3HfkSQ; UN=qq_40932988; p_uid=U010000; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_8043419840-1618720225762-906214!5744*1*qq_40932988; c-login-auto=1; UserName=qq_40932988; UserInfo=8e3ea6355fc14a15a84036bb5c2f9fc5; UserToken=8e3ea6355fc14a15a84036bb5c2f9fc5; UserNick=小白入; AU=34D; BT=1619595467445; ssxmod_itna=Yq0xnDgQKxuD0lDzOD2YLDkfYi=zw6hILxGkQ0DBLfT4iNDnD8x7YDvmIOIKzKSlGGoaxkGETwQfYm2DLmd=cggqaTt4B3DEx06Kqmii4GGUxBYDQxAYDGDDPDocPD1D3qDkD7EZlMBsqDEDYp9DA3Di4D+8MQDmqG0DDU794G2D7U9RD+9WCd56ubS8i23fA=DjqTD/fqFsA=okZc5BT2bN1ITD0PsB6+YBPh3KYwxagQDzTODtqNMSLddgPtVRkioFipPmAv28Gk5YBe4iiooQOhQ4fpojGG34o/I00kMsDDA4/+GczDxD; ssxmod_itna2=Yq0xnDgQKxuD0lDzOD2YLDkfYi=zw6hILxGkQD8d6SOAfxGNvxGa8iQXoib+x82i6s=fa2Wj5qL7egNIiMiYE28YD8TvKGQMnm8KwOBFu9rfPNLeS7pNPsc=ux1A/UZRRBsk7G1IIjvHKlDOV79zugeT3=0DP/9ktgchKowCsah=41FdQO2=R0BHeawb1m2aNon8K0a8somH18cHv3FQOhLbCtcAkPW=4cHPTZq4cAc+y4jth19NeWujthjFwZm=NX77E6BCBzCaiu3EVUAEhkIrKHtnz6F1VAwOavt0bqpZSqnuhMtSFw2/a+Qbs/wrU4TzwIiBFFYWfiQ3bpzBiBebAYVF78Kw=fYb/YKwx5V4Ps97AYcYgP2c45EklKdNaxRc=bKanb1j23sTw/DiiIiQInBe9KFIUgF8eMA4VlErfwkBOh0e57oqLqeT3qZBifyQg3+4L8Rq6FTxHi3D07aA4brh3hDwBKb2YXp5mmou6Y=0UPT+6AKe0elbTTueAiXqU04M06iW32eAR290r5n6owRF0QBGmRcr4Mxu4xO7UdzUk8n+o0b9ePhxPOqU12oK9t0YnxDLxD2f3QfGxiRqtbGs6zH8dlaNbbqY07BikRxoZibKhsnGsziqFGzs0WC2YYoxmAdlQ53Vkc3uozteD===; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"islogin":{"value":"1","scope":1},"isonline":{"value":"1","scope":1},"isvip":{"value":"0","scope":1},"uid_":{"value":"qq_40932988","scope":1}}; dc_session_id=10_1619658501839.419969; c_first_ref=www.baidu.com; c_first_page=https://blog.csdn.net/lynn_coder/article/details/79504564; c_segment=6; dc_sid=952b42e53b505afcb59f081a59c417ed; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1619509690,1619579169,1619597177,1619658505; announcement-new={"isLogin":true,"announcementUrl":"https://blog.csdn.net/blogdevteam/article/details/112280974?utm_source=gonggao_0107","announcementCount":0,"announcementExpire":3600000}; referrer_search=1619658677992; firstDie=1; c_ref=https://so.csdn.net/so/search?q=ordinal%20not%20in%20range%28256%29&t=&u=; c_pref=https://so.csdn.net/so/search?q=ordinal%20not%20in%20range%28256%29&t=&u=; log_Id_click=146; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1619660575; log_Id_view=432; c_utm_term=ordinal not in range(256); c_utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-5-81119644.first_rank_v2_pc_rank_v29; c_page_id=default; dc_tos=qsay40; log_Id_pv=124'
#
# }
# headers = {
#     "user-agent": UserAgent().random,
#     # 'cookie': '_ga=GA1.2.435005338.1617938518; MONITOR_WEB_ID=1b749639-d3df-42de-8e5e-8c6ba9724457; _gid=GA1.2.660503105.1619424734; _gat=1; _tea_utm_cache_2608={"utm_source":"gold_browser_extension"}',
#
# }
# # url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=S3D1DesUYR3B7pzW0qYFdZQoUvBNYnlNzG_DzdN86DuYokaYocsTbbv9MbG_SbMBI8hdkAfGnwcP_zt4xowDNQ!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1109%2C1138%2C1731%2C8500%2C8601%2C8602%2C8606%2C8810%2C9106%2C9377%2C9470%2C9ggr%2C9ggs%2C9gcz%2C9kkf%2C9f70%2C9hpn%2C9d37%2C9i70%2C9hw6%2C9f06%2C9a19%2C9ggx%2C9ggh%2C9ggg%2C9ggj%2C9gc1%2C9gmx%2C9waq%2C9ych%2C9vw5%2C9ygr%2C9xzj%2Csghh%2Csghf%2Csghg%2C9wso%2C9wae%2C9vug%2C9ig3%2C9vw4%2C9yn2%2C9wad&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=0&pageSize=20&totals='
# url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=JgX5RuXjJkaFHWcgCL44rtQwFM_zIUP-rEgYzlEEJ4flKfHZfZlqsULJG5UxIw3TMMSgv313xt5KYkdLpVFrIA!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1106%2C1107%2C1113%2C1352%2C1457%2C1732%2C6256%2C6322%2C6323%2C6325%2C6402%2C6403%2C6510%2C6671%2C6985%2C6986%2C6987%2C6988%2C7035%2C7053%2C7067%2C7491%2C7528%2C7573%2C8147%2C8148%2C8231%2C8838%2C8839%2C9054%2C9674%2C9xve%2Csbf2%2Csbf1%2C9f08%2C9vqd%2C9go9%2C9vqe%2C9gad%2C9gqp%2C9gqt%2C9led%2C9alc%2C9kmj%2C9xui%2C9vlb%2C9ws3%2C9lc2%2C9vwn%2C9yll%2C9wub%2C9xy8%2C9yjs%2C9vw8%2C9gw9%2C9was%2C9afc%2C9f10%2C9fhe%2C9k29%2C9vqb%2Cefcj%2C9gae%2C9gqm%2C9f12%2C9a91%2C9feb%2C9f09%2C9klg%2C9f11%2C9gqn%2C9gqs%2C9d88%2C9wto%2C9fam%2C9fcm%2C9gmr%2Csbf4%2C9wb2%2C9ale%2Csghw%2C9ald%2C9f94%2C9f14%2C9gag%2C9faa%2C9yja%2Cefcp%2C9d90%2C9vxj%2C9luz%2C9xwz%2C9ib2%2C9vqg%2C9jcc%2C9afg%2C9yj4%2C9gaf%2C9alf%2Csbdh%2C9lvs%2C9jdu%2C9je4%2C9vlc%2C9fcr%2C9e9l%2C9alg%2C34s5%2Cs669%2C9a90%2C9lva%2C9ik4%2C9a92%2C9jby%2C9vkz%2C9kyj%2C9hv9%2Csf19%2C9kmk%2C9vqh%2C9d93%2Csbf3%2Csbf0%2C9lun%2C9xu4%2C9bcg%2C9baj%2C9ble%2C9ggn%2C9d92%2C9wtq%2C9vxw%2C9c20%2C9d99%2C9f20%2C9f21%2C9afd%2C9knv%2C9kn6&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber=20&pageSize=20&totals='
# # html = requests.get(url=url, headers=header, verify=False).json()
# html = requests.get(url=url, headers=header, verify=False).json()
#
# count = html['TotalFoundArticles']
#
# if count % 20 != 0:
#     page_sum = count // 20 + 1
# else:
#     page_sum = count // 20
# print(count, page_sum)
# k = 1165
# # k = 247
# for page in range(69, page_sum):
#     time.sleep(random.randint(30, 35))
#     pages = page * 20
#     # 越南
#     # id_url = "https://www.pressreader.com/api/search/GetArticles?accessToken=8IsT2AnGvSQ9PNYpurBoLIlaOjztWhESotRv4fVIwm7M09dEywvjXRxqrjhDqoj6zjHrGkR-qhBxBG9g_qYLlg!!&searchText=china+poverty&searchAuthor=&languages=en&newspapers=9011%2C9hmc%2C9hmd%2C9hzl%2Cf672&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals="
#     # 柬埔寨
#     id_url = 'https://www.pressreader.com/api/search/GetArticles?accessToken=JgX5RuXjJkaFHWcgCL44rtQwFM_zIUP-rEgYzlEEJ4flKfHZfZlqsULJG5UxIw3TMMSgv313xt5KYkdLpVFrIA!!&searchText=China+poverty&searchAuthor=&languages=en&newspapers=1106%2C1107%2C1113%2C1352%2C1457%2C1732%2C6256%2C6322%2C6323%2C6325%2C6402%2C6403%2C6510%2C6671%2C6985%2C6986%2C6987%2C6988%2C7035%2C7053%2C7067%2C7491%2C7528%2C7573%2C8147%2C8148%2C8231%2C8838%2C8839%2C9054%2C9674%2C9xve%2Csbf2%2Csbf1%2C9f08%2C9vqd%2C9go9%2C9vqe%2C9gad%2C9gqp%2C9gqt%2C9led%2C9alc%2C9kmj%2C9xui%2C9vlb%2C9ws3%2C9lc2%2C9vwn%2C9yll%2C9wub%2C9xy8%2C9yjs%2C9vw8%2C9gw9%2C9was%2C9afc%2C9f10%2C9fhe%2C9k29%2C9vqb%2Cefcj%2C9gae%2C9gqm%2C9f12%2C9a91%2C9feb%2C9f09%2C9klg%2C9f11%2C9gqn%2C9gqs%2C9d88%2C9wto%2C9fam%2C9fcm%2C9gmr%2Csbf4%2C9wb2%2C9ale%2Csghw%2C9ald%2C9f94%2C9f14%2C9gag%2C9faa%2C9yja%2Cefcp%2C9d90%2C9vxj%2C9luz%2C9xwz%2C9ib2%2C9vqg%2C9jcc%2C9afg%2C9yj4%2C9gaf%2C9alf%2Csbdh%2C9lvs%2C9jdu%2C9je4%2C9vlc%2C9fcr%2C9e9l%2C9alg%2C34s5%2Cs669%2C9a90%2C9lva%2C9ik4%2C9a92%2C9jby%2C9vkz%2C9kyj%2C9hv9%2Csf19%2C9kmk%2C9vqh%2C9d93%2Csbf3%2Csbf0%2C9lun%2C9xu4%2C9bcg%2C9baj%2C9ble%2C9ggn%2C9d92%2C9wtq%2C9vxw%2C9c20%2C9d99%2C9f20%2C9f21%2C9afd%2C9knv%2C9kn6&countries=&categories=&range=Anytime&searchIn=ALL&orderBy=Relevance&hideSame=0&rowNumber={}&pageSize=20&totals='
#     ids_url = id_url.format(pages)
#     print(ids_url)
#     html = requests.get(url=ids_url, headers=headers).json()
#     Items = html['Items']
#
#     for item in Items:
#         try:
#             list = []
#             uid = item['RegionId']
#             two_url = 'https://www.pressreader.com/api/articles/GetArticle?accessToken=JgX5RuXjJkaFHWcgCL44rtQwFM_zIUP-rEgYzlEEJ4flKfHZfZlqsULJG5UxIw3TMMSgv313xt5KYkdLpVFrIA!!&key={}&viewType=search'
#             # 拼接详情页链接
#             url1 = two_url.format(uid)
#             time.sleep(random.randint(10, 12))
#             print(url1)
#             html = requests.get(url=url1, headers=headers).json()
#             # 国家
#             CountryCode = html['Issue']['CountryCode']
#             list.append(CountryCode)
#             # 媒体
#             meiti = html['Issue']['Title']
#             list.append(meiti)
#             # 时间
#             shijian = html['Issue']['Date']
#             list.append(shijian)
#             # 标题
#             title = html['Title']
#             list.append(title)
#             # 文章
#             texts = html['Blocks']
#             list_Text = []
#             for text in texts:
#                 Text = text['Text']
#                 list_Text.append(Text)
#             m = ' '.join(list_Text)
#             list.append(m)
#             list.append('南非')
#             print(list)
#             csv_writer.writerow(list)
#             k += 1
#             # print("共", count, "页", "获取了第", k, "篇")
#             print("共", count, "篇", "获取了第", k, "篇")
#         except Exception as e:
#             print("RegionId 为空，继续循环！")
#             continue



