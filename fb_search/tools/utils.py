# -*- coding: utf-8 -*-
# @Time : 2021/1/24 13:45
# @Author : python
# @File : utils.py
# @Project : fb_selenium
from time import mktime, strptime, localtime


def check_pub_time(pubTime, e_day=7):
    """检查过期时间
    过期 false
    没有过期 True
    """
    if not pubTime:
        return False
    try:
        pub_time = int(pubTime)
    except:
        pub_time = int(mktime(strptime(pubTime, '%Y-%m-%d %H:%M:%S')))
    now_time = int(mktime(localtime()))
    time_line = now_time - 86400 * e_day  # 过期时间线
    if pub_time > now_time:
        # 如果发布时间大于现在时间，说明时间错误，返回false
        return False
    # print(pubTime, pub_time, time_line)
    if pub_time >= time_line:
        return True
    else:
        return False