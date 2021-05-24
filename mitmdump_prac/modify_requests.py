"""
author:张鑫
date:2021/4/28 10:07
"""
import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.number = 0
    def request(self,flow:mitmproxy.http.HTTPFlow):
        # 忽略非百度搜索地址
        if flow.request.host!='www.baidu.com' and not flow.request.path.startswith('/s'):
            return 5
        # 确认请求参数中有搜索词
        if 'wb' not in flow.request.query.keys():
            ctx.log.warn('can not find key word %s'% flow.request.pretty_url)
            return



