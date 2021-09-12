#!/usr/bin/pyhton
# -*- coding: UTF-8 -*-

URL = "http://localhost:1080"


class HttpRequestData:
    req_header = {
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3683.103 Safari/537.36 '
    }
    req_body = {'PRCOD': 'LR152011',
                'WEBCOD': '',
                'ERRMSG': '',
                'ISUTIM': '',
                'ISUDAT': '',
                'RTNLVL': '',
                'DALCOD': '',
                'TARSVR': ''}
    info_body_inner_map = {}
    req_url = URL

    def set_info_body(self, info_body):
        self.info_body_inner_map = info_body
        if 'INFBDY' in self.req_body:
            print('yes')
            del self.req_body['INFBDY']
        self.req_body['INFBDY'] = info_body

    def append_last_line(self):
        self.req_body['RTNCOD'] = ''


if __name__ == "__main__":
    example = HttpRequestData()
    print(example.req_body)

