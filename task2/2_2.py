#!/usr/bin/env python
# coding=utf-8
import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010"
    }
    url = "http://www.dxy.cn/bbs/thread/626626"
    r = requests.get(url, headers=headers)
    tree = etree.HTML(r.text)
    user = tree.xpath('//div[@class="auth"]/a/text()')
    content = tree.xpath('//td[@class="postbody"]')
    print content
    data = []
    for i in range(0, len(user)):
        print user[i].strip()+":"+content[i].xpath('string(.)').strip()
