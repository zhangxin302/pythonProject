import pymysql
import requests

url = 'https://ah2.zhangyue.com/zybk/api/detail/book?bid=11290347&pluginVersion=125&pk=ch_feature&zysid=c89ab5434d569bcc9cf71e8e92e34680&usr=i3219068747&rgt=7&p1=YHj%2BiXK2QAoDABKLnHZx1gpD&pc=10&p2=108032&p3=17410069&p4=501669&p5=19&p6=IJIGAAIBABCBHIECCBBD&p7=__621028764144779&p9=0&p12=&p16=LIO-AN00&p21=10203&p22=5.1.1&p25=74101&p26=22&p28=&p29=zye5b814'
response = requests.get(url=url)
html = response.json()['body']['favInfo']
db = pymysql.connect(
    host='localhost',
    # 数据库名称
    db='ireader',
    # 端口号
    port=3306,
    # 用户名
    user='root',
    # 密码
    passwd='zhangxin941021',
    charset='utf8',
    use_unicode=False
)
cursor = db.cursor()
for item in html:
    # 作者
    author = item['author']
    # 书名
    bookName = item['bookName']
    # 类型
    icon = item['icon']
    # id
    novel_id = item['id']
    # 图片链接
    picUrl = item['picUrl']
    # 文章链接
    url = item['url']

    # 链接数据库

    # xs：是表名称
    sql = '''
           insert into ireader values(%s,%s,%s,%s,%s,%s)

    '''

    cursor.execute(sql, (author, bookName, icon, novel_id, picUrl, url))

    db.commit()
