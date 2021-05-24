import pymongo
import pandas as pd

client = pymongo.MongoClient('192.168.1.158', 27017)
db = client["test"]
c = db.companyInformation0128

data_lst = []

for l in list(c.find()):
    try:
        data_lst+=l.get('xianzhixiaofeiLisr')
    except Exception:
        print(l.get('_id'))

ds = pd.DataFrame(data_lst,index=range(1,len(data_lst)+1))
ds.to_excel('./限制消费数据20210303.xlsx',encoding='utf_8_sig')
