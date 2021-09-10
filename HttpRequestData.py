#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-


class HttpRequestData:
    req_header = None
    req_body = None
    req_url = ""

    def __init__(self, h, b, url_):
        self.req_header = h
        self.req_body = b
        self.req_url = url_
