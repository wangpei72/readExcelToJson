#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
import HttpRequestData
import ExcelFileParser as exp
from RequestType import RequestType

TARGET = 'LR152011X1'

''' ---------------------这个类已经废弃-----------------'''
class HttpRequestDataPool:
    req_body_pool = []
    kvt_list = []

    def __init__(self, name):
        self.get_kvt_list(name)
        self.get_body_from_xls_kvt_list(self.kvt_list)

    def get_body_from_xls_kvt_list(self, kvt_list):
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
            self.req_body_pool.append(new_obj)
            # del new_obj
        return res

    def get_kvt_list(self, name):
        self.kvt_list = exp.ExcelFileParser(name).dataList_withType

    def fix_bug(self):
        for obj in self.req_body_pool:
            obj.req_body['INFBDY'] = obj.info_body_inner_map




if __name__ == '__main__':
    ex = HttpRequestDataPool('data1.xlsx')

    for req in ex.req_body_pool:
        print("before", req.req_body['INFBDY'])
        req.req_body['INFBDY'] = req.info_body_inner_map
        print("after,", req.req_body['INFBDY'])

    for i in ex.req_body_pool:
        print(i.req_body['INFBDY'])
