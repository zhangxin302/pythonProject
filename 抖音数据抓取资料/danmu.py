# import requests
#                                            #695082694959130499
# url = '{{wss://webcast3-ws-c-lq.amemv.com/webcast/im/push/?os_api=22&imprp=d4Y1GCoDbxCUS&device_type=OPPO%20R17&live_id=1&manifest_version_code=150401&dpi=240&uuid=866174577028778&cursor=1618388533328_6950925821456632963_1_1&current_network_quality_info=%7B%22http_rtt%22%3A39%2C%22tcp_rtt%22%3A39%2C%22quic_rtt%22%3A39%2C%22downstream_throughput_kbps%22%3A1600%2C%22video_download_speed%22%3A754%2C%22quic_receive_loss_rate%22%3A-1%2C%22quic_send_loss_rate%22%3A-1%2C%22net_effective_connection_type%22%3A7%7D&identity=audience&webcast_sdk_version=1950&webcast_gps_access=1&app_name=aweme&webcast_locale=zh_CN&version_name=15.4.0&ts=1618388533&sid=&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=15409900&channel=wandoujia_1128_0401&_rticket=1618388533887&device_platform=android&iid=4275344646608974&version_code=150400&cdid=8a2b5272-9913-4e2f-945d-7fdbe7ca43ce&rid=6950826949591304996&openudid=24418ce44d005740&device_id=3712386320050727&compress=gzip&resolution=720*1280&room_id=6950826949591304996&os_version=5.1.1&language=zh&device_brand=Android&aid=1128&webcast_language=zh&minor_status=0&mcc_mnc=46007?aid=1128&device_id=3712386320050727&access_key=b12c5620b81026a51e0a4edad127e6fe&fpid=9&sdk_version=3&iid=4275344646608974&pl=0&ne=1&version_code=150400}}/douyin/liveroom/chat?room_id=695082694959130499'
# #url = 'http://192.168.2.107/douyin/liveroom/chat?token=c67840c4457f4565c159253e23260f17&room_id=695082694959130499'
# html = requests.get(url=url).text
# print(html)


import time

# timestamp = items.get('created')  # 时间戳
timestamp = 1618668772  # 时间戳
time_local = time.localtime(int(timestamp))  # 注意：这里的整数不能超过11位数

pub_date = time.strftime("%Y-%m-%d", time_local)
pub_time = time.strftime("%H:%M:%S", time_local)
T = pub_date + ' | ' + pub_time
print(T)

