# coding:utf-8
# qian -> 111 111
# 乾
# 天
# 乾为天
#
# 履 -> lv0 因为履在上经，所以排第一
# 旅 -> lv1 因为旅在下经，所以排第二
#
# 因为懒不想动脑子折腾，就直接用if-elif-else来实现下面的功能

__author__ = 'hanpeizhi'

# inVar = ''
# outBin = ''
# global outBin


def to_bin(inVar):  # inVar 不能同时是全局变量和函数元素
    global outBin
    if inVar == '乾' or inVar == '乾为天' \
            or inVar == 'qian' \
            or inVar == '天' or inVar == 'tian' \
            or inVar == '乾乾' or inVar == 'qianqian'\
            or inVar == '111111' or inVar == '1':  # 1
        outBin = '111111'
        return outBin

    elif inVar == '坤' or inVar == '坤为地' \
            or inVar == 'kun' \
            or inVar == '地' or inVar == 'di' \
            or inVar == '坤坤' or inVar == 'kunkun' \
            or inVar == '000000' or inVar == '2':  # 2
        outBin = '000000'
        return outBin

    elif inVar == '屯' or inVar == '水雷屯' \
            or inVar == 'tun' or inVar == 'zun' or inVar == 'zhun' \
            or inVar == '水雷' or inVar == 'shuilei' or inVar == 'suilei' \
            or inVar == '坎震' or inVar == 'kanzhen' or inVar == 'kanzen' \
            or inVar == 'kanzheng' or inVar == 'kanzeng' \
            or inVar == '010001' or inVar == '3':  # 3
        outBin = '010001'
        return outBin

    elif inVar == '蒙' or inVar == '山水蒙' \
            or inVar == 'meng' or inVar == 'men' \
            or inVar == '山水' or inVar == 'shanshui' or inVar == 'sansui' \
            or inVar == 'shansui' or inVar == 'sanshui'\
            or inVar == '艮坎' or inVar == 'genkan' or inVar == 'gengkan' \
            or inVar == '100010' or inVar == '4':
        outBin = '100010'
        return outBin

    elif inVar == '需' or inVar == '水天需'\
            or inVar == 'xu'\
            or inVar == '水天' or inVar == 'shuitian' or inVar == 'suitian'\
            or inVar == '坎乾' or inVar == 'kanqian'\
            or inVar == '010111' or inVar == '5':  # 5
        outBin = '010111'
        return outBin

    elif inVar == '讼' or inVar == '天水讼' \
            or inVar == 'song' or inVar == 'son' or inVar == 'shon'or inVar == 'shong' \
            or inVar == '天水' or inVar == 'tianshui' or inVar == 'tiansui'\
            or inVar == '乾坎' or inVar == 'qiankan' \
            or inVar == '111010' or inVar == '6':  # 6
        outBin = '111010'
        return outBin

    elif inVar == '师' or inVar == '地水师' \
            or inVar == 'shi' or inVar == 'si' \
            or inVar == '地水' or inVar == 'dishui' or inVar == 'disui'\
            or inVar == '坤坎' or inVar == 'kunkan' \
            or inVar == '000010' or inVar == '7':  # 7
        outBin = '000010'
        return outBin

    elif inVar == '比' or inVar == '水地比' \
            or inVar == 'bi' \
            or inVar == '水地' or inVar == 'shuidi' or inVar == 'suidi' \
            or inVar == '坎坤' or inVar == 'kankun' \
            or inVar == '010000' or inVar == '8':  # 8
        outBin = '010000'
        return outBin

    elif inVar == '小畜' or inVar == '风天小畜' \
            or inVar == 'xiaochu' or inVar == 'xiaocu'\
            or inVar == '风天' or inVar == 'fengtian' or inVar == 'fentian' \
            or inVar == '巽乾' or inVar == 'xunqian' \
            or inVar == '110111' or inVar == '9':  # 9
        outBin = '110111'
        return outBin

    elif inVar == '履' or inVar == '天泽履' \
            or inVar == 'lv0' \
            or inVar == '天泽' or inVar == 'tianze' or inVar == 'tianzhe' \
            or inVar == '乾兑' or inVar == 'qiandui' \
            or inVar == '111011' or inVar == '10':  # 10
        outBin = '111011'
        return outBin

    elif inVar == '泰' or inVar == '地天泰' \
            or inVar == 'tai' \
            or inVar == '地天' or inVar == 'ditian' \
            or inVar == '坤乾' or inVar == 'kunqian' \
            or inVar == '000111' or inVar == '11':  # 11
        outBin = '000111'
        return outBin

    elif inVar == '否' or inVar == '天地否' \
            or inVar == 'pi' or inVar == 'fou' \
            or inVar == '天地' or inVar == 'tiandi' \
            or inVar == '乾坤' or inVar == 'qiankun' \
            or inVar == '111000' or inVar == '12':  # 12
        outBin = '111000'
        return outBin

    elif inVar == '同人' or inVar == '天火同人' \
            or inVar == 'tongren' or inVar == 'tonren' \
            or inVar == '天火' or inVar == 'tianhuo' \
            or inVar == '乾离' or inVar == 'qianli' \
            or inVar == '111101' or inVar == '13':  # 13
        outBin = '111101'
        return outBin

    elif inVar == '大有' or inVar == '火天大有' \
            or inVar == 'dayou' \
            or inVar == '火天' or inVar == 'huotian' \
            or inVar == '离乾' or inVar == 'liqian' \
            or inVar == '101111' or inVar == '14':  # 14
        outBin = '101111'
        return outBin

    elif inVar == '谦' or inVar == '地山谦' \
            or inVar == 'qian' \
            or inVar == '地山' or inVar == 'dishan' or inVar == 'disan' \
            or inVar == '坤艮' or inVar == 'kungen' or inVar == 'kungeng' \
            or inVar == '000100' or inVar == '15':  # 15
        outBin = '000100'
        return outBin

    elif inVar == '豫' or inVar == '雷地豫' \
            or inVar == 'yu' \
            or inVar == '雷地' or inVar == 'leidi' \
            or inVar == '震坤' or inVar == 'zhenkun' or inVar == 'zhengkun' \
            or inVar == 'zenkun' or inVar == 'zengkun' \
            or inVar == '0010000' or inVar == '16':  # 16
        outBin = '001000'
        return outBin

    elif inVar == '随' or inVar == '泽雷随'\
            or inVar == 'sui' or inVar == 'shui' \
            or inVar == '泽雷' or inVar == 'zelei' or inVar == 'zhelei' \
            or inVar == '兑震' or inVar == 'duizhen' or inVar == 'duizheng' \
            or inVar == 'duizeng' or inVar == 'duizheng' \
            or inVar == '011001' or inVar == '17':  # 17
        outBin = '011001'
        return outBin

    elif inVar == '蛊' or inVar == '山风蛊'\
            or inVar == 'gu' or inVar == 'chong' or inVar == 'cong' \
            or inVar == '山风' or inVar == 'shanfeng' or inVar == 'shanfen'\
            or inVar == 'sanfeng' or inVar == 'sanfen' \
            or inVar == '100110' or inVar == '18':  # 18
        outBin = '100110'
        return outBin

    elif inVar == '临' or inVar == '地泽临' \
            or inVar == 'lin' or inVar == 'ling' \
            or inVar == '地泽' or inVar == 'dize' or inVar == 'dizhe' \
            or inVar == '坤兑' or inVar == 'kundui' \
            or inVar == '000011' or inVar == '19':  # 19
        outBin = '000011'
        return outBin

    elif inVar == '观' or inVar == '风地观' \
            or inVar == 'guan' or inVar == 'guang' \
            or inVar == '风地' or inVar == 'fengdi' or inVar == 'fendi' \
            or inVar == '巽坤' or inVar == 'xunkun' \
            or inVar == '110000' or inVar == '20':  # 20
        outBin = '110000'
        return outBin

    elif inVar == '噬嗑' or inVar == '火雷噬嗑' \
            or inVar == 'shike' or inVar == 'shihe' or inVar == 'sike' or inVar == 'sihe' \
            or inVar == '火雷' or inVar == 'huolei' \
            or inVar == '离震' or inVar == 'lizhen' or inVar == 'lizheng' \
            or inVar == 'lizen' or inVar == 'lizeng' \
            or inVar == '101001':  # 21
        outBin = '101001'
        return outBin

    elif inVar == '贲' or inVar == '山火贲' \
            or inVar == 'ben' or inVar == 'beng' or inVar == 'fen' or inVar == 'feng' \
            or inVar == '山火' or inVar == 'shanhuo' or inVar == 'sanhuo' \
            or inVar == '艮离' or inVar == 'genli' or inVar == 'gengli' \
            or inVar == '100101' or inVar == '22':  # 22
        outBin = '100101'
        return outBin

    elif inVar == '剥' or inVar == '山地剥' \
            or inVar == 'bo' or inVar == 'lu' or inVar == 'po' \
            or inVar == '山地' or inVar == 'shandi' or inVar == 'sandi' \
            or inVar == '艮坤' or inVar == 'genkun' or inVar == 'gengkun' \
            or inVar == '100000' or inVar == '23':  # 23
        outBin = '100000'
        return outBin

    elif inVar == '复' or inVar == '地雷复' \
            or inVar == 'fu' \
            or inVar == '地雷' or inVar == 'dilei' \
            or inVar == '坤震' or inVar == 'kunzhen' or inVar == 'kunzheng' \
            or inVar == 'kunzen' or inVar == 'kunzeng' \
            or inVar == '000001' or inVar == '24':  # 24
        outBin = '000001'
        return outBin

    elif inVar == '无妄' or inVar == '天雷无妄' \
            or inVar == 'wuwang' \
            or inVar == '天雷' or inVar == 'tianlei' \
            or inVar == '乾震' or inVar == 'qianzhen' or inVar == 'qianzheng' \
            or inVar == 'qianzen' or inVar == 'qianzeng' \
            or inVar == '111001' or inVar == '25':  # 25
        outBin = '111001'
        return outBin

    elif inVar == '大畜' or inVar == '山天大畜' \
            or inVar == 'dachu' or inVar == 'dacu' or inVar == 'daxu' \
            or inVar == '山天' or inVar == 'shantian' or inVar == 'santian' \
            or inVar == '艮乾' or inVar == 'genqian' or inVar == 'gengqian' \
            or inVar == '100111' or inVar == '26':  # 26
        outBin = '100111'
        return outBin

    elif inVar == '颐' or inVar == '山雷颐' \
            or inVar == 'yi' or inVar == 'gu' \
            or inVar == '山雷' or inVar == 'shanlei' or inVar == 'sanlei' \
            or inVar == '艮震' or inVar == 'genzhen' or inVar == 'gengzhen' \
            or inVar == 'genzheng' or inVar == 'gengzheng' \
            or inVar == 'genzen' or inVar == 'genzeng' \
            or inVar == '100001' or inVar == '27':  # 27
        outBin = '100001'
        return outBin

    elif inVar == '大过' or inVar == '泽风大过' \
            or inVar == 'daguo' \
            or inVar == '泽风' or inVar == 'zefeng' or inVar == 'zefen' \
            or inVar == 'zhefeng' or inVar == 'zhefen' \
            or inVar == '兑巽' or inVar == 'duixun' \
            or inVar == '011110' or inVar == '28':  # 28
        outBin = '011110'
        return outBin

    elif inVar == '水' or inVar == '坎为水' \
            or inVar == 'shui' or inVar == 'sui' \
            or inVar == '坎' or inVar == 'kan' \
            or inVar == '坎坎' or inVar == 'kankan' \
            or inVar == '010010' or inVar == '29':  # 29
        outBin = '010010'
        return outBin

    elif inVar == '火' or inVar == '离为火' \
            or inVar == 'huo' \
            or inVar == '离' or inVar == 'li' \
            or inVar == '离离' or inVar == 'lili' \
            or inVar == '1011011' or inVar == '30':  # 30  上经
        outBin = '101101'
        return outBin

    elif inVar == '咸' or inVar == '泽山咸' \
            or inVar == '011100' or inVar == '31':  # 31 下经
        outBin == '011100'
        return outBin

    elif inVar == '' or inVar == '不动' \
            or inVar == 'budong' or inVar == 'don' \
            or inVar == '0':
        outBin = ''
        return outBin
    else:
        return "不要调皮！"

# lookup_dic(inVar)
# print(outBin, inVar)
