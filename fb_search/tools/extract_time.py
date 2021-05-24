# -*- coding: utf-8 -*-
# @Time : 2021/1/24 1:16
# @Author : python
# @File : extract_time.py
# @Project : fb_selenium
import re
from traceback import format_exc
from time import localtime, mktime, strptime, strftime
import logging
import datetime
import time

logger = logging.getLogger(__name__)


def time_stamp(nums, str_format, _year=None, re_msg=''):
    '''
    :param num_li: 时间列表
    :param str_format: 格式化
    :return:时间戳
    '''
    # print(str_format)
    try:
        put_time_str = '-'.join([str(i) for i in nums])
        ir_urltime = int(mktime(strptime(put_time_str, str_format)))
    except Exception as e:
        # print('解析错误 {}'.format(e))
        ir_urltime = None
        pass

    # if ir_urltime:
    #     print('解析方式：', re_msg)
    #     pass

    return ir_urltime


# 发布时间处理器
def handle_pub_time(result_content, parse_date_mode=''):
    '''

    :param result_content: 时间提取
    :param parse_date_mode: 判断时间是那种解析方式
    :return:
    '''
    if not result_content:
        return
    result_content = re.compile('\t|\r|\n').sub(' ', str(result_content))
    result_content = result_content.replace(' ', ' ')  # 替换不一样的空格
    ir_urltime = None
    _year = localtime().tm_year
    _mon = localtime().tm_mon
    _day = localtime().tm_mday
    _hour = localtime().tm_hour
    _min = localtime().tm_min
    _sec = localtime().tm_sec
    # 判断是哪种解析方式
    # parse_english_day_mon_year 解析时间：  01/03/2019 日/月/年
    # 针对英语解析 01/03/2019 日/月/年 还是 月/日/年
    # 默认是 月/日/年
    if parse_date_mode == 'parse_english_day_mon_year':
        print('解析特殊时间 日/月/年')
        #  01/03/2019 01:23
        #  01-03-2019 01:23
        #  01.03.2019 01:23
        if not ir_urltime:
            re_msg = '([0123]*\d)[\./-]([01]*\d)[\./-](20[012]\d)[,]* (\d{1,2}):(\d{1,2})'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                str_format = '%d-%m-%Y-%H-%M'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

        # 01/03/2019
        # 01-03-2019
        # 01.03.2019
        # 01. 03. 2018
        if not ir_urltime:
            re_msg = '([0123]*\d)[\./-][ ]*([01]*\d)[\./-][ ]*(20[012]\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                str_format = '%d-%m-%Y'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 英语提取
    if not ir_urltime:
        try:
            ir_urltime = parse_english_time(result_content, _year, _mon, _day, _hour, _min, _sec)
        except:
            print('\n{}\n英语时间处理错误'.format(format_exc()))

        if ir_urltime:
            print('英语时间处理')

    # 精准匹配
    # 2019年05月10日04:38:10
    if not ir_urltime:
        re_msg = '(20[012]\d)[-/ 年\.](\d{1,2})[-/ 月\.](\d{1,2})[T-日号/號 \.][T]*[ ]*(\d{1,2}):(\d{1,2}):(\d{1,2})'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m-%d-%H-%M-%S'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    #  2019/05/10/04:38
    if not ir_urltime:
        re_msg = '(20[012]\d)[-/ 年\.](\d{1,2})[-/ 月\.](\d{1,2})[T-日/号號 \.][T]*[ ]*(\d\d{1,2}):(\d\d{1,2})'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m-%d-%H-%M'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 2019年05月10日 04
    if not ir_urltime:
        re_msg = '(20[012]\d)[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[T-日/号號 \.][T]*[ ]*(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m-%d-%H'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 2019年05月10日
    if not ir_urltime:
        re_msg = '(20[012]\d)[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[T-日号/號 \.]*'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m-%d'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 2019 年 03 月 19 日
    # 2019年3 月19 日
    if not ir_urltime:
        re_msg = '(20[012]\d)[ ]*年[ ]*(\d{1,2})[ ]*月[ ]*(\d{1,2})[ ]*[T日号號]'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m-%d'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 2018, 9. 10
    # 2018,9.10
    if not ir_urltime:
        re_msg = '(20[012]\d)[\.,][ ]*([01]*\d)[\.,][ ]*([0-3]*\d)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = nums[0]
            str_format = '%Y-%m-%d'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # -----------------------------------------------------
    # 精准匹配年缺年份在后面
    # 05月10日2019年 04:38:10
    if not ir_urltime:
        re_msg = '(\d+)[-/ 月\.](\d+)[-日号/號 \.](20[012]\d)[-/ 年,\.][ ]*(\d+):(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%m-%d-%Y-%H-%M-%S'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    #  05/10/2019 04:38
    if not ir_urltime:
        re_msg = '([01]*\d)[-/ 月\.]([0123]*\d)[-日号/號 \.](20[012]\d)[-/ 年,\.][ ]*(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%m-%d-%Y-%H-%M'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 05月10日2019年 04
    if not ir_urltime:
        re_msg = '(\d+)[-/ 月\.](\d+)[-日/号號 \.](20[012]\d)[-/ 年,\.][ ]*(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%m-%d-%Y-%H'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 05月10日2019年
    # 01.03.2018
    if not ir_urltime:
        re_msg = '(\d+)[-/月\. ][ ]*(\d+)[-日/号號\. ][ ]*(20[012]\d)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%m-%d-%Y'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
    # -----------------------------------------------------
    # 精准匹配年份少位数
    # 19年05月10日04:38:10
    if not ir_urltime:
        re_msg = '(\d{2})[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[-日/号號 \.][ ]*(\d+):(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%Y-%m-%d-%H-%M-%S'
            nums = list(nums[0])
            nums[0] = '{}{}'.format(str(_year)[:2], nums[0])
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    #  19/05/10/04:38
    if not ir_urltime:
        re_msg = '(\d{2})[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[-日/号號 \.][ ]*(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%Y-%m-%d-%H-%M'
            nums = list(nums[0])
            nums[0] = '{}{}'.format(str(_year)[:2], nums[0])
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 19年05月10日 04
    if not ir_urltime:
        re_msg = '(\d{2})[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[-日/号號 \.][ ]*(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%Y-%m-%d-%H'
            nums = list(nums[0])
            nums[0] = '{}{}'.format(str(_year)[:2], nums[0])
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # -----------------------------------------------------
    # 精准匹配年缺少年份
    # 05月10日04:38:10
    if not ir_urltime:
        re_msg = '(\d+)[-/ 月\.](\d+)[-日/号號 \.][ ]*(\d+):(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%m-%d-%H-%M-%S-%Y'
            nums = list(nums[0])
            nums.append(_year)
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    #  05/10 04:38
    if not ir_urltime:
        re_msg = '(\d+)[-/ 月\.](\d+)[-日/号號 \.][ ]*(\d+):(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%m-%d-%H-%M-%Y'
            nums = list(nums[0])
            nums.append(_year)
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 05月10日 04
    if not ir_urltime:
        re_msg = '(\d+)[-/ 月\.](\d+)[-日号/號 \.][ ]*(\d+)'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%m-%d-%H-%Y'
            nums = list(nums[0])
            nums.append(_year)
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 链接提取时间
    # 针对报刊那种
    # https://m.yyrb.cn/html/iywb/20161205/index.html
    if not ir_urltime:
        re_msg = '.*?(20[012]\d[01]\d[0123]\d).*'
        num = re.compile(re_msg).findall(result_content)
        if num:
            num = [num[0], ]
            str_format = '%Y%m%d'
            ir_urltime = time_stamp(num, str_format, re_msg=re_msg)

    # http://www.hoptodo.hk/life/news/2017/0516/31393.html
    # http://www.hoptodo.hk/life/news/2017-0516/31393.html
    if not ir_urltime:
        re_msg = '(20[012]\d+)[/-]([01]\d[0123]\d)'
        num = re.compile(re_msg).findall(result_content)
        if num:
            num = list(num[0])
            str_format = '%Y-%m%d'
            ir_urltime = time_stamp(num, str_format, re_msg=re_msg)

    # 链接提取时间
    # 针对报刊那种
    # http://124.224.204.62:8081/szb/pc/201908/15/c183346.html
    # http://124.224.204.62:8081/szb/pc/201908-15/c183346.html
    # http://124.224.204.62:8081/szb/pc/201908.15/c183346.html
    if not ir_urltime:
        re_msg = '.*?(20[012]\d[01][1-9])[-/\.]([0123]\d).*'
        num = re.compile(re_msg).findall(result_content)
        if num:
            num = list(num[0])
            str_format = '%Y%m-%d'
            ir_urltime = time_stamp(num, str_format, re_msg=re_msg)

    # 05月10日 05月10日
    if not ir_urltime:
        re_msg = '(\d{1,2})[-/ 月\.](\d{1,2})[-日号/號 \.]*'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%m-%d-%Y'
            nums = list(nums[0])
            nums.append(_year)
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # ------------------------------
    # 年份缺少位数
    # 19年05月10日 19年05月10日
    if not ir_urltime:
        re_msg = '(\d{2})[-/ 年\.](\d+)[-/ 月\.](\d{1,2})[-日号/號\.]*'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            str_format = '%Y-%m-%d'
            nums = list(nums[0])
            nums[0] = '{}{}'.format(str(_year)[:2], nums[0])
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # ------------------------------
    #  特殊处理
    # 日月 年 20 11月, 2018
    if not ir_urltime:
        re_msg = '(\d+)[-/ 日号號\.](\d+)[-月,/ \.][, ]*(\d{4})[-/ 年\.]*'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%d-%m-%Y'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # ------------------------
    # 缺少天 2019年05月 19年05月
    if not ir_urltime:
        re_msg = '(\d{4})[-/ 年\.](\d{1,2})[-/ 月號\.]*'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%Y-%m'
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # ------------------------
    # 缺少年月日天 15:30
    if not ir_urltime:
        re_msg = '(\d{2}):(\d{2})'
        nums = re.compile(re_msg).findall(result_content)
        if nums:
            nums = list(nums[0])
            str_format = '%H-%M-%Y-%m-%d'
            nums.append(_year)
            nums.append(_mon)
            nums.append(_day)
            ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)

    # 今天
    if not ir_urltime:
        today = re.compile('今[ ]*天').findall(result_content)
        if today:
            ir_urltime = int(mktime((_year, _mon, _day, 0, 0, 0, 0, 0, 0)))

    # 昨天
    if not ir_urltime:
        yesterday = re.compile('昨[ ]*天').findall(result_content)
        if yesterday:
            ir_urltime = int(mktime((_year, _mon, _day - 1, 0, 0, 0, 0, 0, 0)))

    # 前天
    if not ir_urltime:
        before_yesterday = re.compile('前[ ]*天').findall(result_content)
        if before_yesterday:
            ir_urltime = int(mktime((_year, _mon, _day - 2, 0, 0, 0, 0, 0, 0)))

    # 几天前
    if not ir_urltime:
        num = re.compile('(\d+)[天 ]').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon, _day - num, 0, 0, 0, 0, 0, 0)))

    # 几周前
    if not ir_urltime:
        num = re.compile('(\d+)[周週 ]').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon, _day - (num * 7), 0, 0, 0, 0, 0, 0)))

    # 几月前
    if not ir_urltime:
        num = re.compile('(\d+)[月 ]').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon - num, 0, 0, 0, 0, 0, 0, 0)))

    # 几个月前
    if not ir_urltime:
        num = re.compile('(\d+)[ ]*个月前').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon - num, 0, 0, 0, 0, 0, 0, 0)))

    # 几年前
    if not ir_urltime:
        num = re.compile('(\d+)[年 ]').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year - num, 0, 0, 0, 0, 0, 0, 0, 0)))

    # 几小时前
    if not ir_urltime:
        num = re.compile('(\d+)[小 ]+[时時 ]*').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon, _day, _hour - num, 0, 0, 0, 0, 0)))

    # 半小时前
    if not ir_urltime:
        semih = re.compile('[半 ]+[小 ]+[时時 ]+[前]*').findall(result_content)
        if semih:
            ir_urltime = int(mktime((_year, _mon, _day, _hour, _min - 30, 0, 0, 0, 0)))

    # 几分钟前
    if not ir_urltime:
        num = re.compile('(\d+)[分 ]+[钟鐘 ]').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon, _day, _hour, _min - num, 0, 0, 0, 0)))

    # 几秒前
    if not ir_urltime:
        num = re.compile('(\d+)[秒 ]*').findall(result_content)
        if num:
            num = int(num[0])
            ir_urltime = int(mktime((_year, _mon, _day, _hour, _min, _sec - num, 0, 0, 0)))

    # 大范围匹配
    # 只有年
    # if not ir_urltime:
    #     num = re.compile('.*?(\d+).*?年.*').findall(result_content)
    #
    #     if num:
    #         # 解决 19年 变成2019年
    #         if len(num) != 4:
    #             num = '{}{}'.format(str(_year)[:2], num[0])
    #         else:
    #             num = num[0]
    #         num = int(num)
    #         ir_urltime = int(mktime((int(num), 0, 0, 0, 0, 0, 0, 0, 0)))

    # 英文处理
    # year-2018 month-09 day
    # if 'year' in result_content or 'month' in result_content or 'day' in result_content:
    #     ir_urltime = english_time(result_content)
    #     m = '提取发布时间：（{}）匹配结果为 {}'.format(result_content, ir_urltime)
    #     set_logging(m)
    #     return ir_urltime

    if ir_urltime:
        # m = '提取发布时间：（{}）匹配结果为 {}（{}）'.format(result_content, ir_urltime, strftime("%Y-%m-%d %H:%M:%S", localtime(ir_urltime)))
        # logger.debug(m)
        return ir_urltime
    else:
        m = '提取发布时间：（{}）匹配 失败'.format(result_content)
        logger.error(m)
        return False


