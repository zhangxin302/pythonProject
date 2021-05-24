import json
import pymongo

def response(flow):
    client = pymongo.MongoClient('localhost', port=27017)  # 连接
    db = client['DouYin_text']  # 创建库
    fs_douyin = db['dongchedi']  # 创建表
    print("************************数据表创建成功！***************************")
    # api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list
    # https://api5-normal-c-hl.amemv.com/aweme/v1/user/follower/list/?user_id=3579617596422716&sec_user_id=MS4wLjABAAAAmCZWzhmaMnJlkbOY3t2HJb2yALmz0ZTAQM6Z684NM4hclVsrnrggKpFL-lKInYWr&max_time=1618365591&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&vcd_count=0&ts=1618365591&cpu_support64=false&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&_rticket=1618365592042&minor_status=0&
    # https://api5-normal-c-hl.amemv.com/aweme/v2/comment/list/?aweme_id=6949141033045314824&cursor=0&count=20&address_book_access=2&gps_access=1&forward_page_type=1&channel_id=0&city=441800&hotsoon_filtered_count=0&hotsoon_has_more=0&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAiTiVZ9_SCfXXp1iuQnHBVawf1C0pRDG9pqY8E3A3_Ig&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618368319&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618368320210&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
    # https://api3-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id=6952424196722933760&cursor=0&count=3&top_ids&item_id=6952405020973354276&insert_ids&channel_id=3&city=441800&follower_count=0&is_familiar=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAlUX2rlhr3FNCQu-cnOp6KwnHTujT1MzYIuxxXcPkq7k&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618976106&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618976107982&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
    # https://api3-normal-c-hl.amemv.com/aweme/v2/comment/list/?aweme_id=6953411950646775077&cursor=20&count=20&insert_ids&address_book_access=1&gps_access=1&forward_page_type=1&channel_id=0&city=441800&hotsoon_filtered_count=0&hotsoon_has_more=0&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAABmqD00tUwB1xO0xr_NvOoHUJN7C7ZnmFWHFvDZOvnA4&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618979472&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618979472964&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
    if 'api5-normal-c-hl.amemv.com/aweme/v2/comment/list/' in flow.request.url:

        for data in json.loads(flow.response.text)['comments']:
            user_info = dict()
            user_info['nickname'] = data['user']['nickname']
            user_info['uid'] = data['user']['uid']
            user_info['douyin_id'] = data['user']['short_id']
            # user_info['sec_uid'] = data['sec_uid']
            user_info['text'] = data['text']
            user_info['zan'] = data['digg_count']
            if user_info['douyin_id'] == '0':
                user_info['douyin_id'] = data['user']['unique_id']
                user_info['update_time'] = data['user']['unique_id_modify_time']
            print(user_info)
            fs_douyin.insert(user_info)
        # api3-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id=6952424196722933760&cursor=0&count=3&top_ids&item_id=6952405020973354276&insert_ids&channel_id=3&city=441800&follower_count=0&is_familiar=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAAlUX2rlhr3FNCQu-cnOp6KwnHTujT1MzYIuxxXcPkq7k&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618976106&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618976107982&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
    elif 'api5-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id' in flow.request.url:
        for data in json.loads(flow.response.text)['comments']:
            user_info = dict()
            user_info['nickname'] = data['user']['nickname']
            user_info['uid'] = data['user']['uid']
            user_info['douyin_id'] = data['user']['short_id']
            # user_info['sec_uid'] = data['sec_uid']
            user_info['text'] = data['text']
            user_info['zan'] = data['digg_count']
            if user_info['douyin_id'] == '0':
                user_info['douyin_id'] = data['user']['unique_id']
                user_info['update_time'] = data['user']['unique_id_modify_time']
            print(user_info)
            fs_douyin.insert(user_info)
    # api3-normal-c-hl.amemv.com/aweme/v2/comment/list/?aweme_id=6953411950646775077&cursor=40&count=20&insert_ids&address_book_access=1&gps_access=1&forward_page_type=1&channel_id=0&city=441800&hotsoon_filtered_count=0&hotsoon_has_more=0&follower_count=0&is_familiar=0&page_source=0&user_avatar_shrink=64_64&aweme_author=MS4wLjABAAAABmqD00tUwB1xO0xr_NvOoHUJN7C7ZnmFWHFvDZOvnA4&item_type=0&os_api=22&device_type=OPPO+R17&ssmix=a&manifest_version_code=150401&dpi=240&uuid=866174577028778&app_name=aweme&version_name=15.4.0&ts=1618979756&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618979757438&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&openudid=24418ce44d005740&device_id=3712386320050727&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&minor_status=0&mcc_mnc=46007
    elif 'api3-normal-c-hl.amemv.com/aweme/v2/comment/list/' in flow.request.url:

        for data in json.loads(flow.response.text)['comments']:
            user_info = dict()
            user_info['nickname'] = data['user']['nickname']
            user_info['uid'] = data['user']['uid']
            user_info['douyin_id'] = data['user']['short_id']
            # user_info['sec_uid'] = data['sec_uid']
            user_info['text'] = data['text']
            user_info['zan'] = data['digg_count']
            if user_info['douyin_id'] == '0':
                user_info['douyin_id'] = data['user']['unique_id']
                user_info['update_time'] = data['user']['unique_id_modify_time']
            print(user_info)
            fs_douyin.insert(user_info)

    elif 'api3-normal-c-hl.amemv.com/aweme/v1/comment/list/reply/?comment_id' in flow.request.url:
        for data in json.loads(flow.response.text)['comments']:
            user_info = dict()
            user_info['nickname'] = data['user']['nickname']
            user_info['uid'] = data['user']['uid']
            user_info['douyin_id'] = data['user']['short_id']
            # user_info['sec_uid'] = data['sec_uid']
            user_info['text'] = data['text']
            user_info['zan'] = data['digg_count']
            if user_info['douyin_id'] == '0':
                user_info['douyin_id'] = data['user']['unique_id']
                user_info['update_time'] = data['user']['unique_id_modify_time']
            print(user_info)
            fs_douyin.insert(user_info)
