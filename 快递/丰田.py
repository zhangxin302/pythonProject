"""
author:张鑫
date:2021/4/22 17:30
"""
import requests
from lxml import etree
import re
url = "http://weixin.915566.com/index_do.asp"

payload = "wuliugongsi=%20http%3A%2F%2Fqintian.915566.com%2Fweixin%2Fydgz.asp&danhao=%200506744-1&undefined="
headers = {
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Upgrade-Insecure-Requests': "1",
    'Origin': "http://weixin.915566.com",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Referer': "http://weixin.915566.com/qintian.asp",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cookie': "ASPSESSIONIDSSTASDAQ=GIBBIIFANFIAFPHCFNCLDMPB; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1619078886; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1619079903",
    'cache-control': "no-cache",
    'Postman-Token': "6d2dce05-f0aa-4ff2-a6db-537d2c79b777"
    }

response = requests.request("POST", url, data=payload, headers=headers)
html_str=response.content.decode('gbk')
de = re.sub('<(.*?)>','',html_str)
print(de)

# time = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", html_str)
# content = html_str
# print(content)
# content = str(html_str).replace("<script >parent.unsubmitx();</script>","").replace("<span style='color:blue;'>","").replace("-","").replace("</span>","").split("<br>")
# print(len(content),content)
# for item in content:
#    print(item)