"""
author:张鑫
date:2021/4/15 11:22
"""
from bs4 import BeautifulSoup
import requests, json

# from tools.headers import headers

session = requests.Session()
session.trust_env = False
headers = {
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76",
              'Referer': 'https://www.youtube.com/'
          }

url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
data = {
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',

}
response = session.post(url=url, headers=headers, data=data)

html = response.json()
print(html)
