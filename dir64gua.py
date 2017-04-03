# 用法, 查value，返回key
# >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# >>> for k, v in knights.items():
# ...     print(k, v)
# ...
# gallahad the pure
# robin the brave
#
# >>> s = {1:['123', '2', '44']}
# >>> if '2' in s[1]:
#	print("1")
#
#
# 1
#
#
# 履 在上经是 lv0
# 旅 在下经是 lV1
#

chk_64gua = {
    ' ': [' ', '不动', 'budong', 'budon', "", '', " ", ',s', '0'],

    '111111': ['1', '乾为天',
               '乾', 'qian',
               '天', 'tian',
               '乾乾', 'qianqian',
               '111111'],

    '000000': ['2', '坤为地',
               '坤', 'kun',
               '地', 'di',
               '坤坤', 'kunkun',
               '000000'],

    '010001': ['3', '水雷屯',
               '屯', 'tun', 'zun', 'zhun',
               '水雷', 'shuilei', 'suilei',
               '坎震', 'kanzhen', 'kanzen', 'kanzheng','kanzeng',
               '010001'],

    '100010': ['4', '山水蒙',
               '蒙', 'meng', 'men',
               '山水', 'shanshui', 'sansui', 'shansui', 'sanshui',
               '艮坎', 'genkan','gengkan',
               '100010'],

    '010111': ['5','水天需',
               '需', 'xu',
               '水天', 'shuitian', 'suitian'
               '坎乾','kanqian',
               '010111'],

    '111010': ['6', '天水讼',
               '讼', 'song', 'son', 'shon', 'shong',
               '天水', 'tianshui', 'tiansui',
               '乾坎', 'qiankan',
               '111010'],

    '000010': ['7', '地水师' 
               '师', 'shi', 'si',
               '地水', 'dishui', 'disui'
               '坤坎', 'kunkan',
               '000010'],

    '010000': ['8', '水地比',
               '比', 'bi',
               '水地', 'shuidi', 'suidi',
               '坎坤', 'kankun',
               '010000'],

    '110111': ['9', '风天小畜',
               '小畜', 'xiaochu', 'xiaocu',
               '风天', 'fengtian', 'fentian',
               '巽乾', 'xunqian', 'xungqian',
               '110111' ],

    '111011': ['10', '天泽履',
               '履','lv0',
               '天泽', 'tianze', 'tianzhe',
               '乾兑', 'qiandui',
               '111011'],

    '000111': ['11', '地天泰',
               '泰', 'tai',
               '地天', 'ditian',
               '坤乾', 'kunqian',
               '000111'],

    '111000': ['12', '天地否',
               '否', 'pi' 'fou',
               '天地', 'tiandi',
               '乾坤', 'qiankun',
               '111000'],

    '111101': ['13', '天火同人',
               '同人', 'tongren', 'tonren',
               '天火', 'tianhuo',
               '乾离', 'qianli',
               '111101'],

    '101111': ['14', '火天大有',
             '大有', 'dayou',
             '火天', 'huotian',
             '离乾', 'liqian',
             '101111', ],

    '000100': ['15', '地山谦',
               '谦', 'qian',
               '地山', 'dishan', 'disan',
               '坤艮', 'kungen', 'kungeng',
               '000100'],

    '0010000': ['16', '雷地豫',
                '豫', 'yu',
                '雷地', 'leidi',
                '震坤', 'zhenkun', 'zhengkun',
                'zenkun','zengkun',
                '0010000'],

    '011001': ['17', '泽雷随',
               '随', 'sui', 'shui',
               '泽雷', 'zelei', 'zhelei',
               '兑震', 'duizhen', 'duizheng',
               'duizeng', 'duizheng',
               '011001', ],

    '100110': ['18', '山风蛊',
               '蛊','gu', 'chong', 'cong',
               '山风', 'shanfeng', 'shanfen',
               'sanfeng', 'sanfen',
               '艮巽', 'genxun', 'genxung',
               'gengxun', 'gengxung',
               '100110'],

    '000011': ['19', '地泽临',
               '临', 'lin', 'ling',
               '地泽', 'dize', 'dizhe',
               '坤兑', 'kundui',
               '000011'],

    '110000': ['20', '风地观',
               '观', 'guan', 'guang',
               '风地', 'fengdi', 'fendi',
               '巽坤', 'xunkun', 'xungkun',
               '110000'],

    '101001': ['21', '火雷噬嗑',
               '噬嗑', 'shike', 'shihe', 'sike', 'sihe',
               '火雷', 'huolei',
               '离震', 'lizhen', 'lizheng',
               'lizen', 'lizeng',
               '101001'],

    '100101': ['22', '山火贲',
               '贲', 'ben', 'beng', 'fen', 'feng',
               '山火', 'shanhuo', 'sanhuo',
               '艮离', 'genli', 'gengli',
               '100101'],

    '100000': ['23', '山地剥',
               '剥', 'bo', 'lu', 'po',
               '山地', 'shandi', 'sandi',
               '艮坤', 'genkun', 'gengkun',
               '100000'],

    '000001': ['24', '地雷复',
               '复', 'fu',
               '地雷', 'dilei',
               '坤震', 'kunzhen', 'kunzheng',
               'kunzen', 'kunzeng',
               '000001'],

    '111001': ['25', '天雷无妄',
               '无妄','wuwang',
               '天雷', 'tianlei',
               '乾震', 'qianzhen', 'qianzheng',
               'qianzen', 'qianzeng',
               '111001'],

    '100111': ['26', '山天大畜',
               '大畜', 'dachu', 'dacu', 'daxu',
               '山天', 'shantian', 'santian',
               '艮乾', 'genqian', 'gengqian',
               '100111'],

    '100001': ['27', '山雷颐',
               '颐', 'yi', 'gu',
               '山雷', 'shanlei', 'sanlei',
               '艮震', 'genzhen', 'gengzhen',
               'genzheng', 'gengzheng',
               'genzen', 'genzeng',
               '100001'],

    '011110': ['28', '泽风大过',
               '大过', 'daguo',
               '泽风', 'zefeng', 'zefen',
               'zhefeng', 'zhefen',
               '兑巽', 'duixun', 'duixung',
               '011110'],

    '010010': ['29', '坎为水',
               '水', 'shui', 'sui',
               '坎', 'kan',
               '坎坎', 'kankan',
               '010010'],

    '101101': ['30', '离为火',
               '火', 'huo',
               '离', 'li',
               '离离', 'lili',
               '101101'],               # 30  上经

    '011100': ['31', '泽山咸',
               '咸', 'xian', 'gan', 'yan',
               '泽山', 'zeshan', 'zesan',
               'zheshan', 'zhesan',
               '兑艮', 'duigen', 'duigeng',
               '011100'],               # 31  下经

    '001110': ['32', '雷风恒',
               '恒', 'heng', 'hen', 'dan',
               '雷风', 'leifeng', 'leifen',
               '震巽', 'zhenxun', 'zhengxun',
               '001110'],

    '111100': ['33', '天山遁', '天山遯',
               '遁', '遯', 'dun',
               '天山', 'tianshan', 'tiansan',
               '乾艮', 'qiangen', 'qiangeng',
               '111100'],

    '001111': ['34', '雷天大壮',
               '大壮', 'dazhuang',
               '雷天', 'leitian',
               '震乾', 'zhenqian', 'zhengqian',
               'zenqian', 'zengqian',
               '001111'],

    '101000': ['35', '火地晋',
               '晋', 'jin', 'jing',
               '火地', 'huodi',
               '离坤', 'likun',
               '101000'],

    '000101': ['36', '地火明夷',
               '明夷', 'mingyi',
               '地火', 'dihuo',
               '坤离', 'kunli',
               '000101'],

    '110101': ['37', '风火家人',
               '家人', 'jiaren', 'jiareng',
               '风火', 'fenghuo', 'fenhuo',
               '巽离', 'xunli', 'xungli',
               '110101'],

    '101011': ['38', '火泽睽',
               '睽', 'kui', 'gui',
               '火泽', 'huoze', 'huozhe',
               '离兑', 'lidui',
               '101011'],

    '010100': ['39', '水山蹇',
               '蹇', 'jian', 'chu', 'cu',    #'zhi', 'zi'
               '水山', 'shuishan', 'shuisan', 'suishan', 'suisan',
               '坎艮', 'kangen', 'kangeng',
               '010100'],

    '001010': ['40', '雷水解',
               '解', 'jie', 'xie',
               '雷水', 'leishui', 'leisui',
               '震坎', 'zhenkan', 'zhengkan', 'zenkan', 'zengkan',
               '001010'],

    '100011': ['41', '山泽损',
               '损', 'sun', 'shun',
               '山泽', 'shanze', 'shanzhe', 'sanze', 'sanzhe',
               '艮兑', 'gendui', 'gengdui',
               '100011'],

    '110001': ['42', '风雷益',
               '益', 'yi',
               '风雷', 'fenglei', 'fenlei',
               '巽震', 'xunzhen', 'xunzheng', 'xunzen', 'xunzeng',
               '110001'],

    '011111': ['43', '泽天夬',
               '夬', 'guai', 'yang', 'jue',
               '泽天', 'zetian', 'zhetian',
               '兑乾', 'duiqian',
               '011111'],

    '111110': ['44', '风天姤', '风天媾',
               '姤', '媾', 'gou',
               '风天', 'fengtian', 'fentian',
               '巽乾', 'xunqian',
               '111110'],

    '011000': ['45', '泽地萃',
               '萃', 'cui', 'chui',
               '泽地', 'zedi', 'zhedi',
               '兑坤', 'duikun',
               '011000'],

    '000110': ['46', '地风升',
               '升', 'sheng', 'shen', 'seng', 'sen',
               '地风', 'difeng', 'difen',
               '坤巽', 'kunxun',
               '000110'],

    '011010': ['47', '泽水困',
               '困', 'kun',
               '泽水', 'zeshui', 'zheshui', 'zesui', 'zheshui',
               '兑坎', 'duikan',
               '011010'],

    '010110': ['48', '水风井',
               '井', 'jing', 'jin',
               '水风', 'shuifeng', 'shuifen', 'suifeng', 'suifen',
               '坎巽', 'kanxun',
               '010110'],

    '011101': ['49', '泽火革',
               '革', 'ge',
               '泽火', 'zehuo', 'zhehuo',
               '兑离', 'duili',
               '011101'],

    '101110': ['50', '火风鼎',
               '鼎', 'ding', 'din',
               '火风', 'huofeng', 'huofen',
               '离巽', 'lixun',
               '101110'],

    '001001': ['51', '震为雷',
               '震', 'zhen', 'zheng', 'zen', 'zeng',
               '雷', 'lei',
               '震震', 'zhenzhen', # 'zhengzhen', 'zhenzheng',
               # 'zhenzen', 'zhengzen', 'zhenzeng'
               # 'zenzhen', 'zengzhen', 'zenzheng',
               'zenzen', # 'zengzen', 'zenzeng',
               'zhengzheng',
               'zengzeng',
               '001001'],

    '100100': ['52', '艮为山',
               '艮', 'gen', 'geng',
               '山', 'shan', 'san',
               '艮艮', 'gengen', 'genggeng',
               '100100'],

    '110100': ['53', '风山渐',
               '渐', 'jian',
               '风山', 'fengshan', 'fenshan',
               '巽艮', 'xungen', 'xungeng',
               '110100'],

    '001011': ['54', '雷泽归妹',
               '归妹', 'guimei',
               '雷泽', 'leize', 'leizhe',
               '震兑', 'zhendui', 'zhengdui',
               'zendui', 'zengdui',
               '001011'],

    '001101': ['55', '雷火丰',
               '丰', 'feng', 'fen',
               '雷火', 'leihuo',
               '震离', 'zhenli', 'zhengli', 'zenli', 'zengli',
               '001101'],

    '101100': ['56', '火山旅',
               '旅', 'lv1',
               '火山', 'huoshan', 'huosan', 'huoshang',
               '离艮', 'ligen', 'ligeng',
               '101100'],

    '110110': ['57', '巽为风',
               '巽', 'xun',
               '风', 'fen', 'feng',
               '巽巽', 'xunxun',
               '110110'],

    '011011': ['58', '兑为泽',
               '兑', 'dui',
               '泽', 'ze', 'zhe',
               '兑兑', 'duidui',
               '011011'],

    '110010': ['59', '风水涣',
               '涣', 'huan', 'huang'
               '风水', 'fengshui', 'fenshui',
               'fengsui', 'fensui',
               '巽坎', 'xunkan',
               '110010'],

    '010011': ['60', '水泽节',
               '节', 'jie',
               '水泽', 'shuize', 'suize',
               'shuizhe', 'suizhe',
               '坎兑', 'kandui',
               '010011'],

    '110011': ['61', '风泽中孚',
               '中孚', 'zhongfu', 'zongfu',
               '风泽', 'fengze', 'fenze',
               'fenzhe', 'fengzhe',
               '巽兑', 'xundui',
               '110011'],

    '001100': ['62', '雷山小过',
               '小过', 'xiaoguo',
               '雷山', 'leishan', 'leisan',
               '震艮', 'zhengen', 'zhengeng',
               'zhenggen', 'zhenggeng',
               'zengen', 'zengeng', 'zenggen', 'zenggeng',
               '001100'],

    '010101': ['63', '水火既济',
               '既济', 'jiji',
               '水火', 'shuihuo', 'suihuo',
               '坎离', 'kanli',
               '010101'],

    '101010': ['64', '火水未济',
               '未济', 'weiji',
               '火水', 'huoshui', 'huosui',
               '离坎', 'likan',
               '101010']
}
