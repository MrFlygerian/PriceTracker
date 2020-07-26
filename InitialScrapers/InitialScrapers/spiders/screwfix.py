# -*- coding: utf-8 -*-
import scrapy


class ScrewfixSpider(scrapy.Spider):
    name = 'screwfix'
    allowed_domains = ['https://www.screwfix.com/c/heating-plumbing/boilers/cat6660001']
    start_urls = ['https://www.screwfix.com/c/heating-plumbing/boilers/cat6660001/']

    def parse(self, response):
        print("procesing:" + response.url)
        #product_name = response.xpath('//a[@id="product_description_1"]/text()')

        pass
