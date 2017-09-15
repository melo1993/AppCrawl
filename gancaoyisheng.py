#encoding=utf-8
import cookielib
import sys
import urllib2
from cookielib import CookieJar
import json
import csv
import random
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = file('/Users/nuo/Downloads/gancaoyisheng.csv','wb')
writer = csv.writer(csvfile)
writer.writerow(['ID','姓名','职称','问答量'])


loginUrl = 'https://api.igancao.com/index.php/doctorplus/getlist'

headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'LiquoriceDoctorProject/2.8.0 (iPhone; iOS 10.2.1; Scale/2.00)',
'Host': 'api.igancao.com',
'uuid':'06F27A18-B847-419E-AA77-4AB8D44B62A7',
'Token':'ivw2pvksnso6hua15hgl2guelix6me13fsz04gb4aw6ettpyrgzjrw78dun8nvvmtp2dd10361',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip, deflate',
}

loginData = "did=111326"
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