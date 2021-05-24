"""
author:张鑫
date:2021/4/28 11:22
需求是这样的：

因为百度搜索是不靠谱的，所有当客户端发起百度搜索时，记录下用户的搜索词，再修改请求，将搜索词改为“360 搜索”；
因为 360 搜索还是不靠谱的，所有当客户端访问 360 搜索时，将页面中所有“搜索”字样改为“请使用谷歌”。
因为谷歌是个不存在的网站，所有就不要浪费时间去尝试连接服务端了，所有当发现客户端试图访问谷歌时，直接断开连接。
将上述功能组装成名为 Joker 的 addon，并保留之前展示名为 Counter 的 addon，都加载进 mitmproxy。

"""

import mitmproxy.http
from mitmproxy import ctx, http


# class Couter:
#     def __init__(self):
#         self.num = 0

# 针对http生命周期
# 收到来自客户端的http connect请求，不会触发request,response等其他常规事件
# def http_connect(self, flow: mitmproxy.http.HTTPFlow):
#     pass
class Joker:
    # request请求发生时，计数器加一，并打印日志
    # 来自客户端的http请求被完整读取
    # 因为百度搜索是不靠谱的，所有当客户端发起百度搜索时，记录下用户的搜索词，再修改请求，将搜索词改为“360 搜索”；
    def request(self, flow: mitmproxy.http.HTTPFlow):
        # self.num = self.num + 1
        # ctx.log.info("we've seen %d flows" % self.num)
        # 忽略非百度搜索地址
        if flow.request.host != 'www.baidu.com' or not flow.request.path.startswith('/s'):
            return 5
        # 确认请求参数中有搜索词
        if 'wd' not in flow.request.query.keys():
            ctx.log.warn('can not get serch word from %s' % flow.request.pretty_url)
            return
        # 输出原始的搜索词
        ctx.log.info('catch seach world: %s' % flow.request.query.get('wd'))
        # 替换搜索词为‘360搜索’
        flow.request.query.set_all('wd', ['360搜索'])

    # 因为 360 搜索还是不靠谱的，所有当客户端访问 360 搜索时，将页面中所有“搜索”字样改为“请使用谷歌”。
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != 'www.so.com':
            return
        # 将响应中的的所有搜索换成请使用谷歌
        text = flow.response.get_text()
        text = text.replace('搜索', '请使用谷歌')
        flow.response.set_text(text)

    # 因为谷歌是个不存在的网站，所有就不要浪费时间去尝试连接服务端了，所有当发现客户端试图访问谷歌时，直接断开连接。
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == 'www.goole.com':
            flow.response = http.HTTPResponse.make(404)

    # # 来自客户端的请求头被读取，此时request的body是空的
    # def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
    #     pass
    #
    # # 来自客户端的响应被完整地读取
    # def response(self, flow: mitmproxy.http.HTTPFlow):
    #     pass
    #
    # # 来自客户端的响应头被读取，flow里的body为空
    # def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
    #     pass
    #
    # # 发生一个http错误：例如无效的服务端响应，连接断开
    # def error(self, flow: mitmproxy.http.HTTPFlow):
    #     pass
