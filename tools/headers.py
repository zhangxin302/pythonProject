"""
author:张鑫
date:2021/4/9 11:55
"""
import random

from fake_useragent import UserAgent

cookie = [
    '_ga=GA1.2.435005338.1617938518; MONITOR_WEB_ID=1b749639-d3df-42de-8e5e-8c6ba9724457; _gid=GA1.2.660503105.1619424734; _gat=1; _tea_utm_cache_2608={"utm_source":"gold_browser_extension"}',
    'HMACCOUNT_BFESS=0FB5EA19987932D3; BCLID_BFESS=8208666407574368787; BDSFRCVID_BFESS=Y_KOJeC62xCapwveqGRqDujpRgKKbX7TH6aoKfXFfMZuzNIw5U9dEG0PVM8g0KubuNzsogKK0eOTHvIF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbCeoDI-JC83fP36qROh24FtK2T22-usyGOi2hcH0KLKJhOpKbJ-bJ_10lQR-4TjLDviabo9JMb1MRjvyPjiQ4KIWloEWfcfJGI80p5TtUJ48DnTDMRh-RLN2lbyKMnitIT9-pnKWlQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHj53jH-83e',
    '_ga=GA1.2.435005338.1617938518; MONITOR_WEB_ID=1b749639-d3df-42de-8e5e-8c6ba9724457; _gid=GA1.2.660503105.1619424734; _tea_utm_cache_2608={"utm_source":"gold_browser_extension"}; _gat=1',
    '__cfduid=d9391bef5871c7e4fda7d8097e9d192e51618887550; lng=zh; AProfile=0EDkOAeCihJReBh4TaO/BcAe3QAxAQAkCAAAtChBIFwsR90=; _ga=GA1.2.264113929.1618887583; _fbp=fb.1.1618887584538.1489414263; _hjid=048b3404-ac23-49ed-bacd-d3d8a5dd4817; sbjs_migrations=1418474375998=1; sbjs_current_add=fd=2021-04-26 14:53:35|||ep=https://www.pressreader.com/|||rf=(none); sbjs_first_add=fd=2021-04-26 14:53:35|||ep=https://www.pressreader.com/|||rf=(none); sbjs_first=typ=typein|||src=(direct)|||mdm=(none)|||cmp=(none)|||cnt=(none)|||trm=(none); sbjs_current=typ=typein|||src=(direct)|||mdm=(none)|||cmp=(none)|||cnt=(none)|||trm=(none); _gid=GA1.2.4401332.1619420030; sbjs_udata=vst=2|||uip=(none)|||uag=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46; sbjs_session=pgs=1|||cpg=https://www.pressreader.com/search?query=China%20poverty&newspapers=1109%2C1138%2C1731%2C8500%2C8601%2C8602%2C8606%2C8810%2C9106%2C9377%2C9470%2C9ggr%2C9ggs%2C9gcz%2C9kkf%2C9f70%2C9hpn%2C9d37%2C9i70%2C9hw6%2C9f06%2C9a19%2C9ggx%2C9ggh%2C9ggg%2C9ggj%2C9gc1%2C9gmx%2C9waq%2C9ych%2C9vw5%2C9ygr%2C9xzj%2Csghh%2Csghf%2Csghg%2C9wso%2C9wae%2C9vug%2C9ig3%2C9vw4%2C9yn2%2C9wad&languages=en&in=ALL&date=Anytime&hideSimilar=0&type=2&state=2',
    '_ga=GA1.2.884352555.1619425886; _gid=GA1.2.691285321.1619425886; _gat_gtag_UA_141228404_1=1',
    '_ga=GA1.2.884352555.1619425886; _gid=GA1.2.691285321.1619425886',
    '_ga=GA1.2.884352555.1619425886; _gid=GA1.2.691285321.1619425886; Hm_lvt_54b918eee37cb8a7045f0fd0f0b24395=1619426075; Hm_lpvt_54b918eee37cb8a7045f0fd0f0b24395=1619426309',
]
cookie = random.choices(cookie)
headers = {
    "user-agent": UserAgent().random,
    'Connection': 'close',

}
