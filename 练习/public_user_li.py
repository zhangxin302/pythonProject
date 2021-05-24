def get_user_name():
    public_user_li = [
        {"user_id": "wix", "author": "wix"},
        {"user_id": "tsaiingwen", "author": "蔡英文 Tsai Ing-wen"},
        {"user_id": "BBCChinese", "author": "BBC中文网"},
        {"user_id": "voachina", "author": "美国之音中文网"},
        {"user_id": "RFAChinese", "author": "Radio Free Asia Chinese 自由亚洲电台普通话"},
        {"user_id": "ntdtv.com.tw", "author": "新唐人亞太電視台"},
        {"user_id": "sfdjy", "author": "大紀元&新唐人－舊金山（EpochTimes & NTDTV - San Francisco）"},
        {"user_id": "DuoWeiNews", "author": "多維新聞"},
        {"user_id": "TaipeiMOCA", "author": "台北當代藝術館 MOCA Taipei"},
        {"user_id": "aboluowang", "author": "阿波罗网"},
        {"user_id": "kwongwah.my", "author": "光华日报    Kwong Wah Yit Poh"},
        {"user_id": "nanyang.nysp", "author": "南洋商报 Nanyang Siang Pau"},
        {"user_id": "ChinaPressCP", "author": "China Press (中國報)"},
        {"user_id": "zaobaosg", "author": "Lianhe Zaobao 联合早报"},
        {"user_id": "ASIACHINESEMEDIA", "author": "人民邮报 - The Rakyat Post Chinese Version"},
        {"user_id": "ChineseWSJ", "author": "华尔街日报中文版 The Wall Street Journal"},
        {"user_id": "financialtimeschinese", "author": "FTChinese.com - FT中文网"},
        {"user_id": "chinadigitaltimeschinese", "author": "中国数字时代 China Digital Times"},
        {"user_id": "sinausnews", "author": "北美新浪"},
        {"user_id": "sputniknews.cn", "author": "俄羅斯衛星通訊社"},
        {"user_id": "hbrtaiwan", "author": "哈佛商業評論"},
        {"user_id": "dw.chinese", "author": "DW 中文 - 德国之声"},
        {"user_id": "BastilleAustralia", "author": "巴士的澳洲"},
        {"user_id": "nytimeschinese", "author": "The New York Times Chinese -Simplified     纽约时报中文网"},
        {"user_id": "worldjournalnews", "author": "World Journal 世界日報"},
        {"user_id": "OrientalDailyNewsMalaysia", "author": "馬來西亞東方日報 Oriental Daily News Malaysia"},
        {"user_id": "OrientalCrimeMalaysia", "author": "東方直擊Oriental Crime"},
        {"user_id": "mkinicn", "author": "当今大马 (Malaysiakini Chinese Version)"},
        {"user_id": "stlchinese", "author": "聖路易時報 St. Louis Chinese American News"},
        {"user_id": "Studying.Australia", "author": "AMET Australia 艾梅特澳洲留學澳洲移民"},
        {"user_id": "malaysiaorganisation", "author": "忠政快讯"},
        {"user_id": "TaipeiZoo", "author": "Taipei Zoo 臺北市立動物園"},
        {"user_id": "okwork", "author": "台北人力銀行"},
        {"user_id": "police.taipei", "author": "臺北波麗士"},
        {"user_id": "2010TaipeiFlora", "author": "花博公園"},
        {"user_id": "TaipeiMOCA", "author": "台北當代藝術館 MOCA Taipei"},
        {"user_id": "taipeifineartsmuseum", "author": "臺北市立美術館 Taipei Fine Arts Museum"},
        {"user_id": "TPEgovEDU", "author": "臺北市教育局"},
        {"user_id": "taipeilabornews", "author": "勞動臺北"},
        #{"user_id": "台北植物園-Taipei-Botanical-Garden-321991691227057", "author": "台北植物園 Taipei Botanical Garden"},
        {"user_id": "ecotcpd", "author": "反詐騙小金剛"},
        {"user_id": "tpctax", "author": "北市稅處"},
        {"user_id": "land.taipei", "author": "臺北地政"},
        {"user_id": "nit.taipei", "author": "臺北市新移民會館"},
        {"user_id": "myntpc", "author": "我的新北市"},
        {"user_id": "ntpcartcenter", "author": "新北市藝文中心"},
        {"user_id": "ntctour", "author": "新北旅客"},
        {"user_id": "artzone435", "author": "板橋435藝文特區"},
        {"user_id": "ilaborntpc", "author": "新北勞動雲"},
        {"user_id": "pinglin.tea.m", "author": "新北市坪林茶業博物館"},
        {"user_id": "NewTaipeiCityLibrary", "author": "新北市立圖書館"},
        {"user_id": "13hangmuseum", "author": "新北市立十三行博物館"},
        {"user_id": "tpc58801", "author": "新北市政府動物保護防疫處"},
        {"user_id": "tamsuihistoricalmuseum", "author": "淡水古蹟博物館"},
        {"user_id": "social.klcg", "author": "基隆市政府社會處"},
        {"user_id": "klgpolice", "author": "基隆警馨雲"},
        {"user_id": "ilovekeelung", "author": "早安基隆  基隆市政府產業發展處"},
        {"user_id": "keelungpubliclibrary", "author": "基隆市公共圖書館Keelung City Public Library"},
        {"user_id": "KLCCABTW", "author": "基隆市文化局"},
        {"user_id": "KLCS.gov.tw", "author": "關務署基隆關"},
        {"user_id": "kltbtax", "author": "基隆市稅務局"},
        {"user_id": "chiayitax", "author": "嘉市稅精靈"},
        {"user_id": "at.tainan", "author": "我在台南"},
        {"user_id": "tnpd.gov.tw", "author": "臺南市政府警察局"},
        {"user_id": "tndais", "author": "臺南區農業改良場"},
        {"user_id": "tntb100", "author": "臺南市政府財政稅務局 - 稅樂園．好康報"},
        {"user_id": "tnpdcic", "author": "臺南市政府警察局刑事警察大隊"},
        #{"user_id": "南市圖-303388935849", "author": "南市圖"},
        {"user_id": "taichungresort", "author": "大玩台中-臺中觀光旅遊局"},
        {"user_id": "tcpbcid", "author": "臺中市刑大"},
        {"user_id": "tdares", "author": "臺中區農業改良場"},
        {"user_id": "taichung.police", "author": "臺中市政府警察局"},
        {"user_id": "hepingdist", "author": "臺中市和平區公所"},
        #{"user_id": "臺中市大安區公所-506754166074824", "author": "臺中市大安區公所"},
        {"user_id": "southtaichung", "author": "臺中市南區區公所"},
        {"user_id": "tccfd800", "author": "臺中市政府消防局第八救災救護大隊"},
        {"user_id": "xinshe103", "author": "臺中市新社區公所"},
        #{"user_id": "臺中市少年警察隊-123267641092779", "author": "臺中市少年警察隊"},
        {"user_id": "TCCcustoms", "author": "臺中關服務小精靈"},
        {"user_id": "civilQ", "author": "臺中市政府民政局"},
        {"user_id": "hsinchunew", "author": "新竹市 新鮮事"},
        {"user_id": "www.hcct.gov.tw", "author": "新竹市稅務局-稅務風兒"},
        {"user_id": "hccp.gov", "author": "新竹市警察局"},
        {"user_id": "HCCPCIB", "author": "新竹市警察局刑事警察大隊"},
        {"user_id": "tytax1", "author": "桃園市政府地方稅務局"},
        {"user_id": "traveltaoyuan", "author": "樂遊桃園"},
        {"user_id": "KaohsiungPolice", "author": "高雄市政府警察局"},
        {"user_id": "ntak.gov", "author": "高雄國稅局-稅務e達人"},
        {"user_id": "bravo.Kaohsiung", "author": "高雄一百"},
        {"user_id": "kaohsiungmuseum", "author": "高雄市立美術館"},
       # {"user_id": "高雄市稅捐處-稅稅戀-189616624426618", "author": "高雄市稅捐處-稅稅戀"},
        {"user_id": "coamdais", "author": "苗栗區農業改良場"},
		{"user_id": "YunlinCountyGov", "author": "雲林縣政府"},
        {"user_id": "yunlintax", "author": "雲林縣稅務局"},
        {"user_id": "ipingtung", "author": "i屏東～愛屏東"},
        {"user_id": "HSWEC", "author": "屏東國立海洋生物博物館"},
        {"user_id": "likeYS.TW", "author": "高屏澎東分署 / YS青年職涯發展中心"},
        {"user_id": "pttbgov", "author": "屏東縣政府財稅局"},
        {"user_id": "ptcriminal", "author": "屏東縣政府警察局刑警大隊"},
        {"user_id": "PingDongPolice", "author": "屏東縣政府警察局"},
        {"user_id": "taitung.gov", "author": "台東不一樣"},
        {"user_id": "NTCT.EDU.TW", "author": "南投縣政府教育處"},
        {"user_id": "ntepb", "author": "南投縣政府環境保護局"},
        {"user_id": "TWCYPD", "author": "嘉義縣警察局"},
        {"user_id": "kinmentour", "author": "樂遊金門"},
        {"user_id": "ChangTax", "author": "彰化縣地方稅務局"},
        {"user_id": "hlgov", "author": "花蓮縣政府"},
        {"user_id": "hltb.gov.tw", "author": "花蓮縣地方稅務局"},
        {"user_id": "chutax", "author": "新竹縣政府稅務局"},
        {"user_id": "PenghuGov", "author": "澎湖縣政府"},
        {"user_id": "DoctorKoWJ", "author": "柯文哲"},
        #{"user_id": "drtingsc", "author": "丁守中"},
        {"user_id": "YaoTurningTaipei", "author": "姚文智"},
        {"user_id": "gogogoeball", "author": "蘇貞昌"},
        #{"user_id": "houyou.yi", "author": "Hou You Yi"},
        {"user_id": "uchange.keelung", "author": "林右昌UChange"},
        {"user_id": "openKeelung", "author": "謝立功"},
        {"user_id": "chenoupo", "author": "陳歐珀"},
        {"user_id": "LinZiMiaopage", "author": "林姿妙"},
        {"user_id": "happiness.miaoli", "author": "徐耀昌加油讚"},
        {"user_id": "tingchen0104", "author": "徐定禎"},
        #{"user_id": "黃玉燕-智那蓮心-429165180608294", "author": "黃玉燕 智那蓮心"},
        {"user_id": "UprightYung", "author": "李進勇"},
        {"user_id": "yunlin.lishan", "author": "張麗善"},
        {"user_id": "taiwanweicher", "author": "黃偉哲"},
        {"user_id": "hsiushuang", "author": "黃秀霜"},
        {"user_id": "PospoKao", "author": "高思博 A Po"},
        {"user_id": "pan.menan1", "author": "潘孟安"},
        {"user_id": "ptdrsu", "author": "蘇清泉"},
        {"user_id": "ChaoHaoLiu", "author": "劉櫂豪"},
        {"user_id": "Taitungaprilyao", "author": "饒慶鈴"},
       # {"user_id": "洪國浩-1453579871625806", "author": "洪國浩"},
        {"user_id": "LiFaWeiYuanLinMingQin", "author": "南投縣長‧林明溱"},
        {"user_id": "onlychiayi", "author": "翁章梁 Weng Chang-Liang"},
        {"user_id": "Labour.tw", "author": "吳育仁-勞心勞力"},
        {"user_id": "go333", "author": "蕭淑麗粉絲團"},
       # {"user_id": "劉增應粉絲團-1571724343041507", "author": "劉增應粉絲團"},
       # {"user_id": "陳福海-275539222468954", "author": "陳福海"},
        {"user_id": "KinmenMyLove", "author": "陳玉珍 珍愛金門"},
        {"user_id": "yang.chengwu", "author": "躍動金門-楊鎮浯"},
        {"user_id": "laifengwei", "author": "賴峰偉"},
        {"user_id": "chenkuangfu1025", "author": "陳光復Chen Kuang-fu"},
        {"user_id": "chengwentsan", "author": "鄭文燦"},
        {"user_id": "junglicity", "author": "陳學聖"},
        {"user_id": "linweijo", "author": "立法委員林為洲"},
        {"user_id": "WKYang.HC", "author": "楊文科"},
        #{"user_id": "100002986231743", "author": "陳見賢"},
        {"user_id": "shesinging.tw", "author": "徐欣瑩"},
        {"user_id": "liuhsiaomei1215", "author": "劉曉玫"},
        {"user_id": "forpeople", "author": "林佳龍"},
        {"user_id": "LuShiowYen", "author": "盧秀燕"},
        {"user_id": "MingkuWeiDPP", "author": "魏明谷"},
        {"user_id": "wang.huimei", "author": "王惠美"},
        {"user_id": "HMSloveCH", "author": "洪敏雄"},
       # {"user_id": "100011126163362", "author": "陳宜民"},
        {"user_id": "twherohan", "author": "韓國瑜"},
        {"user_id": "genewu5568", "author": "吳益政－理想城市高雄市"},
        {"user_id": "taiwango0527", "author": "林智堅"},
        {"user_id": "HSU290339", "author": "許明財"},
        {"user_id": "wudunyi2017", "author": "吳敦義 Wu, Den-Yih"},
        {"user_id": "haulb", "author": "郝龍斌"},
        #{"user_id": "yongquanc", "author": "曾永權"},
        {"user_id": "tsaichengyuan", "author": "蔡正元"},
        {"user_id": "kib16259", "author": "李明賢 -阿賢之聲"},
        {"user_id": "lintefu", "author": "林德福"},
       # {"user_id": "100000154021068", "author": "曾文培"},
        #{"user_id": "diorhou", "author": "侯佳齡"},
        #{"user_id": "wonderer8", "author": "黄啟明"},
        {"user_id": "johnnyccchiang", "author": "江啟臣"},
       # {"user_id": "蔣根煌-268742576664777", "author": "蔣根煌"},
        #{"user_id": "100000767670473", "author": "李傅中武"},
        #{"user_id": "100007483273063", "author": "李國勝"},
        {"user_id": "tsangmin11", "author": "林滄敏"},
        {"user_id": "wunrueilin", "author": "林文瑞"},
        #{"user_id": "100002064436517", "author": "呂學樟"},
        #{"user_id": "100004063997902", "author": "沈慶光"},
        {"user_id": "eqmame.tw", "author": "沈智慧"},
        {"user_id": "ptdrsu", "author": "蘇清泉"},
        {"user_id": "zhanghua8382277", "author": "蕭景田"},
        #{"user_id": "徐榛蔚-1765791806973716", "author": "徐榛蔚"},
        {"user_id": "YangChiungYing", "author": "好立委 楊瓊瓔"},
        {"user_id": "chung.siao.ping", "author": "鍾小平"},
        {"user_id": "ashow.tpe", "author": "李彥秀"},
        {"user_id": "seanlien2014", "author": "連勝文"},
        #{"user_id": "立法委員孔文吉-134086613358799", "author": "立法委員孔文吉"},
        #{"user_id": "費鴻泰阿力克司-893657620668012", "author": "費鴻泰（阿力克司）"},
        #{"user_id": "100002444414434", "author": "廖國棟"},
        {"user_id": "LuShiowYen", "author": "盧秀燕"},
        #{"user_id": "賴士葆-1573873889493647", "author": "賴士葆"},
        #{"user_id": "ChienUliw", "author": "簡東明"},
        {"user_id": "mtlo.tw", "author": "羅明才"},
        #{"user_id": "100004700057932", "author": "蔣乃辛"},
        {"user_id": "nantou.go", "author": "立法委員 馬文君"},
        #{"user_id": "許淑華-130771133668155", "author": "許淑華"},
        {"user_id": "wang.huimei", "author": "王惠美"},
        #{"user_id": "100002600612191", "author": "呂玉玲"},
        #{"user_id": "100000526333158", "author": "陳超明"},
        {"user_id": "junglicity", "author": "陳學聖"},
        #{"user_id": "srakacaw", "author": "鄭天財"},
        {"user_id": "linweijo", "author": "立法委員林為洲"},
        {"user_id": "kuanheng99", "author": "顏寬恒"},
        {"user_id": "hsu0731", "author": "徐志榮"},
        {"user_id": "19771002vivi", "author": "我是新移民  林麗蟬"},
        {"user_id": "KoChihEn", "author": "柯志恩"},
        {"user_id": "YiMingArthurChen", "author": "陳宜民教授"},
       # {"user_id": "100002730369711", "author": "陳雪生"},
        {"user_id": "yunlin.lishan", "author": "張麗善"},
        {"user_id": "congress.jason", "author": "許毓仁"},
        {"user_id": "TsengMingChung", "author": "曾銘宗"},
       # {"user_id": "100007752692215", "author": "楊鎮浯"},
        {"user_id": "chiangwanan", "author": "蔣萬安"},
        {"user_id": "kikuChen", "author": "陳菊(花媽)"},
        {"user_id": "DoctorKoWJ", "author": "柯文哲"},
        {"user_id": "uchange.keelung", "author": "林右昌UChange"},
        {"user_id": "taiwango0527", "author": "林智堅"},
        {"user_id": "chengwentsan", "author": "鄭文燦"},
        {"user_id": "llchu", "author": "朱立倫"},
        {"user_id": "forpeople", "author": "林佳龍"},
        #{"user_id": "李孟諺-753274604869524", "author": "李孟諺"},
        {"user_id": "flowerhome520", "author": "張花冠"},
        {"user_id": "happiness.miaoli", "author": "徐耀昌加油讚"},
        {"user_id": "MingkuWeiDPP", "author": "魏明谷"},
        #{"user_id": "chubeioffice", "author": "邱鏡淳"},
        {"user_id": "pan.menan1", "author": "潘孟安"},
        #{"user_id": "劉增應粉絲團-1571724343041507", "author": "劉增應粉絲團"},
        {"user_id": "LiFaWeiYuanLinMingQin", "author": "南投縣長‧林明溱"},
        {"user_id": "Yilanashang", "author": "林聰賢"},
        {"user_id": "UprightYung", "author": "李進勇"},
        {"user_id": "Fu.KunChi", "author": "傅崐萁"},
        {"user_id": "chenkuangfu1025", "author": "陳光復Chen Kuang-fu"},
        #{"user_id": "陳福海-275539222468954", "author": "陳福海"},
        {"user_id": "kerchenming", "author": "柯建銘"},
        {"user_id": "kolasyotaka.tw", "author": "Kolas Yotaka"},
        {"user_id": "yumeinu", "author": "尤美女立委"},
        {"user_id": "wdy19690305", "author": "王定宇"},
        {"user_id": "iamyungchang", "author": "立法委員 江永昌"},
        {"user_id": "Yuwanju", "author": "余宛如"},
        #{"user_id": "ly2115", "author": "Yuchin Wu"},
        {"user_id": "Wubray", "author": "吳秉叡"},
        {"user_id": "TaipeiNeedYou", "author": "吳思瑤"},
        {"user_id": "Wukuenyuh", "author": "吳焜裕教授"},
        {"user_id": "wuqiming519", "author": "吳琪銘"},
        {"user_id": "shirleylu312", "author": "呂孫綾"},
        {"user_id": "power2tw", "author": "李昆澤"},
        {"user_id": "chunyileefans", "author": "李俊俋"},
        {"user_id": "legislatorlifenglee", "author": "李麗芬"},
        {"user_id": "RiceChouChunMi", "author": "周春米 立委"},
        {"user_id": "LinDaiHua", "author": "林岱樺"},
        {"user_id": "seeklin", "author": "林俊憲"},
        {"user_id": "linshufen.fans", "author": "林淑芬"},
        {"user_id": "LinCYminorta", "author": "林靜儀醫師"},
        #{"user_id": "邱志偉-1588286501409955", "author": "邱志偉"},
        {"user_id": "denjen2020", "author": "登真-邱議瑩"},
        {"user_id": "YaoTurningTaipei", "author": "姚文智"},
        {"user_id": "tuanyikang", "author": "段宜康"},
        #{"user_id": "erhlinyi", "author": "洪宗熠"},
        {"user_id": "gaojyhpeng", "author": "高志鵬 Gao Jyh Peng"},
        {"user_id": "hunglueball", "author": "張宏陸"},
        {"user_id": "wanchien0209", "author": "堅持．張廖萬堅"},
       # {"user_id": "lawyer0420", "author": "莊瑞雄"},
        #{"user_id": "100001602950538", "author": "陳明文"},
        {"user_id": "fififans", "author": "陳亭妃"},
        {"user_id": "chengSayYes", "author": "陳素月SayYes"},
        {"user_id": "manli0205", "author": "陳曼麗 Chen Manli"},
        {"user_id": "chenoupo", "author": "陳歐珀"},
        #{"user_id": "ying.chen.9484", "author": "陳瑩"},
        {"user_id": "su.mei0110", "author": "陳賴素美 粉絲團"},
        {"user_id": "smilefangfang", "author": "黃秀芳"},
        {"user_id": "taiwanweicher", "author": "黃偉哲"},
        #{"user_id": "黃國書-566381323386617", "author": "黃國書"},
        #{"user_id": "penghu.yao", "author": "楊曜"},
        {"user_id": "YehYiJin", "author": "葉宜津"},
        {"user_id": "biling.kuan", "author": "管碧玲 (kuanbiling)"},
        {"user_id": "skychao6238", "author": "趙天麟"},
        {"user_id": "JhengYuOfficeBlog", "author": "趙正宇"},
        {"user_id": "2016newpower", "author": "愛信任-劉世芳"},
        {"user_id": "liucnko.fans", "author": "劉建國"},
        {"user_id": "ChaoHaoLiu", "author": "劉櫂豪"},
        {"user_id": "taichunggogogo", "author": "蔡其昌"},
        #{"user_id": "clbundlaw", "author": "蔡易餘"},
        {"user_id": "ahuitsai.tw", "author": "蔡培慧 慧做事真實在"},
        {"user_id": "keelungING", "author": "蔡適應"},
        {"user_id": "nicepongpong", "author": "鄭運鵬專頁"},
        {"user_id": "boching520", "author": "鄭寶清"},
        {"user_id": "Bikhim", "author": "蕭美琴 Bi-khim Hsiao"},
        {"user_id": "zenolai2", "author": "賴瑞隆"},
        {"user_id": "cafe1965", "author": "鍾佳濱"},
        {"user_id": "voteforlo", "author": "羅致政粉絲團"},
        {"user_id": "chiaohui.su", "author": "蘇巧慧"},
        {"user_id": "suchihfen", "author": "蘇治芬"},
       # {"user_id": "100000445699070", "author": "蘇震清"},
        {"user_id": "ShihYiFang0210", "author": "施義芳"},
        #{"user_id": "100007823383936", "author": "鍾佳濱"},
        {"user_id": "kcfor2016", "author": "黃國昌"},
        {"user_id": "polymh", "author": "徐永明"},
        {"user_id": "limfreddy", "author": "林昶佐 Freddy Lim"},
        {"user_id": "muming.yok", "author": "郁慕明觀察站"},
        {"user_id": "bingzhong.wang", "author": "王炳忠"},
        {"user_id": "HanTingHou", "author": "侯漢廷"},
        #{"user_id": "林明正-1001317079882909", "author": "林明正"},
        #{"user_id": "邱毅談天論地話縱橫-127907197272507", "author": "邱毅『談天論地話縱橫』"},
        {"user_id": "tsaiingwen", "author": "蔡英文 Tsai Ing-wen"},
        {"user_id": "chencj", "author": "陳建仁 Chen Chien-Jen"},
        {"user_id": "weikang.pan331", "author": "潘維剛"},
        {"user_id": "ChanChiShean", "author": "能革者 詹啟賢"},
        {"user_id": "twherohan", "author": "韓國瑜"},
        #{"user_id": "100003322437993", "author": "李來希"},
        {"user_id": "DrDemocracy", "author": "李登輝(Lee Teng-hui)"},
        {"user_id": "ChenShuibian.Page", "author": "陳水扁(Chen Shui-bian)"},
        {"user_id": "MaYingjeou", "author": "馬英九"},
        {"user_id": "LinChuanTW", "author": "林全"},
        {"user_id": "annettelu.vp", "author": "呂秀蓮"},
        {"user_id": "TCUSTFamous", "author": "蕭萬長名人講座"},
        {"user_id": "presidentialoffice.tw", "author": "總統府發言人"},
        {"user_id": "MilitarySpokesman", "author": "國防部發言人"},
        {"user_id": "chientailang", "author": "簡太郎"},
        {"user_id": "NeilPeng.tw", "author": "馮光遠"},
        {"user_id": "ChuChuPepper", "author": "洪秀柱"},
        {"user_id": "debatelo", "author": "羅智強"},
        {"user_id": "507Chenyichieh", "author": "陳怡潔"},
       # {"user_id": "taipeihjlee", "author": "李鴻鈞"},
        #{"user_id": "100006764016335", "author": "周陳秀霞"},
        {"user_id": "gogogoeball", "author": "蘇貞昌"},
        {"user_id": "frankcthsiehfans", "author": "謝長廷"},
        #{"user_id": "yousikun.fans", "author": "游錫堃"},
       # {"user_id": "100005197895320", "author": "謝東龍"},
        {"user_id": "DienlinHsiehchcc", "author": "謝典霖 / 找服務按電鈴 典霖服務處"},
        #{"user_id": "shuli.hsiao.3", "author": "蕭淑麗"},
        {"user_id": "Taitungaprilyao", "author": "饒慶鈴"},
       # {"user_id": "lin.chi.shan", "author": "林棋山"},
       # {"user_id": "100006132073856", "author": "李曉鐘"},
       # {"user_id": "許原龍服務團隊-395123487308016", "author": "許原龍服務團隊"},
       # {"user_id": "100002685960525", "author": "何勝豐"},
        #{"user_id": "郭信良-174094425951157", "author": "郭信良"},
        #{"user_id": "kuocouncilor", "author": "郭明賓"},
       #{"user_id": "100002049025236", "author": "陳文昌"},
       #{"user_id": "100003126867025", "author": "陳雙全"},
        #{"user_id": "100002986231743", "author": "陳見賢"},
        #{"user_id": "100000222516069", "author": "陳怡岳"},
        {"user_id": "cwz1967", "author": "陳文治"},
        #{"user_id": "100009885730439", "author": "蔡旺璉"},
        #{"user_id": "changda.gogo", "author": "蔡昌達"},
        {"user_id": "chingte", "author": "賴清德"},
        #{"user_id": "shu.w.zhengwei", "author": "唐鳳"},
        {"user_id": "tommyhsu47", "author": "徐國勇"},
       # {"user_id": "jiunnrong.yeh", "author": "葉俊榮"},
        {"user_id": "dpptw", "author": "民主進步黨"},
        {"user_id": "mykmt", "author": "中國國民黨 KMT"},
        {"user_id": "newpowerparty", "author": "時代力量 New Power Party"},
        {"user_id": "TaiwanGreenParty", "author": "綠黨"},
        {"user_id": "tsu.org", "author": "台灣團結聯盟"},
        {"user_id": "treesparty2014", "author": "樹黨"},
        {"user_id": "newparty.antifake", "author": "新黨打假除亂"},
        {"user_id": "npsunion", "author": "無黨團結聯盟"},
        {"user_id": "PFPTW", "author": "親民黨 People First Party"},
        {"user_id": "china999", "author": "中華統一促進黨"},
        {"user_id": "tommyhsu47", "author": "徐國勇"},
        {"user_id": "macgov", "author": "大陸委員會"},
        {"user_id": "ncsa0428", "author": "「全國公務人員協會」"},
        {"user_id": "qiaobaowang", "author": "美国侨报网"},
        {"user_id": "bannedbook.org", "author": "禁闻网"},
        {"user_id": "MyMalaysianNews", "author": "My Malaysian News 大马新闻抢先看"},
    ]