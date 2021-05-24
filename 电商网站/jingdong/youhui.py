"""
author:张鑫
date:2021/5/14 15:11
"""
import json
import requests
import re
# headers={
#     'cookie':'__jdu=426969531; areaId=1; PCSYCityID=CN_110000_110100_110108; shshshfpa=366d928d-06eb-5943-f480-5971e14c067d-1620456201; _pst=jd_54ab10fc8fcab; unick=鲲鹏最好吃; pin=jd_54ab10fc8fcab; _tp=XscganD4lk1hnS3moiR7UR4jyAhrRF+oOj7k2q0kXO0=; shshshfpb=jC/fD H82b1BaOWcRqggnrQ==; ipLoc-djd=1-2800-55811-0; unpl=V2_ZzNtbUAEQBJxXE5UK0wLB2IGRggRVEcUcQFCU3tOWgNjUxMJclRCFnUUR1BnGV0UZwQZXUpcQxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH4aWw1gCxZfQmdzEkU4dlB8HVQDYDMTbUNnAUEpCEBTcxlfSGIAFVVFX0cXdThHZHg=; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3b265e91adf344edb25058561f775a0e|1620634752933; shshshfp=2afb5484dd8026d401443a6c2ce0deb5; logintype=qq; npin=jd_54ab10fc8fcab; user-key=b9b59a8d-b0a4-4b8c-9ac3-fc01200c1a79; mba_muid=426969531; __jda=122270672.426969531.1620456200.1620973124.1620976018.6; __jdc=122270672; 3AB9D23F7A4B3C9B=BAQ5TRHBUONJFWMSDO25VNTZB6FEYJWY2A5ODQE63HHSQNP26H64VTTTUAX623AIW24GQCXMLMKNCXUBZVEONYZRLQ; shshshsID=ebf7d3e6640244a66d51f9eb86cfc5f4_2_1620976093799; __jdb=122270672.2.426969531|6.1620976018',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
# }
from tools.headers import headers

url = 'https://item.jd.com/100008483105.html'

html = requests.get(url=url,headers=headers,verify=False).content.decode()
print(html)