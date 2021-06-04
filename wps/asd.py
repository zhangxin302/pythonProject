"""
author:张鑫
date:2021/5/27 14:53
"""
from docxtpl import DocxTemplate
from datetime import datetime
import time
import datetime
import pandas as pd
import os

# getcwd 获取工作目录的绝对路径
zpath=os.getcwd()+'\\'
# zpath=r'D:\【批量工具_效率工作】\批量_使用Python根据excel中数据批量生成word文件(word文件填空)'+'\\'
current_file_path=zpath+r'\文档生成结果'+str(datetime.date.today())
try:
    os.mkdir(current_file_path)
except:
    pass
# tpl = DocxTemplate(zpath+'模板.docx')

#这些字段从csv中获取
grade = pd.read_excel(zpath+'成绩单.xls')

# stid = grade['学号']
name = grade['姓名'].str.rstrip()  # str.rstrip()用于去掉换行符
yy = grade['英语']
yw = grade['语文']
sx = grade['数学']

# 遍历成绩单，逐个生成通知书
num = grade.shape[0]
print(num)
for i in range(num):
    tpl = DocxTemplate(zpath + '模板.docx')
    print(i)
    context = {
       "name": name[i],
       "yy": yy[i],
       "yw": yw[i],
       "sx": sx[i],
       "date": time.strftime('%Y-%m-%d',time.localtime(time.time())),
    }
    print(context)
    tpl.render(context)
    tpl.save(current_file_path+r"\{}的建大附小家长通知书.docx".format(name[i]))