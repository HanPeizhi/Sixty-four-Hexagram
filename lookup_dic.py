# coding:utf-8
# qian -> 111 111
# 乾
# 天
# 乾为天

# 履 -> lv0 因为履在上经，所以排第一
# 旅 -> lv1 因为旅在下经，所以排第二
#
# 因为懒不想动脑子折腾，就直接用if-elif-else来实现下面的功能

__author__ = 'hanpeizhi'

# in＿name = ''
# out_binary = ''
# global out_binary


def to_bin(in＿name):  # in_name 不能同时是全局变量和函数元素
    global out_binary
    if in＿name == '乾' or in_name == '乾为天' \
            or in＿name == 'qian' \
            or in_name == '天' or in＿name == 'tian' \
            or in＿name == '乾乾' or in＿name == 'qianqian'\
            or in_name == '111111' or in＿name == '1':  # 1
        out_binary = '111111'
        return out_binary

    elif in＿name == '坤' or in＿name == '坤为地' \
            or in＿name == 'kun' \
            or in＿name == '地' or in＿name == 'di' \
            or in＿name == '坤坤' or in＿name == 'kunkun' \
            or in＿name == '000000' or in＿name == '2':  # 2
        out_binary = '000000'
        return out_binary

    elif in＿name == '屯' or in＿name == '水雷屯' \
            or in＿name == 'tun' or in＿name == 'zun' or in＿name == 'zhun' \
            or in＿name == '水雷' or in＿name == 'shuilei' or in＿name == 'suilei' \
            or in＿name == '坎震' or in＿name == 'kanzhen' or in＿name == 'kanzen' \
            or in＿name == 'kanzheng' or in＿name == 'kanzeng' \
            or in＿name == '010001' or in＿name == '3':  # 3
        out_binary = '010001'
        return out_binary

    elif in＿name == '蒙' or in＿name == '山水蒙' \
            or in＿name == 'meng' or in＿name == 'men' \
            or in＿name == '山水' or in＿name == 'shanshui' or in＿name == 'sansui' \
            or in＿name == 'shansui' or in＿name == 'sanshui'\
            or in＿name == '艮坎' or in＿name == 'genkan' or in＿name == 'gengkan' \
            or in＿name == '100010' or in＿name == '4':
        out_binary = '100010'
        return out_binary

    elif in＿name == '需' or in＿name == '水天需'\
            or in＿name == 'xu'\
            or in＿name == '水天' or in＿name == 'shuitian' or in＿name == 'suitian'\
            or in＿name == '坎乾' or in＿name == 'kanqian'\
            or in＿name == '010111' or in＿name == '5':  # 5
        out_binary = '010111'
        return out_binary

    elif in＿name == '讼' or in＿name == '天水讼' \
            or in＿name == 'song' or in＿name == 'son' or in＿name == 'shon'or in＿name == 'shong' \
            or in＿name == '天水' or in＿name == 'tianshui' or in＿name == 'tiansui'\
            or in＿name == '乾坎' or in＿name == 'qiankan' \
            or in＿name == '111010' or in＿name == '6':  # 6
        out_binary = '111010'
        return out_binary

    elif in＿name == '师' or in＿name == '地水师' \
            or in＿name == 'shi' or in＿name == 'si' \
            or in＿name == '地水' or in＿name == 'dishui' or in＿name == 'disui'\
            or in＿name == '坤坎' or in＿name == 'kunkan' \
            or in＿name == '000010' or in＿name == '7':  # 7
        out_binary = '000010'
        return out_binary

    elif in＿name == '比' or in＿name == '水地比' \
            or in＿name == 'bi' \
            or in＿name == '水地' or in＿name == 'shuidi' or in＿name == 'suidi' \
            or in＿name == '坎坤' or in＿name == 'kankun' \
            or in＿name == '010000' or in＿name == '8':  # 8
        out_binary = '010000'
        return out_binary

    elif in＿name == '小畜' or in＿name == '风天小畜' \
            or in＿name == 'xiaochu' or in＿name == 'xiaocu'\
            or in＿name == '风天' or in＿name == 'fengtian' or in＿name == 'fentian' \
            or in＿name == '巽乾' or in＿name == 'xunqian' \
            or in＿name == '110111' or in＿name == '9':  # 9
        out_binary = '110111'
        return out_binary

    elif in＿name == '履' or in＿name == '天泽履' \
            or in＿name == 'lv0' \
            or in＿name == '天泽' or in＿name == 'tianze' or in＿name == 'tianzhe' \
            or in＿name == '乾兑' or in＿name == 'qiandui' \
            or in＿name == '111011' or in＿name == '10':  # 10
        out_binary = '111011'
        return out_binary

    elif in＿name == '泰' or in＿name == '地天泰' \
            or in＿name == 'tai' \
            or in＿name == '地天' or in＿name == 'ditian' \
            or in＿name == '坤乾' or in＿name == 'kunqian' \
            or in＿name == '000111' or in＿name == '11':  # 11
        out_binary = '000111'
        return out_binary

    elif in＿name == '否' or in＿name == '天地否' \
            or in＿name == 'pi' or in＿name == 'fou' \
            or in＿name == '天地' or in＿name == 'tiandi' \
            or in＿name == '乾坤' or in＿name == 'qiankun' \
            or in＿name == '111000' or in＿name == '12':  # 12
        out_binary = '111000'
        return out_binary

    elif in＿name == '同人' or in＿name == '天火同人' \
            or in＿name == 'tongren' or in＿name == 'tonren' \
            or in＿name == '天火' or in＿name == 'tianhuo' \
            or in＿name == '乾离' or in＿name == 'qianli' \
            or in＿name == '111101' or in＿name == '13':  # 13
        out_binary = '111101'
        return out_binary

    elif in＿name == '大有' or in＿name == '火天大有' \
            or in＿name == 'dayou' \
            or in＿name == '火天' or in＿name == 'huotian' \
            or in＿name == '离乾' or in＿name == 'liqian' \
            or in＿name == '101111' or in＿name == '14':  # 14
        out_binary = '101111'
        return out_binary

    elif in＿name == '谦' or in＿name == '地山谦' \
            or in＿name == 'qian' \
            or in＿name == '地山' or in＿name == 'dishan' or in＿name == 'disan' \
            or in＿name == '坤艮' or in＿name == 'kungen' or in＿name == 'kungeng' \
            or in＿name == '000100' or in＿name == '15':  # 15
        out_binary = '000100'
        return out_binary

    elif in＿name == '豫' or in＿name == '雷地豫' \
            or in_name == 'yu' \
            or in_name == '雷地' or in_name == 'leidi' \
            or in_name == '震坤' or in_name == 'zhenkun' or in_name == 'zhengkun' \
            or in_name == 'zenkun' or in_name == 'zengkun' \
            or in＿name == '0010000' or in_name == '16':  # 16
        out_binary = '001000'
        return out_binary

    elif in＿name == '随' or in＿name == '泽雷随'\
            or in_name == 'sui' or in_name == 'shui' \
            or in_name == '泽雷' or in_name == 'zelei' or in_name == 'zhelei' \
            or in_name == '兑震' or in_name == 'duizhen' or in_name == 'duizheng' \
            or in_name == 'duizeng' or in_name == 'duizheng' \
            or in＿name == '011001' or in_name == '17':  # 17
        out_binary = '011001'
        return out_binary

    elif in＿name == '蛊' or in＿name == '山风蛊'\
            or in_name == 'gu' or in_name == 'chong' or in_name == 'cong' \
            or in_name == '山风' or in_name == 'shanfeng' or in_name == 'shanfen'\
            or in_name == 'sanfeng' or in_name == 'sanfen' \
            or in＿name == '100110' or in_name == '18':  # 18
        out_binary = '100110'
        return out_binary

    elif in＿name == '临' or in＿name == '地泽临' or in＿name == '000011':  # 19
        out_binary = '000011'
        return out_binary

    elif in＿name == '观' or in＿name == '风地观' or in＿name == '110000':  # 20
        out_binary = '110000'
        return out_binary

    elif in＿name == '噬嗑' or in＿name == '火雷噬嗑' or in＿name == '101001':  # 21
        out_binary = '101001'
        return out_binary

    elif in＿name == '贲' or in＿name == '山火贲' or in＿name == '100101':  # 22
        out_binary = '100101'
        return out_binary

    elif in＿name == '剥' or in＿name == '山地剥' or in＿name == '100000':  # 23
        out_binary = '100000'
        return out_binary

    elif in＿name == '复' or in＿name == '地雷复' or in＿name == '000001':  # 24
        out_binary = '000001'
        return out_binary

    elif in＿name == '无妄' or in＿name == '天雷无妄' or in＿name == '111001':  # 25
        out_binary = '111001'
        return out_binary

    elif in＿name == '大畜' or in＿name == '山天大畜' or in＿name == '100111':  # 26
        out_binary = '100111'
        return out_binary

    elif in＿name == '颐' or in＿name == '山雷颐' or in＿name == '100001':  # 27
        out_binary = '100001'
        return out_binary

    elif in＿name == '大过' or in＿name == '泽风大过' or in＿name == '011110':  # 28
        out_binary = '011110'
        return out_binary

    elif in＿name == '水' or in＿name == '坎为水' or in＿name == '坎' or in＿name == '010010':  # 29
        out_binary = '010010'
        return out_binary

    elif in＿name == '火' or in＿name == '离为火' or in＿name == '离' or in＿name == '1011011':  # 30  上经
        out_binary = '101101'
        return out_binary

    elif in＿name == '' or in_name == '不动' or in_name == '0':
        out_binary = ''
        return out_binary
    else:
        return "不要调皮！"

# lookup_dic(in＿name)
# print(out_binary, in＿name)
