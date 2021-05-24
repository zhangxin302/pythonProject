import random
import time

import requests
from utils.headers import headers_with_ChromeUA

for page in range(1,21):
    time.sleep(random.randint(2,5))
    import requests
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    s = requests.session()
    s.keep_alive = False # 关闭多余连接

    url = f"https://m2.qiushibaike.com/article/list/text?page={page}&count=12"
    s.get(url) # 你需要的网址l.
    response = requests.get(url,headers_with_ChromeUA,verify=False)
    for item in response.json()["items"]:
        print(item)

