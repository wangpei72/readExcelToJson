#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
import HttpRequestData
import HttpRequestDataPool
import ExcelFileParser


class PoolInitializer:
    """将xls解析结果初始化为requestPool"""
    pool = None

    def __init__(self, pool_):
        self.pool = pool_

    def init_pool(self):
