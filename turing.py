# -*- coding: utf-8 -*-
import scrapy


class TuringSpider(scrapy.Spider):
    name = 'turing'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