def parse_english_time(result_content, _year, _mon, _day, _hour, _min, _sec):
    # 把英文全部转换为小写
    result_content = str(result_content).lower()

    ir_urltime = None
    mon1_li = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    mon2_li = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
               "november", "december"]
    mon3_li = ['十一', '十二', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

    # 时间格式一
    for index, format_mon in enumerate(mon2_li):
        if format_mon in result_content:

            # 时间格式
            # AUGUST 15th, 2019 AT 7:47 PM  st nd rd th
            # AUGUST 15, 2019 AT 7:47 PM
            # AUGUST 15, 2019 AT 07:47 PM
            # AUGUST 15. 2019 AT 07:47 PM
            re_msg = format_mon + ' ([0123]*\d)[\.,snrt][tdh,]* (20[012]\d) at ([0-6]*\d):([0-6]*\d)[ ]*([pa]*[m]*)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                # 判断上午AM 还是下午 PM 如果是下午 把时间加上十二
                hours_format = nums.pop()
                if 'pm' == hours_format:
                    nums[-2] = int(nums[-2]) + 12

                nums.append(index + 1)
                str_format = '%d-%Y-%H-%M-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # August 22nd, 2018 st nd rd th
            # December 10, 2018
            # December 10 2018
            # December-10-2018
            # December.10.2018
            # December ,10.2018
            re_msg = format_mon + '[\. ,-][ ,]*([0123]*\d)[\. ,-snrt][tdh,]*[ ]*(20[012]\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 22nd, March 2018  st nd rd th
            # 19 March 2018
            # 19 March, 2018
            # 19-March-2018
            # 19.March.2018
            # 19 ,March.2018
            re_msg = '([0123]*\d)[\. ,-snrt][tdh,]*[ ,]*' + format_mon + '[-\., ][ ]*(20[012]\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 2017 March 25
            # 2017 March, 25
            # 2017, March 25
            # 2017-March-25
            # 2017.March.25
            # 2017 ,March.25
            re_msg = '(20[012]\d)[\. ,-][ ,]*' + format_mon + '[-\., ][ ]*([0123]*\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%Y-%d-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

    # 时间格式二
    for index, format_mon in enumerate(mon1_li):

        if format_mon in result_content:

            # 时间格式
            # Sep 09th 2018 04:00 pm  st nd rd th
            # Sep 09[,.] 2019 04:00 pm
            # Sep 09[,.] 2019 4:0 pm
            # 9月有两个写法 Sep == Sept
            if format_mon == 'sep':
                re_msg = format_mon + '[t]*[\. ,-][\. ,]*([0123]*\d)[\. ,-snrt][tdh,]*[ ,]*(20[012]\d) (\d{1,2}):(\d{1,2})[ ]*([pa]*[m]*)'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = format_mon + '[\. ,-][\. ,]*([0123]*\d)[\. ,-snrt][tdh,]*[ ,]*(20[012]\d) (\d{1,2}):(\d{1,2})[ ]*([pa]*[m]*)'
                nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                print(nums)
                hours_format = nums.pop()
                if 'pm' == hours_format:
                    nums[-2] = int(nums[-2]) + 12
                nums.append(index + 1)
                str_format = '%d-%Y-%H-%M-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # Sep.09th.2018 st nd rd th
            # Sep.09.2018
            # Sep-09-2018
            # Aug 27 2018
            # Aug 27, 2018
            # Sep ,11 2018
            # 9月有两个写法 Sep == Sept
            if format_mon == 'sep':
                re_msg = format_mon + '[t]*[\. ,-][\. ,]*([0123]*\d)[-\., snrt][tdh,]*[\. ]*(20[012]\d)'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = format_mon + '[\. ,-][ .,]*([0123]*\d)[-\., snrt][tdh,]*[\. ]*(20[012]\d)'
                nums = re.compile(re_msg).findall(result_content)

            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 29st Aug, 2019
            # 29 Aug, 2019
            # 29 Aug 2018
            # 29.Aug.2018
            # 29-Aug-2018
            # 29 ,Aug 2018
            # 9月有两个写法 Sep == Sept
            if format_mon == 'sep':
                re_msg = '([0123]*\d)[\. ,-snrt][tdh,]*[\. ,]*' + format_mon + '[t]*[- \.,][ ]*(20[012]\d)'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = '([0123]*\d)[\. ,-snrt][tdh,]*[\. ,]*' + format_mon + '[- \.,][ ]*(20[012]\d)'
                nums = re.compile(re_msg).findall(result_content)

            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 2017 May 25
            # 2017.May.25
            # 2017-May-25
            # 2017 May, 25
            # 2017 ,May, 25
            # 9月有两个写法 Sep == Sept
            if format_mon == 'sep':
                re_msg = '(20[012]\d)[\. ,-][ ,]*' + format_mon + '[t]*[- \.,][ ]*([0123]*\d)'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = '(20[012]\d)[\. ,-][ ,]*' + format_mon + '[- \.,][ ]*([0123]*\d)'
                nums = re.compile(re_msg).findall(result_content)

            if nums:
                nums = list(nums[0])
                nums.append(index + 1)
                str_format = '%Y-%d-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 19th Oct 19, 9:49pm
            # 19th Oct 19, 9:49am
            # 19th Oct 19, 9:49
            if format_mon == 'sep':
                re_msg = '(\d{1,2})[snrt][tdh][\. ,]*[\. ,]*' + format_mon + '[t]*[- \.,][ ]*(\d{2})[\. ,-][ ,]*(\d{1,2}):(\d{1,2})[ ]*([pa]*[m]*)'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = '(\d{1,2})[snrt][tdh]*[\. ,]*[\. ,]*' + format_mon + '[- \.,][ ]*(\d{2})[\. ,-][ ,]*(\d{1,2}):(\d{1,2})[ ]*([pa]*[m]*)'
                nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                nums[1] = '20' + nums[1]
                hours_format = nums.pop()
                if 'pm' == hours_format:
                    nums[-2] = int(nums[-2]) + 12

                nums.append(index + 1)
                str_format = '%d-%Y-%H-%M-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 19th Oct 18
            # 19th, Oct 18
            # 19th Oct, 18
            if format_mon == 'sep':
                re_msg = '(\d{1,2})[snrt][tdh][\. ,]*[\. ,]*' + format_mon + '[t]*[- \.,][ ]*(\d{2})'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = '(\d{1,2})[snrt][tdh]*[\. ,]*[\. ,]*' + format_mon + '[- \.,][ ]*(\d{2})'
                nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                print(nums)
                nums[1] = '20' + nums[1]
                nums.append(index + 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间解析 放在最后
            # 01 Sep  缺少年
            # 9月有两个写法 Sep == Sept
            if format_mon == 'sep':
                re_msg = '([0123]*\d)[ \.-]+' + format_mon + '[t]*'
                nums = re.compile(re_msg).findall(result_content)
            else:
                re_msg = '([0123]*\d)[ \.-]+' + format_mon + ''
                nums = re.compile(re_msg).findall(result_content)

            if nums:
                nums.append(index + 1)
                nums.append(_year)
                str_format = '%d-%m-%Y'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

    # 时间格式三
    for index, format_mon in enumerate(mon3_li):
        if format_mon in result_content:
            # 时间格式
            # 十二月 21, 2017
            # 十二月 21 2017
            # 十二月-21-2017
            # 十二月.21.2017
            # 十二月, 21 2017
            # 二月, 21 2017
            re_msg = format_mon + '月[\. ,-][ ]*([0123]*\d)[\. ,-][ ]*(20[012]\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                if format_mon == '十一':
                    nums.append(11)
                elif format_mon == '十二':
                    nums.append(12)
                else:
                    nums.append(index - 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 29 四月 2016
            # 29 一月, 2016
            # 29 十一月, 2016
            # 29.四月.2016
            # 29-四月-2016
            re_msg = '([0123]*\d)[- \.]' + format_mon + '月[- \.,][ ]*(20[012]\d)'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                if format_mon == '十一':
                    nums.append(11)
                elif format_mon == '十二':
                    nums.append(12)
                else:
                    nums.append(index - 1)
                str_format = '%d-%Y-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

            # 时间格式
            # 2017年 十二月 21
            # 2017, 十二月 21
            # 2017 十二月[,.] 21
            # 2017 十二月 21
            # 2017十二月21
            re_msg = '(20[012]\d)[年,]*[ ]*' + format_mon + '月[\.,]*[ ]*([0123]*\d)[日]*'
            nums = re.compile(re_msg).findall(result_content)
            if nums:
                nums = list(nums[0])
                if format_mon == '十一':
                    nums.append(11)
                elif format_mon == '十二':
                    nums.append(12)
                else:
                    nums.append(index - 1)
                str_format = '%Y-%d-%m'
                ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
                return ir_urltime

    # 时间格式
    # 8 月 13, 2018
    re_msg = '([01]*[1-9])[ ]*[月 ]+([0123]*\d)[,\.][ ]*(20[012]\d)'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_format = '%m-%d-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 缺少年份
    # 8 月 13, 19
    # 11 月 12, 12
    re_msg = '([01]*[1-9])[ ]*[月 ]+([0123]*\d)[,\.][ ]*([012]\d)'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_year = nums.pop()
        nums.append('20{}'.format(str_year))
        str_format = '%m-%d-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 时间格式
    # 民國107年9月3日(二)下午14:00
    # 民國107年7月5日(五)14:00-16:30
    # 107年7月5日(五)14:00-16:30
    re_msg = '[民]*[国國]*[ ]*(1[01]\d)年([01]*[1-9])月([0-3]*\d)[日号號].*?(\d{1,2}):(\d{1,2})'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_year = int(nums.pop(0)) + 1911
        nums.append(str_year)
        str_format = '%m-%d-%H-%M-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 时间格式
    # 民國107年9月3日
    # 民國107年7月5日
    # 107年7月5日(五)
    re_msg = '[民]*[国國]*[ ]*(1[01]\d)年([01]*[1-9])月([0-3]*\d)[日号號]'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_year = int(nums.pop(0)) + 1911
        nums.append(str_year)
        str_format = '%m-%d-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 时间格式
    # 民國107-9-3 16:40
    # 108-08-01 16:40
    re_msg = '[民]*[国國]*[ ]*(1[01]\d)-([01]*[1-9])-([0-3]*\d) (\d{1,2}):(\d{1,2})'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_year = int(nums.pop(0)) + 1911
        nums.append(str_year)
        str_format = '%m-%d-%H-%M-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 时间格式
    # 民國107-9-3
    # 108-08-01
    re_msg = '[民]*[国國]*[ ]*(1[01]\d)-([01]*[1-9])-([0-3]*\d)'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        nums = list(nums[0])
        str_year = int(nums.pop(0)) + 1911
        nums.append(str_year)
        str_format = '%m-%d-%Y'
        ir_urltime = time_stamp(nums, str_format, re_msg=re_msg)
        return ir_urltime

    # 时间格式
    # 2 days ago
    nums = re.compile('(\d{1,2}) days ago').findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day - n, _hour, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 时间格式
    # Today
    nums = re.compile('today').findall(result_content)
    if nums:
        ir_urltime = int(mktime((_year, _mon, _day, _hour, _min, 0, 0, 0, 0)))
        return ir_urltime

    # Yesterday
    nums = re.compile('yesterday').findall(result_content)
    if nums:
        ir_urltime = int(mktime((_year, _mon, _day - 1, _hour, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 1 week ago
    # 2 weeks ago
    re_msg = '(\d+)[ ]*week[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0]) * 7
        ir_urltime = int(mktime((_year, _mon, _day - n, _hour, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 1 day ago
    # 11 days ago
    re_msg = '(\d+)[ ]*day[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day, _hour - n, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 23 hours ago
    re_msg = '(\d+)[ ]*hour[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day, _hour - n, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 11 Hrs ago
    re_msg = '(\d+)[ ]*hr[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day, _hour - n, _min, 0, 0, 0, 0)))
        return ir_urltime

    # 43 Mins ago
    re_msg = '(\d+)[ ]*min[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day, _hour, _min - n, 0, 0, 0, 0)))
        return ir_urltime

    # 46 minutes ago
    re_msg = '(\d+)[ ]*minute[s]* ago'
    nums = re.compile(re_msg).findall(result_content)
    if nums:
        n = int(nums[0])
        ir_urltime = int(mktime((_year, _mon, _day, _hour, _min - n, 0, 0, 0, 0)))
        return ir_urltime

    return ir_urltime


if __name__ == '__main__':
    while True:
        __r = input('请输入检测的日期：\n')
        _ir_urltime = handle_pub_time(__r, 'parse_english_day_mon_year')
        x = strftime("%Y-%m-%d %H:%M:%S", localtime(_ir_urltime))
        print(_ir_urltime, x)
        print('正常提取')
        _ir_urltime = handle_pub_time(__r, )
        x = strftime("%Y-%m-%d %H:%M:%S", localtime(_ir_urltime))
        print(_ir_urltime, x)
    # result_content = '20 11月, 2018'
    # nums = re.compile('.*?(\d+).*?[-/年 月\.].*?(\d+).*?[-/月日\.].*?(\d+).*?[-日 号年\./]?.*') \
    #     .findall(result_content)
    # print(nums)
