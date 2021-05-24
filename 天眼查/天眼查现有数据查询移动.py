import pandas as pd
import time

def change_date(name):
    data_lst = []
    ds = pd.read_excel('./'+name)
    for l in ds.values:
        l[2] = time.strftime('%Y-%m-%d',time.localtime(int(str(l[2]))/1000))
        # l[-3] = time.strftime('%Y-%m-%d',time.localtime(int(str(l[-3]))/1000))
        data_lst.append(l)
    ds = pd.DataFrame(data_lst,index=range(1,len(data_lst)+1))
    ds.to_excel('./2'+name)



change_date('联易融POC第二部分被执行人tyc数据_20200707.xlsx')