# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        filename = 'teacher.html'
        # response.body is a Byte object, and decode() turns it into strings
        open(filename, "w").write(response.body.decode('utf-8')).close()
