#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup as bs 
import requests

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010"
    }
    url = "http://www.dxy.cn/bbs/thread/626626"
    r = requests.get(url, headers=headers)
    html = bs(r.text, "lxml")
    data = []
    for item in html.find_all("tbody"):
        try:
            userid = item.find("div", class_="auth").get_text(strip=True)
            #print userid
            content = item.find("td", class_="postbody").get_text(strip=True)
            #print content
            data.append((userid, content))
        except:
            pass
    for i in data:
        print i[0], i[1]
