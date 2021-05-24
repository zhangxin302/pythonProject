import pymongo
import pandas as pd
import time
import re

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client["test"]
c = db.sxr_info
def get_dic(lst):
    dic = {}
    tt_lst = ['xx','areaName','businessentity','cardNum','caseCode','courtName','disruptTypeName','duty','gistId','gistUnit','hexFingerprint','inactive','iname','lastModifiedDate','performance','publishDate','regDate','updateDate']
    dic[tt_lst[1]] = lst[1]
    dic[tt_lst[2]] = lst[2]
    dic[tt_lst[3]] = lst[3]
    dic[tt_lst[4]] = lst[4]
    dic[tt_lst[5]] = lst[5]
    dic[tt_lst[6]] = lst[6]
    dic[tt_lst[7]] = lst[7]
    dic[tt_lst[8]] = lst[8]
    dic[tt_lst[9]] = lst[9]
    dic[tt_lst[10]] = lst[10]
    dic[tt_lst[11]] = lst[11]
    dic[tt_lst[12]] = lst[12]
    dic[tt_lst[13]] = lst[13]
    dic[tt_lst[14]] = lst[14]
    dic[tt_lst[15]] = lst[15]
    dic[tt_lst[16]] = lst[16]
    dic[tt_lst[17]] = lst[17]
    return dic

def luru():
    '''
    录入抓取数据
    :return:
    '''
    ds = pd.read_excel('./联易融POC公司第二部分失信人zq数据_20200707.xlsx')
    for l in ds.values:
        data = get_dic(l)
        print(data)
        c.insert(data)

def find():
    ds = pd.read_excel('./联易融POC第二部分失信人tyc数据_20200707.xlsx')
    data_lst = []
    for l in ds.values:
        cn = re.sub('（|\(','[\(|（]',l[5])
        cn = re.sub('\)|）','[\)|）]',cn)
        pn = re.sub('（|\(','[\(|（]',l[-13])
        pn = re.sub('（|\(','[\(|（]',pn)
        rc1 = re.compile(cn)
        rc2 = re.compile(pn)
        if len(list(c.find({'iname':rc2,'caseCode':rc1}))) == 0:
            l[-1] = '是'
        else:
            l[-1] = '否'
        data_lst.append(l)
    ds = pd.DataFrame(data_lst,index=range(1,len(data_lst)+1))
    ds.to_excel('./2联易融POC第二部分失信人tyc数据_20200707.xlsx')

find()