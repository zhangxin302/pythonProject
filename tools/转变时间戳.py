"""
author:张鑫
date:2021/4/14 10:54
"""
import time


def time_turn(timenum):
    timeArray = time.localtime(timenum)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)


if __name__ == '__main__':
    while 1:
        timenum = int(input("请输入一个数："))
        time_turn(timenum)
