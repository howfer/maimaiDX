import json

arcades_lines = '''
环游嘉年华天河店
广东省广州市天河区天河路208号天河城6楼
环游嘉年华番禺易发店
广东省广州市番禺区市桥街易发商业街新大新百货5楼
哆啦乐图西安钟楼店
陕西省西安市碑林区骡马市60号文商大厦一层
风云再起上海店
上海市黄浦区人民大道221号迪美广场负一楼227-229#
城市英雄东莞长安店
广东省东莞市长安镇长青南路1号7栋万科广场三楼3039室城市英雄
风云再起南京新街口天丰大厦店
江苏省南京市秦淮区洪武路26号天丰大厦1楼风云再起
城市英雄衡阳解放路店
湖南省衡阳市石鼓区解放路26号
北京乐酷电玩
北京市海淀区远大路一号世纪金源购物中心5楼
深圳KKMALL星际传奇
广东省深圳市罗湖区深南东路5016号京基百纳空间KKMALL三楼313A星际传奇
深圳反斗乐园中心城店
广东省深圳市福田区福华一路怡景中心城UG层反斗乐园
胖东来动漫乐园
河南省许昌市七一路胖东来时代广场五楼动漫乐园
大玩家广州白云万达店
广东省广州市白云区云城东路503号万达广场B区一层大玩家
风云再起北京西单店
北京市西城区堂子胡同9号新一代商城六层
风云再起天津和平路店
天津市和平区和平路万达广场A座
大玩家北京通州万达店
北京市通州区新华西街58号万达广场3楼大玩家
大玩家泉州浦西万达店
福建省泉州市丰泽区宝洲街689号浦西万达广场娱乐楼二楼play1家庭娱乐中心
大玩家沈阳太原街万达店
辽宁省沈阳市和平区太原街万达广场三楼
大玩家上海宝山万达店
上海市宝山区128纪念路万达广场3楼大玩家
风云再起淮河路店
安徽省合肥市庐阳区淮河路步行街99号风云再起电玩城
大玩家哈尔滨哈西万达店
黑龙江省哈尔滨市南岗区中兴大道168号万达广场三楼大玩家超乐场
大玩家南京江宁万达店
江苏省南京江宁区东山街道竹山路68号万达广场2号门2楼大玩家超乐场
大玩家合肥包河万达店
安徽省合肥市包河区芜湖路万达广场
playone武汉菱角湖万达店
湖北省武汉市江汉区唐家墩菱角湖万达广场2层playone
大玩家南昌红谷滩万达店
江西省南昌市红谷滩区大玩家万达店
大玩家青岛城阳万达店
青岛市城阳区向阳中路万达广场二楼大玩家
天空之城南通圆融店
江苏省南通市崇川区工农路57号圆融广场三楼天空之城
金色年华电玩沙龙中街店
辽宁省沈阳市大东区小东路1号中街新玛特7F
风云再起西安骡马市民生百货店
陕西省西安市碑林区骡马市民生百货负一楼风云再起
汤姆熊大连罗斯福店
辽宁省大连市沙河口区西安路139号天兴罗斯福四楼
环游嘉年华金沙洲永旺店
广东省广州市白云区金沙洲永旺梦乐城
大玩家福州仓山万达店
福州仓山区浦上大道万达广场二楼答大玩家
大玩家荆门万达店
湖北省荆门市掇刀区象山大道万达广场三楼大玩家超乐场
环游嘉年华江门店
广东省江门市蓬江区白石大道166号汇悦城3楼
三亚金润阳光南梦园
海南省三亚市天涯区河西路金润阳光三楼南梦园
环游嘉年华东莞民盈国贸店
广东省东莞市东城街道东泰社区鸿福东路1号民盈国贸城5号楼L3001-3003
风云再起太原老鼠街店
山西省太原市迎泽区铜锣湾老鼠街尚品购物中心三层风云再起
城市英雄星沙吾悦店
湖南省长沙市长沙县吾悦广场
星河奇迹肇庆星湖店
广东省肇庆市端州区星湖广场四楼星河奇迹
城市英雄长沙梅溪湖步步高店
湖南省长沙市岳麓区梅溪湖步步高负一层城市英雄
风云再起郑州大上海城店
河南省郑州市管城回族区东太康路大上海城五楼风云再起
风云再起正洪大厦店
江苏省南京市秦淮区洪武路38号正洪大厦102栋
城市英雄步步高店
湖南省岳阳市步步高店
风云再起无锡苏宁广场店
无锡市梁溪区人民中路111号无锡苏宁广场三层309E号商铺
哆啦星球小寨店
陕西省西安市雁塔区长安中路215号西旅国际一楼
星舰梦航荔湾广百店
广东省广州市荔湾区坑口地铁站荔胜广场3F-10
城市英雄长沙五一广场店
湖南省长沙市天心区春天百货负一楼城市英雄电玩
神采飞扬杭州湖滨银泰店
浙江省杭州市上城区延安路湖滨IN77C区D区负一楼
大玩家烟台芝罘万达店
山东省烟台市芝罘区南大街万达广场二楼大玩家超乐场
威龙传奇济南世茂广场店
山东省济南市历下区泉城路26号世茂国际广场东座3楼E322威龙传奇
风云再起西宁店
青海省西宁市城西区西关大街42-52号西宁国芳百货2层风云再起
上海JOYPOLIS世嘉都市乐园
上海市普陀区中山北路3300号月星环球港四楼世嘉都市乐园
极客森深圳龙岗丹竹头店
深圳市龙岗区丹竹头时光里购物中心3座3楼极客森电玩城
南京风云再起常发广场店
江苏省南京市玄武区红山路88号常发广场3F风云再起
玩家会
北京市昌平区悦荟万科广场五层
环游嘉年华奥园店
广东省广州市番禺区福德路281号奥园广场负一楼
珠海富华里反斗乐园
广东省珠海市香洲区富华里商业街12栋201反斗乐园
风云再起淮安店
江苏省淮安市淮海北路10号茂业天地广场6F风云再起电玩城
哈尔滨大玩家香坊万达店
黑龙江省哈尔滨香坊区衡山路17号万达广场三楼大玩家超乐场
风云再起钦州店
广西钦州市钦南区金海湾东大街1号新城吾悦广场第四层Z12风云再起
风云再起咸阳店
咸阳市秦都区正兴广场三楼风云再起
风云再起杭州店
浙江省杭州市下城区新天地购物中心五楼风云再起
环游嘉年华佛山南海永旺店
佛山市南海区大沥联窖窖口路13号永旺梦乐城二楼201
大玩家武汉经开万达店
湖北省武汉市蔡甸区东风大道111号万达大玩家
风云再起昆明金鹰店
云南省昆明市威远街168号金鹰B座7楼风云再起
大玩家呼和浩特万达店
内蒙古呼和浩特市赛罕区万达广场二楼大玩家
城市英雄司门口店
湖南省长沙市解放西路147号
冰河世纪动漫城
东莞市万江区华南摩尔D区三楼冰河世纪动漫城
风云再起镇江苏宁广场店
江苏省镇江市京口区解放路111号苏宁广场三楼风云再起
风云再起天津爱琴海店
天津市河东区津滨大道160号爱琴海购物公园F446风云再起
风云再起秦皇岛店
河北省秦皇岛市海港区白塔岭街道河北大街西段368号茂业天地4楼风云再起
城市英雄常州天宁吾悦广场店
江苏省常州市天宁区吾悦广场三楼
大玩家沈阳北一路万达店
辽宁省沈阳市铁西区北一路万达广场三楼大玩家超乐场
银川金凤万达大玩家
宁夏省银川市正源北街金凤万达广场二楼大玩家
风云再起苏州观前街店
江苏省苏州市姑苏区观前街粤海广场1号楼2层风云再起
风云再起南京湖南路店
江苏省南京市鼓楼区湖北路64号风云再起
城市英雄天津津南吾悦广场店
天津市津南区吾悦广场三楼
大玩家秦皇岛万达店
河北省秦皇岛市海港区燕山大街万达广场二楼大玩家
大玩家石景山万达店
北京市石景山区石景山路乙18号万达广场1楼大玩家家庭娱乐中心
星际传奇珠海海韵城店
珠海海韵城星际传奇
反斗乐园华强北九方分店
深圳市福田区华强北街道中航九方购物中心L511商铺
大玩家顺德大融城店
佛山市顺德区大融城3楼大玩家
南京茂业天空之城
江苏省南京市秦淮区夫子庙街道茂业天地3楼天空之城
深圳星际传奇上梅林卓悦汇店
广东省深圳市福田区梅林街道中康路与梅林路交汇处卓悦汇购物中心L3层17号
玩家英雄珠海家和城广场店
广东省珠海市斗门区湖心路1138号家和城广场第二层2002号铺位
城市英雄赣州店
江西省赣州市章贡区红旗大道33号步步高新天地四楼
欢乐工坊电玩城
贵州省贵阳市花溪区清溪路111号万宜广场负一楼
51区动漫游乐广州白云店
广东省广州市白云区云霄路353栋的5号停机坪三层L3002N
壹零壹潮漫万家丽负一楼店（偶予电玩）
湖南省长沙市芙蓉区东沌渡街道万家丽中路一段99－101号B1楼B42&B43－1号商铺
上海烈火游戏机娱乐有限公司
上海市静安区江宁路77号4楼
福州东二环星际传奇
福建省福州市晋安区岳峰镇竹屿路6号东二环泰禾广场商业中心22号楼第4层L410-3商铺
51区动漫游乐天津西青店
天津市西青区中北镇阜盛道永旺梦乐城2楼51区动漫游乐场
风云再起长沙黄兴南路店
湖南省长沙市天心区黄兴广场E区四楼
风云再起上海长风大悦城店
上海市普陀区长风新村街道大渡河路168弄136号长风大悦城室外商场3楼L3-13室风云再起
神采飞扬青岛伟东乐客城店
山东青岛市李沧区伟东乐客城三楼神采飞杨
风云再起辽宁沈阳恒隆广场店
辽宁省沈阳市沈河区皇城恒隆广场211风云再起动漫娱乐中心
GOOGOOISLAND咕咕岛河北涿州君悦广场店
河北省保定市涿州市范阳路君悦广场3楼GOOGOOISLAND
星际传奇龙华天虹店
深圳市龙华区民治街道人民路九方购物中心三楼L312星际传奇
星际传奇昆山万象汇店
江苏省苏州市昆山市玉山镇前进西路1266号昆山万象汇商业中心L3层L323号商铺
汤姆熊天津恒隆广场店
天津市和平区小白楼街兴安路166号3030室恒隆广场汤姆熊欢乐世界
阿凡达电玩山西太原柳巷店
山西省太原市迎泽区柳巷商业街工贸大厦四楼阿凡达电玩嘉年华
世纪华联弘哲动漫城
河南省新乡市五一路与新中大道交叉口向南500米易美家居负一楼世纪华联超市
乐满堂电玩常州武进吾悅广场店
江苏省常州市武进区人民路吾悅广场3楼
城市英雄江西南昌店
江西省南昌市新建区长棱大道新城吾悦广场2楼
风云再起安徽滁州苏宁广场店
安徽省滁州市琅琊区南瞧北路810号苏宁广场负一楼
星乐荟上海浦东金汇广场店
上海市浦东新区华夏东路2255号金汇广场3楼星乐荟欢乐世界
风云再起四川成都天府广场店
四川省成都市青羊区天府广场负一楼今站购物中心B50商铺
环游嘉年华番禺永旺店
广东省广州市番禺区亚运大道1号永旺梦乐城3楼3001铺环游嘉年华
风云再起郑州大卫城店
河南省郑州市金水区二七路西泰康路大卫城6楼风云再起
环游嘉年华广州黄埔绿地店
广东省广州市黄埔区亿创大街3号绿地缤纷城3楼301铺
星际传奇大千里店
广东省深圳市宝安区坪洲大千里3楼
天天玩上海徐汇汇银广场店
上海市徐汇区华山路2088号汇银广场南楼7M层天天玩
疯狂牛仔城广州荔湾上下九店
广东省广州市荔湾区下九路90号东急新天地购物广场三楼疯狂牛仔城
赛乐联盟广州新塘合生店
广东省广州市增城区新塘合生汇G1赛乐联盟
大玩家广州海珠万达店
广东省广州市海珠区逸景路238号海珠万达广场三楼大玩家
风云再起青岛金狮广场店
山东省青岛市崂山区香港东路195号天狮广场乙L2-01B风云再起
城市英雄郴州店
湖南省郴州市北湖区人民中路8号
真快活武汉江汉国际广场店
湖北省武汉市江汉区解放大道690号武汉国际广场7楼
真快活武汉洪山中商店
湖北省武汉市洪山区中商世界里负一楼真快活动漫体验中心
吉林市丰满区世宇乐园
吉林省吉林市吉林大街1~2号欧亚综合体三楼
银河系辽宁大连中古店
辽宁省大连市西岗区五四路66号恒隆广场319号银河系
真快活武汉汉阳摩尔城店
湖北省武汉市汉阳区龙阳大道王家湾摩尔城B座5楼真快活动漫体验中心
真快活武汉洪山银泰店
湖北省武汉市洪山区珞喻路35号银泰创意城7楼真快活电玩
真快活江西南昌王府井店
江西省南昌市青云谱区洪城路188号王府井购物中心六楼真快活台球电玩
城市英雄浙江义乌吾悦广场店
浙江省义乌市江东街道吾悦广场3楼城市英雄
星球小镇儿童乐园汕头龙湖店
广东省汕头市龙湖区华山路57号充耀号商住中心一层星球小镇儿童乐园
都市玩家武汉青山店
湖北省武汉市青山区和平大道奥山世纪城3楼都市玩家
乐炫风福州鼓楼东百中心店
福建省福州市鼓楼区东街东百中心C馆负一楼乐炫风
梦幻谷游艺佛山禅城东方店
广东省佛山市禅城区东方广场翡翠城负一楼梦幻谷
冒险岛深圳南山方大城店
广东省深圳市南山区西丽龙珠四路2号方大城购物中心三层冒险岛
星河奇迹韶关浈江U购城店
广东省韶关市浈江区兴隆街28号U购城一楼星河奇迹游乐体验馆
风云再起上海长泰广场店
上海市浦东新区外高桥保税区自由贸易试验区祖冲之路1239弄长泰广场地下一层59-1室风云再起
酷卡贝滁州琅琊乐彩城店
安徽省滁州市琅瑯区南谯北路860号乐彩城第三层酷卡贝家庭娱乐中心
量子空间杭州东站西广场C座店
浙江省杭州市江干区火车东站西广场C座一层量子空间未来主题乐园
好宜多电玩城惠州惠阳店
广东省惠州市惠阳区淡水镇南门东街好宜多商贸广场五楼电玩城
晴空乐园汕头F16购物中心店
广东省汕头市黄山路F16购物中心三楼晴空乐园电玩城
真快活十堰茅箭人民商城店
湖北省十堰市茅箭区五堰街道人民北路1号武商十堰人民商城8楼真快活美乐园电玩城
真快活武汉循礼门M＋店
湖北省武汉市江汉区京汉大道循礼门M＋购物中心5楼真快活
北京海淀嗨翻竞技体育乐园
北京市海淀区复兴路69号嗨翻竞技主题乐园
风云再起南京水平方店
江苏省南京市秦淮区健康路3号水平方三楼风云再起
风云再起郑州二七广场店
河南省郑州市二七区百年德化风情购物公园尚潮汇负一楼
风云再起石家庄华强广场店
河北省石家庄市新华区民族路华强广场五楼风云再起动漫娱乐中心
风云再起天津南京路店
天津市和平区南京路209号吉利大厦四楼
汤姆熊上海正大广场店
上海市浦东新区陆家嘴西路168号正大广场2楼汤姆熊
汤姆熊上海大悦城店
上海市静安区西藏北路166号大悦城南座601-605室
汤姆熊欢乐世界上海日月光店
上海市徐汇区漕宝路33号徐汇日月光中心L4-51号
汤姆熊宁波天一广场店
浙江省宁波市海曙区华楼巷10号天一广场
闪电部落西安新城益田假日店
陕西省西安市新城区长乐东路益田假日广场F3
风云再起上海维璟广场店
上海市闵行区维璟广场四楼风云再起
佐佐佑佑电玩城
浙江省温州市鹿城区公园路163号名城广场A栋3楼
极速时代淮安新亚广场店
江苏省淮安市清江浦区淮海街道新亚广场7楼极速时代动漫城
世佳乐园石狮德辉广场店
福建省泉州市石狮市德辉广场7楼世佳乐园
星际传奇宁波万象汇店
浙江省宁波市鄞州区钱湖北路267号万象汇四楼星际传奇
兰州城关奥德乐家庭游乐中心
甘肃省兰州市城关区杉杉奥特莱斯306奥德乐家庭游乐中心
反斗乐园北京朝阳星际传奇店
北京市朝阳区朝阳北路常营乡龙湖长楹天街商业区东区三楼星际传奇
星际传奇深圳万象天地店
广东省深圳市南山区深南大道9668号万象天地4层SL435星际传奇
汕尾信利广场城市英雄
广东省汕尾市城区信利城市广场4楼城市英雄动漫游戏体验中心
菲利斯星球乐园临沂首联旺角店
山东省临沂市兰山区通达路377号首联旺角一楼菲利斯星球乐园
奇特冰雪乐园温州鹿城店
浙江省温州市鹿城区瓯江路589号杨府山涂村奇特冰雪乐园
童年搭档广安邻水店
四川省广安市邻水县广邻大道宏帆广场宁洋百货一楼童年搭档
反斗乐园深圳宝安壹方城星际传奇店
广东省深圳市宝安区宝安中心壹方城购物中心三楼星际传奇
汤姆熊上海长宁龙之梦店
上海市长宁区长宁路1810号龙之梦购物中心6楼汤姆熊欢乐世界
城市英雄长沙岳麓奥克斯店
湖南省长沙市岳麓区岳麓大道奥克斯广场3楼城市英雄
嗨森汇乐园武汉东湖光谷店
湖北省武汉市东湖高新区光谷世界城3楼嗨森汇乐园
真快活荆门东宝银泰城店
湖北省荆门市东宝区龙泉街道象山一路6号银泰城七楼真快活美乐园
风云再起上海中环百联店
上海市普陀区真光路1288号中环百联3楼风云再起
欢乐梦工场长治潞州店
山西省长治市潞州区东大街90号欢乐梦工场
乐满堂欢乐王国嘉兴店
浙江省嘉兴市城南路1532号华府广场2F-012、2F-013号乐满堂欢乐王国
环游嘉年华成都都江堰店
四川省成都市都江堰市融创文旅城融创茂3楼环游嘉年华
壹家庭游乐园宁波店
浙江省宁波市北仑区富邦世纪D区3楼3031号壹家庭游乐园
风云再起沈阳大悦城店
辽宁省沈阳市大东区万泉街道小东路6-1号大悦城B馆F4
猿计划游艺MALL佛山店
广东省佛山市南海区南海万科广场负一层
极客森超乐场深圳宝能城店
广东省深圳市南山区西丽留仙大道塘朗地铁站C出口宝能城三楼极客森超乐场
风云再起沈阳佳兆业广场店
辽宁省沈阳市佳兆业广场风云再起动漫娱乐中心
星世纪动漫台球体验中心七星店
湖南省株洲市芦淞区建设街道钟鼓岭路118号七星潮流购物公园星世纪动漫台球中心
风云再起沈阳沈北华强广场店
辽宁省沈阳市沈北新区道义街道华强广场三楼风云再起
新动力电玩长沙万家丽广场店
湖南省长沙市芙蓉区万家丽购物广场负一楼新动力电玩城
壹家庭游乐园临沂店
山东省临沂市兰山区泰盛广场3楼壹家庭游乐园
风云再起南京金鹰店
江苏省南京市建邺区应天大街888号河西金鹰3楼
海口日不落动漫网咖
海南省海口市美兰区明珠广场6楼日不落
城市英雄电玩长春欧亚新生活店
吉林省长春市朝阳区红旗街新民广场欧亚新生活5楼城市英雄电玩城
晴空进击社广州荔湾店
广东省广州市荔湾区西湾路150号悦汇城三楼晴空进击社
一起玩家年华泰安爱琴海店
山东省泰安市爱琴海购物广场二楼一起玩嘉年华
风云再起太原茂业店
山西省太原市小店区亲贤北街茂业天地三楼风云再起
赛乐联盟广州海珠合生广场店
广东省广州市海珠区叠景路168号合生广场L3-04/05
大玩家广州黄埔南岗万达店
广东省广州市黄埔区康富路16号万达广场二楼大玩家
嗨森汇乐园成都金牛凯德店
四川省成都市金牛区交大路183号凯德广场一期四楼嗨森汇乐园
现代嘉年华珲春店
吉林省珲春市沿河西街1463号现代百货
真快活合肥银泰城店
安徽省合肥市包河区云谷路银泰城三楼真快活美乐园
风云再起宿迁宝龙广场店
江苏省宿迁市西湖路6号宿迁宝龙广场4楼风云再起
玩趣时代江门星汇广场店
广东省江门市新会区会城大新路50号星汇广场2层玩趣时代
嘻品堂电玩娱乐
湖南省长沙市万家丽中路99号万家丽国际购物广场五楼嘻品堂电玩
酷乐大玩家鄂尔多斯店
内蒙古鄂尔多斯市东胜区星河COCO City二期二楼
大玩家广州番禺万达店
广东省广州市番禺区南村镇兴南大道万达广场二楼大玩家超乐场
大玩家上海江桥万达店
上海市嘉定区金沙江西路1051号万达广场一楼大玩家
大玩家上海周浦万达店
上海市浦东新区周浦镇周浦万达广场二楼大玩家
大玩家长春红旗街万达店
吉林省长春市红旗街万达广场三楼大玩家
轩轩窝桌游电玩屋深圳店
广东省深圳市龙华区民治街道樟坑一区91栋1层（91-4）
彩虹王国深圳众冠店
广东省深圳市南山区桃源区留仙大道1213号益田假日里3楼彩虹王国动漫体验中心
哈尔滨道里欢乐集合地店
黑龙江省哈尔滨市道里区友谊路悦荟广场A座二楼欢乐集合地
城市动力珠海香洲弘桥商城店
广东省珠海市香洲区南屏镇南湾北路弘桥商城一楼城市动力动漫娱乐中心
深圳铃屋店
广东省深圳市龙岗区龙翔大道5022号雅庭名苑B栋一楼商铺
真快活武汉武昌光谷广场店
湖北省武汉市武昌区珞瑜路726号光谷世界城4楼
环游嘉年华海口龙华上邦百汇城店
海南省海口市龙华区龙华路上邦百汇城环游嘉年华
好特电玩柳州五星店
广西省柳州市城中区解放南路87号两面针大厦负一楼好特电玩五星店
鞍山四隆广场主题公园
辽宁省鞍山市铁东区东山街55号
巷战英雄电玩长春欧亚万豪店
吉林省长春市二道区欧亚万豪购物中心5楼巷战英雄电玩城
疯狂动物城大理泰业国际店
云南省大理市白族自治州大理市泰业国际广场三楼疯狂动物城
大玩家邯郸万达店
河北省邯郸市邯山区万达广场三楼大玩家
西安市酷玩码头电玩城
陕西省西安市未央区艾斯广场一楼酷码头电玩城
桂林玛丽奥电玩俱乐部
广西省桂林市秀峰区中山中路36号桂林大世界负一楼玛丽奥电玩
星月方舟肇庆敏捷广场店
广东省肇庆市端州区敏捷广场3楼3038号星月方舟
星悦潮玩无锡店
江苏省无锡市锡山区锡东八佰伴3楼星悦潮玩
大玩家马桥万达店
上海市马桥万达广场三楼大玩家
城市英雄武汉k11店
湖北省武汉市硚口区解放大道632号K11艺术购物中心4层S418-S419Party House
潮人电玩温州店
浙江省温州市鹿城区第一桥纱帽河商城二楼潮人电玩
汤姆熊天津熙悦汇店
天津市南开区黄河道513号熙悦汇购物中心1楼37b
梦时代电玩城贵阳玖福城店
贵州省贵阳市观山湖区观山西路3号玖福城购物中心4楼
天津麦趣熊泉汇店
天津市河西区大沽南路1118号泉汇购物中心一楼
环游嘉年华超乐场德港万达店
新疆乌鲁木齐市经济技术开发区德港万达6楼环游嘉年华超乐场
疯狂牛仔城清远清城世纪荟店
广东省清远市清城区先锋东路3号世纪荟广场疯狂牛仔城
阿尔法南昌西湖商夏店
江西省南昌市西湖区中山路282号西湖商厦负一楼阿尔法游艺中心
娱乐至上成都都江堰店
四川省成都市都江堰市幸福街道幸福社区都江堰大道106号1号楼4层13b室
奇奇乐园宜昌兴发店
湖北省宜昌市伍家岗区中南路35号兴发广场3楼奇奇乐园
裕隆动漫城鹤壁店
河南省鹤壁市淇滨区鹤煤大道与兴鹤大街交叉口裕隆爱之城动漫城
北京上地华联嘉贝乐
北京市海淀区农大南路1号院1号楼华联商厦上地店
星世纪动漫游戏体验中心邵阳店
湖南省邵阳市双清区友阿国际广场三楼星世纪动漫游戏体验中心
嗨倍堂超级乐园南通店
江苏省南通市海门区龙信广场嗨倍堂超级乐园
星世纪长沙五一广场万代店
湖南省长沙市开福区通泰街道万代大酒店一楼
星世纪合肥唯品会店
安徽省合肥市蜀山区金寨路811号唯品会城市奥莱广场3楼
爱宝游乐园南通崇川店
江苏省南通市崇川区青年路星城路交叉口大有镜购物中心3楼
汤姆熊上海百联又一城店
上海市杨浦区淞沪路8号百联又一城购物中心8楼汤姆熊欢乐世界
奇奇乐园上海店
上海市闵行区都市路5001号3楼61号奇奇乐园
星际传奇佛山南海南宇广场店
广东省佛山市南海区桂城街道石龙南路6号南宇广场L3层D14单元
汤姆熊上海旭辉广场店
上海市浦东新区张扬路2389弄2号旭辉广场4F-1B汤姆熊
猿计划游艺MALL顺德大良店
广东省佛山市顺德区大良华侨城O.PLAZA商场3楼
风云再起大连胜利广场店
辽宁省大连市中山区青泥洼桥街道胜利广场28号夹层D102风云再起
漫无止境动漫城武汉汉阳店
湖北省武汉市汉阳区龙阳大道56号汉阳人信汇商业广场第十幢C馆二层
环游嘉年华番禺天河城店
广东省广州市番禺区汉溪大道东366号天河城广场3F-4F环游嘉年华
可可猩球南开大悦城店
天津市南开区南门外大街大悦城北区2楼1号可可猩球电玩
量子时空舱长沙店
湖南省长沙市万家丽北路19号蟠龙时代广场
龙小湖探索乐园重庆沙坪坝店
重庆市沙坪坝区北站东路188号附3号金沙天街B馆1F-21LT、2F-21LT、3F-21
环游嘉年华瑞安新湖广场店
浙江省瑞安市万松东路1588号新湖广场2楼1218号环游嘉年华
51区超级乐园天津津南店
天津市津南区辛庄永旺3楼五十一区超级乐园
打上花火铜陵吾悦广场店
安徽省铜陵市西湖镇吾悦广场三楼Z301打上花火游乐汇
超级英雄衡阳蒸湘店
湖南省衡阳市蒸湘区船山西路49号金钟大雁城L1-02-05超级英雄
51区超级乐园天津西青友谊南路店
天津市西青经济开发区友谊南路111号A区永旺梦乐城2楼51区超级乐园
大玩家汕头金平万达店
广东省汕头市金平区光华街道潮汕路61号4F大玩家超乐场
城市英雄长春亚泰新动力店
吉林省长春市二道区东盛大街与吉林大路交汇亚泰新动力
核客电玩城深圳罗湖店
广东省深圳市罗湖区深南东路3020号百货广场大厦西座一楼
天津宝坻区金满家购物广场店
天津市宝坻区天赋源金满家购物广场三楼儿童乐园
风云再起苏州莱迪店
江苏省苏州市姑苏区观前街碧凤坊41号莱迪购物三楼风云再起
奥飞欢乐世界太原来福店
山西省太原市万柏林区世纪联华来福购物中心三楼
风云再起无锡清扬茂业天地店
江苏省无锡市梁溪区清扬路128号茂业天地3楼风云再起
大玩家上海闵行浦江万达店
上海市闵行区浦江镇永跃路浦江万达广场二楼
大玩家厦门湖里区万达店
福建省厦门市湖里区仙岳路万达广场三楼
大玩家漳州碧湖万达店
福建省漳州市龙文区步文镇建元东路碧湖万达广场二楼大玩家
益家攻略东营王府井店
山东省东营市东营区黄河路与天目山路交叉口王府井广场4楼益家攻略
插电师电玩北京西单大悦城店
北京市西城区西单大悦城八楼PLAYCE插电师电玩
大玩家广州萝岗万达店
广州市黄埔区科丰路89号萝岗万达广场
大玩家南宁江南万达店
广西省南宁市江南区亭洪路48-1江南万达广场一号门二楼
大玩家西安大明宫万达店
陕西省西安市未央区太华北路369号大明宫万达广场二楼
大玩家益阳赫山万达店
湖南省益阳市赫山区万达广场二楼大玩家
大玩家福州福清万达店
福建省福州市福清市音西街道清昌大道105号万达广场内购物中心娱乐楼二层
大玩家南京建邺万达店
江苏省南京市建邺区万达广场2楼大玩家
大玩家兰州城关万达店
甘肃省兰州市城关区万达广场2楼play1家庭娱乐中心
大玩家上海松江万达店
上海市松江区万达广场二楼大玩家
大玩家福州金融街万达店
福建省福州市台江区鳌峰路8号万达广场二楼大玩家超乐场
大玩家上海金山万达店
上海市金山区山阳镇龙皓路1088号万达广场三楼大玩家
威龙传奇潍坊奎文店
山东省潍坊市奎文区泰华新天地三楼威龙传奇电玩城
哇哇哇游乐城广州天河正佳店
广东省广州市天河区天河路228号正佳广场七楼
大玩家常州新北万达店
江苏省常州市新北区万达广场三楼大玩家
大玩家成都金牛二店
四川省成都市金牛区一环路北三段万达广场大玩家
奇奇乐园随州曾都店
湖北省随州市曾都区区大润发3楼奇奇乐园娱乐电玩
大玩家西安民乐园万达店
陕西省西安市新城区民乐园万达广场四楼大玩家
大玩家厦门集美万达店
福建省厦门市集美区银江路137号万达广场二楼大玩家
大玩家成都锦江万达店
四川省成都市锦江区二环路东五段万达广场三楼play1家庭娱乐中心
乐贪玩沈阳和平印象城店
辽宁省沈阳市和平区太原街印象城三楼乐贪玩
城市英雄扬州邗江吾悦广场店
江苏省扬州市邗江区竹西路23号扬州新城吾悦广场二层2002-1商铺
大玩家唐山南区万达店
河北省唐山市路南区万达广场二层play1家庭娱乐中心
大玩家无锡滨湖万达店
江苏省无锡市滨湖区万达广场一楼大玩家超乐场
晴空超乐场揭阳揭东店
广东省揭阳市揭东区天虹购物中心晴空超乐场
杭州神采飞扬城西银泰第一回合店
浙江省杭州市拱墅区丰潭路城西银泰城三楼第一回合
101电玩长沙芙蓉万家丽店
湖南省长沙市芙蓉区万家丽8楼101电玩
爱玩星球驻马店
河南省驻马店市经济开发区乐山大道与置地大道交叉口爱克玖隆茂购物中心三楼爱玩星球
奇奇乐园襄阳樊城天元店
湖北省襄阳市樊城区定中街天元四季城二楼奇奇乐园
奇奇乐园随州水西门店
湖北省随州市水西门新世纪购物中心2店4楼奇奇乐园
真快活仙桃武商店
湖北省仙桃市武商购物中心七楼真快活美乐园电玩城
拿酷科幻城湛江赤坎店
广东省湛江市赤坎区沙湾街道丽悦新天M层拿酷科幻城
北京丰台莱蜜欢乐城
北京市丰台区丽泽桥丰北路18号金唐购物中心三层
都市玩家荆门掇刀万达店
湖北省荆门市掇刀区万达广场4楼都市玩家
风云再起宿州苏宁广场店
安徽省宿州市埇桥区苏宁广场三层风云再起
克罗米星VR电玩1903店
云南省昆明市西山区公园1903店克罗米星VR电玩
风云再起南京浦口弘扬广场店
江苏省南京市浦口区大桥北路48号弘阳广场B2区8号
爱玩嘉年华江北观音桥店
重庆市江北区观音桥天天尚街爱玩嘉年华
PPG潮玩汇天津大悦城店
天津市南开区南门外大街大悦城南区四楼
神采飞扬宁波万达店
浙江省宁波市鄞州区四明中路999号万达广场二楼
第一回合南通中南城店
江苏省南通市桃园路12号中南城购物中心3楼第一回合
木马王国杭州江干店
浙江省杭州市江干区新塘路108号天虹购物中心B座3楼木马王国
环游时代电玩盘锦兴隆店
辽宁省盘锦市兴隆台区钻井生活广场三楼环游时代电娱乐城
极客森深圳万科里店
广东省深圳市龙岗区龙城万科里负一楼极客森
成都银泰城第一回合
四川省成都市武侯区益州大道1999号银泰城
第一回合苏州中心店
江苏省苏州市苏州中心六楼南区第一回合
第一回合宜兴八佰伴店
江苏省无锡市宜兴市解放东路288号八佰伴生活广场四楼
星河奇迹佛山王府井紫薇港店
广东省佛山市禅城区石湾街道季华四路68号王府井百货L3032-2
北京莱利嘉年华
北京市海淀区远大路金源购物中心-1层B12
爱玩嘉年华金沙店娱乐厅
重庆市沙坪坝区三峡广场金沙天街B馆五楼爱玩嘉年华
大玩家石家庄裕华万达店
河北省石家庄市裕华区建华南大街万达广场3楼大玩家
奥纪电玩城汕尾明珠店
广东省汕尾市城区香洲路明珠广场三楼奥纪电玩城
星月方舟动漫湖南宁乡翡翠广场店
湖南省长沙市宁乡市春城北路翡翠广场
风云再起南宁朝阳路店
广西省南宁市朝阳路西南商都负一楼风云再起游乐汇
玩美世界e动城郑州店
河南省郑州市金水区金水东路80号绿地新都会.新田360A馆四楼
好玩谷动漫游戏主题乐园东莞店
广东省东莞市南城莱蒙商业中心三楼好玩谷动漫游戏主题乐园
欢乐城市嘉年华沈阳沈河店
辽宁省沈阳市沈河区中街路268号益田假日世界一楼欢乐城市嘉年华
星际传奇北京丰台丽泽天街店
北京市丰台区丽泽路300号丽泽天街三楼
酷漫总动员成都郫都店
四川省成都市郫都区犀浦镇双铁路69号负一层47、48、49、51号酷漫总动员
游戏童年PLAYGROW佛山顺德店
广东省佛山市顺德区裕和路109号东平保利广场3楼游戏童年PLAYGROW家庭娱乐中心
小酋长武汉江汉店
湖北省武汉市江汉区中山大道818号HAPPY站台
星际传奇成都龙泉驿世茂店
四川省成都市龙泉驿区世茂广场4F星际传奇
金色年华电玩沙龙于洪店
辽宁省沈阳市于洪区黄海路45号新玛特7楼金色年华电玩
星际传奇渝北光环商场店
重庆市渝北区鸳鸯街道光环购物公园L3楼26-27星际传奇
纷纷乐园扬州邗江文昌店
江苏省扬州市邗江区中集文昌商业中心1号楼2楼纷纷乐园
嘉贝乐电玩北京丰台永旺店
北京市丰台区丰葆路88号院一号楼永旺梦乐城4楼嘉贝乐电玩城
王者之风电玩天津金都店
天津市滨海新区金街银泰负一楼王者之风电玩城
汤姆熊上海浦东lalaport店
上海市浦东新区新金桥路738号lalaport(啦啦宝)3楼320汤姆熊欢乐世界
小勇士家庭娱乐中心济南店
山东省济南市天桥区济泺路缤纷五洲一楼小勇士家庭娱乐中心
头号玩家洛阳泉舜店
河南省洛阳市洛龙区泉舜购物中心4楼头号玩家
汤姆熊成都温江珠江广场店
四川省成都市温江区光华大道三段1588号合生汇广场4楼汤姆熊
大风车威海嘉禾天地店
山东省威海市威高广场嘉禾天地三楼大风车游乐场
玩美世界e动城太康路店
河南省郑州市金水区太康路四楼西北角
惠州美多儿童游乐城
广东省惠州市惠东县平山街道新平路297号惠州市美多儿童游乐城
星际传奇厦门集美世贸店
福建省厦门市集美区侨英街道滨水中二里世茂广场32-33号2层2005号商铺
太空球乐园福州晋安店
福建省福州市晋安区福马路788号Livat荟聚L1层01A41号太空球乐园
天空之城扬州三盛店
江苏省扬州市邗江区三盛国际广场3楼天空之城
偶予电玩青岛宝龙店
山东省青岛市即墨区宝龙广场四楼偶予电玩
幸运星南昌万象汇店
江西省南昌市青山湖区万象汇三楼幸运星游乐中心
电玩橙六盘水钟山店
贵州省六盘水市钟山区荷城街道大润发三楼电玩橙家庭娱乐中心
慢车道欢聚中心泰安吾悦店
山东省泰安市泰山区吾悦广场慢车道欢聚中心
摩兜欢乐岛黄岩吾悦店
浙江省台州市黄岩区新城吾悦广场三楼摩兜欢乐岛
一号机长长沙开福万达店
湖南省长沙市开福区中山路589号万达广场娱乐楼3楼（Z-3F-A）一号机长
super101合肥店
安徽省合肥市庐阳区逍遥津街道淮河路步行街寿春路城改时代合肥super101
星际传奇光明大仟里店
广东省深圳市光明区公明街道天汇城一期商业裙楼三楼L323-325号商铺星际传奇
晴空超乐场汕头峡山店
广东省汕头市潮南区合胜广场3楼晴空超乐场
treasure dream北京店
北京市朝阳区建国路16号院（星空文娱）C区二楼梦与宝藏
反斗星长沙岳麓店
湖南省长沙市岳麓区洋湖街道先导路69号长沙龙湖洋湖天街A2-3F-16, A2-3F-17
朗玩广州新塘永旺店
广东省广州市增城区宁西街创新大道15号永旺梦乐城1栋3084朗玩文化
11Lab天津店
天津市滨海新区新城西路k11商场2楼
星际传奇济南融创茂店
山东省济南市历城区经十东路融创文旅城L1-B星际传奇商铺
天空之城合肥蜀山之心店
安徽省合肥市蜀山区长江西路之心城7楼天空之城
真快活三河燕郊永旺店
河北省三河市燕郊镇永旺梦乐城负一楼真快活美乐园
玩美世界e动城南阳店
河南省南阳市卧龙区建设中路新田360四楼玩美世界e动城
汤姆熊延吉店
吉林省延吉市光明街608号百货大楼八楼汤姆熊欢乐世界
乐趣时代贵港港北店
广西省贵港市港北区贵城街道客世界三楼乐趣时代
大玩家西宁万达店
青海省西宁市城东区中惠万达广场3楼大玩家
PPG潮玩汇兰州店
甘肃省兰州市城关区东方红广场广场南路8号G层
大玩家杭州富阳万达店
浙江省杭州市富阳区万达广场二楼大玩家
嗨倍堂长沙宁乡吾悦广场店
湖南省长沙市宁乡市白马桥街道吾悦广场四楼4001室嗨倍堂超级乐园
星城战记衡阳万达店
湖南省衡阳市珠晖区酃湖万达广场2楼星城战记
子洋联盟长沙望城奥莱店
湖南省长沙市望城区金星北路砂之船奥莱3楼子洋联盟动漫体验中心
东方英雄鞍山奥莱店
辽宁省鞍山市铁东区二道街71号万熹佳柏奥特莱斯7层东方英雄嘉年华
龙小湖世界武汉江宸天街店
湖北省武汉市江汉区青年路518号江宸天街3F-33号
风云再起北京北投爱琴海店
北京市通州区新华东街289号院1号楼北京北投爱琴海购物公园M层
星际传奇武汉龙湖江宸天街店
湖北省武汉市江汉区航测村青年路与马场角小路交汇处武汉江宸天街A-4F-28，A-4F-29
汤姆熊上海环球港店
上海市中山北路3300号环球港购物中心3楼3166室汤姆熊欢乐世界
星际传奇泰州万象城店
江苏省泰州市海陵区永定路华润国际社区3期万象城三楼星际传奇
乐传动漫襄阳樊城店
湖北省襄阳市樊城区关圣古镇13栋
城市英雄长沙荟聚店
湖南省长沙市岳麓区洋湖街道 潭州大道宜家荟聚购物中心三楼
迪卡丘菏泽牡丹店
山东省菏泽市牡丹区佳和城二楼迪卡丘嘉年华
反斗乐园南京浦口万象汇店
江苏省南京市浦口区浦珠北路1号万象汇3楼330
阿凡达北京海淀店
北京市海淀区北下关街道四道口路2号京果商厦b座三层电玩城
子洋联盟长沙雨花店
湖南省长沙市雨花区运达汇商场负一楼子洋联盟
环游嘉年华乌鲁木齐汇嘉店
新疆维吾尔自治区乌鲁木齐新市区北京中路汇嘉三楼环游嘉年华超乐场
星际传奇深圳前海欢乐港湾店
广东省深圳市宝安区新安街道海滨社区欢乐港湾2号东L1-027
米乐多邯郸丛台店
河北省邯郸市丛台区苏曹乡天虹广场米乐多家庭中心
大玩家天津东丽万达店
天津市东丽开发区先锋东路6号万达广场3F
环游嘉年华西安环球港店
陕西省西安市新城区韩森路幸福林带环球港C-D3026
萌漫公社衡阳蒸湘店
湖南省衡阳市蒸湘区融冠大食代3楼萌漫公社
米其动漫茂名店
广东省茂名市茂南区河东街道1959文创街米其动漫城
韩多多梦幻城威海店
山东省威海市经区韩乐坊南首一层韩多多梦幻城
极客森超乐场西安店
陕西省西安市雁塔区雁展路1111号万象天地
淘乐幻享许昌魏都店
河南省许昌市魏都区莲城大道新田360广场三楼
风云再起成都凯德店
四川省成都市金牛区凯德广场负一楼
大玩家大连周水子万达店
辽宁省大连市甘井子区虹韵路6号机场万达1B层
晴空超乐场揭阳普宁店
广东省揭阳市普宁环市北路COCOCity购物广场E栋4层
聚玩堂上海龙之梦店
上海市长宁区长宁路龙之梦购物中心五楼
嘻游玩家德州店
山东省德州市德城区天衢街道办事处大学西路1566号银座商城318嘻游玩家游乐场
沭阳宝乐城宿迁沐阳店
江苏省宿迁市沭阳县人民中路金王朝大酒店一楼沭阳宝乐城
星乐荟上海松江店
上海市松江区佘月路27号宝乐汇生活广场2楼星乐荟
真快活武汉硚口荟聚店
湖北省武汉市硚口区荟聚中心3楼
骇客码头昆明五华百大店
云南省昆明市五华区南屏街百大新天地6A
游壹番柳州兴隆店
广西省柳州市中山中路2号兴隆大厦负一层、负一层夹层
嗨玩队长武汉光谷店
湖北省武汉市洪山区光谷步行街一期D区4楼
大玩家赤峰松山万达店
内蒙古赤峰市松山区万达广场3楼大玩家
梦幻雨林铜仁大十字店
贵州省铜仁市大十字西门悦萃城二楼梦幻雨林娱乐中心
大玩家齐齐哈尔万达店
黑龙江省齐齐哈尔市建华区新江路万达广场三楼大玩家
星际传奇深圳海雅缤纷城店
广东省深圳市宝安区建安1路海雅缤纷城4楼星际传奇
疯狂牛仔城佛山南海店
广东省佛山市南海区广佛路嘉洲广场3楼疯狂牛仔城
星悦蓝海欢乐园苏州店
江苏省苏州市姑苏区石路街道广济南路219号天虹九楼星悦蓝海欢乐园
大玩家西宁城北万达店
青海省西宁市城北区宁张路68号万达广场2楼大玩家
企萌电玩上海浦东店
上海市浦东新区秀浦路668号3楼303新田360广场康桥店
超级星座哈尔滨香坊店
黑龙江省哈尔滨市香坊区哈平路凯旋新生活购物广场三楼超级星座
宠娃星球天津武清店
天津市武清区杨村街道泉州北路西侧住总大光明中心三层宠娃星球
AREA-51区超级乐园青岛永旺店
山东省青岛市黄岛区漓江西路永旺梦乐城1楼东馆AREA-51区超级乐园
大玩家拉萨堆龙德庆万达店
西藏自治区拉萨市堆龙德庆区柳梧万达广场2楼大玩家
大玩家哈尔滨太平桥百盛店
黑龙江省哈尔滨市太平桥百盛商场3楼大玩家
热带雨林邯郸丛台店
河北省邯郸市丛台区人民东路环球中心美乐城五层热带雨林主题乐园
天一动漫邢台襄都店
河北省邢台市襄都区天一城B座三层天一亲子动漫乐园
部落酷玩金华永康店
浙江省金华市永康市西城街道解放街188号宝龙广场A馆3楼部落酷玩
部落酷玩温州瓯海店
浙江省温州市瓯海区娄桥街道瓯海大道1299号三楼3010-3013
天空之城龙岩新罗万宝店
福建省龙岩市新罗区龙岩大道万宝广场三楼天空之城
汤姆熊上海闵行南方店
上海市闽行区沪闵路7388号南方商城一区五楼汤姆熊
邢台信都知止商城
河北省邢台市信都区冶金南路物兴广场知止商城
潮玩世界太原万柏林店
山西省太原市万柏林区公元时代购物中心2楼潮玩世界
秀斗城邦绍兴越城店
浙江省绍兴市越城区金帝银泰城地下一层秀斗城邦
汤姆熊惠州惠东大润发店
广东省惠州市惠东县平山街道华侨城大润发一楼汤姆熊王国
汤姆熊武汉销品茂店
湖北省武汉市徐东大街18号销品茂4楼汤姆熊
大玩家牡丹江西安万达店
黑龙江省牡丹江市西安区新安街万达广场三楼大玩家
第四元素深圳罗湖IBC店
广东省深圳市罗湖区布心路3008号IBC商场二楼201第四元素家庭娱乐中心
梦想嘉年华抚州临川店
江西省抚州市临川区赣东大道万象新城梦想嘉年华潮玩店
晴空超乐场潮州枫溪店
广东省潮州市枫溪区财富中心b区三楼晴空超乐场
一同潮玩AcePlay东莞店
广东省东莞市塘厦镇天虹购物中心4楼一潮同玩AcePlay
哈雷慧淄博张店银泰城店
山东省淄博市张店区四宝山街道银泰城3楼哈雷慧6号星球电玩城
爱玩嘉年华重庆江北二店
重庆市江北区观音桥1楼大融城爱玩嘉年华
潮玩社潍坊坊子泰华城店
山东省潍坊市坊子区凤凰街泰华城潮玩社
酷动乐园德州澳德乐店
山东省德州市经济开发区澳德乐时代广场酷动乐园
卡通尼武汉硚口荟聚店
湖北省武汉市硚口区汇聚4楼卡通尼乐园
大玩家揭阳榕城万达店
广东省揭阳市榕城区万达广场三楼大玩家超乐场
星际传奇合肥高新店
安徽省合肥市高新区望江西路888号三层3018号星际传奇
猩派玩家汕头潮阳店
广东省汕头市潮阳区谷饶镇阳光百汇购物广场猩派玩家
玛丽奥电玩南宁兴宁店
广西省南宁市兴宁区步行街红星金逸影城1楼玛丽奥电玩城
卡通尼南京虹悦城店
江苏省南京市雨花台区应天大街619号虹悦城3楼卡通尼乐园
大玩家北京华联万柳店
北京市海淀区海淀街道巴沟路2号华联万柳购物中心二楼大玩家
都市玩家杭州萧山宝龙店
浙江省杭州市萧山区建设一路宝龙城市广场3楼都市玩家
卡通尼苏州常熟永旺店
江苏省苏州市常熟市东南大道168号永旺梦乐城
热带雨林深圳宝安店
广东省深圳市宝安区翠岗西路方元城3楼热带雨林主题乐园
卡通尼武汉金银潭店
湖北省武汉市东西湖区永旺金银潭店4F卡通尼乐园
骇客码头昆明五华吾悦店
云南省昆明市五华区王筇路吾悦广场三楼3037商铺
星空间动漫宝鸡高新店
陕西省宝鸡市渭滨区高新大道高新天下汇4F西厅星空间动漫游艺体验中心
娱乐至上成都成华店
四川省成都市成华区凯德广场魅力城三楼娱乐至上
玩家英雄珠海金湾华发商都店
广东省珠海市金湾区三灶镇金河东路720号金湾华发商都中心C馆C2002-C2003商铺
央哥之城沈阳沈河店
辽宁省沈阳市沈河区 北中街路123-2号央哥之城
乐游悦动青岛黄岛吾悦店
山东省青岛市黄岛区滨海大道2888号吾悦广场c区2楼2018乐游悦动
沃克公园温州乐清正大店
浙江省温州乐清市正大广场二楼沃克公园
星际传奇瑞虹天地太阳宫店
上海上海市虹口区嘉兴路街道瑞虹路181号
跨特世界北京长阳龙湖店
北京市长阳镇熙悦龙湖天街B馆4F
动感无限沧州店
河北省沧州市沧州商城二楼北区 动感无限
都市玩家西安太白印象城店
陕西省西安市碑林区太白印象城负一楼
菲游乐杭州丁桥龙湖天街店
浙江省杭州市江干区丁兰街道丁城路515号A幢4楼02号
城市英雄西安熙地港店
陕西省西安市未央区凤城七路熙地港购物中心五楼
晴空乐园汕头群光店
广东省汕头市龙湖区长平路98号群光汇3楼
天空之城上海青浦吾悦店
上海青浦区淀山湖大道218号吾悦广场2楼
星河部落川沙百联店
上海市浦东新区5398号3楼
大玩家天门万达店
湖北省天门市竟陵街道陆羽大道万达广场二楼大玩家
环游嘉年华东莞运动汇一城店
广东省东莞市南城街道鸿福路200号第一财富中心5栋103-202室
星际玩家耒阳店
湖南省衡阳市耒阳市蔡子池街道环球100五一电影城负一楼星际玩家
漫奈斯广州白云金铂店
广东省广州市白云区同和金铂广场2楼漫奈斯
欢乐哆贺州彰泰新旺角店
广西贺州市建设中路129号彰泰新旺角b1-8-1013欢乐哆
51区天津南开熙悦汇店
天津天津市南开区熙悦汇购物中心3F 51区超级乐园
酷客领域沧州吾悦店
河北省沧州市运河区吾悦广场二楼酷客领域电玩城
星际传奇汕头万象城店
广东省汕头市龙湖区长平路95号华润大厦万象城L5A08和L5A16号商铺
梦幻之城石嘴山店
宁夏省石嘴山市惠农区东大街5号万德隆广场三楼
星际传奇合肥庐阳万科店
安徽省合肥市庐阳区大杨镇万科广场三楼星际传奇
风云再起上海嘉定百联店
上海市嘉定区澄浏中路3172号3层003室
城市英雄长沙大悦城店
湖南省长沙市开福区湘江北路北辰三角洲大悦城三楼
幸运星惠州惠城金山湖店
广东省惠州市惠城区隆生金山湖商业中心三楼幸运星家庭娱乐中心
加菲队长衡阳店
湖南省衡阳市衡阳县蒸阳大道与培元路交汇处步步高新时代广场二楼
乐游悦动临沂齐鲁吾悦店
山东省临沂市兰山区汶河路与济南路交汇齐鲁吾悦广场4楼
星际传奇合肥蜀山万象城店
安徽省合肥市蜀山区潜山路华润万象城四楼星际传奇
美乐彼徐州云龙万科店
江苏省徐州市云龙区和平大道118号万科新淮中心4楼
星际传奇杭州萧山奥体店
浙江省杭州市萧山奥体印象城星际传奇
1号机长常德武陵店
湖南省常德市武陵区武陵大道998号和瑞欢乐城3楼3030号
明日世界昆明和谐店
云南省昆明市五华区和谐广场C座二楼天空之城明日世界
部落酷玩温州店
浙江省温州市空港宝龙广场店二楼017
部落酷玩宁波奉化宝龙店
浙江省宁波市奉化区岳林街道金海路156号奉化宝龙广场2楼016商铺
极客森张家港吾悦广场店
江苏省苏州市张家港市金港大道338号吾悦广场三楼311号极客森
汤姆熊济南槐荫店
山东省济南市槐荫区经七纬十二路和谐广场3楼汤姆熊
明日世界昆明新西南店
云南省昆明市五华区人民中路昆百大新西南东区4F天空之城明日世界
极客森芜湖镜湖店
安徽省芜湖市镜湖区华强吾悦广场三楼极客森
明日世界昆明呈贡店
云南省昆明市呈贡区七彩云南第壹城南区地下负一层Q–B2–B F008号商铺天空之城明日世界
星世纪蚌埠蚌山吾悦店
安徽省蚌埠市蚌山区解放路吾悦广场二楼2023铺星世纪电玩娱乐中心
超级玩咖沈阳沈北万达店
辽宁省沈阳市沈北新区蒲昌路万达广场二楼超级玩咖
快乐电堂齐齐哈尔百大店
黑龙江省齐齐哈尔百货大楼6楼快乐电堂动漫娱乐中心
风云再起沈阳苏宁广场店
辽宁省沈阳市和平区苏宁广场6F风云再起
朗玩深圳壹方天地店
广东省深圳市龙华区龙华街道景龙社区壹成中心花园三区E座壹方天地C区L1-001A~L4-001
AREA-51区烟台福山永旺店
山东省烟台市福山区永旺梦乐城302b
天空之城南宁良庆宜家店
广西省南宁市良庆区平乐大道12号宜家家居天空之城游乐体验世界
纷纷乐园泰州泰兴新天地店
江苏省泰州市泰兴市国庆东路171号鼓楼新天地3楼01-02纷纷乐园
星世纪岳阳步行街店
湖南省岳阳市巴陵西路康星百货北门负二楼星世纪
第一回合杭州金沙印象城
浙江省杭州经济技术开发区下沙街道金沙大道97号金沙印象城
极客森深圳罗湖宝能店
广东省深圳市罗湖区宝安北路3008号宝能中心4层4017极客森超乐场
万有引力沈阳欧亚长青城店
辽宁省沈阳市浑南区长青南街6甲号欧亚长青城
极客森包头吾悦店
内蒙古包头市东河区吾悦广场3楼极客森
汤姆熊苏州大悦城店
江苏省苏州市相城区元和街道御窑路1999号大悦春风里购物中心三楼
星际传奇成都高新环球中心店
四川省 成都市高新区天府大道北段1700号4FB02星际传奇
超时空河源东源万达店
广东省河源市东源县万达广场3F-B铺超时空乐场
大玩家梧州万秀万达店
广西省梧州市万秀区高旺路1号万达广场二楼大玩家
风云再起马鞍山花山店
安徽省马鞍山市花山区雨山东路863号印象汇3楼风云再起
酷乐电玩城拉萨经开店
西藏自治区拉萨市经济技术开发区格桑路18号海鑫国际商业广场三楼
V动地带兴城兴隆大家庭店
辽宁省兴城市兴隆大家庭五楼V动地带电玩城
第一回合温州印象城店
浙江省温州市鹿城区南汇街道府东路333号温州印象城负一层
星际传奇上海松江印象城店
上海市松江区广富林路1788弄松江印象城3楼星际传奇L337
NATAKIDS银川兴庆吾悦店
宁夏回族自治区银川市兴庆区吾悦广场3楼NATAKIDS
星际传奇宁波环宇城店
浙江省宁波市鄞州区江东南路689号环宇城购物中心A栋3楼
超级星座昆明官渡海乐店
云南省昆明市官渡区永中路海乐世界购物中心3层超级星座游戏体验中心
大玩家武汉新洲万达店
湖北省武汉市新洲区阳逻街柴泊大道119号万达广场2楼大玩家
城市英雄株洲芦淞店
湖南省株洲市芦淞区美佳you范mall-3楼城市英雄
星际传奇珠海宝龙城店
广东省珠海市香洲区金鼎高新宝龙城3楼
大玩家哈尔滨道里悦荟店
黑龙江省哈尔滨道里区友谊路187号悦荟广场C座一楼
合电占金华义乌宝龙店
浙江省金华市义乌市青口宝龙广场合电占动漫娱乐空间
MY泛娱乐中心鹤岗红星店
黑龙江省鹤岗市工农区新南街道解放路246号红星万象城3楼
万有引力北京顺义店
北京市顺义区新顺南大街隆化购物中心五楼万有引力
大玩家佛山顺德大良万达店
广东省佛山市顺德区大良街道 南江社区南霞新路9号顺德美的万达广场内购物中心2F层2F-A铺
真快活武汉洪山店
湖北省武汉市洪山区文楚路维佳佰港城3楼
大玩家贵阳南明亨特店
贵州省贵阳市南明区机场路18号亨特城市广场176号商铺大玩家
星际传奇贵阳观山湖华润店
贵州省贵阳市观山湖区华润万象汇星际传奇
小酋长湘潭雨湖店
湖南省湘潭市雨湖区九华步步高新天地商场四楼4002小酋长动漫游戏
大玩家厦门集美灌口万达店
福建省厦门市集美区灌口镇石笔路6号万达广场三楼大玩家
星世纪合肥滨湖唯品会店
安徽省合肥市滨湖唯品会三楼星世纪
风云再起上海宝山日月光店
上海市宝山区沪太路1933号日月光中心三层
萌多拉张家港金港店
江苏省张家港市金港镇崇真路中骏世界城东门2楼萌多拉
朗玩上海宝山日月光店
上海市宝山区沪太路1933号日月光中心三楼朗玩娱乐中心
风云再起南宁青秀爱琴海店
广西壮族自治区南宁市青秀区南湖街道民族大道181号爱琴海城市广场二楼
风云再起上海龙阳广场店
上海市浦东新区龙阳路2000号2楼201室风云再起
风云再起昆明盘龙爱琴海店
云南省昆明市盘龙区瑞鼎城爱琴海购物公园4楼
大玩家咸阳秦都万达店
陕西省咸阳市秦都区人民路万达广场二楼大玩家
摩儿大狂欢金华兰溪宝龙店
浙江省金华市兰溪市兰江街道振兴路299号宝龙广场M1-L2-009号商铺
大玩家福州苍山白湖亭万达店
福建省福州市仓山区盖山镇则徐大道398号白湖亭万达广场2楼大玩家
一起玩烟台龙口保利店
山东省烟台市龙口市南山路保利广场一起玩
奕部落金华义乌爱琴海店
浙江省金华市义乌市廿三里街道爱琴海购物公园三楼奕部落科技动漫城
娱乐至上成都新都店
四川省成都市新都区旭辉广场4楼
风云再起武汉江汉路站店
湖北省武汉市江汉区地铁二号线江汉路站JH2-009风云再起
惠州鹅窝KATTYUU
广东省惠州市惠城区桥东街道方直君御18栋2层206-207鹅窝KATTYUU
天空之城佛山顺德悦然店
广东省佛山市顺德区北滘镇诚德路美的悦然广场3楼天空之城
星际传奇武汉壹方南馆店
湖北省武汉市江岸区中山大道壹方南馆三楼星际传奇
一同潮玩AcePlay惠州博罗店
广东省惠州市博罗县罗阳镇天虹购物中心负一楼一同潮玩
环游嘉年华成都武侯店
四川省成都市武侯区仁和新城购物中心5楼
Mestage郑州郑东云尚店
河南省郑州市郑东新区商都路63号（云尚购物中心）B1层B1075
星河部落海宁长安奥特莱斯店
浙江省海宁市长安镇启潮路199号奥特莱斯二期1号楼3楼E301-E314星河部落电玩城
深圳市大中华国际交易广场店
广东省深圳市福田区福华一路大中华国际交易广场G层中心广场
第一回合湖州吴兴爱山银泰店
浙江省湖州市吴兴区南街558号爱山银泰城2楼第一回合
星际传奇杭州萧山银泰店
浙江省杭州市萧山区新塘街道通惠南路667号银泰百货3楼星际传奇
星潮电玩合肥新站店
安徽省合肥市新站区梦溪路与学府路交口黉街6号楼202~203
极力特梦幻城惠州惠东天虹店
广东省惠州市惠东县华侨城大道15号天虹商场三楼
酷漫地带成都新都苏宁店
四川省成都市新都区新都大道苏宁易购广场3楼酷漫地带
潮范动漫城社濮阳南乐店
河南省濮阳市南乐县兴华路与一行路交叉口新壹城购物中心4楼
乐趣游戏空间郑州郑东店
河南省郑州市郑东新区平安大道197号永和时光里乐趣游戏空间电玩城
乐酷电玩景德珠山金鼎店
江西省景德镇市珠山区广场南路金鼎购物广场1楼
嘻哈传奇济宁任城店
山东省济宁市任城区运河城嘻哈传奇
天空之城南通崇川万象城店
江苏省南通市崇川区北大街111号万象城四楼天空之城
王者之风秦皇岛海港店
河北省秦皇岛市海港区世纪港湾三楼王者之风
欢悦游艺武汉江夏店
湖北省武汉市江夏区藏龙岛光谷青年汇5号楼二楼欢悦游艺互动体验中心
独山子美美影城克拉玛依店
新疆维吾尔自治区克拉玛依市独山子区西宁路街道大庆东路34号文化中心影院
梦想嘉年华临沂兰山店
山东省临沂市兰山区解放路女人街A109梦想嘉年华
真快活北京西城coohooMax
北京市西城区西单北大街130号华威大厦五楼
城市英雄长沙岳麓金茂店
湖南省长沙市岳麓区天顶街道金茂览秀城LG层28号
王者之风邢台信都店
河北省邢台市信都区中华大街街道逗号立方广场四楼王者之风
IN竞技现场武汉洪山光谷店
湖北省武汉市洪山区光谷世界城德国风情街IN竞技现场
疯狂牛仔城佛山三水店
广东省佛山市三水区西南街道三水广场三楼疯狂牛仔城
super101电玩城吉首店
湖南省吉首市镇溪街道和盛堂一楼01号super101电玩城
炫e潮玩太原万通广场店
山西省太原市柳巷街道柳巷南路63号万通购物广场一层141号
第一回合杭州滨江宝龙店
浙江省杭州市滨江区宝龙广场三楼第一回合
51区超级乐园济南印象城店
山东省济南市历城区花园路136号印象城5楼L519-L522
疯狂牛仔城广州番禺大石店
广东省广州市番禺区大石镇万民广场2层
纷享星球泉州安溪店
福建省泉州市安溪县财富广场纷享星球
51区青岛市北悦荟广场店
山东省青岛市市北区人民路269号悦荟广场5楼
威尼斯辽源东旺店
吉林省辽源市步行街东旺集贸三楼威伲斯电玩馆
PPG潮玩汇九江店
江西省九江市浔阳区联盛九龙广场五楼PPG潮玩汇
熊孩子乐园安庆望江店
安徽省安庆市望江县云珠国际广场三楼
汤姆熊上海杨浦合生汇店
上海市杨浦区翔殷路1099号合生汇购物广场2楼L2-16汤姆熊欢乐世界
爱玩嘉年华重庆合川店
重庆市合川区合阳城街道财富广场LG层
世纪欢乐城长治潞州店
山西省长治市潞州区长治高新技术开发区保宁门西街金威店三楼
城市英雄岳阳步行街店
湖南省岳阳市岳阳楼区步行街康星百货负一楼
SMILEPLAY佛山南海店
广东省佛山市南海区大沥镇瑞安购物中心三楼SMILEPLAY泛娱乐体验中心
蓝鲸乐园宁德东侨店
福建省宁德市东侨经济开发区万安东路6号德润二期9号楼德润尚街商业广场2层
嘻游嘉年华诸暨店
浙江省诸暨市暨阳街道青悦城2-20嘻游嘉年华
酷儿游乐金华婺城店
浙江省金华市婺城区新狮街道迎宾大道699号金华万固广场2楼212号
爱玩嘉年华重庆渝北店
重庆市渝北区仙桃街道渝北区仙桃街道中央公园大悦城4楼爱玩嘉年华
潮玩社潍坊青州店
山东省潍坊市青州市泰华城一楼潮玩社
偶予潮玩潍坊潍城店
山东省潍坊市潍城区北宫西街清平路交叉口中百奥莱四楼偶予潮玩
大玩家贵阳观山湖万达店
贵州省贵阳观山湖云潭南路交汇处万达广场2f大玩家
一同潮玩连云港店
江苏省连云港苏宁广场三楼
大玩家连云港海州万达店
江苏省连云港市海州区新东街道凌州东路7号万达广场2F大玩家超乐场
大玩家广州新塘万达店
广东省广州市增城区新塘镇新塘万达广场2楼大玩家
大玩家苏州太仓万达店
江苏省苏州市太仓市上海东路188号万达广场二楼大玩家
大玩家内江高新万晟汇店
四川省内江市高新区汉安大道东段万晟汇购物中心一号门二楼大玩家超乐场
爱玩嘉年华福州闽侯店
福建省福州市闽侯县上街镇东百城永嘉天地1楼爱玩嘉年华
大玩家抚顺新抚万达店
辽宁省抚顺市新抚区浑河南路中段56号万达广场二楼
城市英雄重庆九龙坡喜盈门店
重庆市九龙坡区渝州路街道奥体路1号喜盈门范城2楼
汤姆熊德阳广汉店
四川省德阳市广汉市中山大道南一段10号百伦广场4楼
大玩家九江濂溪万达店
江西省九江市濂溪区万达广场三楼大玩家
大玩家重庆万州万达广场店
重庆市万州区高笋塘街道北滨大道998号万达二楼大玩家超乐场
大玩家廊坊广阳万达店
河北省廊坊市广阳区万达广场三楼大玩家超乐场
大玩家包头青山万达店
内蒙古自治区包头市青山区钢铁大街万达广场二楼大玩家
大玩家南昌青山湖万达店
江西省南昌市青山湖区京东南大道万达广场二楼大玩家
天空之城广州白云店
广东省广州市白云区望岗鹤龙二路85号金铂天地二楼天空之城
天空之城佛山南海大沥店
广东省佛山市南海区大沥镇广佛路黄岐金铂天地二楼天空之城游乐体验世界
天空之城佛山南海金沙洲店
广东省佛山市南海区金沙洲建设大道金铂天地3楼天空之城游艺世界
303Lab天津宁河店
天津市宁河区芦台镇商业道60高百荣商厦303LAB
大玩家山东泰安万达店
山东省泰安市泰山区泰山大街万达广场三楼大玩家超乐场
真快活洪山光谷大悦城
湖北省武汉市洪山区光谷大悦城真快活
大玩家台州经开万达店
浙江省台州市经开万达三楼家庭娱乐中心
大玩家丹东振兴万达店
辽宁省丹东市振兴区锦山大街万达广场大玩家超乐场
大玩家大庆萨尔图万达店
黑龙江省大庆市萨尔图万达二楼大玩家
大玩家石河子万达店
新疆维吾尔自治区石河子市开发区万达广场三楼C大玩家
大玩家安庆迎江吾悦店
安徽省安庆市迎江区菱湖南路1号新城吾悦广场三楼大玩家
乐欣谷电玩汕头潮阳店
广东省汕头市潮阳区和平镇紫南路3号万欣广场3楼
乐为先徐州邳州店
江苏省徐州市邳州市新苏购物中心四楼乐为先
希美潮玩邯郸丛台店
河北省邯郸市丛台区环球中心
阿凡达爱玩荟吕梁孝义店
山西省吕梁市孝义新义街道新义街255号华美新天地三层北片
迪咔嗨玩嘉年华长垣店
河南省长垣市银河新天地二楼
大风车威海环翠威高广场店
山东省威海市环翠区新威路威高广场嘉禾天地负一楼
纷享星球泉州石狮店
福建省泉州市石狮市九二路长银路交叉口泰禾广场2楼L211纷享星球电玩
王者之风邢台襄都万达店
河北省邢台市襄都区万达广场二楼王者之风
大玩家济南高新万达店
山东省济南市高新区万达广场三楼大玩家
部落酷玩无锡宜兴宝龙店
江苏省无锡市宜兴市丁蜀镇白宕北路200号宝龙广场二楼部落酷玩
天空之城清远清城万达店
广东省清远市清城区凤城街道湖西路万达广场1号门3楼天空之城
大海豚乐园湛江霞山店
广东省湛江市霞山区新园街道人民大道南116号鼎盛广场购物中心五层大海豚乐园
美吉熊儿童乐园昌平店
北京市昌平区天通苑东三区2号楼
大玩家上海临港万达店
上海市浦东新区泥城镇临港万达广场二楼大玩家
星际传奇南宁江南店
广西壮族自治区南宁市江南区金凯路8号
炫动四方长春居然世界里店
吉林省长春市高新区居然世界里三楼炫动四方电玩城
美吉熊儿童乐园房山店
北京市房山区拱辰南大街7号院1号楼美吉熊儿童乐园
极限主场湛江吴川奥园店
广东省吴川市海滨大道奥园广场三楼极限主场
第一回合杭州余杭店
浙江省杭州市余杭区古墩路1888号永旺梦乐城3F第一回合
风云再起上海青浦百联店
上海市青浦区盈港路1616号百联购物中心2楼风云再起
风云再起南京软件谷店
江苏省南京市雨花台区中国南京软件谷软件大道109号雨花客厅EPARK购物中心3楼
星悦时光无锡江阴店
江苏省无锡市江阴市申港红豆万花城二楼星悦时光家庭娱乐中心
奇梦星球大同爱琴海店
山西省大同市城区武定北路爱琴海6层
晴天G-BOX潮玩社佛山南海店
广东省佛山市南海区桂城街道季华东路27号顺联公园里西座三楼晴天G-BOX潮玩社
一同潮玩深圳福田店
广东省深圳市福田区石夏北二街89号马成时代广场
爱玩星球郑州金水店
河南省郑州市金水区东风路瀚海海尚mall-B146号爱玩星球
酷哆啦长沙天心万家丽店
湖南省长沙市天心区万家丽南路暮云街道步步高广场二F酷哆啦家庭娱乐中心
风云再起上海虹口百联店
上海市虹口区曲阳路800号百联曲阳购物中心3楼风云再起
天空之城淮南田家庵八佰伴店
安徽省淮南市田家庵区朝阳中路八佰伴购物中心3楼最东侧
奇妙之城周口项城店
河南省周口市项城市恒太城2楼奇妙之城电玩城
寻游纪嗨众武汉江夏店
湖北省武汉市江夏区北华街九全嘉国际广场3楼
欢乐嘉时光绵阳安州店
四川省绵阳市安州区银河大道108号汇星广场四楼安州欢乐嘉时光电玩城
万德隆电玩城南阳理工店
河南省南阳市宛城区长江路万德隆超市
非玩不可重庆涪陵店
重庆市涪陵区泽胜中央广场一楼非玩不可游乐场
kikis其趣游乐广州白云店
广东省广州市白云区同和大道金铂天地2层kikis其趣游乐体验世界
成都极音音游体验馆
四川省成都市武侯区保利中心A座1515-1516
GGS创产音游窝
广东省佛山市三水区乐平镇三花路23号创产6楼
酷漫地带自贡自流井店
四川省自贡市自流井区华商爱琴海购物公园二楼酷漫地带
星奇多潮玩合肥蜀山店
安徽省合肥市蜀山区莲花社区正大广场四楼星奇多潮玩世界
奥康潮玩城滁州全椒店
安徽省滁州市全椒县奥康商业步行街新华街1号奥康潮玩城
星际梦想城重庆渝中店
重庆市渝中区解放碑街道八一路183号二层星际梦想城
星河奇迹佛山创产店
广东省佛山市禅城区季华四路创意产业园1号楼星河奇迹
骑士玩国长沙北辰凤凰海店
湖南省长沙市开福区晴岚路68号凤凰海购物公园二楼骑士玩国
1号机长常德澧县店
湖南省常德市澧县欢乐城22号入口1号机长超乐场
安吉美奇湖州安吉店
浙江省湖州市安吉县安吉大道城东美颂广场2幢3楼
酷奇绍兴越城店
浙江省绍兴市越城区塔山街道金帝银泰城1幢3F202
极限主场清远城市广场店
广东省清远市先锋中路城市广场三楼极限主场
风云再起兰州国芳百货店
甘肃省兰州市城关区广场南路4-6号国芳百货8楼风云再起
魔逗潮玩社恩施和润城店
湖北省恩施土家族苗族自治州恩施市和润城三楼
潮玩世纪娄底娄星店
湖南省娄底市娄星区氐星路春园步行街时尚春天一楼潮玩世纪家庭娱乐中心
晶灵玩家广州花都店
广东省广州市花都区永发路14号雅乐城晶灵玩家
极客森北京朝阳店
北京市朝阳区姚家园万象汇4楼L405极客森超乐场
思诺卡佛山南海新都汇店
广东省佛山市南海区大沥镇金茂大道6号南海新都会购物中心思诺卡俱乐部
绮绮王囯内蒙科尔沁店
内蒙古自治区通辽市科尔沁区科尔沁大街与平安路交汇处平安南区北门绮绮王囯
联华成都邛崃鼎盛时代店
四川省成都市邛崃市临邛镇朱水碾街281号附鼎盛时代广场联华精彩生活广场
八爪鱼重庆涪陵店
重庆市涪陵区中山路铂金国际写字楼4一1八爪鱼嘉年华
乐玩客潮玩城合川
重庆市合川区财富广场2楼乐玩客潮玩城
风云再起徐州鼓楼苏宁广场店
江苏省徐州市鼓楼区淮海东路29号苏宁广场3F326
大玩家龙岩上杭万达店
福建省龙岩市上杭县二环路金山路交叉口东南角万达广场二楼大玩家
天空之城重庆两江新区店
重庆市两江新区鸳鸯街道金渝大道58号馆-2F-24.25.26号天空之城
第8街潮玩安顺西秀古城店
贵州省安顺市西秀区小十字安顺古城A2号楼一层商铺
JAJAPOP一番赏天津和平店
天津市和平区南京路221号国际商场负一层JAJAPOP一番赏
第一回合嘉兴八佰伴店
浙江省嘉兴市南湖区中山路1360号嘉兴八佰伴购物中心B1层
星际传奇沈阳皇姑万象汇店
辽宁省沈阳市皇姑区崇山东路皇姑万象汇b1层星际传奇
冲锋熊猫南京江宁店
江苏省南京市江宁区百家湖1912冲锋熊猫
米吉姆宁波鄞州银泰店
浙江省宁波市鄞州区首南街道天童南路1088号句章东路999号银泰环球城内购物中心3F层
盐城酷玩空间青岛胶州店
山东省青岛市胶州市香港路277号A栋F39
UFOCENTER广州从化欣荣店
广东省广州市从化区欣荣时尚广场A区B栋2楼UFO-CENTER
奇奇乐园襄阳樊城万达店
湖北省襄阳市樊城区长虹路万达广场三楼奇奇乐园
The one电玩城嘉兴桐乡店
浙江省嘉兴市桐乡市梧桐街道公园路22号万嘉中心2楼电玩城
城市英雄长沙雨花喜盈门店
湖南省长沙市雨花区喜盈门范城3-8栋G层B1-326号城市英雄
星世纪娄底娄星万豪店
湖南省娄底市娄星区氐星路万豪城市广场2楼星世纪动漫游戏体验中心
大玩家巴中巴州经开万达店
四川省巴中市巴州区经开万达广场三楼大玩家
奇奇乐园襄阳樊城南国店
湖北省襄阳市樊城区长虹路泛悦4楼奇奇乐园
乐玩客遵义湄潭方圆荟店
贵州省遵义市湄潭县方圆荟购物中心乐玩客家庭娱乐中心
引力矩阵青岛胶州龙湖天街店
山东省青岛市胶州市海尔大道龙湖天街引力矩阵
都市玩家江汉路大润发店
湖北省武汉市江汉区江汉路大润发一楼都市玩家
奇奇乐园武汉硚口西汇店
湖北省武汉市硚口区解放大道387号南国西汇城市广场负一楼奇奇乐园
乐酷欢乐世界安顺店
贵州省安顺开发区南马广场乐酷欢乐世界
一同潮玩南昌旭辉店
江西省南昌市经开区蛟桥街道双港西大街旭辉Cmall4楼011号一同潮玩
奇奇乐园宜昌西陵CBD店
湖北省宜昌市西陵区夷陵大道58号CBD购物中心三楼奇奇乐园
城市玩家通辽科尔沁店
内蒙古通辽市科尔沁区太平洋商场一楼城市玩家大乐场
风云再起南京金茂览秀城店
江苏省南京市鼓楼区中央路201号金茂览秀城3楼
爱游乐第e玩家绍兴新昌店
浙江省绍兴市新昌县海洋城3层301爱游乐第e玩家
super101潮漫电玩绥化北林店
黑龙江省绥化市北林区中兴东大街世纪华辰五楼super101潮漫电玩
一同潮玩惠州惠城天益城店
广东省惠州市惠城区陈江街道天益城购物中心1期号门直上3楼001铺
鑫天空之城哈尔滨阿城区店
黑龙江省哈尔滨市阿城区鑫城街道印象城5楼鑫天空之城
乐玩客泸州大世界店
四川省泸州市迎晖路2号大世界1楼乐玩客潮玩城
神秘之境深圳横岗银信广场店
广东省深圳市龙岗区横岗街道银信广场二期三楼
佛山萌豚窝
广东省佛山市禅城区祖庙街道百花广场27楼2727号
牧童乐园威海环翠店
山东省威海市环翠区威高广场生活汇2楼 牧童乐园家庭娱乐中心
环游嘉年华珠海华发店
广东省珠海市香洲区珠海大道8号华发商都C馆三楼C3031号环游嘉年华
小洋人宝贝王保定雄县店
河北省保定市雄县购物广场二楼小洋人宝贝王
阿拉丁绥化北林春天店
黑龙江省绥化市北林区中兴春天购物广场4层阿拉丁电玩城
欢乐拾光清远汇利安店
广东省 清远市东湖路汇利安广场壹号3层商铺306-308号
大玩家金华永康万达店
浙江省金华市永康市东城街道长城西大道万达广场2楼大玩家
趣多多宿州泗县绿城深蓝店
安徽省宿州市泗县绿城深蓝中心商业楼三楼趣多多超乐空间
都市玩家襄阳樊城泛悦店
湖北省襄阳市樊城区泛悦四楼都市玩家
大玩家徐州云龙万达店
江苏省徐州市云龙区云龙万达2楼大玩家
大玩家宁德蕉城万达店
福建省宁德市蕉城区万达广场2号门2楼大玩家超乐场
酷豆番襄阳襄城店
湖北省襄阳市襄城区檀溪路306号美联购物中心一楼酷豆番电玩公社
大玩家莆田城厢万达店
福建省莆田市城厢区霞林街道荔华东大道8号万达广场4楼大玩家超乐场
大玩家如皋新城吾悦店
江苏省如皋市如城街道惠政路吾悦广场三楼大玩家
大玩家延吉万达店
吉林省延吉市公园街道万达广场二楼大玩家
大玩家泰州海陵万达店
江苏省泰州市海陵区济川路万达广场三楼大玩家
星际传奇苏州吴中店
江苏省苏州市吴中区吴郡路366歌林公园东区3楼星际传奇
城市英雄重庆渝中喜盈门店
重庆市渝中区袁家岗重庆喜盈门范城L2层
大凡曲靖麒麟店
云南省曲靖市麒麟区寥廓南路218美食城旁大凡欢乐馆
环游嘉年华乌鲁木齐时代广场店
新疆维吾尔自治区乌鲁木齐市天山区光明路39号时代广场3楼F3-037号环游嘉年华超乐场
大玩家超乐场乌海万达店
内蒙古自治区乌海市海勃湾区万达广场三楼大玩家超乐场
泷威嘉年华西安雁塔店
陕西省 西安市雁塔区崇业路凯德广场三楼泷威嘉年华
朗玩南京江宁金鹰店
江苏省南京市江宁区双龙大道1688号金鹰购物中心1F-3F
嘻品堂长沙天心中海店
湖南省长沙市天心区中意二路中海环宇城二楼嘻品堂乐园
城市英雄长沙雨花德思勤店
湖南省长沙市雨花区湘府中路18号德思勤城市广场三楼
量子攻略北京朝阳金隅嘉品店
北京市朝阳区东坝中路金隅嘉品mall3层量子攻略游戏体验中心
十二星球岳阳华容店
湖南省岳阳市华容县西正街步步高新天地十二星球
骇客码头昆明西山第壹城店
云南省昆明市西山区滇池路569号南亚风情第壹城A1栋3楼
漫步者新乡卫滨新都汇店
河南省新乡市卫滨区新都汇购物中心一楼漫步者家庭娱乐中心
乐翻天承德双桥店
河北省承德市双桥区酒仙庙路2号乐翻天游乐城
星世纪岳阳天虹店
湖南省岳阳市岳阳楼区东茅岭路42号天虹商场负一楼
酷玩空间盐城盐都店
江苏省盐城市盐都区西环路88号万达广场三楼酷玩空间
游戏大魔方修改高新宝龙店
广东省珠海市高新区宝龙广场三楼游戏大魔方
风云再起常州龙湖天街店
江苏省常州钟楼区五星街道勤业路295号龙湖天街3楼风云再起
星河奇迹漳州龙海万科店
福建省漳州市龙海区海澄镇万科广场四楼星河奇迹电子游艺厅
创游星际喀什明升国际广场店
新疆维吾尔自治区喀什地区喀什市库木代尔瓦扎街道克孜勒都维路喀什明升国际广场5楼创游星际电玩
星际战城邓州建业店
河南省邓州市建业360广场楼星际战城动漫竞技馆
天空之城东莞店
广东省东莞市东城东路229号星河城3F-302号商铺
大玩家东莞虎门万达店
广东省东莞市虎门镇万达广场3楼play1家庭娱乐中心
乐炫风福州闽侯永嘉天地店
福建省福州市闽侯县上街镇永嘉天地三楼乐炫风
梦幻之城南昌青云谱店
江西省南昌市青云谱区井冈山大道300号朗贤广场二楼梦幻之城
大玩家泉州晋江万达店
福建省泉州市晋江市梅岭街道世纪大道888号万达广场二楼肯德基旁大玩家
魔兜欢乐岛台州椒江店
浙江省台州市椒江区黄海公路5号宝龙城
天空之城南京建邺店
江苏省南京市建邺区云龙山路89号河西天街2楼2F一01号商铺
城市玩家阜阳颍泉店
安徽省阜阳市颍泉区香港财富广场新天地购物中心四楼A29号
摩兜欢乐岛湖州南浔店
浙江省湖州市南浔区吾悦广场三楼摩兜欢乐岛
骑士玩国长沙华创国际广场店
湖南省长沙市开福区芙蓉北路街道华创国际广场负一层南区骑士玩国
潮玩社济南历下龙湖天街店
山东省济南市历下区奥体西路龙湖天街5楼潮玩社
城市英雄渝北龙湖礼嘉天街店
重庆市渝北区龙湖礼嘉天街A馆负一楼
金思乐廊坊广阳店
河北省廊坊市广阳区新朝阳二期一楼金思乐
乐玩客潮玩城达州大竹店
四川省达州市大竹县煌歌广场一楼乐玩客潮玩城
小洋人宝贝王廊坊店
河北省廊坊市大城县鑫达新天地三楼
熊开心福州台江店
福建省福州市台江区上海街道万象九宜城二楼熊开心家庭娱乐
终爵游乐成都郫都店
四川省成都市郫都区蜀都太平洋四楼终爵游乐
SUPER101青岛市北店
山东省青岛市市北区辽阳西路366号丽达茂购物广场
茶窝新余渝水店
江西省新余市渝水区长青北路北湖公园东门堎上购物广场茶窝电竞音游休闲室
提莫玩本电竞酒店南京店
江苏省南京市鼓楼区云南北路28号
奇妙之城佛山高明店
广东省佛山市高明区荷富路801号钧明城三楼
凯尔游艺淮安清江浦店
江苏省淮安清江浦区淮海南路727号永业梦乐广场三楼凯尔游艺
第九区马鞍花山店
安徽省马鞍山市花山区星悦广场三楼01铺位第九区
超级星座哈尔滨阿城店
黑龙江省哈尔滨市阿城区庆客隆广场超级星座家庭娱乐中心
卡奇部落达州通州店
四川省达州市通川区西外镇罗浮广场4楼卡奇部落
布隆家族南阳卧龙店
河南省南阳市卧龙区梅溪街道新华城市广场三楼布隆家族儿童娱乐中心
聚玩堂益阳安化店
湖南省益阳市安化县东坪镇城南区元畅恒太城5楼聚玩堂
星河奇迹汕尾海丰店
广东省汕尾市海丰县蓝天广场三楼星河奇迹游乐体验馆
十二星球潮玩城吉首店
湖南省湘西自治州吉首市人民中路天虹购物中心四楼
爱尚潮玩沧州黄骅店
河北省沧州市黄骅市学院西路信源购物广场4楼
偶予电玩长沙岳麓店
湖南省长沙市岳麓区河西王府井商业广场6楼偶予电玩
潮玩社潍坊奎文店
山东省潍坊市奎文区银座商城
乐玩之星武汉江汉店
武汉市江汉区万松街街道武展东路金崇光时肖广场特1号负一楼乐玩之星动漫体验城
城市英雄西安龙首印象城店
陕西省西安市未央区未央路33号龙首印象城三楼
星世纪九江浔阳步行街店
江西省九江市浔阳区湓浦街道大中路步行街444号信华广场1号楼
趣玩家嘉兴南湖店
浙江省嘉兴市南湖区长水街道星河coco city2楼趣玩家
环游乐园永州零陵店
湖南省永州市零陵区芝山北路春天广场购物中心三楼环游乐园
51区超级乐园天津和平店
天津市和平区滨江道商业街143号
极限主场河源源城万隆城店
广东省河源市源城区中山大道218号万隆城3楼极限主场
Super101呼和浩特新城店
内蒙古自治区呼和浩特市新城区新华广场地铁站网红街H区第H005-H010/H030/H036潮漫电玩城
一号机长湘潭岳塘天虹商场店
湖南省湘潭市岳塘区天虹商场4楼一号机长超乐场
爱玩嘉年华涪陵店
重庆市涪陵区荔枝街道泽胜中央广场2楼爱玩嘉年华
杭州大悦城木马王国店
杭州市拱墅区隐秀中粮大悦城三楼
乐玩客重庆南岸万达店
重庆市南岸区江南大道8号南坪万达广场金街乐玩客潮玩城
风云再起北京西西友谊店
北京市西城区二环西单北大街109号西西友谊商城2层
潮玩社深圳光明万达店
广东省深圳市光明区万达广场4楼4011潮玩社电玩中心
晴空超乐场汕头龙湖苏宁店
广东省汕头市龙湖区长平路90苏宁广场第3F层302号商铺
大玩家晋城万达店
山西省晋城市城区钟家庄街道万达广场2楼大玩家
进珠游乐城三明三元店
福建省三明市三元区和仁新村44栋梅列大厦地下城进珠游乐城
天空之城安庆大观吾悦店
安徽省安庆市大观区市府路汇峰新城吾悅广场三楼天空之城
1号机长怀化溆浦万达店
湖南省怀化市溆浦县万达广场三楼3F-A
卡通尼东莞大朗店
广东省东莞市大朗镇名座广场项目里悦里购物中心商铺L3-001三楼卡通尼乐园
爱游乐第一玩家南京高淳店
江苏省南京市高淳区宝龙广场二楼爱游乐第一玩家
快乐佳游站丹阳店
江苏省丹阳市新民东路金鹰国际广场二楼快乐佳游站
邢台信都冀中能源
河北省邢台市信都区冀中能源5号楼5单元501
风云再起南京大观天地店
江苏省南京市鼓楼区建宁路300号大观天地2F-138号风云再起
维京传奇沈阳浑南店
辽宁省沈阳市浑南区智慧四街5号龙湖天街商场2楼42铺维京传奇
C站杭州余杭店
浙江省杭州市余杭区南苑街道迎宾路501号余之城生活广场186单元
汤姆熊成都锦江群光店
四川省成都市锦江区春熙南路南段8号群光广场7楼
酷豆番荆州沙市店
湖北省荆州市沙市区人信汇负一楼酷豆番电玩公社
星河部落台州临海银泰店
浙江省台州市临海市东方大道1号银泰城三楼星河部落乐园
快乐街区长沙开福金源店
湖南长沙开福区金泰路199号世纪金源购物中心F4
城市英雄重庆大学城店
重庆沙坪坝区熙街商业街C区1C-20城市英雄电玩城
欢悦天堂太空之城凯德西城店
湖北省武汉硚口区解放大道18号凯德西城4楼
嘉贝乐北京五道口店
北京市海淀区成府路28号五道口购物中心三层
构想星球厦门思明店
福建省厦门市思明区宝龙一城三楼构想星球电玩城
天空之城江苏沭阳店
江苏省宿迁市沭阳县吾悦广场二楼天空之城
超级英雄江西章贡店
江西省赣州市章贡区赣江街道超级英雄
真快活武汉经开永旺店
湖北省武汉市经济开发区江城大道388号B馆3楼真快活动漫体验中心
真快活芜湖银泰店
安徽省芜湖市弋江区中南街道利民西路189号银泰城二楼真快活
爱巴爱麻江津爱琴海店
重庆市江津区双福爱琴海购物公园3楼爱巴爱麻家庭娱乐中心
潮玩社诸城百盛店
山东省诸城市百盛广场二楼潮玩社
欢乐嘉时光绵阳茂业店
四川省绵阳市涪城区茂业百货三楼欢乐嘉时光电玩城
GoPlay潮玩中山石岐店
广东省中山市石岐区大信南路3号7卡GoPlay潮玩
潮玩世纪怀化鹤城店
湖南省怀化市鹤城区天星东路锦绣五溪商业广场8栋一层潮玩世纪家庭娱乐中心
大玩家莆田秀屿万达店
福建省莆田市秀屿区笏石镇万达广场3楼大玩家
超级星座昆明盘龙七彩店
云南省昆明市盘龙区白塔路399号七彩me town购物中心F3超级星座家庭娱乐中心
快乐星球呼和浩特新城喜悦店
内蒙古自治区呼和浩特市新城区喜悦广场3楼快乐星球
乐满堂常州金坛吾悦店
江苏省常州市金坛区南环二路1208号常州金坛新城吾悦广场3楼乐满堂
欢悦天堂武汉范湖万达店
湖北省武汉市江汉区范湖万达广场B区2F
嘻哈乐普宁美佳乐店
广东省普宁市流沙开心广场美佳乐3楼嘻哈乐动漫电玩中心
天空之城大理爱情海店
云南省大理市下关镇鸡足山路爱琴海购物公园2楼天空之城
乐玩客重庆观音桥店
重庆市观音桥步行街8号大融城LG层乐玩客潮玩城
天空之城南京浦口龙湖天街店
江苏省南京市浦口区文景路99号龙湖天街3楼天空之城
兔子团都市乐园苏州吴中店
江苏省苏州市吴中区木渎镇金山南路288号木渎影视城1号楼兔子团都市乐园
天空之城重庆江津双福店
重庆市江津区双福街道南北大道北段路390号天空之城游乐体验世界
图灵欢乐城绍兴柯桥店
浙江省绍兴市柯桥区钱清街道金帝星隆城三楼3022/3022一3
大玩小乐重庆江津店
重庆市江津区浒溪南路万达广场大玩小乐
PPG潮玩汇大同平城店
山西省大同市平城区绿地缤纷汇6号楼二层
梦想之城周口沈丘店
河南省周口市沈丘县快乐小镇三楼梦想之城家庭游乐中心
风云再起北京西单明珠店
北京市西城区横二条59号楼7层1－263号7025风云再起
米其动漫东莞虎门店
广东省东莞市虎门镇连升中路44号地标广场（天虹商场）2号楼1层
快乐星球动漫城邵阳禹忠华店
湖南省邵阳市隆回县桃花坪街道桃洪中路禹忠华商业楼地上第一层
真快活宜昌西陵吾悦广场店
湖北省宜昌市西陵区窑湾街道东山四路吾悦广场2楼真快活电玩城
第一回合厦门湖里海上世界店
福建省厦门市湖里区双狮西路海上世界购物中心2F-L222第一回合
天空之城南昌进贤吾悦店
江西省南昌市进贤县滨湖大道吾悦广场三楼Z08商铺
乖乖鼠南平建阳店
福建省南平市建阳区建发悦城三楼乖乖鼠游乐园
星际传奇南京万象天地店
江苏省南京市秦淮区中山南路666号万象天地3层L-318号星际传奇
M+娱乐空间南宁兴宁店
广西南宁市兴宁区朝阳路9号百盛步行街广场5楼M+娱乐空间
反斗乐园派长沙雨花星城店
湖南省长沙市雨花区中意一路与湘府路交叉口步步高星城天地L3-3046
super101青岛崂山店
山东省青岛市崂山区丽达广场super101
天空之城镇江丹阳店
江苏省镇江市丹阳市开发区吾悦广场三楼天空之城
次元奥义长沙雨花店
湖南省长沙市雨花区洞井街道湘府中路48号高升大汉悦中心1栋1层1002号次元奥义电玩潮玩
玩美攻略济南历下店
山东省济南市历下区泉城路111号华典大厦玩美攻略潮玩街区（休闲娱乐）
星际传奇东莞万象汇店
广东省东莞市松山湖万象汇F314星际传奇
可多梦北京丰台店
北京市丰台区南四环西路76号花乡奥莱村13号楼13101-B号
麦兜熊杭州上城万泰店店
浙江省杭州市上城区万泰城2楼麦兜熊潮玩空间
欢悦天堂武汉江汉南国北都泛悦店
湖北省武汉市江汉区姑嫂路南国北都泛悦城市广场三楼欢悦天堂南国店
彩虹王国汕尾海丰天虹店
广东省汕尾市华耀城海丰天虹购物中心
多乐世界秦皇岛海港店
河北省秦皇岛市海港区乐都汇4层多乐世界
夏意乐园动漫城增城店
广东省广州市增城区东汇城大润发二楼出口
丰华动漫湛江赤坎店
广东省湛江市赤坎区椹川大道376号湛江印象汇B1-29~33号丰华动漫
趣玩时光冷水江步步高店
湖南省冷水江市步步高广场三楼
万有引力沈阳盛京大东城店
辽宁省沈阳市大东区东陵西路37号4f万有引力盛京大东城店
嘻品堂武汉青山印象城店
湖北省武汉市青山区印象城3楼L3-13B商铺嘻品堂
威龙传奇济南华山环宇城店
山东省济南市将军路华山环宇城
比特王台州温岭宝龙店
浙江省台州市温岭市中心大道宝龙广场3楼比特王欢乐世界
幻游嘉年华郑州二七店
河南省郑州市二七区德化街100号百年德化风情购物公园负一层F100号郑州幻游嘉年华游乐体验中心
维京传奇沈阳沈河环球汇店
辽宁省沈阳市沈河区青年大街268号前海环球汇246铺维京传奇
你我家园宁德霞浦店
福建省宁德市霞浦县福宁大道88号s1幢方圆荟三层3001你我家园娱乐中心
童年搭档重庆江北店
重庆市江北区观音桥天天尚街童年搭档
万德隆南阳唐河店
河南省南阳市唐河县建设路中段泗洲宾馆旁万德隆唐河购物中心电玩城
魔方MIX北京亦庄华联店
北京市亦庄开发区荣华中路力宝华联购物中心3楼魔方MIX家庭娱乐中心
嗨玩社赣州万达店
江西省赣州市经济开发区金岭东路万达商场二楼
魔方MIX北京顺义华联店
北京市顺义区新顺南大街8号华联购物中心3楼魔方MIX家庭娱乐中心
Tizuka音游窝
广东省潮州市湘桥区福安路新居乐花园
小房子广州增城挂绿广场店
广东省 广州市增城区荔城街挂绿路2号挂绿广场A2商业区域小房子亲子游乐园
梦幻之城中山店
广东省中山市中山古镇华丰汇三楼梦幻之城
量子攻略北京大兴旧宫店
北京市大兴旧宫住总万科广场五楼量子攻略
咔奇超乐场石家庄长安店
河北省石家庄市长安区北国先天下6楼咔奇超乐场
奇妙之城南阳方城店
河南省南阳市方城县大裕城购物中心奇妙之城电玩城
泛时空成都武侯店
四川省成都市武侯区天府大道北段1777号招商大魔方三楼3028泛时空
大玩家西安大融城店
陕西省西安市未央区大融城3楼大玩家
汤姆熊上海闵行虹桥天地店
上海市闵行区新虹街道申长路688号虹桥天地购物中心3楼汤姆熊
第一回合渝中龙湖天街店
重庆市渝中区龙湖天街E馆5楼第一回合
白月光太仓店
江苏省太仓市太仓大道115号青草巷广场b1-2白月光沉浸式剧本杀
酷漫地带成都金牛龙湖天街店
四川省成都市金牛区龙湖上城天街三楼酷漫地带
蓝波湾重庆北碚店
重庆市北碚区双元大道国泽生活广场一楼蓝波湾欢乐世界
迪芝尼梧州金苑梦之岛店
广西壮族自治区梧州市长洲区新兴三路3号梦之岛购物广场市政广场店3楼迪芝尼主题乐园
真快活武汉梦时代店
湖北省武汉市武昌区武珞路628号武商梦时代B座801真快活电玩
爱玩嘉年华沙坪坝炫地店
重庆市沙坪坝区三峡广场炫地购物中心负一楼爱玩嘉年华
真快活鄂州鄂城吾悦店
湖北省鄂州市鄂城区临空经济区大桥路吾悦广场2楼Z202铺真快活电玩城
1号机长无锡梁溪店
江苏省无锡市梁溪区广南路万达广场2楼1号机长
天空之城嘉兴桐乡吾悦店
浙江省嘉兴市桐乡市梧桐街道振兴东路439号吾悦广场三楼
菲菲羊台州温岭店
浙江省台州市温岭市银泰城三楼
潮玩社临沂兰陵万达店
山东省临沂市兰陵县万达广场3楼潮玩社
一号机长长沙岳麓店
湖南省长沙市岳麓区茶子山东路112号凯德一中心L2一号机长
欢悦天堂武汉东湖光谷天地店
湖北省武汉市东湖高新区关山大道光谷天地2楼欢悦天堂
泛时空电玩绍兴越城店
浙江省绍兴市越城区府山街道国金大悦城L3-15.16泛时空电玩城
真快活武汉白沙天街店
湖北省武汉市烽胜路龙湖天街A馆4楼真快活Coohoomax
幸运星上饶信州店
江西省上饶市信州区北门街道凤凰东大道89号天虹购物中心3楼3005幸运星乐园
大玩家扬州江都万达店
江苏省扬州市江都区仙女镇新都北路118号万达广场二楼大玩家
天空之城建邺吾悦广场店
江苏省南京市建邺区汉中门大街299号吾悦广场二楼天空之城
梦时代电玩城昆明官渡店
云南省昆明市官渡区世纪金源购物中心C馆4楼梦时代电玩城
环游乐园淄博张店荣盛店
山东省淄博市张店区马尚街道荣盛广场二楼环游乐园
七彩天空杭州临安店
浙江省杭州市临安区青山湖街道宝龙广场七彩天空乐园
渔乐玩家湛江霞山店
广东省湛江市霞山区东新路6号银地上悦广场二层2-2124号商铺
七彩天空杭州临安财富店
浙江省杭州市临安区锦城街道钱王财富中心2楼七彩天空乐园
WAGAME东莞国贸中心
广东省东莞市东城街道东泰社区鸿福东路1号民盈国贸城3L中庭
51区青岛李沧万达店
山东省青岛市李沧区巨峰路万达广场2楼51区超级乐园
嘻游嘉年华廊坊安次万达店
河北省廊坊市安次区南龙道万达广场3楼嘻游嘉年华
星球联盟马鞍山花山大润发店
安徽省马鞍山市花山区雨山东路欧尚大润发1楼星球联盟
风云再起广州海珠富力店
广东省广州市海珠区富力海珠城B区6楼风云再起
大玩家天津西青万达店
天津市西青经济技术开发区西青万达广场2层2F-3号大玩家超乐场
宝贝王抚州临川万达店
江西省抚州市临川区迎宾大道688号万达广场万达宝贝王1F
潮玩社莱西万达店
山东省莱西市万达广场3楼潮玩社
宝贝王宜春袁州万达店
江西省宜春市袁州区万达广场一楼宝贝王
头号玩家上饶广丰店
江西省上饶市广丰区永丰大道1号广丰里三楼
大潮玩沈阳铁西龙之梦店
辽宁省沈阳市铁西区建设西路2号龙之梦大都汇2楼东侧大潮玩家庭娱乐中心
SUPER101潮漫北流店
广西壮族自治区北流市北流万达3F-B ，SUPER101
就好潮玩深圳宝安大仟里店
深圳市宝安区大仟里购物中心B1层B146-151号
潮玩空间丽水青田店
浙江省丽水市青田县龙津路135号香溢广场c001
星际传奇青岛北区万科店
山东省青岛市北区万科未来城L301星际传奇
风云再起浙江丽水银泰城店
浙江省丽水市莲都区宇雷路789号丽水银泰城店地上2层L2002室
星空超乐场乳山九龙汇店
山东省乳山市九龙汇购物广场三楼星空超乐场
龙信体育世界南通店
江苏省南通市崇川区深南路8号龙信广场三楼龙信体育世界
泛时空合肥庐阳店
安徽省合肥市庐阳区宜家家居二楼泛时空
SSG电玩浙江金华店
浙江省金华市婺城区三江街道李渔路888号金华世贸城市广场3楼SSG电玩
天空之城中山小榄汇丰店
广东省中山市小榄镇汇丰城C3-1天空之城游乐体验世界
星乐荟上海奉贤龙湖店
上海市奉贤区金海公路3800号龙湖天街3楼
星奇多潮玩合肥长丰店
安徽省合肥市长丰县双墩镇北城世纪金源购物中心B座2楼2005铺星奇多潮玩世界
天空之城渝中来福士店
重庆市渝中区接圣街8号来福士购物广场3楼65-71号天空之城游乐体验世界
润宝梦潮玩乐园安庆店
安徽省安庆市宜秀区弘阳广场3楼 润宝梦潮玩乐园
卡通尼厦门思明店
福建省厦门市思明区嘉禾路468号SM广场3F-313铺位卡通尼乐园
炫击战卡游艺厅金华店
浙江省金华市婺城区三江街道李渔路 888号世贸广场E区1层E010号
魔力嘟嘟城绍兴上虞店
浙江省绍兴市上虞区曹娥街道上百万悦城购物中心3F
星际传奇张家港金茂店
江苏省张家港市金茂览秀城三楼星际传奇
真快活武汉洪山万科店
湖北武汉市洪山区张家湾街道白沙洲万科城市之光东(白沙二路西)3楼
第一回合成都郫都龙湖天街店
四川省成都市郫都区创智北环路创智公园东侧约100米蜀新龙湖天街4楼第一回合
天空之城兰州店
甘肃省兰州市安宁区吾悦广场3楼天空之城
菲游乐浙江台州店
浙江省台州市玉环万达2楼
乐游悦动滨海万达店
天津市滨海新区万达广场三楼乐游悦动
壹零壹潮漫九江濂溪店
江西省九江市濂溪区青年路818号九江十里万达4F壹零壹潮漫电玩娱乐中心
奇迹喵南宁西乡塘店
广西壮族自治区南宁市西乡塘区明湖大厦二楼奇迹喵动漫游戏体验中心
超乐玩家福清店
福建省福清市江滨路东百利桥古街B1区负一层超乐玩家
大玩家厦门湖里鹭港万达店
福建省厦门市湖里区殿前1路鹭港万达三楼
潮玩社潍坊临朐万达店
山东省潍坊市临朐县万达广场2楼潮玩社
泛时空赣州章贡店
江西省赣州市章贡区长征大道1号赣州中航城二层L229-231商铺
哈雷慧球临沂兰山万达店
山东省临沂市兰山区金雀山路万达广场二F次主5号商铺哈雷慧
大玩家周口文昌万达店
河南省周口市文昌大道与大庆路交叉口周口东新万达广场2F-A商铺大玩家
畅游电玩城徐州邳州店
江苏省徐州市邳州市中钰购物中心6楼畅游电玩城
C翻乐园武汉洪山大悦城店
湖北省武汉市洪山区高新大道718号大悦城3楼
星海英雄汇佛山顺德店
广东省佛山市顺德区裕和路110号爱琴海购物公园2楼F2036星海英雄汇超乐场
夏娃迪卡茂名茂南店
广东省茂名市茂南区茂南大道163号大院6号爱琴海购物公园三楼3019-3025号铺位
晴空进击社广州白云店
广东省广州市白云区黄边北路152号时光汇3楼
汤姆熊王国惠州惠城店
广东省惠州市惠城区华贸天地负一楼汤姆熊王国
潮玩街区如皋吾悦店
江苏省如皋市吾悦广场2楼潮玩街区
天空之城南通永旺店
江苏省南通市开发区新开街道星湖大道1066号永旺梦乐城南通星湖店2F228-A
好玩的家庭娱乐中心许昌店
河南省许昌市八龙路与建安大道交叉口胖东来天使城3楼
欢乐战纪成都成华店
四川省成都市成华区建设北路一段印象城二楼欢乐战纪
炫酷空间天长店
安徽省天长市天康大道天发购物广场一楼炫酷空间游乐场
炫技星空金华义乌之心店
浙江省金华市义乌市稠城街道工人西路9号义乌之心城市生活广场6楼炫技星空
散布的蜗牛扬州邗江店
江苏省扬州市邗江区京华路18号Rmall生活广场三楼散布的蜗牛
欢聚嘉年华宁波北仑银泰店
浙江省宁波市北仑区新碶街道中河路399号银泰城2幢3-4号3F欢聚嘉年华
蓝鲸乐园莆田仙游店
福建省莆田市仙游县方圆荟二楼蓝鲸乐园
KM'Square昆明官渡店
云南省昆明市官渡区新亚洲体育城星耀广场三楼A010-012
嘻品堂邵阳东方凤凰城店
湖南省邵阳市邵阳县渡口路和沿河街交叉口西北角东方凤凰城
雷霆1号临沂兰山店
山东省临沂市兰山区洗砚池街泰盛广场二期负一楼雷霆1号
天空之城镇江吾悦店
江苏省镇江市新区丁卯桥路223号吾悦商场3楼天空之城
阿凡达爱玩荟太原国金店
山西省太原市综改区南中环街426号国际金融中心G座地下一层G132号商铺
偶予动漫三亚天涯店
海南省三亚市天涯区胜利路胜利购物广场1楼
潮立方深圳龙华店
广东省深圳市龙华区清湖地铁口D出口益田假日天地3楼潮立方家庭娱乐中心
潮乐城青岛黄岛店
山东省青岛市黄岛区滨海大道2777号1层中庭西侧潮乐城欢乐世界
王者之风宁波海曙店
浙江省宁波市海曙区海曙印象城3楼王者之风电玩城
TopPlay佛山南海店
广东省佛山市南海区大沥镇黄岐广佛路中南花园嘉美居8-9座太湖路27号铺
潮玩社济南万象城店
山东省济南市历下区经十东路11111号济南万象城三楼365铺潮玩社
咪乐派欢乐谷济南市中店
山东省济南市市中区十六里河街道领秀城贵和购物中心2楼
星际传奇大连甘井子店
辽宁省大连市甘井子区华南广场万象汇2楼
梦幻传奇三门峡湖滨店
河南省三门峡市湖滨区梦之城四楼西南角梦幻传奇娱乐体验中心
乐享潮玩丰城新城店
江西省丰城市新城区雷焕路良辰悦购2楼乐享潮玩
极客星球济源店
河南省济源市北环大道与愚公路交叉口向北100联洋建材城内
TOP玩家银川店
宁夏回族自治区银川新华百货CCpark三层3C02铺TOP玩家家庭娱乐中心
明日世界芜湖镜湖店
安徽省芜湖市镜湖区八佰伴三楼明日世界
星际反斗蛙店
云南省大理白族自治州大理市下关镇 建设路泰业昆百大5楼
星球派对南充高坪店
四川省南充市高坪区万达广场七栋一楼星球派对家庭游乐中心
金满地都匀大西门店
贵州省都匀市大西门广场负一楼金满地家庭娱乐中心
疯狂牛仔城江门蓬江店
广东省江门市蓬江区万达广场二楼疯狂牛仔城
风云再起贵阳云岩店
贵州省贵阳市云岩区中山东路2号智城百货大楼负一楼
西部城市英雄南充高坪店
四川省南充市高坪区江东中路王府井广场五国风情街第LG层第28,29号西部城市英雄游乐场
运动星球杭州上城店
浙江省杭州市上城区富春路80号全民健身中心
星际传奇沈阳中海环宇城店
辽宁省沈阳市和平区南京南街中海环宇城2楼
奇趣酷玩城广州白云店
广东省广州市白云区广州大道北1419号佳润广场一楼其趣酷玩城
童话王国百色田东店
广西百色市田东县中兴城二楼童话王国
'''

arcades_lines = arcades_lines.split('\n')
arcades_lines = [l.replace('\n', '') for l in arcades_lines if l]
with open('arcades.json', 'r', encoding='utf-8') as f:
    arcades = json.load(f)

current_names = [c_a['name'] for c_a in arcades]

for i, name in enumerate(arcades_lines[::2]):
    if name not in current_names:
        arcade_dict = {'name': name,
                       'location': arcades_lines[i * 2 + 1],
                       'num': 1, 'alias': [],
                       'group': [], 'person': 0,
                       'by': '', 'time': ''}
        arcades.append(arcade_dict)
    else:
        arcades[current_names.index(name)]['location'] = arcades_lines[i * 2 + 1]


with open('arcades.json', 'w', encoding='utf-8') as f:
    json.dump(arcades, f, ensure_ascii=False, indent=4)
