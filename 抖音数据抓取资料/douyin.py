#https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id=82617835967&sec_user_id=MS4wLjABAAAAB5KAoNAiFqL85lpM_USNlz8hga_34k9apJhZ_41VIkw&max_time=1618303904&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&vcd_count=0&ts=1618303904&cpu_support64=false&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&_rticket=1618303904610&minor_status=0&
#https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id=82617835967&sec_user_id=MS4wLjABAAAAB5KAoNAiFqL85lpM_USNlz8hga_34k9apJhZ_41VIkw&max_time=1618303656&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&vcd_count=0&ts=1618303916&cpu_support64=false&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&_rticket=1618303917213&minor_status=0&

import json
import csv
import pandas as pd
import pymysql
from mitmproxy import ctx

def response(flow):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Douyin', charset='utf8')
    cur = db.cursor()
    # 2.执行sql命令
    # https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list
    # https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list
    if 'api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list' in flow.request.url:
        print("**********************提取数据！****************************")
        ins = 'insert into yzq values(%s,%s,%s,%s,%s,%s,%s)'
        # l_data = []
        s = 0
        for user in json.loads(flow.response.text)['followers']:
            s+=1
            print("获取成功！")
            list_data = []
            # 抖音名
            list_data.append(user['nickname'])
            # 用户身份证明 优先推送uid权重高的用户作品
            list_data.append(user['uid'])
            # 抖音号
            list_data.append(user['short_id'])
            # 用户身份证明(算法加密)
            list_data.append(user['sec_uid'])
            if list_data[2] == '0':
                list_data.append(user['unique_id'])
            # 获赞
            list_data.append(user['total_favorited'])
            # 关注
            list_data.append(user['following_count'])
            # 粉丝
            list_data.append(user['follower_count'])
            print(list_data)
            # l_data.append(list_data)
            cur.execute(ins, list_data)
            db.commit()
            print("********************写入成功！",s,"***********************")














# **************************************************************************************************


#
# def response(flow):
#     # 1.创建数据库连接对象和游标对象
#     # https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list
#     # https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list
#     # https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id=82617835967&sec_user_id
#     #   api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id
#     if 'api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list' in flow.request.url:
#         db = pymysql.connect(host='localhost', user='root', password='123456', database='Douyin', charset='utf8')
#         cur = db.cursor()
#         # 2.执行sql命令
#         ins = 'insert into yzq values(%s,%s,%s,%s,%s,%s,%s)'
#         print("#######################数据库配置完毕！##############################")
#         print("**********************提取数据！****************************")
#         # l_data = []
#         s = 0
#         for user in json.loads(flow.response.text)['followers']:
#             s += 1
#             print("获取成功！")
#             list_data = []
#             # 抖音名
#             list_data.append(user['nickname'])
#             # 用户身份证明 优先推送uid权重高的用户作品
#             list_data.append(user['uid'])
#             # 抖音号
#             list_data.append(user['short_id'])
#             # 用户身份证明(算法加密)
#             list_data.append(user['sec_uid'])
#             if list_data[2] == '0':
#                 list_data.append(user['unique_id'])
#             # 获赞
#             list_data.append(user['total_favorited'])
#             # 关注
#             list_data.append(user['following_count'])
#             # 粉丝
#             list_data.append(user['follower_count'])
#             print(list_data)
#             # l_data.append(list_data)
#             print("***********************开始写入数据！*******************")
#             cur.execute(ins, list_data)
#             db.commit()
#             print("********************写入成功！", s, "***********************")

