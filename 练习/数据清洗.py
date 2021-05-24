import pymongo
import re
import pandas as pd

client = pymongo.MongoClient('192.168.1.158', 27017)
db = client["LawyerArena"]
lawFirm = db.lawyerFirm05
lawyer = db.lawinfo_clear


def tqhz(str1):
    '''
    提取字符串中的汉字
    '''
    try:
        res1 = ''.join(re.findall('[\u4e00-\u9fa5]', str1))
    except Exception:
        res1 = ''
    return res1


def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    if not ustring:
        return ''
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring


def gender(l):
    '''
    处理律师性别
    '''
    l = tqhz(l)
    if l != '男' and l != '女':
        l = '未知'
    return l


def education():
    lawyer.update({'education': {'$regex': '小学'}}, {'$set': {'education': '小学'}}, multi=True)
    lawyer.update({'education': {'$regex': '初中'}}, {'$set': {'education': '初中'}}, multi=True)
    rc1 = re.compile('高中|高级中学')
    lawyer.update({'education': rc1}, {'$set': {'education': '高中'}}, multi=True)
    rc2 = re.compile('专科|大专')
    lawyer.update({'education': rc2}, {'$set': {'education': '专科'}}, multi=True)
    lawyer.update({'education': {'$regex': '中专'}}, {'$set': {'education': '中专'}}, multi=True)
    rc3 = re.compile('中专|中等职业')
    lawyer.update({'education': rc3}, {'$set': {'education': '中职'}}, multi=True)
    lawyer.update({'education': {'$regex': '中技'}}, {'$set': {'education': '中技'}}, multi=True)
    rc4 = re.compile('本科|大本|学士')
    lawyer.update({'$or': [{'education': rc4}, {'education': '大学'}]}, {'$set': {'education': '本科'}}, multi=True)
    rc5 = re.compile('硕士')
    lawyer.update({'$or': [{'education': rc5}, {'education': '研究生'}]}, {'$set': {'education': '硕士'}}, multi=True)
    rc6 = re.compile('博士')
    rc7 = re.compile('博士后')
    lawyer.update({'$and': [{'education': rc6}, {'education': {'$not': rc7}}]}, {'$set': {'education': '博士'}},
                  multi=True)
    lawyer.update({'education': rc7}, {'$set': {'education': '博士后'}}, multi=True)


def no(l):
    try:
        l = re.sub("\D", "", l)
    except Exception:
        pass
    if len(l) != 17:
        l = '未知'
    print(l)


def tsxNo(l):
    l = strQ2B(l).replace('’', '').replace("'", '').replace(",", '')
    if len(re.findall('\d', l)) == 0 or l.find('组代管') >= 0:
        l = '无'
    return l


def phone(p):
    '''
    phone  fax
    '''
    p = p.strip()
    return p


def address(l):
    try:
        l = l.strip('"').strip(':').strip('：').strip().strip('s')
    except Exception:
        return l
    if len(tqhz(l)) == 0 or l.find('notfound') >= 0:
        l = '未知'
    return l


def director(l):
    try:
        l = ''.join(re.findall('[\u4e00-\u9fa5|a-zA-Z]', l))
    except Exception:
        return l
    if l == '':
        l = '未知'
    return l


if __name__ == '__main__':
    rc = re.compile(' 00:00')
    lst = list(lawFirm.find({'est_time': rc}))
    for l in lst:
        est_time = l.get('est_time').split(' ')[0]
        print(est_time)
        lawFirm.update({'_id': l.get('_id')}, {'$set': {'est_time': est_time}})
