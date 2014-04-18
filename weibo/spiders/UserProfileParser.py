# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from weibo.items import UserProfileItem
import urllib2
import urllib
import re
import lxml.html as HTML

class UserProfileParser:
    def __init__(self, response):
        self.sel = Selector(response)
        self.item = UserProfileItem()

    def decorate_url(self, url):
        if not url.startswith('http://'):
            url = 'http://weibo.cn/%s' % url
        return url

    def extract_target_uid(self, fans_url):
        matchObj = re.match( r'/(\d+)/fans.*', fans_url)
        self.item['uid'] = matchObj.group(1)

    def extract_number_of_connections(self):
        followings = self.sel.xpath('//a/text()').re(ur'关注\[(\d+)\]')[0]
        self.item['number_of_followings'] = followings

        fans = self.sel.xpath('//a/text()').re(ur'粉丝\[(\d+)\]')[0]
        self.item['number_of_fans'] = fans

    def extract_quality_of_post(self):
        comments = self.sel.xpath('//a/text()').re(ur'评论\[(\d+)\]')
        num_list = [int(num) for num in comments]
        self.item['number_of_interactions_in_most_recent_posts'] = sum(num_list)

    def parse(self):
        #extract following url
        following_url = self.sel.xpath('//a/@href').re(r'.*follow.*')[0]
        #extract fans url
        fans_url = self.sel.xpath('//a/@href').re(r'.*fans.*')[0]
        #extract item
        self.extract_target_uid(fans_url)
        self.extract_number_of_connections()
        self.extract_quality_of_post()
        return self.decorate_url(following_url), self.decorate_url(fans_url), self.item