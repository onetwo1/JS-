import re

import requests

headers = {
    'authority': 'sou.zhaopin.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'zh-CN,zh;q=0.9',
}
arg1_pattern = re.compile(r"<html><script>\s*var arg1='(.*?)';", re.S)


def uns_box(arg1):
    _0x4b082b = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32,
                 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
    _0x4da0dc = ['' for _ in range(40)]
    _0x12605e = ''
    for _0x20a7bf in range(len(arg1)):
        _0x385ee3 = arg1[_0x20a7bf]
        for index, _0x217721 in enumerate(_0x4b082b):
            if _0x217721 == _0x20a7bf + 1:
                _0x4da0dc[index] = _0x385ee3
    return ''.join(_0x4da0dc)


def hex_xor(uuu, key='3000176000856006061501533003690027800375'):
    _0x5a5d3b = []
    _0xe89588 = 0
    while _0xe89588 < len(uuu) and _0xe89588 < len(key):
        _0x401af1 = int(uuu[_0xe89588: _0xe89588 + 2], 16)
        _0x105f59 = int(key[_0xe89588: _0xe89588 + 2], 16)
        # '\0x5e' -> 5e
        _0x189e2c = hex(_0x401af1 ^ _0x105f59)[2:]
        if len(_0x189e2c) == 1:
            # 0 -> \x30
            _0x189e2c = '0' + _0x189e2c
        _0x5a5d3b.append(_0x189e2c)
        _0xe89588 += 2
    return ''.join(_0x5a5d3b)


def main():
    params = {
        'p': '1',
        'jl': '530',
        'kw': 'Python',
        'kt': '3'
    }
    response = requests.get('https://sou.zhaopin.com/', headers=headers, params=params)
    if response.status_code == 200 and response.content.__len__() <= 17088:
        # have so-json
        group_object = arg1_pattern.match(response.text)
        assert group_object, 'Not have arg1, Response Text is: {}'.format(response.text)
        arg1 = group_object.group(1)
        print(arg1)
        uuu = uns_box(arg1)
        print(uuu)
        res = hex_xor(uuu)
        print(res)


def just_test_case():
    arg1 = 'B1CCEB756B347960461FC603C545F3A437E6F826'
    uuu = uns_box(arg1)
    print(uuu)
    res = hex_xor(uuu)
    print(res)


if __name__ == '__main__':
    just_test_case()
