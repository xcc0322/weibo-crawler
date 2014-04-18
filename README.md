# Weibo Crawler

4/18/2014 11:59:50 PM 

This is a crawler to crawl http://weibo.cn/ and extract data for further analysis of WeiboSpammerDetector project.

It was built by Chengcheng using [Scrapy Framework](http://scrapy.org/).

The main customized classes are as follows:

+ **weibo_spider.py**: self-defined Spider class, main crawling process

+ **items.py**: self-defined target data

+ **UserConnectionParser**: connection pages parser module

+ **UserProfileParser**: user profile pages parser module

+ **WeiboLogInEngine**: module to deal with the log-in process with reference to [this post](http://qinxuye.me/article/simulate-weibo-login-in-python/).


