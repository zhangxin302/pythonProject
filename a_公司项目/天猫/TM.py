import datetime
import requests
import re
import time
import pandas as pd
# from openpyxl.workbook import Workbook

# 需要修改的参数位于cfg.py

def set_up(times, url_ori, a, b, cookie):
    # 找到评论接口,构造相应页数的接口
    url_comment_list = []
    for i in range(1, page):
        url_comment_list.append(a + str(i) + b)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Host': 'rate.tmall.com',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': url_ori,
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'TE': 'Trailers'
    }

    spider(times, url_comment_list, headers)


def spider(times, url_2, headers):
    Evaluate = []
    k= 1
    for y in range(len(url_2)):
        # print(len(url_2),y)
        response = requests.get(url_2[y], headers=headers, timeout=30).text
        # print(response)
        # 如果相应为空，则结束循环

        # 评价
        evaluate = re.findall('"rateContent":"(.*?)"', response)
        if evaluate == []:
            break
        # 分类
        kinds = re.findall('"auctionSku":"(.*?)",', response)
        # 评论人
        commenter = re.findall('"displayUserNick":"(.*?)",', response)
        # 评论时间
        date = re.findall('"rateDate":"(.*?)",', response)
        # print(evaluate)
        # # print(len(evaluate))
        # print(kinds)
        # # print(len(kinds))
        # print(commenter)
        # # print(len(commenter))
        # print(date)
        # print(len(date))
        print(k)
        k+=1

        for i in range(len(evaluate)):
            Evaluate.append([evaluate[i], kinds[i], commenter[i], date[i]])
            # 判断时间是否符合要求
            # print(date[i])
            # f = judge_time(date[i])
            # if f == '时间符合':
            # 将每一页的评论以字典的形式添加到列表中
            # Evaluate.append({'商品的种类': kinds[i], '商品的评价': evaluate[i], '评论者': commenter[i], '评论时间': date[i]})
        print('第' + str(y + 1) + '页的评论获取成功')
        # print(Evaluate)
        # 延时，防止检测
        time.sleep(10)
        df = pd.DataFrame(Evaluate, columns=['评价', '分类', '评论人', '评论时间'])
        df.to_excel(f'天猫{url_2[y][44:60]}.xlsx', index=False)
    print('一共获取了' + str(len(Evaluate)) + '评论')

    # print(Evaluate)


def judge_time(t):
    if (datetime.datetime.now() - datetime.timedelta(weeks=28)).strftime("%Y-%m-%d %H:%M:%S") < t:
        return '时间符合'


