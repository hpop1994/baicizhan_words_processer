__author__ = 'Xujc'

import urllib.request as urllib2
import urllib.parse
import http.cookiejar
import json
# Enable cookie support for urllib2
cookiejar = http.cookiejar.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

data = b'utf8=%E2%9C%93&authenticity_token=bGFKG20R%2BNk3%2FTT1%2Fg%2BBKcKPUIdRWXLVsmWB8DMeYyY%3D&email=hpop1994%40163.com&raw_pwd=h1234567&remember_me=0'
# request = urllib2.Request(
#     url='http://www.baicizhan.com/',
#     headers={'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '144'},
#     data=data)

request = urllib2.Request("http://www.baicizhan.com/", data)
url = urlOpener.open(request)  # Our cookiejar automatically receives the cookies

pageStr=''
for i in range(1, 24):
    pageStr = str(i)
    data_got = urlOpener.open('http://www.baicizhan.com/user/all_done_words_list?page='+pageStr).readall()
    json_object = json.loads(data_got.decode('utf-8'))
    words_list = json_object['list']
    for words_object in words_list:
        print(words_object['word'] + '\t' + words_object['word_meaning']+'\n')

