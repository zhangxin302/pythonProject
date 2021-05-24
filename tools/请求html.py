"""
author:张鑫
date:2021/4/13 17:07
"""


def get_url(url):
    from bs4 import BeautifulSoup
    import requests
    from fake_useragent import UserAgent

    headers = {
        "user-agent": UserAgent().random,

    }

    response = requests.get(url, headers=headers)

    html = response.content.decode()



