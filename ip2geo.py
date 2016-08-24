#!/usr/bin/env python3
# encoding=utf-8

import argparse
import requests
import urllib
import re

# parse the console params
parser = argparse.ArgumentParser()
parser.add_argument('domain', help='a domain like baidu.com | a ipv4 addr', type=str)
parser.add_argument('-v', help='show request detail info', action='store_true')
parser.add_argument('-s', help='show your public network GEO info', action='store_true')
args = parser.parse_args()

print('Query IP/Host is : %s\n' % args.domain)

# build remote url
ip = args.domain            # query ip addr
host = 'ip.chinaz.com'
url = 'http://ip.chinaz.com/?IP=skinsharp.cn'
payload = {
    'ip': ip,
}
headers = {
    'Host': host,
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': "en-US,en;q=0.5",
    'Accept-Encoding': "gzip, deflate",
    'Referer': url,
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# http request via requests python lib
r = requests.post(url, headers=headers, data=payload, timeout=1)
if args.v:
    print('Request     URL: %s' % url)
    print('Request  header:')
    print(headers)
    print('Request payload: %s' % urllib.parse.urlencode(payload))
    print('Response status: %d' % r.status_code)
    print('Response header:')
    print(r.headers)            # dict type
    # print(r.text)             # ascii text type
    print()

# filter result from the html content
re_code = re.compile(r'<span class=\"Whwtdhalf w(15|50)-0\">(.*?)</span>')
fields = re.findall(re_code, r.text)

# stdout the data
i = 0
cache = []
for zone in fields:
    cache.append(zone[1].strip())
    i = i+1
    if i == 4:
        print('%s \t%-15s \t%s \t%s' % (cache[0], cache[1], cache[2], cache[3]))
        i = 0
        del cache[:]
del cache
del i

# filter the local ip of public network
if args.s:
    re_code = re.compile(r'您来自：</span>(.*)?<span class=\"pl10\">所在区域：</span>(.*)?<a href')
    fields = re.findall(re_code, r.text)
    for i in fields:
        print('\n你的公网IP： %s, IP物理地址：%s' % (i[0].strip(), i[1]))

del fields
