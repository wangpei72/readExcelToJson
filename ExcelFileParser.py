#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd as rd
import xlwt as wt
import os
import KVData as kvt
import RequestType


class ExcelFileParser:
    """我是帮助信息"""

    """以下是xl库相关的属性，path是xls文件路径"""
    rd_wb = None
    rd_wsheet_1 = None
    wt_wb = None
    wt.ws = None
    xls_file_name = ""
    path_to_xls = ""
    curDir = os.path.dirname(os.path.realpath(__file__))

    # 如果只需要读取 第一行 的数据，请把button改成True
    # maybe need change
    button = False

    jsonData = {}

    dataList_withType_str = []
    dataList_withType = []  # 加上了是头还是体的type区分，方便后面组装报文
    dataList = []  # 里面每个元素代表一行记录

    jsonKeyList = []    # 里面包含了所有的键

    num_cols = 0
    num_rows = 0

    def __init__(self, name):
        self.xls_file_name = name
        self.path_to_xls = os.path.join(self.curDir, self.xls_file_name)
        self.rd_wb = rd.open_workbook(self.path_to_xls)
        self.wt_wb = wt.Workbook(encoding='utf-8')
        sheets_name = self.rd_wb.sheet_names()
        self.rd_wsheet_1 = self.rd_wb.sheet_by_name(sheets_name[0])

        self.jsonKeyList = self.get_json_keys()
        self.dataList = self.form_json_data_list()
        self.dataList_withType = self.form_kvt_data_list()

    def get_json_keys(self):
        for i in range(1):
            # print('正在读取第%d' % (i + 1), '个sheet')
            table = self.rd_wb.sheets()[i]
            self.num_rows = table.nrows
            self.num_cols = table.ncols
            for j in range(self.num_cols):
                self.jsonKeyList.append(table.cell_value(0, j))
        return self.jsonKeyList

    def form_json_data_list(self):
        if self.num_cols == 0 or self.num_rows == 0:
            self.get_json_keys()
        for i in range(self.num_rows):
            if self.button and i == 2:
                break
            if i == 0:
                continue
            new_item_to_insert = {}
            table = self.rd_wb.sheets()[0]
            for j in range(self.num_cols):
                jsonKey = self.jsonKeyList[j]
                jsonValue = table.cell_value(i, j)
                # 组装键值对
                new_item_to_insert[jsonKey] = jsonValue
            self.dataList.append(new_item_to_insert)
        return self.dataList

    def form_kvt_data_list(self):
        if self.num_cols == 0 or self.num_rows == 0:
            self.get_json_keys()
        for i in range(self.num_rows):
            if self.button and i == 2:
                break
            if i == 0:
                continue
            table = self.rd_wb.sheets()[0]
            new_kvt_list_for_one_row = []
            new_item_str = []
            for j in range(self.num_cols):
                jsonKey = self.jsonKeyList[j]
                jsonValue = table.cell_value(i, j)

                new_item_with_type = kvt.KVData(jsonKey, jsonValue, RequestType.RequestType.isHeader)

                new_kvt_list_for_one_row.append(new_item_with_type)
                new_item_str.append(new_item_with_type.to_str())

                # TODO 是body的条件待添加

            self.dataList_withType_str.append(new_item_str)
            self.dataList_withType.append(new_kvt_list_for_one_row)

        return self.dataList_withType, self.dataList_withType_str

    def make_up_http_req_from_kvt_list(self):
        # TODO 这边建议写到pool init那里


if __name__ == '__main__':
    example = ExcelFileParser("data1.xlsx")
    print(example.dataList_withType_str)
