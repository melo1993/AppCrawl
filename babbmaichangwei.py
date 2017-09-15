#encoding=utf-8
import cookielib
import sys
import urllib2
from cookielib import CookieJar
import json
import csv
import random
import time
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = file('/Users/nuo/Downloads/babamaichangwei.csv','wb')
writer = csv.writer(csvfile)
writer.writerow(['ID','姓名','擅长病种','职称','问答量','订单量'])


loginUrl = 'http://front.babamai.com.cn/doctortoplist/seltaiolidoctorpagelist.shtml?v=3.0.4&p=ios&c=u'

headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'bbm_user/3.0.4 (iPhone; iOS 10.2.1; Scale/2.00)',
'Host': 'front.babamai.com.cn',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip, deflate',
}


loginData = "d=%7B%0A%20%20%22currPage%22%20%3A%20%223%22%2C%0A%20%20%22tagTypeId%22%20%3A%20%223osvjr92up16jvh0qj%22%0A%7D&t="+str(random.random())+""
print loginData
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
req = urllib2.Request(loginUrl, loginData, headers)
loginResult = opener.open(req).read()
print loginResult

j_data=json.loads(loginResult)

for item in j_data['d']['list']:
    time.sleep(10)
    print item['did']
    print item['name']
    print item['specialty']
    print item['doctorTitleName']
    print item['hospitalName']

    loginUrl = 'http://front.babamai.com.cn/doctorinfo/getdoctorinfobyid.shtml?v=3.0.4&p=ios&c=u'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'bbm_user/3.0.4 (iPhone; iOS 10.2.1; Scale/2.00)',
        'Host': 'front.babamai.com.cn',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    loginData = "d=%7B%0A%20%20%22doctorId%22%20%3A%20%22"+str(item['did'])+"%22%0A%7D&t="+str(random.random())+""
    print loginData
    cookieJar = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    req = urllib2.Request(loginUrl, loginData, headers)
    loginResult1 = opener.open(req).read()
    print loginResult1

    j_datainfo = json.loads(loginResult1)
    print j_datainfo['d']['obj']['postNum']
    print j_datainfo['d']['obj']['orderNum']

    writer.writerow([item['did'],item['name'],item['specialty'],item['doctorTitleName'],item['hospitalName'],j_datainfo['d']['obj']['postNum'],j_datainfo['d']['obj']['orderNum']])