from docxtpl import DocxTemplate
from datetime import datetime
import time
import datetime
import pandas as pd
import os
zpath = os.getcwd() + '\\'

# zpath=r'D:\【批量工具_效率工作】\批量_使用Python根据excel中数据批量生成word文件(word文件填空)'+'\\'
# current_file_path = zpath + r'\文档生成结果' + str(datetime.date.today())
current_file_path=zpath+'文档生成结果'+str(datetime.date.today())
try:
    os.mkdir(current_file_path)
except:
    pass
# tpl = DocxTemplate(zpath + '咬人猫.docx')

# 这些字段从csv中获取
grade = pd.read_excel(zpath + '咬人猫.xls')

# stid = grade['学号']
name = grade['作者'].str.rstrip()  # str.rstrip()用于去掉换行符
publish_time = grade['发布时间']
count = grade['观看次数'].str.rstrip()
dance_name = grade['舞曲名称'].str.rstrip()

# 遍历成绩单，逐个生成通知书
# 矩阵行数
num = grade.shape[0]
print(num)
for i in range(num):
    tpl = DocxTemplate(zpath + '咬人猫.docx')
    print(i)
    context = {
        "name": name[i],
        "publish_time": publish_time[i],
        "count": count[i],
        "dance_name": dance_name[i],
        "date": time.strftime('%Y-%m-%d', time.localtime(time.time())),
        #      "date": {0:%Y}年{0:%m}月{0:%d}日".format(datetime.now()),
        #       "date":time.strftime('%Y-%m-%d',time.localtime(time.time()))
        #       "date": datetime.now(),
    }
    print(context)
    tpl.render(context)
    tpl.save(current_file_path+r"\{}.docx".format(dance_name[i]))