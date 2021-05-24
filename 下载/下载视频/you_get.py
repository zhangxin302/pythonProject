"""
author:张鑫
date:2021/5/14 11:03
目录：D:\下载
变形金刚5：https://v.qq.com/x/cover/qee75hz1x7m6n3s.html?report
_recomm_player=ptag%3Dv_qq_com%7Crtype%3Dcid%7CalgId%3D5410%7CbucketId%3DEXP%3ARERANK%3D10156%7CNRBE%3D10156%7CPROFILE%3D1
0156%7CSELECTOR%3D10156%7CENGINE%3D10156%7CRANK%3D10156%7CINDEX%3D10156%7CACCESS%3D10156%7Creason%3D%7CreasonType%3D%7Ccid
%3Dqee75hz1x7m6n3s%7Cvid%3D%7Cpid%3D%7Cmodule%3D410%7CpageType%3DfilmIndex%7Cseqnum%3D4108485893_1620961930.443991_50%7Cvi
deo_rec_report%3Dis_insert%3A%7Cinsert_type%3A%7Cload_type%3A%7Cflow_rule_id%3A156%7Ca_exp_id%3ARERANK-10156%23NRBE-10156%
23PROFILE-10156%23SELECTOR-10156%23ENGINE-10156%23RANK-10156%23INDEX-10156%23ACCESS-10156%7Ca_src_key%3A100137%7Ca_seqnum%
3A4108485893_1620961930.443991_50%7Ca_area_code%3A%7Ca_scene_type%3A2%7Creturn_item_num%3A97%7Ce_module_type%3A410%7C%7Ca_
module_id%3A20190524007742%7Ce_item_id%3Aqee75hz1x7m6n3s%7Ce_item_type%3A13%7Ce_item_mixid%3A%7C%7Ca_alg_id%3A5410%7Ca_alg
_type%3A0%7Citem_score%3A0.855366
"""
'''
you-get是非常强大的下载工具
安装方法–在cmd命令行中： pip3 install you-get
在python中的使用方法：
1.模拟命令行的方法使用
You-get -o 目录 -O 视频名称（不需要视频格式） url
import os
str = "you-get -o D://video// -O a "+url
os.system(str)

2.调用you-get的any-downlaod函数
from you_get import common
common.any_download(url=url, stream_id=‘mp4’, info_only=False, output_dir=r’D://video//’, merge=True)
3.视频清晰度问题
输入you-get -i +视频链接可以显示可选的清晰度
you-get --format=mp4sd 视频连接可以下载选定的清晰度

'''
