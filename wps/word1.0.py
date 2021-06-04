from docxtpl import DocxTemplate
from datetime import datetime
import time
import datetime
import pandas as pd
import os

# getcwd 获取工作目录的绝对路径
zpath = os.getcwd() + '\\'
# zpath=r'D:\【批量工具_效率工作】\批量_使用Python根据excel中数据批量生成word文件(word文件填空)'+'\\'
current_file_path = zpath + r'\文档生成结果' + str(datetime.date.today())
try:
    os.mkdir(current_file_path)
except:
    pass
# tpl = DocxTemplate(zpath+'模板.docx')

# 这些字段从csv中获取
grade = pd.read_excel(zpath + '东南亚数据0601(1).xls')

quyu = grade['区域']
meiti = grade['媒体名称'].str.rstrip()  # str.rstrip()用于去掉换行符
shijian = grade['发布时间']
biaoti = grade['标题']
text = grade['文章']
guojia = grade['国家']

# 遍历成绩单，逐个生成通知书
num = grade.shape[0]
print(num)
k = 1
for i in range(num):
    tpl = DocxTemplate(zpath + '模板.docx')
    print(i)
    context = {
        "biaoti": biaoti[i],
        "meiti": meiti[i],
        "shijian": shijian[i],
        "guojia": guojia[i],
        "text": text[i],
    }
    print(context)
    tpl.render(context)
    tpl.save(current_file_path + r"\{}.docx".format(biaoti[i]))
    #  + biaoti[i],shijian[i]
    k += 1
