# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log
from weibo.items import UserProfileItem, UserConnectionItem
from weibo.spiders.WeiboLogInEngine import WeiboLogInEngine
from weibo.spiders.UserProfileParser import UserProfileParser
from weibo.spiders.UserConnectionParser import UserConnectionParser


class DmozSpider(Spider):
    name = "weibo"
    start_urls = []

    def start_requests(self):
        username = "xcc0322"
        password = "930322"
        log.start(logfile='LOG_FILE')
        logger = WeiboLogInEngine(username, password)
        url, self.headers = logger.login()
        log.msg("----login succeeded start request----")
        return [Request(
            url,
            headers = self.headers,
            callback = self.parse_profile_page
        )]

    def parse_profile_page(self, response):
        filename = "first_weibo_page"
        open(filename, 'wb').write(response.body)
        log.msg("----start parse profile----")
        following_url, fans_url, item = UserProfileParser(response).parse()
        return [
            Request(
                following_url,
                headers = self.headers,
                callback = self.parse_following_page
            ),Request(
                fans_url,
                headers = self.headers,
                callback = self.parse_fans_page
            ), item
        ]

    def parse_following_page(self, response):
		filename = "first_following_page"
		open(filename, 'wb').write(response.body)
        profile_pages, next_page, item = UserConnectionParser(response, 1).parse()

        requests = [Request(url, headers = self.headers,
          callback = self.parse_profile_page) for url in profile_pages]
        
        if next_page:
            requests.append(Request(next_page, headers = self.headers,
              callback = self.parse_following_page))
		return request + [item]

    def parse_fans_page(self, response):
		filename = "first_fans_page"
		open(filename, 'wb').write(response.body)
        profile_pages, next_page, item = UserConnectionParser(response, 0).parse()
        requests = [Request(url, headers = self.headers,
          callback = self.parse_profile_page) for url in profile_pages]
        
        if next_page:
            requests.append(Request(next_page, headers = self.headers,
              callback = self.parse_fans_page))
		return requests + [item]



