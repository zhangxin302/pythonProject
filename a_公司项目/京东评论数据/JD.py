# -*- coding: utf-8 -*-
import pymysql
import requests
from lxml import etree
from urllib.parse import quote

import json
import time, datetime
import csv

import re


class JD():
    # 评论链接
    def get_url(self):
        url_list = [
            '2783187',  # '100016117396'
        ]
        for url_id in url_list:
            self.get_meagess(url_id)

    # 数据详细信息
    def get_meagess(self, url_id):
        s = requests.session()
        url = 'https://club.jd.com/comment/productPageComments.action'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Cookie': 'shshshfp=4a1eb81ee0fdfbf8714be24c5e9c7802; shshshfpa=786d3aab-6e2e-fffd-841f-225dea209295-1616122470; __jdv=122270672|direct|-|none|-|1616122470651; __jdu=1616122470650718440956; areaId=1; ipLoc-djd=1-2800-55811-0; jwotest_product=99; __jda=122270672.1616122470650718440956.1616122471.1616122471.1616480425.2; __jdc=122270672; shshshfpb=eOlRmJ2biOZ2TlcDDPoL%207w%3D%3D; shshshsID=bc1463bf3364936cc40814eb52931989_2_1616480588234; __jdb=122270672.2.1616122470650718440956|2.1616480425; 3AB9D23F7A4B3C9B=KTS7HJG2FP5NVNP2BAQ3YBDLT3NRMYJHY277MUQG5VJO3A745RJGAYCBB2FMFWW2ZFGVKGYVTM5X4IXPQHVR6FBQ44; JSESSIONID=25A216B223B653BFA38445AD2DADAA6D.s1b                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     '
        }
        data = {
            'callback': 'fetchJSON_comment98',
            'productId': url_id,
            # 'productId':'2783187',
            'score': 0,
            'sortType': 6,
            'pageSize': 10,
            'isShadowSku': 0,
            'page': 0,
        }
        dic = {}
        while True:
            t = s.get(url, params=data, headers=header).text
            ir_urldate = int(time.time())
            try:
                t = re.search(r'(?<=fetchJSON_comment98\().*(?=\);)', t).group(0)
            except Exception as e:
                break
            j = json.loads(t)
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%正在抓取京东第', data['page'] + 1,
                  '页数据！！！%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            commentSummary = j['comments']
            for comment in commentSummary:
                c_content = comment['content']
                c_time = comment['referenceTime']
                c_name = comment['nickname']
                c_id = comment['id']
                c_referenceName = comment['referenceName']
                c_productColor = comment['productColor']
                # 判断时间是否符合规定内日期
                f = self.get_times(c_id, c_content, c_name, c_productColor, c_referenceName, c_time, url_id)
                if f == '时间符合':
                    dic['ir_content'] = c_content
                    dic['ir_urldate'] = int(time.time())
                    dic['ir_title'] = c_referenceName
                    dic['ir_authors'] = c_name
                    dic['ir_urltime'] = c_time
                    dic['Ir_goodstype'] = c_productColor
                    dic['ir_librariytype'] = 9  # 固定为9
                    dic['ir_mediasource'] = '京东'
                    dic['ir_area'] = 2  # 固定位2
                    dic['ir_trade'] = 6  # 血糖测试仪为医疗
                    dic['ir_indexsource'] = 'item.jd.com'
                    ### 数据库操作
                    # 获取数据库链接
                    # '''
                    try:
                        connection = pymysql.connect(
                            host='140.210.4.68',
                            port=3306,
                            user='zsjw_lnn',
                            passwd='zs#@jw_l#PFnn',
                            db='tieba_abroadsystem',
                            charset='utf8mb4'
                        )
                        # connection = pymysql.connect(
                        #     host='140.210.4.78',
                        #     port=3306,
                        #     user='test_openzsjw',
                        #     passwd='kophen#_teqsd#wtj',
                        #     db='test_abroadsystem',
                        #     charset='utf8mb4'
                        # )
                        # 获取会话指针
                        with connection.cursor() as cursor:
                            # 创建sql语句
                            if int(dic["ir_urltime"]) >= day_time:  # 发布时间大于当前凌晨
                                sheet_name = 'cn_allwxwb_abroaddataall'
                                # sheet_name = 'bkyy_wxwb_new'

                            else:  # 历史数据
                                sheet_name = 'cn_allwxwbhistory_abroaddataall'
                                # sheet_name = 'bkyy_wxwb_old'

                            sql = """INSERT INTO {}(ir_authors,ir_urltime,ir_urldate,\
                                                                   ir_content,ir_librariytype,ir_mediasource,ir_indexsource,\
                                                                   ir_title,ir_area,ir_trade)\
                                                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(
                                sheet_name)
                            # 执行sql语句
                            try:
                                cursor.execute(sql, (
                                    dic["ir_authors"], dic["ir_urltime"],
                                    dic["ir_urldate"], dic["ir_content"],
                                    dic["ir_librariytype"],
                                    dic["ir_mediasource"], dic["ir_indexsource"], dic["ir_title"],
                                    dic["ir_area"], dic["ir_trade"]
                                ))
                            except Exception as pymysqlErr:
                                # print(pymysqlErr)
                                # time.sleep(2)
                                continue

                            # 提交数据库
                            connection.commit()
                            print("数据存储成功！")
                    except Exception as e:
                        raise e

                    finally:
                        connection.close()

            data['page'] += 1
            time.sleep(5)

    # 对时间进行判断
    def get_times(self, c_id, c_content, c_name, c_productColor, c_referenceName, c_time, url_id):

        if (datetime.datetime.now() - datetime.timedelta(weeks=28)).strftime("%Y-%m-%d %H:%M") < c_time:
            print('商品的标题：', c_referenceName)
            print('评论的名称(id)：', c_name, '(', c_id, ')')
            print('评论的时间：', c_time)
            print('评论的内容：', c_content)
            print('商品的类型：', c_productColor)
            return '时间符合'


if __name__ == '__main__':
    day_time = int(time.mktime(datetime.date.today().timetuple()))  # 当天凌晨时间
    j = JD()
    j.get_url()
