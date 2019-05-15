#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import json

def get_url(url):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010",
    }
    try:
        r = requests.get(url, headers = header)
        r.raise_for_status()
        return r.text
    except: 
        print "get url error!"

def get_ip(response):
    proxy_ip_list = []
    soup = BeautifulSoup(response, "html.parser")
    proxy_ips = soup.find(id = 'ip_list').find_all('tr')
    for proxy_ip in proxy_ips:
        if len(proxy_ip.select('td')) >= 8:
            ip = proxy_ip.select('td')[1].text
            port = proxy_ip.select('td')[2].text
            protocol = proxy_ip.select('td')[5].text
            if protocol in ("HTTP", "HTTPS", "http", "https"):
                proxy_ip_list.append("{}://{}:{}".format(protocol, ip, port))
    return proxy_ip_list

def open_url_with_proxy(url, proxy):
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010",    
    }
    proxies = {}
    if proxy.startswith(("HTTPS", "https")):
        proxies['https'] = proxy
    else:
        proxies['http'] = proxy
    try:
        r = requests.get(url, headers= header, proxies = proxies, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text, t.status_code)
    except:
        print "get url error " + url + " " + proxy
        return False

def check_proxy_status(proxy):
    url = "http://www.baidu.com"
    result = open_url_with_proxy(url, proxy)
    if result:
        text, status_code = result
        if status_code == 200:
            title = re.findall('<title>.*</title>', text)
            if title[0] == '<title>百度一下，你就知道</title>':
                return True
    return False 

def parse_ip(proxy):
    url = 'https://jsonip.com/'
    try:
        text, status_code = open_url_with_proxy(url, proxy, timeout = 10)
    except:
        return
    print "valid proxy ip: " + proxy
    try:
        source_ip = json.loads(text).get("ip")
        print "source ip: " + source_ip
        print "="*40
    except:
        print "json error"
        print text

#https same
def get_proxies():
    proxyHost = ""
    proxyPort = ""
    proxyUser = ""
    proxyPass = ""
    proxyMeta = "http://{}:{}@{}:{}".format(proxyUser, proxyPass, proxyHost, proxyPort)
    proxies = {
        "http": proxyMeta,
    }

if __name__ == "__main__":
    url = "https://www.xicidaili.com"
    text = get_url(url)
    proxy_ip_list = get_ip(text)
    proxy_valid_list = []
    for proxy in proxy_ip_list:
        valid = check_proxy_status(proxy)
        if valid:
            proxy_valid_list.append(proxy)
            parse_ip(proxy)

