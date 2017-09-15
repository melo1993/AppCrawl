#encoding=utf-8
import cookielib
import sys
import urllib2
from cookielib import CookieJar
import json
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = file('/Users/nuo/Downloads/babamai.csv','wb')
writer = csv.writer(csvfile)
writer.writerow(['ID','姓名','咨询标题','咨询内容','评论数', '点击数'])


loginUrl = 'http://front.babamai.com.cn/wenda/selhomewendapagelist.shtml?v=3.0.4&p=ios&c=u'

headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'bbm_user/3.0.4 (iPhone; iOS 10.2.1; Scale/2.00)',
'Host': 'front.babamai.com.cn',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip, deflate',
}

count = 0
for start in range(1,700):
    loginData = "d=%7B%0A%20%20%22token%22%20%3A%20%22686fae0dd48effade89224e831368283dd7e17d0fa6aa6a731f987d2cd3f86db88ad1d266bae0df9%22%2C%0A%20%20%22currPage%22%20%3A%20%22"+str(count)+"%22%0A%7D&t=686fae0dd48effade89224e831368283dd7e17d0fa6aa6a731f987d2cd3f86db88ad1d266bae0df9"
    count = count +1
    cookieJar = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    req = urllib2.Request(loginUrl, loginData, headers)
    loginResult = opener.open(req).read()
    print loginResult

    j_data=json.loads(loginResult)

    for item in j_data['d']['list'][0]['wendaFormBeanList']:
        print item['uid']
        print item['name']
        print item['title']
        print item['content']
        print item['postCount']
        print item['clickCount']

        writer.writerow([item['uid'], item['name'], item['title'], item['content'], item['postCount'], item['clickCount']])