#encoding=utf-8
import cookielib
import sys
import urllib2
from cookielib import CookieJar
import json
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = file('/Users/nuo/Downloads/dongrizhongyi.csv','wb')
writer = csv.writer(csvfile)
writer.writerow(['ID','姓名','专业领域','职称','所属医院','评论数','购买记录数'])


loginUrl = 'http://www.idongri.cn/api/customer/getRecommendDoctorWithVideo'

headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'iDongriCustomer/3.9.2 (iPhone; iOS 10.2.1; Scale/2.00)',
'Host': 'www.idongri.cn',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip, deflate',

}
loginData = "channel=ios&fchanel=%7D%03%0Fdct%05u&imeiCode=1B196F70-29BE-4111-BAF1-6D86C87B8B6C&mobileType=iPhone8%2C1&pageNo=16&pageSize=20&systemType=10.19999980926514&terminal=1&versionCode=3915581&versionName=3.9.2"
cj = CookieJar();
cookie_item = cookielib.Cookie(
    version=0, name="idongriSessionId", value="6fef2fbd-8333-4406-8db9-3ba7a32a4128",
    port=None, port_specified=None,
    domain="", domain_specified=None, domain_initial_dot=None,
    path="/", path_specified=None,
    secure=None,
    expires=None,
    discard=None,
    comment=None,
    comment_url=None,
    rest=None,
    rfc2109=False,
)
cj.set_cookie(cookie_item)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req = urllib2.Request(loginUrl, loginData, headers)
loginResult = opener.open(req).read()

j_data=json.loads(loginResult)

for item in j_data['data']['doctorList']:
    print item['doctorId']
    print item['name']
    print item['expertiseArea']
    print item['title']
    print item['hospital']

    loginUrl = 'http://www.idongri.cn/api/customer/getDoctorCommentListWithAS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'iDongriCustomer/3.9.2 (iPhone; iOS 10.2.1; Scale/2.00)',
        'Host': 'www.idongri.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    loginData = "channel=ios&doctorId="+str(item['doctorId'])+"&fchanel=%7D%03%0Fk%00d%00%00&imeiCode=1B196F70-29BE-4111-BAF1-6D86C87B8B6C&mobileType=iPhone8%2C1&pageNo=16&pageSize=20&systemType=10.19999980926514&terminal=1&versionCode=3915581&versionName=3.9.2"
    cj = CookieJar();
    cookie_item = cookielib.Cookie(
        version=0, name="idongriSessionId", value="6fef2fbd-8333-4406-8db9-3ba7a32a4128",
        port=None, port_specified=None,
        domain="", domain_specified=None, domain_initial_dot=None,
        path="/", path_specified=None,
        secure=None,
        expires=None,
        discard=None,
        comment=None,
        comment_url=None,
        rest=None,
        rfc2109=False,
    )
    cj.set_cookie(cookie_item)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    req = urllib2.Request(loginUrl, loginData, headers)
    loginResult1 = opener.open(req).read()

    j_datainfo = json.loads(loginResult1)


    if(j_datainfo['page']==None):
        var = j_datainfo['page']
        var = 0
    else:
        var = j_datainfo['page']['totalRows']

    loginUrl = 'http://www.idongri.cn/api/open/getServiceUseSkillWithBuyRecord'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'iDongriCustomer/3.9.2 (iPhone; iOS 10.2.1; Scale/2.00)',
        'Host': 'www.idongri.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    loginData = "channel=ios&doctorId="+str(item['doctorId'])+"&fchanel=%7D%03%0Fkuw%7B%7D&imeiCode=1B196F70-29BE-4111-BAF1-6D86C87B8B6C&mobileType=iPhone8%2C1&systemType=10.19999980926514&terminal=1&versionCode=3915581&versionName=3.9.2"
    cj = CookieJar();
    cookie_item = cookielib.Cookie(
        version=0, name="idongriSessionId", value="6fef2fbd-8333-4406-8db9-3ba7a32a4128",
        port=None, port_specified=None,
        domain="", domain_specified=None, domain_initial_dot=None,
        path="/", path_specified=None,
        secure=None,
        expires=None,
        discard=None,
        comment=None,
        comment_url=None,
        rest=None,
        rfc2109=False,
    )
    cj.set_cookie(cookie_item)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    req = urllib2.Request(loginUrl, loginData, headers)
    loginResult2 = opener.open(req).read()

    j_datainfo1 = json.loads(loginResult2)
    if(j_datainfo1['data'].has_key("buyRecordList")==False):
        var_a = 0
    else:
        var_a = len(j_datainfo1['data']['buyRecordList'])

    #item['buyRecordNum'] = len(j_datainfo1['data']['buyRecordList'])

    writer.writerow([item['doctorId'], item['name'], item['expertiseArea'], item['title'], item['hospital'], var, var_a])