"""
author:张鑫
date:2021/4/18 16:12
"""
import requests,json

from tools.headers import headers

url = 'https://ah2.zhangyue.com/zybk/api/detail/index?bid=11290347&pluginVersion=125&pk=ch_feature&zysid=c89ab5434d569bcc9cf71e8e92e34680&usr=i3219068747&rgt=7&p1=YHj%2BiXK2QAoDABKLnHZx1gpD&pc=10&p2=108032&p3=17410069&p4=501669&p5=19&p6=IJIGAAIBABCBHIECCBBD&p7=__621028764144779&p9=0&p12=&p16=LIO-AN00&p21=10203&p22=5.1.1&p25=74101&p26=22&p28=&p29=zye5b814'
response = requests.get(url,headers=headers)
html = response.json()
print(html)