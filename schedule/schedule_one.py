"""
author:张鑫
date:2021/5/13 9:51
"""
import re

import schedule
import time


def job():
    for i in range(100):
        print(i)


def work():
    print("work")


if __name__ == '__main__':
    while 1:
        # 每两秒执行一次
        schedule.every(2).seconds.do(work)
        # 每秒执行一次
        # schedule.every().second.do(job)
        # 每分钟执行一次
        # schedule.every().minute.do(job)
        # 每小时执行一次
        # schedule.every().hour.do(job)
        # 每天执行一次
        # schedule.every().day.do(job)
        # 每天10:12执行一次
        # schedule.every().day.at("10:23").do(work)

        schedule.run_pending()
        time.sleep(10)
