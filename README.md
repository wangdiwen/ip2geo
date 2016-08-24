# ip2geo
A small command tool to query GEO position from your IPv4 or domain name. Your host computer must be online when you using this script tool.

# 说明
这是一个基于Python的命令行小工具，根据域名或者公网IPv4地址，查询到GEO地理位置信息。（使用时需要主机联网）

实现原理：因为本身没有GEO数据库，工具通过向公开的在线IP查询网站ip.chinaz.com发起HTTP请求，然后进行正则解析得出有效结果。

在结果中有一项“数字地址”，这个类似于GPS，可以直接粘贴到百度或者谷歌搜索，直接查看其他更详细的信息。

# Usage
```
$ python ip2geo.py -h
usage: ip2geo.py [-h] [-v] [-s] domain

positional arguments:
  domain      a domain like baidu.com | a ipv4 addr

optional arguments:
  -h, --help  show this help message and exit
  -v          show request detail info
  -s          show your public network GEO info
```

### 举个栗子
查询baidu.com的所有BGP机房出口位置

```
$ python ip2geo.py baidu.com
Query IP/Host is : baidu.com

域名/IP 	获取的IP地址         	数字地址 	IP的物理位置
baidu.com 	111.13.101.208  	1863149008 	北京市 北京百度网讯科技有限公司移动节点
baidu.com 	220.181.57.217  	3702864345 	北京市 北京百度网讯科技有限公司电信节点
baidu.com 	180.149.132.47  	3029697583 	北京市 北京百度网讯科技有限公司电信节点
baidu.com 	123.125.114.144 	2071818896 	北京亦庄联通机房
```

# As a cmd tool
为了方便作为一个命令行工具使用，你也可以这样：
```
$ cp ip2geo.py /usr/local/bin
$ ln -s /usr/local/bin/ip2geo.py /usr/local/bin/ip2geo
$ ip2geo baidu.com
```
