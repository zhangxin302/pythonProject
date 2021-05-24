"""
author:张鑫
date:2021/4/18 16:25
"""
import pymysql,re
import requests, json

from tools.headers import headers
db = pymysql.connect(user='root',passwd='zhangxin941021',database='ireader')
cursor = db.cursor()
url = 'https://ah2.zhangyue.com/zyco/api/circle/comment?timestamp=1618735607510&sign=Cy8LcCIMKOLbgt%2FM00jDLiM5T0mSjcOhVOvjPhPg6LDHGShLj%2BcgehoT%2BGiIUWpZwofKhUg4WdUtDQaXtqIuVtADb0dtMxEPtP6nA9MQdQMFdMVduv8E5AGTShmwuCUAuLV1NP3t45N%2BC2ED%2FYNq38bCMUw4PmUET%2BLwfPKj4iY%3D&page=8&type=data&id=book_11096946&plug=52&pluginVersion=52&zysid=c89ab5434d569bcc9cf71e8e92e34680&usr=i3219068747&rgt=7&p1=YHj%2BiXK2QAoDABKLnHZx1gpD&pc=10&p2=108032&p3=17410069&p4=501669&p5=19&p6=IJIGAAIBABCBHIECCBBD&p7=__621028764144779&p9=0&p12=&p16=LIO-AN00&p21=10203&p22=5.1.1&p25=74101&p26=22&p28=&p29=zye5b814 '
response = requests.get(url, headers=headers)
html = response.json()['body']['data']
for item in html:
    # 用户昵称
    nick = item['user']['nick']
    # 等级
    level = item['user']['level']
    # 评论时间
    # createTime =item['createTime']
    # createTime = createTime.replace('月','-').replace('日','')
    # 评论内容
    content = item['content']

    sql = '''
    insert into content values(%s,%s,%s)
    '''
    cursor.execute(sql,(nick,level,content))
    db.commit()
    # db.close()
    #
    # print(f"用户昵称:{nick}\n等级:{level}\n评论时间:{createTime}\n评论内容:{content}\n")
    # print(f"用户昵称:{nick}\n等级:{level}\n评论内容:{content}\n")
