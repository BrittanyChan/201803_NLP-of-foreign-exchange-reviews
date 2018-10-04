#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import request
from urllib import parse

def main():
    # 配置您申请的APPKey
    appkey = "ffc8f5a0e28afb98041e143f8f574aa0"
    # 1.常用汇率查询
    request1(appkey, "GET")
    # 2.货币列表
    request2(appkey, "GET")
    # 3.实时汇率查询换算
    request3(appkey, "GET")

# 常用汇率查询
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/query"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
    }
    params = parse.urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print (res["result"])
        else:
            print ("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print ("request api error")

# 货币列表
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/list"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = parse.urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print (res["result"])
        else:
            print ("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print ("request api error")

# 实时汇率查询换算
def request3(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/currency"
    params = {
        "from": "USD",  # 转换汇率前的货币代码
        "to": "CNY",  # 转换汇率成的货币代码
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = parse.urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print (res["result"])
        else:
            print ("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print ("request api error")

if __name__ == '__main__':
    main()