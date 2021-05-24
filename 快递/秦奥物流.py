import requests


def query(no):
    url = "http://wx2.qinyue56.cn/winlogicapi-web/v1/wxapi/wxwaybill/getorderbycode2"

    querystring = {"token": "%20"}

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n{\"code\":\"2104273591\"}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'Host': "wx2.qinyue56.cn",
        'Connection': "keep-alive",
        'Origin': "http://wx2.qinyue56.cn",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)",
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Accept': "*/*",
        'Referer': "http://wx2.qinyue56.cn/wx/",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
        'Cookie': "JSESSIONID=48470196A30614D06A24365D5367B92A",
        'cache-control': "no-cache",
        'Postman-Token': "4e96b3d2-f7e9-4604-bed0-90398fcf640d"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    html = response.content.decode()
    print(html)


if __name__ == "__main__":
    # print(query(sys.argv[1]))
    print(query('2104273591'))
