import time
import requests
import smtplib
import datetime
from email.mime.text import MIMEText



url = "http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp"
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'no-cache',
#     'Pragma': 'no-cache',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Origin': 'http://yqtb.nwpu.edu.cn',
#     'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
#     'Accept-Encoding': 'gzip, deflate',
#     'Cookie': 'JSESSIONID=4A6F8E4B756B483C836DE5AC775E0D7B',
# }
headers = {
    'label'
}
data = {
    'sfczbcqca': '',
    'czbcqcasjd': '',
    'sfczbcfhyy': '',
    'czbcfhyysjd': '',
    'actionType': 'addRbxx',
    'userLoginId': '2018302993',
    'userName': '%E7%8E%8B%E8%A3%B4',
    'szcsbm': '330108',
    'szcsmc': '%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E6%BB%A8%E6%B1%9F%E5%8C%BA',
    'sfjt': '0',
    'sfjtsm': '',
    'sfjcry': '0',
    'sfjcrysm': '',
    'sfjcqz': '0',
    'sfyzz': '0',
    'sfqz': '0',
    'ycqksm': '',
    'glqk': '0',
    'glksrq': '',
    'gljsrq': '',
    'tbly': 'sso',
    'glyy': '',
    'qtqksm': '',
    'sfjcqzsm': '',
    'sfjkqk': '0',
    'jkqksm': '',
    'sfmtbg': '',
    'userType': '2',
    'qrlxzt': '',
    'bdzt': '0',
    'xymc': '%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2',
    'xssjhm': '15555546431'
}

# url = "https://xxcapp.xidian.edu.cn/ncov/wap/default/save"
# headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#            'Accept': 'application/json, text/javascript, */*; q=0.01',
#            'Accept-Language': 'zh-cn',
#            'Accept-Encoding': 'gzip, deflate, br',
#            'Host': 'xxcapp.xidian.edu.cn',
#            'Origin': 'https://xxcapp.xidian.edu.cn',
#            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) '
#                          'Version/13.1 Safari/605.1.15',
#            'Connection': 'keep-alive',
#            'Referer': 'https://xxcapp.xidian.edu.cn/ncov/wap/default/index',
#            'Content-Length': '2314',
#            # Cookie是身份标识
#            'Cookie': 'Hm_lpvt_48b682d5d22a90111e44886b972e3268=1590108209; '  # Hm_lpvt_xxxxxxx 为当前时间戳（秒）
#            # Hm_lvt_xxx 为一串时间戳。最近的一次访问时间戳追加在后面，最多保留4个时间戳。可以通过关闭浏览器然后再访问相同页面查看其cookie值来验证。
#                      'Hm_lvt_48b682a90111e46b9d4885d2272e3268=1590108209; UUkey=99cf86f295b522e264680402bf6b221e; '
#                      'Uqn3iPIDZBpD3wJU=vqtbQwSD1sjDM; eai-sess=prshbd3vo96po8i27a4mod1i67',
#            'X-Requested-With': 'XMLHttpRequest',
#            }
# data = {
#     'uid': '123671', 'date': str(datetime.date.today() - datetime.timedelta(days=1)).replace("-", ""),
#     'tw': '3',  # 体温：第三项，36.5-36.9
#     'sfcxtz': '0',  # 是否出现
#     'sfyyjc': '0',  # 是否医院检查
#     'jcjgqr': '0',  # 检查结果确认
#     'sfjcbh': '0',  # 是否接触病患
#     'sfcxzysx': '0',  # 是否出现
#     'address': '', 'area': '', 'province': '',  # 地址
#     'city': '',  # 城市
#     # 伽利略定位系统详情
#     'geo_api_info': '{"type":"complete","position":{"P":11.203296169705,"O":11.667691514757,"lng":11.667692,'
#                     '"lat":11.203296},"location_type":"html5","message":"Get ipLocation failed.Get geolocation '
#                     'success.Convert Success.Get address success.","accuracy":15,"isConverted":true,"status":1,'
#                     '"addressComponent":{"citycode":"0001","adcode":"123456","businessAreas":[],'
#                     '"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"",'
#                     '"streetNumber":"","province":"","city":"","district":"","township":""},'
#                     '"formattedAddress":"","roads":[],"crosses":[],"pois":[],'
#                     '"info":"SUCCESS"}',
#     'created': str(int(time.time())),  # 创建时间
#     'sfzx': '0',  # 是否在校 否
#     'sfjcwhry': '0',  # 是否接触武汉人员 否
#     'sfcyglq': '0',  # 是否处于隔离期 否
#     'sftjwh': '0',  # 是否途径武汉 否
#     'sftjhb': '0',  # 是否途径湖北 否
#     'fjsj': '0',
#     'sfjchbry': '0',  # 是否接触湖北人员 否
#     'sfsfbh': '0',  # 是否
#     'jhfjsftjwh': '0',  # *****是否途径武汉 否
#     'jhfjsftjhb': '0',  # *****是否途径湖北 否
#     'szsqsfybl': '0',
#     'sfygtjzzfj': '0',  # 是否
#     'sfjcjwry': '0',  # 是否接触境外人员 否
#     'id': '4393912',
#     'ismoved': '0',  # 与上次地点是否有不同
# }


if __name__ == "__main__":
    # sendEmail('')
    r = requests.post(url=url, data=data, headers=headers)
    # sendEmail(eval(requests.post(url=url, data=data, headers=headers).text)['state'])
