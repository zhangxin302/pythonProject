import requests
import redis
def get_keyword_1():
    # 从接口取关键词存入redis数据库
    key1_url = "http://v.chinadata8.com/keyword/info"
    response_1= requests.get(key1_url).json()
    # client_id1 = response_1['jjyk']['client_id']
    keyword=response_1['jjyk']['keyword_list']
    keyword_list = keyword.split(",")
    print(keyword_list)
    for kw1 in keyword_list:
        r.sadd("keyword",kw1)
def get_keyword_2():
    key2_url ="http://v.chinadata8.com/keyword/autocore_info"
    response_2 = requests.get(key2_url).json()
    for value in response_2.values():
        # client_id2 = value["client_id"]
        keyword = value['keyword_list']
        keyword_list = keyword.split(",")
        print(keyword_list)
        # for kw2 in keyword_list:
        #     r.sadd("keyword",kw2)
def get_keyword_3():
    key3_url="http://v.chinadata8.com/keyword/test_inner_autocore_info"
    response_3 = requests.get(key3_url).json()
    # client_id3 = response_3["国内测试"]["client_id"]
    keyword = response_3["国内测试"]['keyword_list']
    keyword_list = keyword.split(",")
    print(keyword_list)
    # for kw3 in keyword_list:
    #     r.sadd("keyword",kw3)
# http://v.chinadata8.com/keyword/test_outer_autocore_info
def get_keyword_4():
    key4_url="http://v.chinadata8.com/keyword/test_outer_autocore_info"
    response_4 = requests.get(key4_url).json()
    for i in response_4:
        keyword=response_4[i]["keyword_list"]
        keyword_list = keyword.split(",")
        print(keyword_list)
        for kw4 in keyword_list:
            r.sadd("keyword",kw4)
if __name__ == '__main__':
    r=redis.StrictRedis(host='localhost', port=6379, db=1)
    # get_keyword_1()
    # print("**********************************************************")
    # get_keyword_2()
    # print("**********************************************************")
    # get_keyword_3()
    # print("**********************************************************")
    # get_keyword_4()
    print(r.scard("keyword"))
