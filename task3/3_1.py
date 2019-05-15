#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://mail.163.com/")
time.sleep(5)
browser.switch_to.frame(0)
mail = browser.find_element_by_name("email")
mail.send_keys("zp1968453044@163.com")
password = browser.find_element_by_name("password")
password.send_keys("******")
login_em = browser.find_element_by_id("dologin")
login_em.click()
time.sleep()
