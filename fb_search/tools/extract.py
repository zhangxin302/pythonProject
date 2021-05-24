""""
提取 内容
"""
import json
import re
import time
from lxml import etree
import hashlib

from jsonpath import jsonpath

from tools.logger_server import logger
from tools.extract_time import handle_pub_time


class Extract:

    def __init__(self):
        self.logger = logger
    @staticmethod
    def parse_post(pagesource,url,keyword):
        """
        提取贴子内容
        :param pagesource:
        :return:
        """
        html=etree.HTML(pagesource)
        divlist=html.xpath('//div[@role="main"]/div[4]/div[1]')[0]
        post_data_li = []
        postdic={}
        # 主贴作者信息
        div2=divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[2]')[0]
        ir_authors=div2.xpath('./div/div[2]//div/div[1]//text()')[0]  # 作者的名字(ir_authors)
        urltime_text="".join(div2.xpath('./div/div[2]//div/div[2]//text()'))
        ir_urltime=handle_pub_time(urltime_text.replace("=",'').split('·')[1].strip())   # 文章发布时间
        ir_sid=re.findall("\d{10,}",url)[0]              # 作者的id(ir_sid)
        ir_content = "".join(divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[3]/div[1]//text()'))
        ir_title = ir_content[:60] if len(ir_content) > 60 else ir_content  # 文章的标题(ir_title)
        # 评论数据（包含主贴转赞评）
        div4=divlist.xpath('.//div[@role="article"]/div/div/div/div/div/div/div/div[4]')[0]
        # 主贴转赞评
        zzp=div4.xpath('./div/div/div[1]/div/div[1]//text()')
        try:
            ir_nresrved1 = re.findall('\d+', zzp[4])[0]  # 文章分享数(ir_nresrved1)
        except:
            ir_nresrved1 = ""
        try:
            ir_nresrved2 = "".join(re.findall('\d+', zzp[2]))
        except:
            ir_nresrved2 = ""  # 文章点赞数(ir_nresrved2)
        try:
            ir_nresrved3 = re.findall('\d+', zzp[3])[0]  # 文章评论数(ir_nresrved3)
        except:
            ir_nresrved3 = ""
        postdic["ir_authors"]=ir_authors
        postdic["ir_keyword"] = keyword
        postdic["ir_urltime"]=ir_urltime
        postdic["ir_urldate"]=int(time.time())
        postdic["ir_url"]=url
        postdic["ir_sid"]=ir_sid
        postdic["ir_content"]=ir_content
        postdic["ir_title"]=ir_title
        postdic["ir_nresrved1"]=ir_nresrved1
        postdic["ir_nresrved2"]=ir_nresrved2
        postdic["ir_nresrved3"]=ir_nresrved3
        postdic["ir_ispost"] =1   # 1为主贴 2为评论
        postdic["ir_area"]=1      #1为国外  2为国内
        postdic["ir_mediatype"] = 8
        postdic["ir_mediasource"] ="facebook"
        postdic["ir_firsturl"] =url
        postdic["ir_md5"] =hashlib.md5(url.encode(encoding='UTF-8')).hexdigest()
        post_data_li.append(postdic)
        print("主贴作者名：",ir_authors,"标题：",ir_title)
        print("内容：", ir_content)
        print("关键字:",keyword,"发布时间", ir_urltime,"主贴url:", url)
        #评论数据
        try:
            commen_list = div4.xpath('.//div/div/div[2]/ul/li')
            for i in commen_list:
                try:
                    commendic = {}
                    comment_authors = i.xpath('./div/div/div[2]//a//span[@dir="auto"]/text()')[0]
                    comment_textdiv = i.xpath('.//div[@role="article"]/div[2]/div')
                    if len(comment_textdiv) < 2:
                        comment_content = "".join(
                            i.xpath('.//div[@role="article"]/div[2]/div[1]//div[@dir="auto"]//text()'))
                        try:
                            img_list = i.xpath('.//div[@role="article"]/div[2]/div[1]//div[@dir="auto"]//img')
                            for img in img_list:
                                comment_content += img.xpath("./@alt")[0]
                        except:
                            pass
                    else:
                        comment_content = ""
                        try:
                            img_list = i.xpath('.//div[@role="article"]/div[2]/div[2]//img')
                            for img in img_list:
                                comment_content += img.xpath("./@src")[0]
                        except:
                            pass
                    comment_url = i.xpath('.//div[@role="article"]/div[2]//li[3]/a/@href')[0]
                    try:
                        comment_urltime = handle_pub_time(
                            i.xpath('//div[@role="article"]/div[2]//li[3]/a//text()')[0].strip())
                    except:
                        print("时间转换错误，提取时间为————————————————————",
                              i.xpath('//div[@role="article"]/div[2]//li[3]/a//text()')[0].strip())
                    commendic["ir_authors"] = comment_authors
                    commendic["ir_urltime"] = comment_urltime
                    commendic["ir_keyword"] = keyword
                    commendic["ir_urldate"] = int(time.time())
                    commendic["ir_url"] = comment_url
                    commendic["ir_sid"] = ""
                    commendic["ir_content"] = comment_content
                    commendic["ir_title"] = ir_content
                    commendic["ir_nresrved1"] = ""
                    commendic["ir_nresrved2"] = ""
                    commendic["ir_nresrved3"] = ""
                    commendic["ir_ispost"] = 2  # 1为主贴 2为评论
                    commendic["ir_area"] = 1  # 1为国外  2为国内
                    commendic["ir_mediatype"] = 8
                    commendic["ir_mediasource"] = "facebook"
                    commendic["ir_firsturl"] = url
                    commendic["ir_md5"] = hashlib.md5(comment_url.encode(encoding='UTF-8')).hexdigest()
                    print("评论作者名：", comment_authors,"评论标题：", ir_content)
                    print("评论内容：", comment_content)
                    print("关键字:",keyword,"评论时间:", comment_urltime,"评论url:", comment_url)
                    post_data_li.append(commendic)
                except:
                    continue
        except:
            print("没有评论数据")











        return post_data_li

    @staticmethod
    def parse_comment_json(json_content, is_test=False):
        """解析评论json"""
        if is_test:
            with open(r'D:\python_demo\spider_demo\fb_demo\fb_selenium\api_file\comment_10157244560781065_1611497862.8389676.json', 'r', encoding='utf-8') as f:
                json_content = json.load(f)

        feedback = json_content.get('data').get('feedback')
        post_id = str(feedback.get('subscription_target_id'))
        edges_li = feedback.get('display_comments').get('edges')
        node_li = [edges.get('node') for edges in edges_li]
        comment_data_li = []
        for node in node_li:
            comment_time_stamp = node.get('created_time')
            comment_url = node.get('url')
            try:
                comment_content = node.get('body_renderer').get('text')
            except:
                comment_content = None

            try:
                comment_content = node.get('body').get('text') if not comment_content else comment_content
            except:
                # '表情或图片等其他内容'
                # https://www.facebook.com/tsaiingwen/posts/10157248056716065?comment_id=2823530344565313
                attachments = node.get('attachments')
                image_li = jsonpath(attachments, '$..image..uri')
                if image_li:
                    comment_content = '\n'.join(image_li).strip()
                else:
                    comment_content = '表情或图片等其他内容'

                pass
            author_msg = node.get('author', dict())
            author_id = author_msg.get('id')
            author_url = author_msg.get('url')
            author_gender = author_msg.get('gender')
            author = author_msg.get('name')
            author = author_msg.get('short_name') if not author else author

            c_feedback = node.get('feedback', dict())
            # 评论数
            try:
                comment_num = c_feedback.get('comment_count').get('total_count')
            except:
                # https://www.facebook.com/wix/posts/10158975324100429?comment_id=10158981876605429&reply_comment_id=10158984295180429
                comment_num = 0
            # 点赞类型
            like_num = c_feedback.get('reactors').get('count')
            try:
                like_edges = c_feedback.get('top_reactions').get('edges')
                emoji_edges = [] if not like_edges else like_edges
            except:
                emoji_edges = []
            emoji_data = dict()
            for emoji_msg in emoji_edges:
                emoji_name = emoji_msg.get('node').get('reaction_type')
                emoji_num = emoji_msg.get('reaction_count')
                emoji_data[emoji_name] = emoji_num

            comment_data = {
                "post_id": post_id,
                "comment_comment_num": comment_num,
                "comment_like_num": like_num,
                "comment_emoji_data": emoji_data,
                "comment_time_stamp": comment_time_stamp,
                "comment_url": comment_url,
                "comment_content": comment_content,
                "author_id": author_id,
                "author_url": author_url,
                "author_gender": author_gender,
                "author": author,
            }
            comment_data_li.append(comment_data)
        print(json.dumps(comment_data_li, ensure_ascii=False))
        return comment_data_li



# if __name__ == '__main__':
#     Extract().parse_comment_json('', is_test=True)