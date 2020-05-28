# -*- coding: utf-8 -*-
import scrapy


class AmazonNewBalanceShoesSpider(scrapy.Spider):
    name = 'amazon_new_balance_shoes'
    allowed_domains = ['https://www.amazon.co.uk']
    start_urls = ['http://https://www.amazon.co.uk/s?k=new+balance+shoes+mens/']

    def parse(self, response):
        pass
