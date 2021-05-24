# import csv
# import time
# import random
#
#
# data = [['dy8gweyx63k4', '1389381445230063', '3793672946', 'MS4wLjABAAAA19GUkyrhBDZajUjLJhPRIy87snH-kkQ4HxZbB3Z5W3TwkiDYuMjaVw49y_Smq_ZD', 10, 806, 383],
# ['用户4275335602349', '4410844525635400', '2923173093', 'MS4wLjABAAAA01KCDtR7HbJ_Iaki15Qujz8D5iLgCd3a7yHgMrNY0mdvmLySeICDh5nAH_-CUi1E', 5556, 216, 835],
# ['快乐常在', '109965405922', '1938035925', 'MS4wLjABAAAA26RGegDLVwWEXbwJiS9gHcIcEdWL21aVlfkNa1jC5Bk', 15428, 518, 986]
#         ]
#
# f = open('粉丝数据.csv', 'w', encoding='utf-8')
# csv_writer = csv.writer(f)
# csv_writer.writerow(["抖音", "uid(权重)", "抖音号", "sec_uid", "赞", "关注", "粉丝"])
# for l in data:
#     #list_data = ['芳芳6640442892177', '89395945198', '576296731', 'MS4wLjABAAAASFj7P2MV90c_xvyx4lwJUxkgKnlk2YamcHUh6NW5-L4', 64858, 4182, 5005]
#     print("写入")
#     csv_writer.writerow(l)
#     print("成功！")
#     time.sleep(random.randint(2,3))





# import csv
# import time
# import random
# import pymysql
#
# data = [['dy8gweyx63k4', '1389381445230063', '3793672946', 'MS4wLjABAAAA19GUkyrhBDZajUjLJhPRIy87snH-kkQ4HxZbB3Z5W3TwkiDYuMjaVw49y_Smq_ZD', 10, 806, 383],
# ['用户4275335602349', '4410844525635400', '2923173093', 'MS4wLjABAAAA01KCDtR7HbJ_Iaki15Qujz8D5iLgCd3a7yHgMrNY0mdvmLySeICDh5nAH_-CUi1E', 5556, 216, 835],
# ['快乐常在', '109965405922', '1938035925', 'MS4wLjABAAAA26RGegDLVwWEXbwJiS9gHcIcEdWL21aVlfkNa1jC5Bk', 15428, 518, 986]
#         ]
# # 1.创建数据库连接对象和游标对象
# db = pymysql.connect(host='localhost', user='root', password='123456', database='Douyin', charset='utf8')
# cur = db.cursor()
# # 2.执行sql命令
# ins = 'insert into douyin values(%s,%s,%s,%s,%s,%s,%s)'
# for l in data:
#     #list_data = ['芳芳6640442892177', '89395945198', '576296731', 'MS4wLjABAAAASFj7P2MV90c_xvyx4lwJUxkgKnlk2YamcHUh6NW5-L4', 64858, 4182, 5005]
#     print("写入")
#     cur.execute(ins, l)
#     db.commit()
#     print("提交成功！")
#     time.sleep(random.randint(12,13))
#
# cur.close()
# db.close()


# li = ('model3','2万公里','2020','自动','0L','北京','24.99万')
#
# # 3.提交到数据库执行
#
# # 4.关闭游标,断开数据库连接
# cur.close()
# db.close()

# import pymongo
# dict1 = {'name':'dy8gweyx63k4', 'uid':'1389381445230063', 'gongzhonghao':'3793672946', 's_uid':'MS4wLjABAAAA19GUkyrhBDZajUjLJhPRIy87snH-kkQ4HxZbB3Z5W3TwkiDYuMjaVw49y_Smq_ZD','zan': 10, 'guanzu':806, 'fensi':383}
# client = pymongo.MongoClient('localhost',port=27017)# 连接
# db = client['DY'] # 创建库
# fs_douyin = db['douyin']  # 创建表
# fs_douyin.insert(dict1)
# print("存入成功！")


"""
更多评论2
https://api5-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id=6941116015938306089&cursor=3&count=10&top_ids&item_id=6940954265036852511&insert_ids&channel_id=0&city=441800&follower_count=0&is_familiar=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAyktCazjXBxo0Pa09jWTh4n4w_ZjXBfjDENZkDEO_oBA&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618370043&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618370043648&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
更多评论1
https://api5-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id=6940957195652120614&cursor=0&count=3&top_ids&item_id=6940954265036852511&insert_ids&channel_id=0&city=441800&follower_count=0&is_familiar=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAyktCazjXBxo0Pa09jWTh4n4w_ZjXBfjDENZkDEO_oBA&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618370116&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618370117297&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
https://api5-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id=6941116015938306089&cursor=0&count=3&top_ids&item_id=6940954265036852511&insert_ids&channel_id=0&city=441800&follower_count=0&is_familiar=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAyktCazjXBxo0Pa09jWTh4n4w_ZjXBfjDENZkDEO_oBA&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618369768&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618369769867&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
首页评论
https://api5-normal-c-hl.amemv.com/aweme/v2/comment/list/?aweme_id=6940954265036852511&cursor=0&count=20&address_book_access=2&gps_access=1&forward_page_type=1&channel_id=0&city=441800&hotsoon_filtered_count=0&hotsoon_has_more=0&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAyktCazjXBxo0Pa09jWTh4n4w_ZjXBfjDENZkDEO_oBA&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618369743&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618369744446&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
"""



import random
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

option = {
    "platformName": "Android",
    "platformVersion": "Andriod5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    "noReset": True,
    "unicodekeyboard": True,
    "resetkeyboard": True,
    "automationName": "UiAutomator1"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', option)

time.sleep(10)
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/b_3')):
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/b_3').click()
        print("第一步运行结束")
        time.sleep(10)
except:
    pass


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#
# try:
#     print(1)
#     if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/aia')):
#         print(2)
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').click()
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').send_keys('lv123052')
#         # 第二步运行结束
#         print("第二步运行结束")
#         time.sleep(20)
#
#         if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/kvg')):
#             driver.find_element_by_id('com.ss.android.ugc.aweme:id/kvg').click()
#             # 第三步运行结束
#             print("第三步运行结束")
#             time.sleep(20)
#     print(3)
#     if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_id('android:id/text1')):
#         print(4)
#         driver.find_element_by_id('android:id/text1').click()
#         # 第四步运行结束
#         print("第四步运行结束")
#         time.sleep(20)
#         print(5)
#         # com.ss.android.ugc.aweme:id/efb
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/efb').click()
#         # driver.find_element_by_class_name('android.widget.ImageView').click()
#         # 第五步运行结束
#         print("第五步运行结束")
#         time.sleep(20)
# except:
#     pass
#
# try:
#     if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/cz0')):
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/cz0').click()
#         # 第六步运行结束
#         print("第六步运行结束")
#         time.sleep(15)
# except:
#     pass

size = get_size()

print("开始滑动！")
while (True):
    l1 = random.randint(3,4)
    l1 = l1 /10
    print(l1)
    time.sleep(random.randint(15, 16))
    driver.swipe(int(size[0] * 0.5), int(size[1] * l1), int(size[0] * 0.7), int(size[1] * 0.2))

