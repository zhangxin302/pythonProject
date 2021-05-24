"""
author:张鑫
date:2021/4/19 15:57
"""

import requests, json, pymysql,time

from tools.headers import headers
from tools.转变时间戳 import time_turn

db = pymysql.connect(user='root', passwd='zhangxin941021', database='qqmusic')
cursor = db.cursor()
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=137106212&g_tk=1176323532&loginUin=1247371788&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=106318183&cmd=8&needmusiccrit=0&pagenum=1&pagesize=25&lasthotcommentid=song_106318183_2097521454_1605715065_396340163_1617634003&domain=qq.com&ct=24&cv=10101010'
response = requests.get(url=url, headers=headers)
html = response.json()['comment']['commentlist']
for item in html:
    # 昵称
    nick = item['nick']
    # 评论
    rootcommentcontent = item['rootcommentcontent']
    # 时间
    time = item['time']
    time = time_turn(time)
    print(nick,rootcommentcontent,time)

    sql = '''
    insert into qqmusic_comment values(%s,%s,%s)
    '''
    execute = cursor.execute(sql, (nick, rootcommentcontent, time))
    db.commit()
db.close()