# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class YoulaSpider(scrapy.Spider):
    name = 'youla.auto'
    allowed_domains = ['youla.ru']
    start_urls = ['https://auto.youla.ru/rossiya/cars/used/?vinChecked=1']

    def parse(self, response:HtmlResponse):
        links = response.xpath('//a[@class="SerpSnippet_name__3F7Yu SerpSnippet_titleText__1Ex8A blackLink"]/@href').extract()
        for link in links:
            yield response.follow(link, callback=self.parse_links)

    def parse_links(self, response:HtmlResponse):
        pass

# class="SerpSnippet_name__3F7Yu SerpSnippet_titleText__1Ex8A blackLink"
# target="_blank" data-target="serp-snippet-title" title="Nissan X-Trail с пробегом">Nissan X-Trail, T31 [рестайлинг]</a>