if __name__ == '__main__':
    page = 100
    url_ori_list = [
        'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.852d77661auRVO&id=534612389032&skuId=3739156226695&user_id=2107759029&cat_id=2&is_b=1&rn=5c7dda49cdbe1fc819d8d6c44af8e030',
        'https://detail.tmall.com/item.htm?id=563392434345&ali_refid=a3_430673_1006:1109661758:N:XlO0X82J14/FaMbipJ/KhXkskhM6gLCg:213c47787536178bba4925ec887d29ee&ali_trackid=1_213c47787536178bba4925ec887d29ee&spm=a2e0b.20350158.31919782.1',

    ]
    url_comment_list = [
        'https://rate.tmall.com/list_detail_rate.htm?itemId=534612389032&spuId=1938496010&sellerId=2107759029&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvh9vPvohvU9CkvvvvvjiWPLSOzjtRPsFp0jivPmPvljtjRLcUtjrRn2zZzjlPPFu%2BvpvoEvF2v%2BLhvHoq84GiExRDDaznRvhvCvvvvvm%2BvpvBUvsVviRLvhpG84%2F9nh2ExLVevpvhvvmv9F9Cvvpvvvvv29hvCvvvvvvUvpCWmCz5vva4KWjxsLpZwDKQD7zheutKjrcnI4vODVQEfwLZaBwgnZ43IWkyHdUf8rBlKWVTKo9vQ8oQD40OaokgQacnnCB17bmxfwoXdd9Cvm9vvvvvphvvvvvv9krvpvpgvvmm86Cv2vvvvUUdphvUOQvv9krvpv3Fuvhvmvvv92syH51tkvhvC99vvOCgppvCvvOvUvvvphmVvpvhvvpvv8QCvvyvvjwvZlWvjvm%2BvpvEvvL%2BvDDXvhke9vhvHnM5wx1y7rMNzzCUMHS8zt2NIYAa&needFold=0&_ksTS=1617675040185_1501&callback=jsonp1502',
        'https://rate.tmall.com/list_detail_rate.htm?itemId=563392434345&spuId=1950925891&sellerId=2107759029&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvd9vEvbQvUpCkvvvvvjiWPLSw0jrbPsLwsj1VPmPU6j1PR25plj3RRs5O0jrRPIOCvvpv9hCvi9hvCvvvpZpRvpvhMMGvvv9CvhQmYo%2Bdjwofd3RAVAdhaB4AdX3l8PLt%2Bu0O5C61D70O58TJEcqhl8gL%2Bul1pj7Q%2Bu0Oe369%2FX7reEAKfvDr1EAK5dUf8r1lhq8rejh%2BuvhvmvvvpLeu2EwikvhvC9hvpyP9tb9Cvm9vvhCvvvvvvvvvBBWvvv2bvvCHhQvv9pvvvhZLvvvCfvvvBBWvvvH%2BvvhvC9vhphvvv29CvvpvvhCv&needFold=0&_ksTS=1617760041371_539&callback=jsonp540',

    ]
    cookie = 'lid=%E6%9C%9F%E5%AF%84yy; enc=2DTuGd2XspJNYe5S%2FvmJqSPaGiZnSdFvD%2FYdlpn7nAi%2BbwLAIlYo7R7w33ulGHFpyvayFeP09D%2BdqlsFEsPksA%3D%3D; cna=VzToGMXJ5QcCAd6ABp64op27; xlly_s=1; t=790261b8e38a8909ef9f4144b04f434a; tracknick=%5Cu671F%5Cu5BC4yy; lgc=%5Cu671F%5Cu5BC4yy; _tb_token_=fefbee84b76e4; cookie2=1e4d63b7e5e8aec96ac8770715a8a3fe; dnk=%5Cu671F%5Cu5BC4yy; x5sec=7b22726174656d616e616765723b32223a223361333365626531353462623234636633373038343666613537633562633638434c485273494d47454a32733161756a776353633777456f416a447475662f632f762f2f2f2f3842227d; uc1=existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&cookie14=Uoe1hdZmbJDnBA%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0; uc3=vt3=F8dCuwubNjaVpOpS5X8%3D&id2=UU6nQr8AGnu1Bw%3D%3D&nk2=pZjxEMvW&lg2=V32FPkk%2Fw0dUvg%3D%3D; _l_g_=Ug%3D%3D; uc4=nk4=0%40py%2FEp9WWJXE05qi%2FOJ6Ak6A%3D&id4=0%40U2xqJtbweV%2FOJrdqeH6LehFLx3G1; unb=2663699306; cookie1=VANCxijFzDaK%2BjoAZfUfA%2F5FEcPQWLbn6I%2BxYcqiNpM%3D; login=true; cookie17=UU6nQr8AGnu1Bw%3D%3D; _nk_=%5Cu671F%5Cu5BC4yy; sgcookie=E100%2Bb06k7tkD%2BLXFvHpjh3tr2igX27sYDabqbO1kgEGKWq%2FOj%2BsCvdtbtKaUATKr3E9jY8ZEGt2xBAA7TqAZL9aug%3D%3D; sg=y60; csg=4d7bb58b; tfstk=cZ7lB7Yrgg-7UX-cfzT5NRFp5rQlZIGyFhKVuwVbB5odGK_ViImqb-UKFKWlJD1..; l=eBxuebHujJxbWJLfBO5CPurza77toIRb8rVzaNbMiInca6hP_Umo_NCQv7gw8dtjgtCfbetzhg8L7RFy8QzdgZqhuJ1REpZZ4xvO.; isg=BPX1qc-y-djKYR1s_V6RFFVTBHGvcqmEX9FWgXcaO2yUThRAP8MAVCOImBL4CME8'
    for i in range(len(url_ori_list)):
        url_ori = url_ori_list[i]
        url_comment_split = url_comment_list[i].split('currentPage=1')
        url_before_curPage = url_comment_split[0] + 'currentPage='
        url_after_curPage = url_comment_split[1]
        set_up(i, url_ori, url_before_curPage, url_after_curPage, cookie)
