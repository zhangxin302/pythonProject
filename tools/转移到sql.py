import pymysql
import pymongo
import time
from datetime import datetime
import uuid

import schedule


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


client = pymongo.MongoClient('192.168.1.158', 27017)
db = client["LawyerArena"]
c = db.wechatAt

# db = pymysql.connect('192.168.1.147', 'root', '3edcVFR$', 'vx_article', charset='utf8mb4')

cursor = db.cursor()
def zhuanyi():
    now = datetime.now().strftime('%Y-%m-%d')
    print(now)
    error_lst = []
    n = 0
    for l in list(c.find({'crawDate':now})):
        names = '(pubDate,source,url,title,content,articleType,id,crawDate)'
        lst = [l.get('pubDate'),l.get('source'),l.get('url'),l.get('title'),l.get('content'),l.get('articleType'),''.join(str(uuid.uuid4()).split('-'))]
        lst.append(datetime.now().strftime('%Y-%m-%d'))
        lst[0] = str(parse_ymd(lst[0]))
        lst[-1] = str(parse_ymd(lst[-1]))
        s_num = ('%s,' * len(list(lst)))[:-1]
        query = f"insert into articles {names} values ({s_num})"
        try:
            cursor.execute(query, tuple(lst))
        except Exception as e:
            if str(e).find('Duplicate') < 0:
                print(str(e))
                input('查看')
            else:
                print('已存在')
                continue
        print(l.get('title'))
        c.update({'_id':l.get('_id')},{'$set':{'tag':1}})
        db.commit()
    print(error_lst)
    cursor.close()
    db.close()
    print(n)
zhuanyi()



