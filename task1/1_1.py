#!/usr/bin/env python
# coding=utf-8
import requests

def getRequest(url):
    print "start get %s"%(url)
    print "------------------"
    param = {}
    header = {}

    param["wd"] = "datawhale"
    param["id"] = "utf-8"
    #fill header and params
    header["Accept-Encoding"] = "gzip, deflate, br" 
    header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    header["Upgrade-Insecure-Requests"] = "1"
    header["Accept-Language"] = "zh-CN,zh;q=0.9,en;q=0.8"
    header["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    r = requests.get(url, params=param, headers=header)
    print r.text, r.status_code
def PostRequest(url):
    param = {}
    r = requests.post(url, data=param)
if __name__ == "__main__":
    url = "https://www.baidu.com"
    getRequest(url)
