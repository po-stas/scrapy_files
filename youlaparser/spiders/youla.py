# -*- coding: utf-8 -*-
import scrapy


class YoulaSpider(scrapy.Spider):
    name = 'youla'
    allowed_domains = ['youla.ru']
    start_urls = ['http://youla.ru/']

    def parse(self, response):
        pass
