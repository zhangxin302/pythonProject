"""
author:张鑫
date:2021/4/28 15:24
"""
import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num += 1
        ctx.log.info('we have seen %s flows' % self.num)
