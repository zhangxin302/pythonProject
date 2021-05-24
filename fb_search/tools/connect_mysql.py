import hashlib
import jsonpath
import json
import redis
import pymysql
import time, datetime


def Save_Data(datas):
    # connect = pymysql.Connect(
    #     host='140.210.4.78',
    #     port=3306,
    #     user='jwykxs',
    #     passwd='djwbyktxs',
    #     db='abroadsystem_six',
    #     charset='utf8mb4'
    # )
    connect = pymysql.Connect(
        host='140.210.4.68',
        port=3306,
        user='zsjw_lnn',
        passwd='zs#@jw_l#PFnn',
        db='hkby_abroadsystem',
        charset='utf8mb4'
    )
    cursor = connect.cursor()

    for data in datas:
        day_time = int(time.mktime(datetime.date.today().timetuple()))
        try:
            if int(data["ir_urltime"]) >= day_time:
                cursor.execute(
                    """insert into hkby_facebook_abroaddataall(ir_keyword,ir_authors,ir_urltime,ir_urldate,ir_url,ir_sid,ir_content,ir_title,ir_nresrved1,ir_nresrved2,ir_nresrved3,ir_ispost,ir_area,ir_mediatype,ir_mediasource,ir_firsturl,ir_md5)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (data["ir_keyword"],data["ir_authors"], data["ir_urltime"], data["ir_urldate"], data["ir_url"], data["ir_sid"],
                     data["ir_content"], data["ir_title"], data["ir_nresrved1"], data["ir_nresrved2"],
                     data["ir_nresrved3"], data["ir_ispost"], data["ir_area"], data["ir_mediatype"],
                     data["ir_mediasource"], data["ir_firsturl"], data["ir_md5"]))
                connect.commit()
                print("——————————-——————————————存入当天库成功！！！！——————————-——————————————")
            else:
                cursor.execute(
                    """insert into hkby_facebookhistory_abroaddataall(ir_keyword,ir_authors,ir_urltime,ir_urldate,ir_url,ir_sid,ir_content,ir_title,ir_nresrved1,ir_nresrved2,ir_nresrved3,ir_ispost,ir_area,ir_mediatype,ir_mediasource,ir_firsturl,ir_md5)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (data["ir_keyword"],data["ir_authors"], data["ir_urltime"], data["ir_urldate"], data["ir_url"], data["ir_sid"],
                     data["ir_content"], data["ir_title"], data["ir_nresrved1"], data["ir_nresrved2"],
                     data["ir_nresrved3"], data["ir_ispost"], data["ir_area"], data["ir_mediatype"],
                     data["ir_mediasource"], data["ir_firsturl"], data["ir_md5"]))
                connect.commit()
                print("——————————-——————————————存入历史库成功！！！！——————————-——————————————")

        except Exception as e:
            print("存入数据库出错:", e)
            continue
