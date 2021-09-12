#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
import HttpRequestDataPool as hrdp
import requests
import HttpRequestData
import ExcelFileParser as efp

TARGET = 'LR152011X1'
URL = "http://www.baidu.com"


def get_kvt_list(name):
    res = efp.ExcelFileParser(name).dataList_withType
    return res


def get_body_for_req_body(kvt_list):
    res = []
    for idx in range(len(kvt_list)):
        new_info_outer_map_within_infbdy = {}
        new_info = []
        new_map_in_info = {}
        new_obj = HttpRequestData.HttpRequestData()
        for j in range(len(kvt_list[idx])):
            new_map_in_info[kvt_list[idx][j].key] = kvt_list[idx][j].value
        new_info.append(new_map_in_info)
        new_info_outer_map_within_infbdy[TARGET] = new_info
        new_obj.set_info_body(new_info_outer_map_within_infbdy)
        new_obj.append_last_line()
        res.append(new_obj)
    return res


def get_inner_map_from_list(kvt_list):
    res = []
    for idx in range(len(kvt_list)):
        new_info_outer_map_within_infbdy = {}
        new_info = []
        new_map_in_info = {}
        for j in range(len(kvt_list[idx])):
            new_map_in_info[kvt_list[idx][j].key] = kvt_list[idx][j].value
        new_info.append(new_map_in_info)
        new_info_outer_map_within_infbdy[TARGET] = new_info
        res.append(new_info_outer_map_within_infbdy)
    return res


def make_up_a_req_and_send(inner_map, my_url=URL):
    HEADER = {
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.103 Safari/537.36 '
    }
    req_body = {'PRCOD': 'LR152011', 'WEBCOD': '', 'ERRMSG': '', 'ISUTIM': '', 'ISUDAT': '', 'RTNLVL': '', 'DALCOD': '',
                'TARSVR': '', 'INFBDY': inner_map, 'RTNCOD': ''}
    # 发的是post请求，用的是requests.post
    r = requests.post(url=my_url, data=req_body, headers=HEADER)
    print("content:", eval(r.content))
    print("text", eval(r.text))
    return r


if __name__ == '__main__':
    kvt_list = get_kvt_list('data1.xlsx')
    req_body_inner_map_list = get_inner_map_from_list(kvt_list)
    for i in range(len(req_body_inner_map_list)):
        # r是response
        r = make_up_a_req_and_send(inner_map=req_body_inner_map_list[i], my_url=URL)
        if r.ok:
            # TODO 这个成功判断条件需要改，结合实际，debug看一下r里面什么变量代表是否成功
            print("当前这条请求执行失败，停止执行")
            break
