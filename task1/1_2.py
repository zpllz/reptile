#!/usr/bin/env python
# coding=utf-8
import requests
import re
import sys

if __name__ == "__main__":
    header = {}
    params = {}
    header["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010"
    params["filter"] = ""
    url = "https://movie.douban.com/top250"
    for j in range(0, 250, 25):
        params["start"] = "%d"%(j)
        r = requests.get(url, headers=header, params=params)
        rank = re.findall("<em class=\"\">(.*)</em>", r.text)
        #match chinese
        pattern = u'<span class="title">((?!&nbsp).+)</span>'
        name = re.findall(pattern, r.text)
        pattern = '([0-9]+).*&nbsp;/&nbsp;'
        year = re.findall(pattern, r.text)
        pattern = u'导演: (.*)<br>'
        directory = re.findall(pattern, r.text)
        for i, _ in enumerate(name):
            item = "rank: %s, name: %s, year: %s, directo: %s"%(rank[i], name[i], year[i], directory[i].split("&nbsp;")[0].replace(".", ""))
            print item
