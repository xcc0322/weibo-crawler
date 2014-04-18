# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from weibo.items import UserConnectionItem
import urllib2
import urllib
import re
import lxml.html as HTML

class UserConnectionParser:
    def __init__(self, response, type_of_connection):
        self.sel = Selector(response)
        self.type_of_connection = type_of_connection
        self.uid = '0000000007'
        self.uid_list = []

    def extract_uids(self):
        uid_list = self.sel.xpath('//a/@href').re(r'.*uid=(\d+).*')
        self.uid = uid_list[0]
        self.uid_list = list(set(uid_list[1:]))

    def extract_profile_links(self):
        #todo
    def extract_next_page(self):
        #todo

    def parse(self):
        profile_pages = self.extract_profile_links()
        next_page = self.extract_next_page()
        # Make an item
        extract_uids()
        item = UserConnectionItem()
        item['uid'] = self.uid
        item['type_of_connections'] = self.type_of_connection
        item['uid_list'] = self.uid_list
        return profile_pages, next_page, item