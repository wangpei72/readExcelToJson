#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
import HttpRequestData


class HttpRequestDataPool:
    req_pool = []

    def __init__(self, pool_):
        self.req_pool = pool_
