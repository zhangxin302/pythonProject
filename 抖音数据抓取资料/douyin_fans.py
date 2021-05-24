"""
https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id=3579617596422716&sec_user_id=MS4wLjABAAAAmCZWzhmaMnJlkbOY3t2HJb2yALmz0ZTAQM6Z684NM4hclVsrnrggKpFL-lKInYWr&max_time=1618214826&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&vcd_count=0&ts=1618214826&cpu_support64=false&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&_rticket=1618214826854&minor_status=0&

"""
# import json
# import csv
#
# def response(flow):
#     # https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list
#     # https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list
#     if 'api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list' in flow.request.url:
#         print("**********************提取数据！****************************")
#         for user in json.loads(flow.response.text)['followers']:
#             print("获取成功！")
#             user_info = dict()
#             user_info['nickname'] = user['nickname']
#             user_info['share_id'] = user['uid']
#             user_info['douyin_id'] = user['short_id']
#             user_info['sec_uid'] = user['sec_uid']
#             if user_info['douyin_id'] == '0':
#                 user_info['douyin_id'] = user['unique_id']
#                 user_info['update_time'] = user['unique_id_modify_time']
#             print(user_info)

import json
import csv
import pandas as pd
def response(flow):
    f = open('抖音某用户粉丝数据.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["抖音", "uid(权重)", "抖音号", "sec_uid","赞","关注","粉丝"])
    # https://api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list
    # https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list
    if 'api3-normal-c-hl.amemv.com/aweme/v1/user/follower/list' in flow.request.url:
        print("**********************提取数据！****************************")
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
            print("***********************开始写入数据！*******************")
            print("********************写入成功！",s,"***********************")




        # df = pd.DataFrame(l_data,columns=["抖音", "uid(权重)", "抖音号", "sec_uid","赞","关注","粉丝"])
        # df.to_excel(f'抖音某用户粉丝数据.xlsx',index=False)

            # user_info = dict()
            # user_info['nickname'] = user['nickname']
            # user_info['share_id'] = user['uid']
            # user_info['douyin_id'] = user['short_id']
            # user_info['sec_uid'] = user['sec_uid']
            # if user_info['douyin_id'] == '0':
            #     user_info['douyin_id'] = user['unique_id']
            #     user_info['update_time'] = user['unique_id_modify_time']
            # print(user_info)

