#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-
import RequestType


class KVData:
    key = None
    value = None
    type = RequestType.RequestType.isBody

    def __init__(self, k, v, t):
        self.key = k
        self.value = v
        self.type = t

    def change_type(self, type_):
        self.type = type_

    def to_str(self):
        return str(self.key) + " : " + str(self.value)
