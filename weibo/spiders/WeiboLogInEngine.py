# -*- coding: utf-8 -*-
import urllib2
import urllib
import re

import lxml.html as HTML

class WeiboLogInEngine:
    def __init__(self, username, password):
        self.username = username
        self.pwd = password
        self.url = "http://www.weibo.cn/login"
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Referer':'','Content-Type':'application/x-www-form-urlencoded'
        }

    def get_rand(self, url):
        headers = {
	    'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9',
            'Referer':''
	}
        request = urllib2.Request(url ,urllib.urlencode({}), headers)
        response = urllib2.urlopen(request)
        login_page = response.read()
        rand = HTML.fromstring(login_page).xpath("//form/@action")[0]
        passwd = HTML.fromstring(login_page).xpath("//input[@type='password']/@name")[0]
        vk = HTML.fromstring(login_page).xpath("//input[@name='vk']/@value")[0]
        return rand, passwd, vk

    def login(self):
        print "---------------------------------url!!!!!!!!!!!!!!!!!!"
        url = 'http://3g.sina.com.cn/prog/wapsite/sso/login.php?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt='
        rand, passwd, vk = self.get_rand(url)
        data = urllib.urlencode({
            'mobile': self.username,
            passwd: self.pwd,
            'remember': 'on',
            'backURL': 'http://weibo.cn/',
            'backTitle': '新浪微博',
            'vk': vk,
            'submit': '登录',
            'encoding': 'utf-8'
        })
        url = 'http://3g.sina.com.cn/prog/wapsite/sso/' + rand
        request = urllib2.Request(url, data, self.headers)
        response = urllib2.urlopen(request)
        link = HTML.fromstring(response.read()).xpath("//a/@href")[0]
        return link, self.headers
