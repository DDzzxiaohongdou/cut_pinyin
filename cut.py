def pinyin_word(string):
    '''
    将一段拼音，分解成一个个拼音
    :param string: 匹配的字符串
    :return: 匹配到的拼音列表
    '''
    max_len = 6  # 拼音最长为6
    string = string.lower()
    stringlen = len(string)
    result = []

    # 读本地拼音表
    with open('pinyin.txt', 'r', encoding='utf-8') as fi:
        pinyinLib = fi.readlines()
        for i in range(len(pinyinLib)):
            pinyinLib[i] = pinyinLib[i][:-1]  # 去换行符

    # 逆向匹配
    while True:
        matched = 0
        matched_word = ''
        if stringlen < max_len:
            max_len = stringlen
        for i in range(max_len, 0, -1):
            s = string[(stringlen - i):stringlen]
            # 字符串是否在拼音表中
            if s in pinyinLib:
                matched_word = s
                matched = i
                break
        # 未匹配到拼音
        if len(matched_word) == 0:
            break
        else:
            result.append(s)
            string = string[:(stringlen - matched)]
            stringlen = len(string)
            if stringlen == 0:
                break
    return result

print("woaini")
print(list(reversed(pinyin_word("woaini"))))