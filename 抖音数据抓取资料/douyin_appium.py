"""
com.ss.android.ugc.aweme:id/e4i
com.ss.android.ugc.aweme:id/aia
com.ss.android.ugc.aweme:id/e2y
com.ss.android.ugc.aweme:id/cz0
"""

# import random
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# option = {
#     "platformName": "Android",
#     "platformVersion": "Andriod5.1.1",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.ss.android.ugc.aweme",
#     "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
#     "noReset": True,
#     "unicodekeyboard": True,
#     "resetkeyboard": True,
#     "automationName": "UiAutomator1"
# }
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', option)
#
# time.sleep(10)
# try:
#     if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/e4i')):
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/e4i').click()
#         print("第一步运行结束")
#         time.sleep(10)
# except:
#     pass
#
#
# def get_size():
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     return (x, y)
#
#
# try:
#     print(1)
#     if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/aia')):
#         print(2)
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').click()
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').send_keys('lv123052')
#         # 第二步运行结束
#         print("第二步运行结束")
#         time.sleep(10)
#
#         if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/kvg')):
#             driver.find_element_by_id('com.ss.android.ugc.aweme:id/kvg').click()
#             # 第三步运行结束
#             print("第三步运行结束")
#             time.sleep(10)
#     print(3)
#     if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_id('android:id/text1')):
#         print(4)
#         driver.find_element_by_id('android:id/text1').click()
#         # 第四步运行结束
#         print("第四步运行结束")
#         time.sleep(10)
#         print(5)
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/e2y').click()
#         # driver.find_element_by_class_name('android.widget.ImageView').click()
#         # 第五步运行结束
#         print("第五步运行结束")
#         time.sleep(10)
# except:
#     pass
#
# try:
#     if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/cz0')):
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/cz0').click()
#         # 第六步运行结束
#         print("第六步运行结束")
#         time.sleep(10)
# except:
#     pass
#
# size = get_size()
# x1 = int(size[0] * 0.5)
# x2 = int(size[0] * 0.7)
# y1 = int(size[1] * 0.9)
# y2 = int(size[1] * 0.2)
#
# while (True):
#     time.sleep(random.randint(12, 15))
#     driver.swipe(x1, y1, x2, y2)
#
#     # print("运行结束！")


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

time.sleep(20)
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/e4i')):
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/e4i').click()
        print("第一步运行结束")
        time.sleep(20)
except:
    pass


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


try:
    print(1)
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/aia')):
        print(2)
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').click()
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/aia').send_keys('lv123052')
        # 第二步运行结束
        print("第二步运行结束")
        time.sleep(20)

        if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/kvg')):
            driver.find_element_by_id('com.ss.android.ugc.aweme:id/kvg').click()
            # 第三步运行结束
            print("第三步运行结束")
            time.sleep(20)
    print(3)
    if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_id('android:id/text1')):
        print(4)
        driver.find_element_by_id('android:id/text1').click()
        # 第四步运行结束
        print("第四步运行结束")
        time.sleep(20)
        print(5)
        # com.ss.android.ugc.aweme:id/efb
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/efb').click()
        # driver.find_element_by_class_name('android.widget.ImageView').click()
        # 第五步运行结束
        print("第五步运行结束")
        time.sleep(20)
except:
    pass

try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/cz0')):
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/cz0').click()
        # 第六步运行结束
        print("第六步运行结束")
        time.sleep(15)
except:
    pass

size = get_size()


while (True):
    l1 = random.randint(3,6)
    l1 = l1 /10
    print(l1)
    time.sleep(random.randint(18, 20))
    driver.swipe(int(size[0] * 0.5), int(size[1] * l1), int(size[0] * 0.7), int(size[1] * 0.2))





# x1 = int(size[0] * 0.5)
# x2 = int(size[0] * 0.7)
# y1 = int(size[1] * 0.9)
# y2 = int(size[1] * 0.2)
#
# while (True):
#     l = random.randint(2, 5)
#     l = l *100
#     print(l)
#     time.sleep(random.randint(9, 11))
#     driver.swipe(x1, y1, x2, y2,duration=l)





    # print("运行结束！")





