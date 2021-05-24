"""
author:张鑫
date:2021/5/14 17:47
"""
import json
import requests
import re
from tools.headers import headers
url='https://mdskip.taobao.com/core/initItemDetail.htm?isUseInventoryCenter=true&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=true&tryBeforeBuy=false&offlineShop=false&itemId=631725862322&showShopProm=false&isPurchaseMallPage=false&itemGmtModified=1620960741000&isRegionLevel=true&household=false&sellerPreview=false&queryMemberRight=false&addressLevel=3&isForbidBuyItem=false&callback=setMdskip&timestamp=1620985945501&isg=eBSlZK_Pj2kO4yAJBO5aPurza77TgQAb4sPzaNbMiInca6ThOFa0DNCCLLJJ5dtjgtCFveKrbZKR2RLHR3jR2xDDBIwAlLFIExvO.&isg2=BBoasgmYLosIZqInEsZfYoYwa8A8S54lR1XBWiSR3614l7rRDdteNeCmZ2MLRxa9&ref=https%3A%2F%2Fwww.tmall.com%2F'
html = requests.get(url=url,headers=headers,verify=False).content.decode('GBK')
print(html)
# 商品名
name = re.findall('target=\"_blank\">(.*?)</a>',html)
print(f"商品名:{name}")